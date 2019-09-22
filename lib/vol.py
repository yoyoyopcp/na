import os

from na_constants import FULL_LUN, VGROUP
from util import exec_cmd


def create_vol(name, size):
    exec_cmd('lvcreate -T -V {} -n {} {}'.format(size, name, FULL_LUN))
    if not os.path.exists('/dev/mapper/{}-{}'.format(VGROUP, name)):
        raise EnvironmentError('Could not find path to {} in dev mapper'.format(name))


def destroy_vol(name):
    pass


def eradicate_vol(name):
    pass


def connect_vol(name, host):
    pass


def list_vols(names):
    all_vols = os.listdir('/dev/{}'.format(VGROUP))
    if not names:
        return all_vols
    return [vol for vol in names if vol in all_vols]
