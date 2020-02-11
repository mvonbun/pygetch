#!/usr/bin/env python3

##########################################################################
# Python class to querry for single character user input without the need
# to press <ENTER>.
#
# Author: Michael Vonbun
# Email : m.vonbun@gmail.com
#
# Sources
# The class definition is mostly taken from
#   http://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/
#
# Example usage
# Calling the script from the command line shows a litle demo, that reads in
# user input, a single character at a time.
#
# Have fun!
##########################################################################


class Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    """Getch implementation for Unix."""

    def __init__(self):
        import tty
        import sys

    def __call__(self):
        import tty
        import sys
        import termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch


class _GetchWindows:
    """Getch implementation for Windows."""

    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch().decode('utf-8')


# demo
if __name__ == '__main__':
    # class instantiate
    getch = _Getch()
    print('Repeatedly type single characters.\nPress [q] to quit.')

    # loop init
    repeat_loop = True
    user_input = ''
    while repeat_loop is True:
        ch = getch()
        if ch is 'q':
            repeat_loop = False
        else:
            user_input += ch

    print('Your input sequence was <{}>'.format(user_input))
