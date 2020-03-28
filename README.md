# MDP Environments for Inverse Reinforcement Learning

This is a fork of [https://github.com/MatthewJA/Inverse-Reinforcement-Learning](https://github.com/MatthewJA/Inverse-Reinforcement-Learning) that includes the following MDP domains:

- Gridworld (Sutton, 1998)
- Objectworld (Levine et al., 2011)

## Requirements
- NumPy

## Module documentation

### mdp

#### gridworld

Implements the gridworld MDP.

**Classes, instance attributes, methods:**

- `Gridworld(grid_size, wind, discount)`: Gridworld MDP.
    - `actions`: Tuple of (dx, dy) actions.
    - `n_actions`: Number of actions. int.
    - `n_states`: Number of states. int.
    - `grid_size`: Size of grid. int.
    - `wind`: Chance of moving randomly. float.
    - `discount`: MDP discount factor. float.
    - `transition_probability`: NumPy array with shape (n_states, n_actions, n_states) where `transition_probability[si, a, sk]` is the probability of transitioning from state si to state sk under action a.
    - `feature_vector(i, feature_map="ident")`: Get the feature vector associated with a state integer.
    - `feature_matrix(feature_map="ident")`: Get the feature matrix for this gridworld.
    - `int_to_point(i)`: Convert a state int into the corresponding coordinate.
    - `point_to_int(p)`: Convert a coordinate into the corresponding state int.
    - `neighbouring(i, k)`: Get whether two points neighbour each other. Also returns true if they are the same point.
    - `reward(state_int)`: Reward for being in state state_int.
    - `average_reward(n_trajectories, trajectory_length, policy)`: Calculate the average total reward obtained by following a given policy over n_paths paths.
    - `optimal_policy(state_int)`: The optimal policy for this gridworld.
    - `optimal_policy_deterministic(state_int)`: Deterministic version of the optimal policy for this gridworld.
    - `generate_trajectories(n_trajectories, trajectory_length, policy, random_start=False)`: Generate n_trajectories trajectories with length trajectory_length, following the given policy.

#### objectworld

Implements the objectworld MDP described in Levine et al. 2011.

**Classes, instance attributes, methods:**

- `OWObject(inner_colour, outer_colour)`: Object in objectworld.
    - `inner_colour`: Inner colour of object. int.
    - `outer_colour`: Outer colour of object. int.

- `Objectworld(grid_size, n_objects, n_colours, wind, discount)`: Objectworld MDP.
    - `actions`: Tuple of (dx, dy) actions.
    - `n_actions`: Number of actions. int.
    - `n_states`: Number of states. int.
    - `grid_size`: Size of grid. int.
    - `n_objects`: Number of objects in the world. int.
    - `n_colours`: Number of colours to colour objects with. int.
    - `wind`: Chance of moving randomly. float.
    - `discount`: MDP discount factor. float.
    - `objects`: Set of objects in the world.
    - `transition_probability`: NumPy array with shape (n_states, n_actions, n_states) where `transition_probability[si, a, sk]` is the probability of transitioning from state si to state sk under action a.
    - `feature_vector(i, discrete=True)`: Get the feature vector associated with a state integer.
    - `feature_matrix(discrete=True)`: Get the feature matrix for this gridworld.
    - `int_to_point(i)`: Convert a state int into the corresponding coordinate.
    - `point_to_int(p)`: Convert a coordinate into the corresponding state int.
    - `neighbouring(i, k)`: Get whether two points neighbour each other. Also returns true if they are the same point.
    - `reward(state_int)`: Reward for being in state state_int.
    - `average_reward(n_trajectories, trajectory_length, policy)`: Calculate the average total reward obtained by following a given policy over n_paths paths.
    - `generate_trajectories(n_trajectories, trajectory_length, policy)`: Generate n_trajectories trajectories with length trajectory_length, following the given policy.
