# -*- coding: utf-8 -*-
#
# co_co_cm_continuous_input_model.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

from pynestml.cocos.co_co import CoCo
from pynestml.meta_model.ast_model import ASTModel
from pynestml.utils.continuous_input_processing import ContinuousInputProcessing


class CoCoCmContinuousInputModel(CoCo):
    @classmethod
    def check_co_co(cls, neuron: ASTModel):
        """
        Checks if this compartmental condition applies to the handed over neuron.
        If yes, it checks the presence of expected functions and declarations.
        :param neuron: a single neuron instance.
        :type neuron: ast_neuron
        """
        return ContinuousInputProcessing.check_co_co(neuron)
