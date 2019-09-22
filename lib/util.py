import contextlib
import dbm
import shlex
import subprocess

from na_constants import HOSTS_DB


def exec_cmd(cmd):
    try:
        return subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        if not exc.output:
            raise
        raise RuntimeError('{}\nOutput: {}'.format(cmd, exc.output.strip()))


@contextlib.contextmanager
def host_db():
    db = dbm.open(HOSTS_DB, 'c')
    try:
        yield db
    finally:
        db.close()
