import curses
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr("hello world from curses")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)