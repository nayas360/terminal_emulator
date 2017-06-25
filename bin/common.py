# commons imports

import os
import configparser as cp
from time import sleep


# String manipulators____________________
def make_s(l):
    __doc__ = '''
    Makes a sentence with spaces
    in between from a list of
    strings.
    returns a string.'''
    s = str()
    for i in l:
        s += i + ' '
    s = s[:-1]
    return s


def make_s2(l):
    __doc__ = '''
    Makes a sentence from a
    list of strings.
    returns a string.'''
    s = str()
    for i in l:
        s += i
    s = s[:-1]
    return s


# Path functions_________________________

# config path
c_path = 'bin/.configs'


def write_config():
    config = cp.ConfigParser()
    config['prop'] = {'path': 'root/'}
    with open(c_path, 'w') as configs:
        config.write(configs)


def get_path():
    __doc__ = '''
    Gets current path
    of the virtual file
    system.
    returns a string.'''
    config = cp.ConfigParser()
    config.read(c_path)
    path = config['prop']['path']
    return path


def set_path(path):
    __doc__ = '''
    Sets current path
    of the virtual file system.
    returns None'''
    config = cp.ConfigParser()
    config.read(c_path)
    if path[-1] != '/':
        path += '/'
    config.set('prop', 'path', path)
    with open(c_path, 'w') as configs:
        config.write(configs)


def get_last_path(path):
    __doc__ = '''
    Gets the last path in
    the current directory.
    returns path as string'''
    last = str()
    ctr = 0
    i = 1
    while ctr != 2:
        last += path[-i]
        if path[-i] == '/':
            ctr += 1
        i += 1
    last = last[:-1]
    last = make_s2(list(reversed(last)))
    return last


def get_prv_path():
    __doc__ = '''
    Gets the previous path
    of the current directory.
    returns path as a string.'''
    path = get_path()
    last = get_last_path(path) + '/'
    path = path[:-len(last)]
    return path


def get_prv_path2(path):
    __doc__ = '''
    Gets the previous path
    of the path given as argument.
    returns path as string.'''
    last = get_last_path(path) + '/'
    path = path[:-len(last)]
    return path


# Others_________________________________
def get_args(inp):
    __doc__ = '''
    Gets the arguments seperated
    by a space from a list.
    The argument input cannot have
    spaces in them for now.
    returns arguments as list.'''
    try:
        old = inp[0].replace(' ', '')
        old = inp[0].replace('"', '')
    except IndexError:
        print('1st argument is missing')
        return []
    try:
        new = inp[1].replace(' ', '')
        new = inp[1].replace('"', '')
    except IndexError:
        print('2nd argument is missing')
        return []
    return [old, new]


def analyze(inp):
    __doc__ = '''
    Basic function to analyze
    the input for other expressions
    returns None'''
    inp = make_s(inp)

    excepts = ['os', 'inp', '[', ']',
               'ArithmeticError', 'AssertionError',
               'AttributeError', 'BaseException',
               'BufferError', 'BytesWarning',
               'DeprecationWarning', 'EOFError',
               'Ellipsis', 'EnvironmentError',
               'Exception',
               'FloatingPointError', 'FutureWarning',
               'GeneratorExit', 'IOError',
               'ImportError', 'ImportWarning',
               'IndentationError', 'IndexError',
               'KeyError', 'KeyboardInterrupt',
               'LookupError', 'MemoryError',
               'NameError', 'None',
               'NotImplemented', 'NotImplementedError',
               'OSError', 'OverflowError',
               'PendingDeprecationWarning',
               'ReferenceError', 'ResourceWarning',
               'RuntimeError', 'RuntimeWarning',
               'StopIteration', 'SyntaxError',
               'SyntaxWarning', 'SystemError',
               'SystemExit', 'TabError',
               'TypeError', 'UnboundLocalError',
               'UnicodeDecodeError', 'UnicodeEncodeError',
               'UnicodeError', 'UnicodeTranslateError',
               'UnicodeWarning', 'UserWarning',
               'ValueError', 'Warning',
               'ZeroDivisionError',
               '_', '__build_class__',
               '__debug__', '__doc__',
               '__import__', '__name__',
               '__package__', 'abs', 'all',
               'any', 'ascii', 'bin', 'bool',
               'bytearray', 'bytes', 'callable',
               'chr', 'classmethod', 'compile',
               'complex', 'copyright', 'credits',
               'delattr', 'dict', 'dir', 'divmod',
               'enumerate', 'eval', 'exec', 'exit',
               'filter', 'float', 'format',
               'frozenset', 'getattr', 'globals',
               'hasattr', 'hash', 'help', 'hex',
               'id', 'input', 'int', 'isinstance',
               'issubclass', 'iter', 'len',
               'license', 'list', 'locals', 'map',
               'max', 'memoryview', 'min', 'next',
               'object', 'oct', 'open', 'ord', 'pow',
               'print', 'property', 'quit', 'range',
               'repr', 'reversed', 'round', 'set',
               'setattr', 'slice', 'sorted',
               'staticmethod', 'str', 'sum',
               'super', 'tuple', 'type', 'vars',
               'zip']

    for i in range(len(excepts)):
        if excepts[i] in inp:
            print('Error[0]: "', inp, '" was not recognised as a command or an expression', sep='')
            return
    try:
        exec('from math import *')
        e = eval(inp)
        if e != None:
            print(e)
    except SyntaxError:
        print("Couldn\'t evaluate the expression")
    except NameError as e:
        print('Error[0]: "', inp, '" was not recognised as a command or an expression', sep='')
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except AttributeError as e:
        print(e)