from threading import Thread
from sys import argv
from os import system
from time import gmtime, strftime

# UNCOMMENT "del" IF YOU don't WANNA HAVE VERSION AVAIABLE
STD_KLIB_VERSION = "1"
#del STD_KLIB_VERSION

# Randomly Selected this. Has no grater meening
SUCCESS_CODE = 11112
FAIL_CODE = 22221
STRING_SUCCESS_CODE = str(SUCCESS_CODE)
STRING_FAIL_CODE = str(FAIL_CODE)

# Variables Class
class var:

    # if string
    def istr(string):
        if type(string) == str:
            return True
        else:
            return False

    # if integer
    def iint(integer):
        if type(integer) == int:
            return True
        else:
            return False

    # if string contains
    def sContain(string, contains):
        if contains in string:
            return True
        else:
            return False

class log:
    def push(text):
        print(" [" + str(strftime("%Y-%m-%d %H:%M:%S", gmtime())) + "] " + str(text))

# print without new line
def prints(text, length = 100000):
    if not type(length) == int:
        print("ERROR: INVALID PRINT")
        exit(0)

    if len(text) > length:
        if length < 0:
            pass
        else:
            print("TOO LONG PRINT METHOD.")
            exit(0)

    print(str(text), end='')

"""
def include(lib):

    ## Will make sure incase you forget the "@" sign
    if not "@" in lib:
        print("ERROR: invalid input file specified")
        print("Example: include(\"@socket\")")
        print("         (Will Include socket class)")
        exit()
    if not lib[0] == "@":
        print("ERROR: MISS-PLACED \"@\" sign")
        print("Example: include(\"@socket\")")
        print("         (Will Include socket class)")
        exit()

    if lib == "@socket" or lib == "@sock":
        from includes.sock import *
        return True
    elif lib == "@gui" or lib == "@tk" or lib == "@tkinter" or lib == "@ui":
        from includes.gui import *
        return True
    else:
        print("WARNING: Invalid File")
        return False
"""
