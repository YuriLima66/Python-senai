import tkinter as tk
import random

class JogoDaCobrinha(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, width=600, height=400, background="black", highlightthickness=0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = self.set_new_food_position()
        self.direction = "Right"
        self.score = 0

        self.create_objects()

        self.bind_all("<Key>", self.on_key_press)

        self.perform_actions()

    def create_objects(self):
        self.create_text(
            100, 12, text=f"Score: {self.score}", tag="score", fill="#fff", font=("TkDefaultFont", 14)
        )
        for x, y in self.snake_positions:
            self.create_rectangle(x, y, x + 20, y + 20, fill="green", tag="snake")
        self.create_rectangle(*self.food_position, self.food_position[0] + 20, self.food_position[1] + 20, fill="red", tag="food")
        self.create_rectangle(7, 27, 593, 383, outline="#525d69")

    def move_snake(self):
        head_x, head_y = self.snake_positions[0]

        if self.direction == "Left":
            new_head_pos = (head_x - 20, head_y)
        elif self.direction == "Right":
            new_head_pos = (head_x + 20, head_y)
        elif self.direction == "Up":
            new_head_pos = (head_x, head_y - 20)
        elif self.direction == "Down":
            new_head_pos = (head_x, head_y + 20)

        self.snake_positions = [new_head_pos] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position[0], position[1], position[0] + 20, position[1] + 20)

    def perform_actions(self):
        if self.check_collisions():
            self.end_game()
            return

        self.check_food_collision()
        self.move_snake()
        self.after(200, self.perform_actions)  # Reduzindo a velocidade para 200 ms

    def check_collisions(self):
        head_x, head_y = self.snake_positions[0]
        return (
            head_x in (0, 600)
            or head_y in (20, 400)
            or (head_x, head_y) in self.snake_positions[1:]
        )

    def on_key_press(self, e):
        new_direction = e.keysym
        all_directions = ("Up", "Down", "Left", "Right")
        opposites = ({"Up", "Down"}, {"Left", "Right"})

        if (
            new_direction in all_directions
            and {new_direction, self.direction} not in opposites
        ):
            self.direction = new_direction

    def check_food_collision(self):
        if self.snake_positions[0] == self.food_position:
            self.snake_positions.append(self.snake_positions[-1])
            self.food_position = self.set_new_food_position()
            self.score += 1
            score = self.find_withtag("score")
            self.itemconfigure(score, text=f"Score: {self.score}", tag="score")
            self.delete("food")
            self.create_rectangle(*self.food_position, self.food_position[0] + 20, self.food_position[1] + 20, fill="red", tag="food")

    def set_new_food_position(self):
        while True:
            x = random.randint(1, 29) * 20
            y = random.randint(3, 19) * 20
            if (x, y) not in self.snake_positions:
                return x, y

    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game Over! Score: {self.score}",
            fill="white",
            font=("TkDefaultFont", 24),
            anchor="center",
        )

root = tk.Tk()
root.title("Jogo da Cobrinha")
root.resizable(False, False)

game = JogoDaCobrinha(root)
game.pack()

root.mainloop()
