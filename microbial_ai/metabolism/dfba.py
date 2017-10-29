# @Author: dileep
# @Date: 2017-10-28 17:43:34
# @Last Modified by:   dileep

"""
Module that handles the dFBA simulation of the genome scale metabolic network
"""

from typing import Sequence, FrozenSet
import cobra
from microbial_ai import Metabolite, Microbe

class DFBA:
    """
        Class that handles the dFBA simulation (static optimization procedure)
        Parameters:
        ----------
        init_models : Tuple of cobra.core.model.Model
            Tuple of organisms (models) present at the start of the simulation
        init_mets : Tuple of Metabolites
            Tuple of metabolites present at the start of the simulation
        Attributes:
        ----------
        models : frozenset
            List of organims in the simulation
        metabolites : frozenset
            List of metaboites in the simulation
    """
    def __init__(self, init_models: Sequence[Microbe], init_mets: Sequence[Metabolite]) -> None:
        self.models = frozenset(init_models)
        self.metabolites = frozenset(init_mets)

    @property
    def model_names(self) -> FrozenSet[str]:
        """
            Get names of the organisms currently in the simulation
            Returns:
            -------
            FrozenSet[str]
                FrozenSet of all the models in the simulation
        """
        return frozenset((x.name for x in self.models))

    @property
    def metabolite_names(self) -> FrozenSet[str]:
        """
            Get names of the metabolites currently in the simulation
            Returns:
            -------
            FrozenSet[str]
                FrozenSet of all the metabolites in the simulation
        """
        return frozenset((x.name for x in self.metabolites))

    #TODO: Update procedures for models and metabolites

    #TODO: Implement a method using a deque object that lets the simulation class pick models one at a time
    # Need to randomize it?
