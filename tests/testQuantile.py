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
import random

from amtStats import Statistics


#----- Globals
RANDOM_SEED_VALUE = 1234
RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100
RANDOM_ODD_VALUE = 35
RANDOM_EVEN_VALUE = 78

#----- Classes
class TestQuantiles(unittest.TestCase):

    def setUp(self):
        random.seed(RANDOM_SEED_VALUE)
        self.obj = Statistics()

    def test_Q1_odd(self):
        for _ in range(RANDOM_ODD_VALUE):
            self.obj.update(random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE))
        
        median = self.obj._quantile(self.obj.values, 1)
        self.assertEqual(median, 12.0)

    def test_Q2_odd(self):
        for _ in range(RANDOM_ODD_VALUE):
            self.obj.update(random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE))
        
        median = self.obj._quantile(self.obj.values, 2)
        self.assertEqual(median, 45.0)

    def test_Q3_odd(self):
        for _ in range(RANDOM_ODD_VALUE):
            self.obj.update(random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE))
        
        median = self.obj._quantile(self.obj.values, 3)
        self.assertEqual(median, 77.0)


    def test_Q1_even(self):
        for _ in range(RANDOM_EVEN_VALUE):
            self.obj.update(random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE))
        
        median = self.obj._quantile(self.obj.values, 1)
        self.assertEqual(median, 12.0)

    def test_Q2_even(self):
        for _ in range(RANDOM_EVEN_VALUE):
            self.obj.update(random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE))
        
        median = self.obj._quantile(self.obj.values, 2)
        self.assertEqual(median, 44.0)

    def test_Q3_even(self):
        for _ in range(RANDOM_EVEN_VALUE):
            self.obj.update(random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE))
        
        median = self.obj._quantile(self.obj.values, 3)
        self.assertEqual(median, 72.0)

    def test_empty_values(self):
        with self.assertRaises(ValueError):
            self.obj._quantile([], 1)
        
    def test_only_one_value(self):
        self.obj.update(42)
        self.assertEqual(self.obj._quantile(self.obj.values, 1), 42)
        