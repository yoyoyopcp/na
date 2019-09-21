#!/usr/bin/env python
from __future__ import print_function
import argparse

from util import exec_cmd


def setup_vg(bdev, name):
    exec_cmd('pvcreate {}'.format(bdev))
    exec_cmd('vgcreate {} {}'.format(name, bdev))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bdev', help='Path to backend block device.')
    parser.add_argument('--name', default='vg1', help='Name of volume group to create.')
    args = parser.parse_args()
    setup_vg(args.bdev, args.name)
    print('Successfully created: {}'.format(args.name))


if __name__ == "__main__":
    main()
