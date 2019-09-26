import os

from na_constants import FULL_LUN, VGROUP
import vol
import util


def create_vol(name, size):
    try:
        util.exec_cmd('lvcreate -T -V {} -n {} {}'.format(size, name, FULL_LUN))
    except RuntimeError as exc:
        if 'already exists' in str(exc):
            util.exit_with_msg('Error on {}: Volume already exists'.format(name))
        raise
    if not os.path.exists('/dev/mapper/{}-{}'.format(VGROUP, name)):
        raise EnvironmentError('Could not find path to {} in dev mapper'.format(name))


def destroy_vol(name):
    rename_vol(name, '.' + name)


def recover_vol(name):
    rename_vol('.' + name, name)


def eradicate_vol(name):
    util.exec_cmd('lvremove -y {}/.{}'.format(VGROUP, name))


def connect_vol(name, host):
    vol_info = vol.list_vols([name])[0]
    with util.host_db() as db:
        if host not in db:
            util.exit_with_msg('Error on {}: Host does not exist.'.format(host))
        iqn = db[host]
    vol_path = '/dev/mapper/{}-{}'.format(VGROUP, vol_info['name'])
    lun_number = util.get_unused_lun()
    util.exec_cmd('tgtadm --lld iscsi --op new --mode logicalunit --tid 1 '
                  '--lun {} -b {}'.format(lun_number, vol_path))
    util.exec_cmd('tgtadm --lld iscsi --op update --mode logicalunit --tid 1 '
                  '--lun {} --params scsi_sn={},vendor_id=PURESTORAGE'
                  .format(lun_number, vol_info['serial']))
    try:
        util.exec_cmd('tgtadm --lld iscsi --op bind --mode target --tid 1 -I ALL')
    except RuntimeError as exc:
        if 'rule already exists' not in str(exc):
            raise


def disconnect_vol(name, host):
    vol_info = vol.list_vols([name])[0]
    with util.host_db() as db:
        if host not in db:
            util.exit_with_msg('Error on {}: Host does not exist.'.format(host))
        iqn = db[host]
    lun_number = util.get_lun_number(name)
    util.exec_cmd('tgtadm --lld iscsi --op delete --mode logicalunit --tid 1 '
                  '--lun {}'.format(lun_number))


def rename_vol(old_name, new_name):
    try:
        util.exec_cmd('lvrename {}/{} {}'.format(VGROUP, old_name, new_name))
    except RuntimeError as exc:
        if 'already exists' in str(exc):
            util.exit_with_msg('Error on {}: Volume already exists.'.format(new_name))
        elif 'not found in' in str(exc):
            util.exit_with_msg('Error on {}: Volume does not exist.'.format(old_name))
        raise


def list_connected_vols(names):
    vols = []
    for vol, lun_num in get_luns():
        pass


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
