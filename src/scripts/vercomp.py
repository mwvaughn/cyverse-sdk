#!/usr/bin/env python

import argparse
from distutils.version import LooseVersion

parser = argparse.ArgumentParser()
parser.add_argument("vers1")
parser.add_argument("vers2")
args = parser.parse_args()

vers1 = LooseVersion(args.vers1)
vers2 = LooseVersion(args.vers2)

print vers1, vers2

if vers1 == vers2:
    print '1'
elif vers1 < vers2:
    print '0'
else:
    print '2'

