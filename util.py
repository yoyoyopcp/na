import shlex
import subprocess


def exec_cmd(cmd):
    return subprocess.check_output(shlex.split(cmd))
