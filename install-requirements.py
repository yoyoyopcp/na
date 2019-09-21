#!/usr/bin/env python
from __future__ import print_function

import apt

PKGS = ['lvm2', 'tgt', 'thin-provisioning-tools']

cache = apt.cache.Cache()
cache.update()
cache.open()

for pkg_name in PKGS:
    pkg = cache[pkg_name]
    if pkg.is_installed:
        print("{} already installed".format(pkg_name))
    else:
        pkg.mark_install()
        try:
            cache.commit()
        except Exception:
            raise EnvironmentError('Failed to install {}'.format(pkg_name))
