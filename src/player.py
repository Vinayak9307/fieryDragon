import tkinter as tk

class Player:
    def __init__(self, canvas , path , color , animals , game):
        self.canvas = canvas
        self.game = game
        self.index = 0
        self.path = path
        self.animals_on_path = animals
        self.color = color
        self.player_token_image = tk.PhotoImage(file=self.color)

        x = path[self.index][0]
        y = path[self.index][1]

        self.steps = 0
        self.player_token = self.canvas.create_image(x, y, image=self.player_token_image, anchor=tk.NW)
        self.moving = False
    
    def move(self, steps):
        self.game.is_any_player_moving = True
        self.steps = steps
        self.moving = True
        self.move_step()

    def move_step(self):
        if self.steps > 0:
            self.index = (self.index + 1)%len(self.path)

            self.canvas.coords(self.player_token, self.path[self.index][0], self.path[self.index][1])
            self.steps -= 1
            self.canvas.after(1000, self.move_step)
        else:
            self.game.is_any_player_moving = False
