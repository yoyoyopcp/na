from __future__ import print_function

import contextlib
import dbm
import shlex
import subprocess
import sys
import time

from na_constants import HOSTS_DB


def exec_cmd(cmd, quiet=False, shell=False):
    try:
        if not shell:
            return subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        if quiet:
            return
        if not exc.output:
            raise
        raise RuntimeError('{}\nOutput: {}'.format(cmd, exc.output.strip()))


def exit_with_msg(msg):
    print(msg)
    sys.exit(1)


def get_lun_number(vol_name):
    for vol, lun_num in get_luns():
        if vol == vol_name:
            return lun_num
    raise ValueError('{} not found'.format(vol_name))


def get_luns():
    try:
        output = exec_cmd('tgtadm --mode target --op show --lld iscsi | '
                          'egrep "LUN:|store path"',
                          shell=True)
    except subprocess.CalledProcessError:
        raise StopIteration
    lines = output.splitlines()
    for num_line, vol_line in zip(lines[::2], lines[1::2]):
        yield vol_line.split('-')[-1].strip(), int(num_line.strip().split()[-1])


def get_unused_lun():
    try:
        output = exec_cmd('tgtadm --mode target --op show --lld iscsi | egrep LUN:',
                          shell=True)
    except subprocess.CalledProcessError:
        return 1
    luns = output.splitlines()
    for num, lun in enumerate(luns):
        if num != int(lun.strip().split()[-1]):
            return num
    return num + 1


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
