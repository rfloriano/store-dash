# This file is part of store-dash.
# https://github.com/rfloriano/store-dash

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Rafael Floriano da Silva <rflorianobr@gmail.com>

# install all dependencies (do not forget to create a virtualenv first)
setup:
	@pip install -U -e .\[tests\] --process-dependency-links

run:
	@cd pydashie && RELOAD=True pydashie
