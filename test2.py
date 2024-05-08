import curses
import logging

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
    print("Starting the program...")  # 确认脚本被执行
    try:
        logging.debug("Program started.")
        curses.wrapper(main)
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")
    print("Ending the program...")  # 确认脚本执行到结尾
    logging.debug("Program ended.")
