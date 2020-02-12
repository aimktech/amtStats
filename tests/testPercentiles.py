# -*- coding: utf-8 -*-
# 
# Unit tests for the Simple Statistics library
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
import unittest

from amtStats import Statistics

#----- Classes
class TestPercentiles(unittest.TestCase):
    
    def populateStats(self):
        stats = Statistics()
        for i in range(100):
            stats.update(i)
        return stats

    def test_empty_values(self):
        stats = Statistics()
        with self.assertRaises(ValueError):
            stats._percentile(50)
    
    def test_only_one_value(self):
        stats = Statistics()
        stats.update(1234)
        self.assertEqual(stats._percentile(35), 1234)
        self.assertEqual(stats._percentile(50), 1234)
        self.assertEqual(stats._percentile(75), 1234)
    
    def test_float_rank_is_too_big(self):
        stats = self.populateStats()
        with self.assertRaises(ValueError):
            stats._percentile(3.5)
    
    def test_int_rank_is_too_big(self):
        stats = self.populateStats()
        with self.assertRaises(ValueError):
            stats._percentile(150)