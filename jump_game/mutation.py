"""_description_
"""
from nn import Agent
import numpy as np


def uncorr_onestep(agent, sigma, rate):
    """
    Apply uncorrelated update on genes of agent
    Args:
        agent (nn): An agent
        sigma (float): step size
        rate (float): mutation rate
    """
    mask_ih = np.random.rand(agent.n_feature, agent.n_hidden) < rate
    mask_ho = np.random.rand(agent.n_hidden, agent.n_out) < rate
    delta_ih = np.random.normal(0, sigma, (agent.n_feature, agent.n_hidden))
    delta_ho = np.random.normal(0, sigma, (agent.n_hidden, agent.n_out))
    agent.w_ih = agent.w_ih + np.multiply(delta_ih, mask_ih)
    agent.w_ho = agent.w_ho + np.multiply(delta_ho, mask_ho)
    
def uncorr_nstep(agent, sigma_ih, sigma_ho, rate):
    """
    Apply uncorrelated update on genes of agent
    Args:
        agent (nn): An agent
        sigmas (list(np.ndarray): contains 
        sigma_ih (np.ndarray): step size for each gene at input layer
        sigma_ho (np.ndarray): step size for each gene at output layer
        rate (float): mutation rate
    """
    delta_ih = np.multiply(np.random.normal(0, 1, (agent.n_feature, agent.n_hidden)), sigma_ih)
    delta_ho = np.multiply(np.random.normal(0, 1, (agent.n_hidden, agent.n_out)), sigma_ho)
    mask_ih = np.random,rand(agent.n_feature, agent.n_hidden) < rate
    mask_ho = np.random,rand(agent.n_hidden, agent.n_out) < rate
    agent.w_ih = agent.w_ih + np.multiply(delta_ih, mask_ih)
    agent.w_ho = agent.w_ho + np.multiply(delta_ho, mask_ho)

mutation = {"onestep": uncorr_onestep,
          "nstep": uncorr_nstep}
