# Computer-Vision
Computer Vision projects/Test

OpenCV is available for installation from the default Ubuntu 20.04 repositories. To install it run:

sudo apt update
sudo apt install libopencv-dev python3-opencv

Verify the installation by importing the cv2 module and printing the OpenCV version:

python3 -c "import cv2; print(cv2.__version__)"

4.2.0

Verify the installation by importing the cv2 module and printing the numPy version:

python3 -c "import numpy; print(numpy.version.version)"


Installing pip for Python 3

sudo apt update
sudo apt install python3-pip

When the installation is complete, verify the installation by checking the pip version:

pip3 --version

To install the current caer you'll need at least Python 3.6.1. If you have an older version of Python, you will not be able to use caer.

pip3 install --upgrade caer