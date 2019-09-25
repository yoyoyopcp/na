#!/usr/bin/env python
from __future__ import print_function
import argparse

from lib.na_constants import FULL_LUN, TARGET_IQN, THINPOOL, VGROUP
from lib.util import exec_cmd


def setup_lun_pool(bdev):
    exec_cmd('pvcreate {}'.format(bdev))
    exec_cmd('vgcreate {} {}'.format(VGROUP, bdev))
    exec_cmd('lvcreate -l 95%FREE -n {} {}'.format(THINPOOL, VGROUP))
    exec_cmd('lvconvert --type thin-pool -y {}'.format(FULL_LUN))


def setup_tgt():
    try:
        exec_cmd('tgtadm --lld iscsi --op new --mode target --tid 1 --targetname {}'
                 .format(TARGET_IQN))
    except RuntimeError as exc:
        if not 'already exists' in str(exc):
            raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bdev', help='Path to backend block device.')
    args = parser.parse_args()
    setup_lun_pool(args.bdev)
    setup_tgt()
    print('Successfully created: {}'.format(FULL_LUN))


if __name__ == "__main__":
    main()
