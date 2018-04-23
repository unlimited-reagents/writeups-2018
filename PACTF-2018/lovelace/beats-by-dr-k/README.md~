# Problem

Dr. K just released her new EP — download her [track](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/beats-by-dr-k/beats.wav) now!

# Hint

Listen to each bit…

# Writeup

This problem was a fun one, probably taking us 25 hours of being stupid in total. We had already finished every other problem by the first day, but this problem took us until about 2 hours remaining x_x.

One of the main fallacies when solving this problem is overanalyzing it. An initial playthrough of the file yields a relatively normal piece of music. Combined with the hint, our team believed that the data was encoded with LSB. However, no ASCII or other files were found after running LSB on the music file. In addition, the long length of the file confused us, as LSB normally does not require extremely long and large files in CTFs.

After giving up on LSB, we tried a variety of other techniques, including DeepSound, DTMF tone detectors, screwing with playback speeds, etc.

However, the method that actually worked occured to us after looking at the spectrogram in Sonic Visualizer.

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/beats-by-dr-k/spec.png "bits spectrogram")

From this spectrogram, it appears as if we need to literally listen to each of the bits (hint). When the high pitched instrument is playing, we write a 1, and when it is not, we write a 0. This gives us the binary string: `01100110 01101100 01100001 01100111 01101001 01110011 01110000 01100001 01100011 01110100 01100110 01101101 01110101 01110011 01101001 01100011`, which is `flagispactfmusic` in ASCII.

Therefore, the flag is `pactfmusic`
