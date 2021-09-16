This repository contains scripts and templates for programming exercises
assigned during the Mathematical Foundations of RL course at UAntwerp.

We will be making use of the [https://www.tensorflow.org/agents](TensorFlow
Agents library) and its interface with
[https://gym.openai.com/envs/#classic_control](OpenAI's gym environments).

# Installation
We strongly recommend that you carry out the following steps using a virtual
environment.

## Virtual environments
For Python 3, you can enter some directory and create a virtual environment
within it executing `python3 -m venv virtualenvironment`. Then, you can
activate your virtual environment by sourcing the activate script in its bin
directory.

## Dependencies
To install everything needed for TensorFlow Agents, you might first need to
install [Bazel](https://bazel.build/). You can then run:
```
pip install tensorflow
pip install tf-agents
pip install 'imageio==2.4.0'
```


