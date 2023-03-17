"""_description_
"""
from nn import Agent
import numpy as np


def uncorr_onestep(agent, sigma):
    """
    Apply uncorrelated update on genes of agent
    Args:
        agent (nn): An agent
        sigma (float): step size
    """
    delta_ih = np.random.normal(0, sigma, (agent.n_feature, agent.n_hidden))
    delta_ho = np.random.normal(0, sigma, (agent.n_hidden, agent.n_out))
    agent.w_ih = agent.w_ih + delta_ih
    agent.w_ho = agent.w_ho + delta_ho
    
def uncorr_nstep(agent, sigma_ih, sigma_ho):
    """
    Apply uncorrelated update on genes of agent
    Args:
        agent (nn): An agent
        sigmas (list(np.ndarray): contains 
            sigma_ih (np.ndarray): step size for each gene at input layer
            sigma_ho (np.ndarray): step size for each gene at output layer
    """
    delta_ih = np.multiply(np.random.normal(0, 1, (agent.n_feature, agent.n_hidden)), sigma_ih)
    delta_ho = np.multiply(np.random.normal(0, 1, (agent.n_hidden, agent.n_out)), sigma_ho)
    agent.w_ih = agent.w_ih + delta_ih
    agent.w_ho = agent.w_ho + delta_ho

mutation = {"onestep": uncorr_onestep,
          "nstep": uncorr_nstep}