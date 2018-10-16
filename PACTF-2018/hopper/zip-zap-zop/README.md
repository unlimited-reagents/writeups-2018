
for i in {2..200}; do printf "\x1f\x8b\x08\x00\x00\x00\x00\x00" |cat - new$i.zip |gzip -dc > new$(expr $i + 1).zip; done