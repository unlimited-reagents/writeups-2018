## Problem - Dog or Frog

### Introduction

This problem asks for an adversarial example input to a network that is perceptually similar to a picture of Trixi, yet classifies very confidently as a tree frog.

There are a couple different ways to generate an adversarial example, but we decided on running a variant of gradient descent (we ended up using Adam at lr=0.01) to update each of the pixels of the image while freezing the weights of the model itself. Hopefully, the gradients calculated w.r.t. each of the pixels would push the image to look more like a tree frog. Basically, instead of training the network to produce a given output from the image, we train the image to fool the network.

We did not incorporate the similarity of the output image and original image in the loss function, as we hoped that the "training" would be fast enough to quickly converge at a solution without interfering with the p-hash.

### Implementation

To do this, we used Keras with the provided helper functions. However, instead of using the solution template, we implemented our solution in a [Jupyter Notebook](https://github.com/unlimited-reagents/writeups-2018/blob/master/PICOCTF-2018/dog-or-frog/solver.ipynb).

#### Setup

After Keras imports and helper functions, we set some helpful variables that allows us to define which category we are optimizing for:

```python
IMAGE_DIMS = (224, 224)
TREE_FROG_IDX = 31
TREE_FROG_STR = "tree_frog"
```

Now, in order to run the model, we must load the model and preprocess the image, all with some code provided in the solution template:

```python
test = Image.open("./trixi.png").resize(IMAGE_DIMS)
plt.imshow(test);
test = prepare_image(test)
model = load_model("./model.h5")
```

This shows us an image of Trixi, before we start dressing her up for Halloween!

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PICOCTF-2018/dog-or-frog/solver_files/solver_7_1.png "Trixi as a dog")

#### Model Construction

Now, we need to start to construct our training loop. Our team wanted to avoid any use of custom training loops with gradient calculation and updating for three reasons. First, we wanted to be able to use optimizers like Adam to hopefully converge faster. In addition, we wanted to simply be able to call `model.fit` instead of updating the image pixels manually every iteration. Finally, we thought the code would be cleaner, but it would have been shorter the other way around in hindsight :<.

To do this, we must somehow construct a model with the image pixels represented as weights in the network. Then, when training, we simply have to freeze all weights except for the image weights and train as normal. In the end, pulling out the image is as simple as defining a new network with the image weights as an output layer and `model.predict`.

We start by constructing the new network. We decided to represent the image with an input layer of 1, a non-biased fully connected layer with 150528 (224\*224\*3) neurons, and a reshape layer to convert the fully connected output into the correct image dimensions. Then, to feed in the image, we simply need to pass an input of [1], which is then multiplied by the fully connected weights. (This may be better represented as a very large convolutional layer in the future)

We do this by:

```python
K.set_learning_phase(1)
tempInput = Input((1,))
v = Dense(IMAGE_DIMS[0]*IMAGE_DIMS[1]*3, use_bias=False)(tempInput)
v = Reshape(IMAGE_DIMS+(3,), name="reshape_3")(v)
```

Then, we need to attach this image representation onto our existing network. Special attention must be paid to the learning phase and weight freezing here, as the weights both need to be frozen and in test phase. This way, batch normalization and dropout will perform consistently throughout adversarial image generation and inference on picoCTF servers.

We can do this by:

```python
model.trainable = False
K.set_learning_phase(0)
layers = [l for l in model.layers]
layers[1].trainable = False
x = layers[1](v)
for i in range(2, len(layers)):
    layers[i].trainable = False
    x = layers[i](x)
```

Finally constructing the model with: `m2 = Model(inputs=tempInput, outputs=x)`

Next, we must actually put the pixels of our image into the network, which can be done with a simple get_weights and set_weights:

```python
tempWeights = m2.get_weights()
tempWeights[0] = np.reshape(test, (1,IMAGE_DIMS[0]*IMAGE_DIMS[1]*3))
m2.set_weights(tempWeights)
```

We compile the model:

```python
m2.compile(optimizer=optimizers.Adam(lr=0.01),
          loss='mean_squared_error',
          metrics=['accuracy'])
```

Note that we use mean_squared_error loss here. Categorical cross entropy would most likely be a better fit, but we changed this to mean_squared_error during a debugging step, and never bothered to change it back after it started to work.

#### Training

We proceed to generate our "training example", which is simply an input of [1] and an output of a one hot vector encoding TREE_FROG_IDX:

```python
x = np.array([1.]*1)
y = keras.utils.to_categorical([TREE_FROG_IDX], num_classes=1000)
```

Next, we write the actual trainer. We `m2.fit` until the confidence in TREE_FROG_IDX exceeds 0.99. In addition, every 10th epoch, we fetch the image pixel weights and constrain them between 1 and -1 to maintain the validity of the image:

```python
while m2.predict(np.expand_dims(np.array([1.]), axis=0))[0][TREE_FROG_IDX]<0.99:
    m2.fit(x, y, epochs=10, batch_size=1, verbose=0, validation_data=(x,y))
    tempWeights = m2.get_weights()
    tempWeights[0][tempWeights[0]>1] = 1
    tempWeights[0][tempWeights[0]<-1] = -1
    m2.set_weights(tempWeights)
    print(m2.predict(x)[0][TREE_FROG_IDX])
```

After this terminates, we have our image encoded in the weights! This image produces a result 99.9819% confident. To save the image, we can construct a helper model with input tempInput and output v, which is the reshape layer we defined earlier. (In hindsight, calling get_weights would have been much more understandable).

#### Exporting the Image

We construct this model with `mtest = Model(inputs=tempInput, outputs=v)`

And pull the image out with: `img = np.squeeze(mtest.predict([1]))`

Before saving, we must denormalize the image:

```python
img+=1.
img/=2.
```

And then finally save it: `plt.imsave("test.png", img)`

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PICOCTF-2018/dog-or-frog/solver_files/solver_27_1.png "Trixi as a frog")

After uploading to picoCTF servers, we get our flag!

Overall, this was a very fun problem, and I look forward to possibly more ML challenges in future CTFs! The code could probably be updated with a custom training loop to be more concise, but I found this network assembly to be a great learning experience.