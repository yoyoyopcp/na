import os

from na_constants import FULL_LUN, VGROUP
import util


def create_vol(name, size):
    util.exec_cmd('lvcreate -T -V {} -n {} {}'.format(size, name, FULL_LUN))
    if not os.path.exists('/dev/mapper/{}-{}'.format(VGROUP, name)):
        raise EnvironmentError('Could not find path to {} in dev mapper'.format(name))


def destroy_vol(name):
    rename_vol(name, '.' + name)


def recover_vol(name):
    rename_vol('.' + name, name)


def eradicate_vol(name):
    util.exec_cmd('lvremove -y {}/.{}'.format(VGROUP, name))


def connect_vol(name, host):
    pass


def rename_vol(old_name, new_name):
    util.exec_cmd('lvrename {}/{} {}'.format(VGROUP, old_name, new_name))


def list_vols(names):
    vol_info = []
    output = util.exec_cmd('lvs --separator , -o lv_name,lv_time,lv_size,uuid '
                           '--aligned --noheadings')
    for vol in output.splitlines():
        name, timestamp, size, uuid = [part.strip() for part in vol.split(',')]
        if name == 'tp1' or name.startswith('.'):
            continue
        if names and name not in names:
            continue
        size = size.replace('.00', '').upper()
        timestamp = '{} {}'.format(timestamp.rsplit(' ', 1)[0], util.localtz())
        vol_info.append(dict(name=name, size=size, source='-',
                             created=timestamp, serial=uuid))

    for name in names:
        if name not in (v['name'] for v in vol_info):
            util.exit_with_msg('Error on {}: Volume does not exist.'.format(name))

    return vol_info
