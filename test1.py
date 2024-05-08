import curses
import logging

# 设置日志记录
logging.basicConfig(filename='snake_game.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main(stdscr):
    logging.debug("Entered main function.")
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
        logging.error("An error occurred inside main function: {}".format(str(e)))  # 添加错误日志

if __name__ == "__main__":
    logging.debug("Program started.")
    try:
        curses.wrapper(main)
        logging.debug("Curses wrapper completed successfully.")
    except Exception as e:
        logging.error("An error occurred while running curses wrapper: {}".format(str(e)))
    logging.debug("Program ended.")
