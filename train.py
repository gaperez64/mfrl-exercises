import numpy as np
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts

# Let's load a simple environment
environment = suite_gym.load("FrozenLake8x8-v1")

# We can print some information about the environment
print('action_spec:', environment.action_spec())
print('observation_spec:', environment.observation_spec())
print('time_step_spec.observation:', environment.time_step_spec().observation)
print('time_step_spec.step_type:', environment.time_step_spec().step_type)
print('time_step_spec.discount:', environment.time_step_spec().discount)
print('time_step_spec.reward:', environment.time_step_spec().reward)

# Load probability and reward structures
environment(environment._state)
P = []
spec = environment.observation_spec()
for i in range(spec.minimum, spec.maximum + 1):
    P[i] = []
    for j in range(spec.minimum, spec.maximum + 1):
        pass
        #P[i][j] = ts.transition(np.array([i])
        #print(f'{i}, {j}')

# Insert here your computation of a policy from the information above


# Execution cycle
action = np.array(1, dtype=np.int32)
time_step = environment.reset()
print(time_step)
i = 0
while not time_step.is_last() and i < 2:
    time_step = environment.step(action)
    print(time_step)
    i += 1
