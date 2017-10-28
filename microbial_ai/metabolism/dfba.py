# @Author: dileep
# @Date: 2017-10-28 17:43:34
# @Last Modified by:   dileep

"""
Module that handles the dFBA simulation of the genome scale metabolic network
"""

from typing import Sequence
import cobra
from cobra import Model
from microbial_ai import Metabolites

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
        models : List
            List of organims in the simulation
        metabolites : List
            List of metaboites in the simulation
    """
    def __init__(self, init_models: Sequence[Model], init_mets: Sequence[Metabolites]) -> None:
        pass
