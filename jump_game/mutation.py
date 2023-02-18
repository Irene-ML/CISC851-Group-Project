"""_description_
"""
import nn

def uncorr_onestep(agent, sigma):
    """
    Apply uncorrelated update on genes of agent
    Args:
        agent (nn): An agent
        sigma (float): step size
    """
    delta_ih = np.random.normal(0, sigma, (nn.n_feature, nn.n_hidden))
    delta_ho = np.random.normal(0, sigma, (nn.n_hidden, nn.n_out))
    agent.w_ih = agent.w_ih + delta_ih
    agent.w_ho = agent.w_ho + delta_ho
    
def uncorr_nstep(agent, sigma_ih, sigma_ho):
    """
    Apply uncorrelated update on genes of agent
    Args:
        agent (nn): An agent
        sigma_ih (np.ndarray): step size for each gene at input layer
        sigma_ho (np.ndarray): step size for each gene at output layer
    """
    delta_ih = np.multiply(p.random.normal(0, 1, (nn.n_feature, nn.n_hidden)), sigma_ih)
    delta_ho = np.multiply(p.random.normal(0, 1, (nn.n_hidden, nn.n_out)), sigma_ho)
    agent.w_ih = agent.w_ih + delta_ih
    agent.w_ho = agent.w_ho + delta_ho
    
