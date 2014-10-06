#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

inputs = []
for line in sys.stdin:
    inputs.append(line)

sys.stdout.writelines(os.linesep.join(inputs))
