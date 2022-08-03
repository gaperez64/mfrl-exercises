This repository contains scripts and templates for programming exercises
assigned during the Mathematical Foundations of RL course at UAntwerp. If
you want a no-installation solution, use 
[the Google Colab notebook instead.](https://colab.research.google.com/drive/1ziFGtkgXmQdtB4yAirEcFPpnwOc88fHm?usp=sharing)

We will be making use of 
[OpenAI's gym environments](https://gym.openai.com/envs/#classic_control).

# Installation
We strongly recommend that you carry out the following steps using a virtual
environment.

## Virtual environments
For Python 3, you can enter some directory and create a virtual environment
within it executing `python3 -m venv virtualenvironment`. Then, you can
activate your virtual environment by sourcing the activate script in its bin
directory.

## Dependencies
To install everything needed, you can now run:
```
pip install gym
```
Alternatively, there is a requirements.txt file in this repository you can
use by running:
```
pip install -r requirements.txt
```

## Plug your code in
There are two places where you need to change the `solve.py` script that
is provided.
1. The policy that is currently provided as an example is one that plays 
   uniformly at random. Please do some computations (based on the theory
   covered during the course) so that you replace this by a more interesting
   policy.
2. To make sure your policy is interesting, we ask that you compute the
   expected value per state if one would follow the policy you construct.
   Additionally, you have to compute the same value (vector) for a random
   policy and (as a sanity check) make sure that yours does better than the
   random policy.
The places in the script where these pieces of code have to be inserted are
clearly marked by comments.

