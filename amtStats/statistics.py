# -*- coding: utf-8 -*-
#
# Simple Statistics Library
# 
# Copyright 2020 AI Mechanics & Tech
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#----- Imports
from __future__ import annotations
from typing import List, Dict, Union

import math


#----- Types aliases
T_VALUE = Union[int, float]
T_VALUES = List[T_VALUE]


#----- Classes
class Statistics:
    """Generic Statistics class"""
    PERCENTILES_RANK: List[int] = [ 10, 30, 50, 70, 90, 95, 97, 99 ]

    def __init__(self) -> None:
        """Constructor"""
        self.values: T_VALUES = []
        self.pct_values: List[int] = self.PERCENTILES_RANK

    def _percentile(self, rank: T_VALUE) -> float:
        """Return the percentile value on a dataset for the specified rank

        :param values: The list of values to get the percentile from
        :param rank: The percentile rank expressed as an integer [0,100] or float [0,1]

        The value returned is the linear interpolation between the two closest ranks.
        """

        # no values in the list
        if len(self.values) == 0:
            raise ValueError("There are no values in the array")

        # only one value
        if len(self.values) == 1:
            return self.values[0]

        # check the rank
        if isinstance(rank, float) and not (0.0 <= rank <= 1.0):
            raise ValueError("Float rank should be between 0.0 and 1.0")

        if isinstance(rank, int) and not (0 <= rank <= 100):
            raise ValueError("Integer rank should be between 0 and 100")
        else:
            rank = rank / 100.0

        # sort the values
        array = self.values.copy()
        array.sort()

        # compute the percentile value
        x = rank * (len(array) - 1)
        y = int(x)
        z = x % 1
        
        return array[y] + z * (array[y+1] - array[y])

    def _quantile(self, values: T_VALUES, quantile: int = 2) -> float:
        """Return the quantile (Q1,Q2,Q3) of the values"""

        # no values in the list
        if len(values) == 0:
            raise ValueError("There are no values in the array")

        # only one value
        if len(values) == 1:
            return values[0]

        # copy the values
        array = values.copy()
        array.sort()

        # length and mid point
        alen = len(array)
        amid = alen >> 1

        if quantile == 1:
            return self._quantile(array[:amid])
        elif quantile == 3:
            return self._quantile(array[amid:])
        else:
            if alen & 1 == 1:
                # array is odd
                return array[amid]
            else:
                # array is even, take mid-point
                return (array[amid-1] + array[amid]) / 2

    def update(self, value: T_VALUE) -> None:
        """Update the statistics array"""
        if not isinstance(value, (int, float)):
            raise TypeError
        self.values.append(value)

    def percentiles(self, pct_values: List[int]) -> List[int]:
        """Change the default percentiles values
        
        :param pct_values: the new list of percentiles

        :return: the previous list of percentiles values
        """
        old_list = self.pct_values.copy()
        self.pct_values = pct_values
        return old_list

    def compute(self) -> Dict[str, T_VALUE]:
        """Compute the statistics
        
        :return: a dict with the statistics computed from the array
        """
        result = {
            'min': min(self.values),
            'max': max(self.values),
            'count': len(self.values),
            'sum': sum(self.values),
            'mean': round(sum(self.values) / len(self.values), 3),
            'median': round(self._percentile(50), 3)
        }

        # retrieve the interquartile range
        result['q1'] = round(self._quantile(self.values, 1), 3)
        result['q3'] = round(self._quantile(self.values, 3), 3)
        result['iqr'] = result['q3'] - result['q1']

        # compute the standard deviation
        acc = 0.0
        for value in self.values:
            acc += (value - result['mean'])**2
        result['stddev'] = round(math.sqrt(acc/result['count']), 7)

        # compute the percentiles
        for percent in self.pct_values:
            result[f'{percent}th'] = round(self._percentile(percent), 3)
        
        return result
