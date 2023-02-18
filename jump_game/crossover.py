"""_description_
"""
import nn

def crossover(agent1, agent2):
        """
        Apply crossover on the chronosome of two agents
        Args:
            agent1, agent2 (nn): nn objects
        """
    offspring1 = nn(agent1.n_feature, agent1.n_hidden, agent1.n_out)
    offspring2 = nn(agent1.n_feature, agent1.n_hidden, agent1.n_out)
    
    offspring1.w_ih = agent1.w_ih
    offspring1.w_ho = agent2.w_ho
    
    offspring2.w_ih = agent2.w_ih
    offspring2.w_ho = agent1.w_ho

    return offspring1, offspring2
