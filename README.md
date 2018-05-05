# study-picamera-examples
A collection of picamera example based on OpenCV

# requirements

* python 3.5
* OpenCV 3.4

```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk2.0-dev libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python3-dev python3-pip
sudo pip3 install numpy opencv-python picamera[array] imutils flask
sudo apt install libqtgui4 libqt4-test
sudo apt install libilmbase12 libopenexr22 libgstreamer1.0-dev
```

# installation

## install isaax agent.

```
$ wget https://isaaxartifacts.blob.core.windows.net/agent/v0.7.1/isaax-agent_v0.7.1_linux_armv7.tar.gz
$ sudo mkdir /opt/isaax-agent/
$ sudo tar xvzf isaax-agent_v0.5.6_linux_armv7.tar.gz -C /opt/
```

## register a device

1. Create an [isaax](https://isaax.io) account
2. Create a project
3. Generate a project token and copy one
4. Login to Raspberry Pi and run `sudo /opt/isaax-agent/isaax-agent --token <project token> install`
