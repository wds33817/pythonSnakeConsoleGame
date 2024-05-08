import curses

def main(stdscr):
    try:
        # 你的脚本逻辑
        stdscr.clear()
        stdscr.addstr("Hello, World!")
        stdscr.refresh()
        stdscr.getkey()
    except Exception as e:
        stdscr.addstr(0, 0, "An error occurred: " + str(e))
        stdscr.refresh()
        stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(main)
