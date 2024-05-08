import random
import curses

class SnakeGame:
    def __init__(self, window, height, width):
        self.window = window
        self.window.keypad(1)
        self.window.timeout(4)
        self.snake = [[height//2, width//4]]
        self.snake_direction = curses.KEY_RIGHT
        self.food = [height//2, width//2]
        self.window.addch(self.food[0], self.food[1], curses.ACS_PI)
        self.score = 0

    def run(self):
        while True:
            next_key = self.window.getch()
            if next_key != -1:
                if not self.is_opposite_direction(next_key):
                    self.snake_direction = next_key

            self.move_snake()

            if self.snake[0] == self.food:
                self.score += 1
                self.place_food()
            else:
                tail = self.snake.pop()
                self.window.addch(tail[0], tail[1], ' ')

            if self.collision():
                break

            self.window.addch(self.snake[0][0], self.snake[0][1], curses.ACS_CKBOARD)

        curses.endwin()
        print(f"Game over! Your final score was: {self.score}")

    def move_snake(self):
        head = self.snake[0][:]
        if self.snake_direction == curses.KEY_DOWN:
            head[0] += 1
        if self.snake_direction == curses.KEY_UP:
            head[0] -= 1
        if self.snake_direction == curses.KEY_LEFT:
            head[1] -= 1
        if self.snake_direction == curses.KEY_RIGHT:
            head[1] += 1

        self.snake.insert(0, head)

    def collision(self):
        sh, sw = self.window.getmaxyx()
        return (self.snake[0][0] in [0, sh] or
                self.snake[0][1] in [0, sw] or
                self.snake[0] in self.snake[1:])

    def place_food(self):
        sh, sw = self.window.getmaxyx()
        while True:
            new_food = [random.randint(1, sh-1), random.randint(1, sw-1)]
            if new_food not in self.snake:
                self.food = new_food
                self.window.addch(self.food[0], self.food[1], curses.ACS_PI)
                break

    def is_opposite_direction(self, next_key):
        opposite_directions = {
            curses.KEY_DOWN: curses.KEY_UP,
            curses.KEY_UP: curses.KEY_DOWN,
            curses.KEY_LEFT: curses.KEY_RIGHT,
            curses.KEY_RIGHT: curses.KEY_LEFT
        }
        return opposite_directions.get(self.snake_direction) == next_key

if __name__ == "__main__":
    curses.initscr()
    curses.curs_set(0)
    sh, sw = curses.LINES, curses.COLS
    win = curses.newwin(sh, sw, 0, 0)
    game = SnakeGame(win, sh, sw)
    game.run()
