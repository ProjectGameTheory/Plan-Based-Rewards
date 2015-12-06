# Plan-Based-Rewards

## Source

Plan-Based Reward Shaping for Multi-Agent Reinforcement Learning
**SAM DEVLIN** and **DANIEL KUDENKO**
_The Knowledge Engineering Review, Vol. 00:0, 1–24_
2004, Cambridge University Press
DOI: 10.1017/S000000000000000

## Overview

Sarsa algorithm with plan-based rewards:

$$Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + F(s,s') + \gamma Q(s',a') - Q(s,a) \right]$$

where 

$$F(s,s') = \gamma \Phi(s') - \Phi(s) $$

### Agent Type 1

For the agents with joint-plan based reward shaping and individual-plan based reward shaping, the potential function $$$\Phi(s)$$$ becomes

$$\Phi(s) = \omega * \text{CurrentStepInPlan}$$

If the current state is not in the state-based representation of the agent’s plan, then the potential used is that of the last state experienced that was in the plan. the potential of all goal/final states is set to zero. we have set the scaling factor $$$\omega$$$ so that the maximum potential of a state is the maximum reward of the environment.

$$\omega = \text{MaxRewards}/\text{NumStepsInPlan}$$

### Agent Type 2

A team of agents with no prior knowledge/shaping.

### Agent Type 3

A team with the domain-specific knowledge that collecting flags is beneficial. These flag-based agents value a state’s potential equal to one hundred times the number of flags it alone has collected.

$$\Phi(s) = 100 * \text{NumFlagsCollected}$$

### Agent Type 4

The combination of the flag-based heuristic with the general methods of joint-plan-based and individual-plan-based shaping. Here the potential function is

$$\Phi(s) = (\text{CurrentStepInPlan}*\text{NumFlagsCollected})*\omega$$

$$\omega = \text{MaxReward}/(\text{NumStepsInPlan}+\text{NumFlagsInWorld}) $$

### Environment

Once an agent reaches the goal state their episode is over regardless of the number of flags collected. The entire episode is completed when both agents reach the goal state. At this time both agents receive a reward equal to one hundred times the number of flags they have collected in combination. No other rewards are given at any other time.

All agents, regardless of shaping, implemented SARSA with $$$\epsilon$$$−greedy action selection and eligibility traces. For all experiments, the agents’ parameters were set such that $$$\alpha$$$ = 0.1, $$$\gamma$$$ = 0.99, $$$\epsilon$$$ = 0.1 and $$$\lambda$$$ = 0.4. For these experiments, all initial $$$Q$$$-values were zero.

All experiments are repeated 30 times. The plots consist of the mean discounted reward per episode.
