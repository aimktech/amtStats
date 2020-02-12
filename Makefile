# -*- coding: utf-8 -*-
#
# Simple Statistics Library - Makefile
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

.PHONY: test package clean

# clean the sources tree
clean:
	@rm -rf .mypy_cache .tox
	@rm -rf build dist *.egg-info
	@rm -f .coverage

# execute the test cases
test:
	@tox -e py

# build the python package
package:
	@rm -rf build dist *.egg-info
	@python setup.py sdist bdist_wheel
