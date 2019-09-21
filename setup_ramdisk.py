#!/usr/bin/env python
from __future__ import print_function
import argparse
import os
import shlex
import subprocess


KB_TO_GB = 1024**2


def exec_cmd(cmd):
    return subprocess.check_output(shlex.split(cmd))


def create_ramdisk(size):
    """Create a ramdisk block device.

    Args:
        size (int): Size in KB of ramdisk.

    Returns:
        bdev (str):  Name of block device under /dev.
    """
    exec_cmd('modprobe brd rd_nr=1 rd_size={} max_part=1'.format(size))
    bdevs = [fname for fname in os.listdir('/dev/') if fname.startswith('ram')]
    if not bdevs:
        raise EnvironmentError('Could not find any ramdisk bdev after creation.')
    for bdev in bdevs:
        bdev_size = exec_cmd('blockdev --getsize64 /dev/{}'.format(bdev)).strip()
        if int(bdev_size) / 1024 == size:  # blockdev size is bytes
            return bdev
    raise EnvironmentError('Could not find ramdisk bdev of size {}.'.format(size))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('size', type=int, default=5*KB_TO_GB,
                        help='Size of ramdisk block device in KB.')
    args = parser.parse_args()
    bdev = create_ramdisk(args.size)
    print('Successfully created: /dev/{}'.format(bdev))


if __name__ == "__main__":
    main()
