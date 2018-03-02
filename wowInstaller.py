#!/usr/bin/env python3
# -*- coding:utf-8 -*-


print "hello"


def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

mongoExists = nodeExists = nodejsExists = npmExists = False

if(isinstance(which("mongo"),str)):
    mongoExists = True

if(isinstance(which("node"),str)):
    nodeExists = True

if(isinstance(which("nodejs"),str)):
    nodejsExists = True

if(isinstance(which("npm"),str)):
    npmExists = True

print mongoExists, nodeExists, nodejsExists, npmExists



