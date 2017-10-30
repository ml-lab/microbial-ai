# @Author: dileep
# @Last Modified by:   dileep

from cobra import Reaction as CobraRxn
from microbial_ai.metabolism import Metabolite, ExMetabolite
from microbial_ai import Microbe

class Reaction:
    """
        Class that represents a reaction in the dFBA simulation
        Parameters:
        ----------
        cobra_rxn : CobraRxn
            Metabolic reaction in the Cobra format
        Attributes:
        ----------
        name : str
            Name of the reactions
        flux : np.float
            Flux through the reaction
    """
    def __init__(self, cobra_rxn: CobraRxn) -> None:
        pass

    def __hash__(self) -> int:
        pass

    def __eq__(self, other: Reaction) -> bool:
        pass

    def update_flux(self, microbe_model: Microbe) -> bool:
        """
            Updates the value of reaction flux given the microbial_model
            Returns True if update was successful
            Parameters:
            ----------
            microbe_model : Microbe
                Microbe model that the reaction is a part of
            Returns:
            -------
            bool
                True if the reaction was successfully updated otherwise False
        """
        pass

class ExReaction(Reaction):
    pass
