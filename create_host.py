#!/usr/bin/env python
from __future__ import print_function
import argparse
import dbm

from na_constants import HOSTS_DB


def create_host(name, iqn):
    db = dbm.open(HOSTS_DB, 'c')
    db[name] = iqn


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Name of host to create.')
    parser.add_argument('iqn', help='IQN of host to create.')
    args = parser.parse_args()
    create_host(args.name, args.iqn)
    print('Successfully created: {}'.format(args.name))


if __name__ == "__main__":
    main()
