import gym

# We will load a DiscreteEnv and retrieve the probability and reward
# information
env = gym.make("FrozenLake8x8-v1", desc=None, map_name=None)
"""
DiscreteEnv has an attribute P which holds everything er want as a
dictionary of lists:
P[s][a] = [(probability, nextstate, reward, done), ...]
"""
# first, we initialize the structures with zeros
prob = {i: {j: {a: 0 for a in range(env.nA)}
            for j in range(env.nS)}
        for i in range(env.nS)}
rewd = {i: {j: {a: 0 for a in range(env.nA)}
            for j in range(env.nS)}
        for i in range(env.nS)}
# then, we fill them with the actual information
for i in range(env.nS):
    for a in range(env.nA):
        for (p, j, r, d) in env.P[i][a]:
            prob[i][j][a] += p
            rewd[i][j][a] += r

# Policy computation: here's where YOU code
"""
Insert your clever policy computation here! make sure to replace the
policy dictionary below by the results of your computation
"""
T = 2  # Given horizon
policy = {t: {i: env.action_space.sample()
              for i in range(env.nS)}
          for t in range(T)}

# Policy evaluation: here's where YOU also code
"""
Insert here your code to evaluate
the total expected rewards over the planning horizon T
if one follows your policy. Do the same for a random policy (i.e. the
sample policy given above). As a sanity check, your policy should get an
expected reward of at least the one obtained by the random policy!
"""

# Simulation: you can try your policy here, just remove the false conditional
if True:
    state = env.reset()
    for t in range(T):
        env.render()
        action = policy[t][state]
        print(f"Action = {action}")
        state, reward, done, _ = env.step(action)
        # if the MDP is stuck, we end the simulation here
        if done:
            print(f"Episode finished after {t + 1} timesteps")
            break
    env.close()
