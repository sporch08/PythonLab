
import os
import mypackage.const as const


# determine the OS and execute the command of screen cleaning respectively.
def clean_screen():
    if os.name == const.OS_WIN:
        os.system(const.CMD_CLEAN_WIN)
    elif os.name == const.OS_UNIX:
        os.system(const.CMD_CLEAN_UNIX)
