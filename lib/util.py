from __future__ import print_function

import contextlib
import dbm
import shlex
import subprocess
import sys
import time

from na_constants import HOSTS_DB


def exec_cmd(cmd, quiet=False):
    try:
        return subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        if quiet:
            return
        if not exc.output:
            raise
        raise RuntimeError('{}\nOutput: {}'.format(cmd, exc.output.strip()))


def exit_with_msg(msg):
    print(msg)
    sys.exit(1)


@contextlib.contextmanager
def host_db():
    db = dbm.open(HOSTS_DB, 'c')
    try:
        yield db
    finally:
        db.close()


def localtz():
    return time.tzname[time.daylight]


def print_columns(rows):
    lens = []
    for col in zip(*rows):
        lens.append(max([len(v) for v in col]))
    format_ = "  ".join(["{:<" + str(l) + "}" for l in lens])
    for row in rows:
        print(format_.format(*row))
