# Flask Object Detection training

Applying Faster RCNN for our training model.

## Getting started

Prerequisite: You are required to have python and virtualenv 
install in your machine

```shell
sudo apt install -y python3-venv
source my_env/bin/activate
```

## Install libraries

The require libraries are already listed in `requirements.txt`.

```shell
pip install -r requirements.txt
```

### Install PyTorch

The dense network 

```shell
pip install torch torchvision
```

## Run the flask application (development)

After created your virtual environment, you can start 
the project with `flask run`.

```shell
export FLASK_APP=app.py
python -m flask run
```