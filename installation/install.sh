sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-pip \
    zip
sudo apt install python3-gpiozero
sudo apt-get clean
sudo apt-get install python3-picamera
sudo pip3 install --upgrade picamera[array]
sudo cp /etc/dphys-swapfile .
sudo cp temp_swapfile /etc/dphys-swapfile 
sudo /etc/init.d/dphys-swapfile restart
mkdir -p dlib
git clone -b 'v19.6' --single-branch https://github.com/davisking/dlib.git dlib/
cd ./dlib
sudo python3 setup.py install --compiler-flags "-mfpu=neon"
sudo pip3 install face_recognition
sudo mv dphys-swapfile /etc/dphys-swapfile 
sudo /etc/init.d/dphys-swapfile restart
sudo apt-get install libatlas-base-dev

