import shlex
import subprocess


def exec_cmd(cmd):
    try:
        return subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        if not exc.output:
            raise
        raise RuntimeError('{}\nOutput: {}'.format(cmd, exc.output.strip()))
