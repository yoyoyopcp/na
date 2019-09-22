#!/usr/bin/env python
from __future__ import print_function
import argparse

from na_constants import FULL_LUN, THINPOOL, VGROUP
from util import exec_cmd


def setup_lun_pool(bdev):
    exec_cmd('pvcreate {}'.format(bdev))
    exec_cmd('vgcreate {} {}'.format(VGROUP, bdev))
    exec_cmd('lvcreate -l 95%FREE -n {} {}'.format(THINPOOL, VGROUP))
    exec_cmd('lvconvert --type thin-pool -y {}'.format(FULL_LUN))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bdev', help='Path to backend block device.')
    args = parser.parse_args()
    setup_lun_pool(args.bdev)
    print('Successfully created: {}'.format(FULL_LUN))


if __name__ == "__main__":
    main()
