# @Author: dileep
# @Date: 2017-10-29 00:56:13
# @Last Modified by:   dileep

"""
Module the encodes the functionality and the behavior of a metabolite
"""

from cobra import Metabolite as CobraMet
from cobra import Reaction as CobraRxn
import re

class Metabolite:
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

    @classmethod
    def from_exchangerxn(cls, exchange_rxn: CobraRxn) -> Metabolite:
        """
            Construct metabolite class from Cobra exchange reaction
            Parameters:
            ----------
            exchange_rxn : CobraRxn
                Exchange reaction in Cobra format
            Returns:
            -------
            Metabolite
                Metabolite class instance containing the metabolite from the exchange reaction
        """
        pass
