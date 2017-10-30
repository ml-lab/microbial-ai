# @Author: dileep
# @Last Modified by:   dileep

"""
Module the encodes the functionality and the behavior of a metabolite
"""

import re
import numpy as np
from cobra import Metabolite as CobraMet
from microbial_ai.metabolism import ExReaction

class Metabolite:
    """
        Class that represents a metabolite in the dFBA simulation
        Parameters:
        ----------
        cobra_met : CobraMet
            Metabolite in the Cobra format
        Attributes:
        ----------
        name : str
            Name of the metabolite
        id : str
            ID of the metabolite in the corresponding model
        compartment : str
            Compartment to which the metabolite belongs to
        annotation : str
            Model ids in various databases. Might be empty
        model_id : str
            Model to which the metabolite belongs to
    """
    def __init__(self, cobra_met: CobraMet) -> None:
        self.name = cobra_met.name
        self.id = self._normalize_id(cobra_met.id)
        self.compartment = self._find_compartment(self.id)
        self.annotation = cobra_met.annotation
        self.model_id = cobra_met.model.id

    def __hash__(self) -> int:
        return hash((self.name, self.id))

    def __eq__(self, other: Metabolite) -> bool:
        if self.name == other.name and self.id == other.id:
            return True
        else:
            return False

    @staticmethod
    def _normalize_id(rawid: str) -> str:
        """
            Normalize input id so that all models are consistent
            NOTE: Strings are normalized to the pattern `\w_\D`
            Parameters:
            ----------
            rawid : str
                Raw id extracted from the cobra model or cobra metabolite class
            Returns:
            -------
            str
                Normalized id
        """
        return re.sub(r'(\w)\[([a-z])\]', r'\1_\2', rawid)

    @staticmethod
    def _find_compartment(normid: str) -> str:
        """
            Returns the compartment of the input normalized id
            Parameters:
            ----------
            normid : str
                Normalized id
            Returns:
            -------
            str
                Compartment the metabolite is located in
        """
        _, compid = normid.split('_')
        if compid == 'c':
            compartment = 'cytosol'
        elif compid == 'e':
            compartment = 'extracellular'
        else:
            compartment = 'unknown'
        return compartment

class ExMetabolite(Metabolite):
    """
        Class that represents an external metabolite in the dFBA simulation
        Parameters:
        ----------
        cobra_met : CobraMet
            Metabolite in the Cobra format
        Attributes:
        ----------
        name : str
            Name of the metabolite
        id : str
            ID of the metabolite in the corresponding model
        compartment : str
            Compartment to which the metabolite belongs to
        annotation : str
            Model ids in various databases. Might be empty
        model_id : str
            Model to which the metabolite belongs to
    """
    def __init__(self, cobra_met: CobraMet) -> None:
        super().__init__(cobra_met)
        assert self.compartment == 'extracellular', "Metabolite not extracellular"
        self.concentration = np.float()
        self.equation #make this a sympy equation

    def update_equation(self, exchange_rxn: ExReaction) -> bool:
        """
            Add update rule from the given exchange reaction and returns True if success
            Parameters:
            ----------
            exchange_rxn : ExReaction
                Exchange reaction that involves the current metabolite
            Returns:
            -------
            bool
                True if the metabolite exchange rule was successfully updated otherwise False
        """
        #1. Check whether reaction has met
        #2. Update self.eqauation with references to the reactions
        pass

    def do_step(self, dt: np.float) -> np.float:
        """
            Updates the concentration for the given time-step and returns the new concentration
            Parameters:
            ----------
            dt : np.float
                Time step for which the concentration has to be updated
            Returns:
            -------
            np.float
                New concentration after update
        """
        #1. Run the update rule with given time step
        pass

    @classmethod
    def from_exreaction(cls, exchange_rxn: ExReaction) -> "ExMetabolite":
        """
            Construct metabolite class from exchange reaction
            Parameters:
            ----------
            exchange_rxn : CobraRxn
                Exchange reaction in Cobra format
            Returns:
            -------
            ExMetabolite
                ExMetabolite class instance containing the metabolite from the exchange reaction
        """
        pass
