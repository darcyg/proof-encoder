
Python ffmpeg encoder in a docker container
####

This is just a proof of concept to demonstrate the use of a docker image with python and ffmpeg installed can pipe mp4 video into a mpeg transport stream file on a shared volume.

Setup
#####

First: clone this repo. Then you have two options:

Option 1 - local machine : 

You need to install ffmpeg for this to work. You can download the right package at : https://www.ffmpeg.org/download.html or user brew: 
```brew install ffmpeg```

You must also have python3 installed with `ffmpy` and `subprocess`
Then from within the project simply run: 
  ```python main.py```
  
Option 2 - Docker image: 

1) Build the image:
from within the repo :
```docker build -t encoder .```

2) run the container of the image, mapping the output folder from within the container to a local volume.


```docker run -v 'pwd':/app/output encoder:latest```

The `-v` command will create a volume. 'pwd' is the location on your machine's filesystem to output the file. '/app/output' is the folder i have set the transcoded files to stream to.
