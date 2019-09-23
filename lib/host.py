import util


def create_host(name, iqn):
    with util.host_db() as db:
        db[name] = iqn


def delete_host(name):
    with util.host_db() as db:
        del db[name]


def list_hosts(names):
    host_info = []
    with util.host_db() as db:
        for host in db.keys():
            if names and host not in names:
                continue
            host_info.append({'name': host, 'iqn': db[host], 'wwn': '-', 'host group': '-'})
    for name in names:
        if name not in (host['name'] for host in host_info):
            util.exit_with_msg('Error on {}: Host does not exist.'.format(name))
    return host_info
