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
RANDOM_SEED = 1234
PERCENTILE_LIST = [15, 35, 75]


#----- Classes
class TestFactory(unittest.TestCase):

    def setUp(self):
        random.seed(RANDOM_SEED)
        self.stats = Statistics()

        # insert values
        for i in range(100):
            self.stats.update(random.randint(1,1000))

        # compute stats
        self.results = self.stats.compute()

    def test_add_non_int_or_float_value(self):
        with self.assertRaises(TypeError):
            self.stats.update('a')
    
    def test_new_percentiles_list(self):
        # change the list
        old_pct_list = self.stats.percentiles(PERCENTILE_LIST)
        self.assertEqual(self.stats.pct_values, PERCENTILE_LIST)

        # restore the previous one
        self.stats.percentiles(old_pct_list)
        self.assertEqual(self.stats.pct_values, old_pct_list)

    def test_min_max_values(self):
        self.assertEqual(self.results['min'], 6)
        self.assertEqual(self.results['max'], 990)

    def test_sum_count_values(self):
        self.assertEqual(self.results['sum'], 44853)
        self.assertEqual(self.results['count'], 100)

    def test_mean_median_values(self):
        self.assertAlmostEqual(self.results['mean'], 448.53)
        self.assertAlmostEqual(self.results['median'], 481.5)
    
    def test_stddev_value(self):
        self.assertAlmostEqual(self.results['stddev'], 313.2295150524612)
    
    def test_percentile_values(self):
        self.assertAlmostEqual(self.results['10th'], 55.2)
        self.assertAlmostEqual(self.results['30th'], 170.8)
        self.assertAlmostEqual(self.results['50th'], 481.5)
        self.assertAlmostEqual(self.results['70th'], 661.9)
        self.assertAlmostEqual(self.results['90th'], 905.1)
        self.assertAlmostEqual(self.results['95th'], 962.15)
        self.assertAlmostEqual(self.results['97th'], 966.42)
        self.assertAlmostEqual(self.results['99th'], 989.01)

    def test_quantile_values(self):
        self.assertAlmostEqual(self.results['q1'],132.5)
        self.assertAlmostEqual(self.results['q3'], 686.0)
        self.assertAlmostEqual(self.results['iqr'], 553.5)
