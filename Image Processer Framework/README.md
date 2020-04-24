# LookingMass

# Team 31

## Members
* Aditya Sidher
* Ethan Park
* Marcus Casey
* Nikita Ignatyuk


# Dependencies, Building, and Running

## Dependency Instructions
This application currently is only supported on Linux and Windows based operating systems. This project requires the instillation of [KIVY](https://kivy.org/doc/stable/installation/installation-linux.html#installation-linux). 

### Ubuntu/Linux
```bash
pip install pillow
pip install numpy
python3 -m pip install --upgrade --user pip setuptools virtualenv
python3 -m virtualenv ~/kivy_venv
python3 -m pip install kivy
python -m pip install ffpyplayer
source ~/kivy_venv/bin/activate
```
### Windows OS
```bash
pip install pillow
pip install numpy
python -m pip install --upgrade pip wheel setuptools virtualenv
python -m virtualenv kivy_venv
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
python -m pip install kivy_deps.gstreamer==0.1.*
python -m pip install kivy_deps.angle==0.1.*
python -m pip install kivy==1.11.1
kivy_venv\Scripts\activate
PAUSE
```

## Building and Running

### To compile and run on Windows
```
python3 -m virtualenv ~/kivy_venv
kivy_venv\Scripts\activate
./engine.py
```

### To compile and run on Linux/Ubuntu
```
python3 -m virtualenv ~/kivy_venv
source ~/kivy_venv/bin/activate
./engine.py
```
