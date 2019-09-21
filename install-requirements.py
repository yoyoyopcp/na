#!/usr/bin/env python
import apt
import sys

pkgs = ['tgt', 'lvm2']

cache = apt.cache.Cache()
cache.update()
cache.open()

for pkg_name in pkgs:
    pkg = cache[pkg_name]
    if pkg.is_installed:
	print "{pkg_name} already installed".format(pkg_name=pkg_name)
    else:
	pkg.mark_install()
	try:
	    cache.commit()
	except Exception, arg:
	    print >> sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg))

