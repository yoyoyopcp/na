from util import host_db


def create_host(name, iqn):
    with host_db() as db:
        db[name] = iqn


def delete_host(name):
    with host_db() as db:
        del db[name]
