# Inverse Reinforcement Learning Application

The aim of this project is to create a simple application that can give the opportunity to all the users to use the Inverse Reinforcement Learning technique. The application is implemented in Python and the interface is made entirely with PyQt5.


<p align="center">
  <img src="Build/gitimages/main_view.png" width="400"/>
  <img src="Build/gitimages/alg_view.png" width="400"/>
</p>

The application is composed by two different View. The first View, left image, is used to set the model or load it. The second View, rigth image, is used for the Inverse Reinforcement Learning technique. This work is inspired from Ibarz, Borja and Leike, Jan and Pohlen, Tobias and Irving, Geoffrey and Legg, Shane and Amodei, Dario work. Please [read the paper](http://papers.nips.cc/paper/8025-reward-learning-from-human-preferences-and-demonstrations-in-atari). 

## Features 

Features include:

- The opportunity to choose from [different environment](Widget/Widget.md).
- Auto save function during the work.
- [History window](Widget/Widget.md) to memorize the user preferencies.
- [Restore previous work sesssion](Widget/Widget.md) before starting a new work.
- [Oracle](ReinforcementLearning/ReinforcemenLearning.md) to speed up the annotations and to debug the policy and reward model.
- [Utility function](Utility/Utils.md) which the user can use to analyze the reward model and to testing the policy and reward model too. 

## Download

Get the app by downloading this repository tapping in 'clone or download' button and then select 'Download Zip' command or from [here](https://github.com/giuliobz/InverseReinforcementLearningApp/archive/master.zip).
After downloading the zip file, extract it and follow the Dependecies instructions and Usage instructions.

## Dependecies

- Pytorch
- NumPy
- OpenAI Gym
- Matplotlib 
- opencv
- PIL

For detailed steps to install PyTorch, follow the [PyTorch installation instruction](https://pytorch.org/get-started/locally/). A typical user can install PyTorch using the following commands:

```bash
# Create virtual environment
conda create -n minigrid python=3.7

# Activate virtual environment
conda activate minigrid

# Install OpenAI Gym
pip3 install gym-minigrid

# Install PyTorch
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
```

For detailed steps to install OpenAI Gym follow the Installation steps in [gym-minigrid github repository](https://github.com/maximecb/gym-minigrid).

The other packet can be installed using pip:


```bash
conda activate minigrid
pip install numpy
pip install mathplotlib
pip install Pillow
pip install opencv-python
```

## Usage

Inverse Reinforcement Learning app is used by terminal support. The user has to go from terminal to the folder in which he has downloaded the github repository and then follow this command:

```bash
# Activate virtual environment in which you have installed all the dependencies
conda activate minigrid

# Go inside the master folder 
cd InverseReinforcementLearningApp-master

# Start application
python Application.py
```