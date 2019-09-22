#!/usr/bin/env python
from __future__ import print_function
import argparse
import os

from na_constants import FULL_LUN, VGROUP
from util import exec_cmd


def create_lv(name, size):
    exec_cmd('lvcreate -T -V {} -n {} {}'.format(size, name, FULL_LUN))
    if not os.path.exists('/dev/mapper/{}-{}'.format(VGROUP, name)):
        raise EnvironmentError('Could not find path to {} in dev mapper'.format(name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Name of LUN to create.')
    parser.add_argument('--size', required=True, help='LUN size.')
    args = parser.parse_args()
    create_lv(args.name, args.size)
    print('Successfully created: {}'.format(args.name))


if __name__ == "__main__":
    main()
