#!/usr/bin/env python3

import getopt
import os
import sys

try:
    import conf
except ImportError:
    import conf_template as conf

import modules

def init():
    os.environ.update(conf.envvars)

    args = modules.parse_args()

if __name__ == "__main__":
    init()
