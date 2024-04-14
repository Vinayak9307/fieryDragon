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
        print(self.steps)
        if self.steps < 0:
            self.move_step_backward()
        else:
            self.move_step_forward()
        
    def move_step_backward(self):
        print(self.steps)
        if self.steps < 0:
            self.index = (self.index - 1)
            if self.index < 0:
                self.index = 0
                self.game.is_any_player_moving = False
            self.canvas.coords(self.player_token, self.path[self.index][0], self.path[self.index][1])
            self.steps += 1
            self.canvas.after(1000 , self.move_step_backward)
        else:
            self.game.is_any_player_moving = False


    def move_step_forward(self):
        print('forward' + str(self.steps))
        if self.steps > 0:
            self.index = (self.index + 1)%len(self.path)

            self.canvas.coords(self.player_token, self.path[self.index][0], self.path[self.index][1])
            self.steps -= 1
            self.canvas.after(1000, self.move_step_forward)
        else:
            self.game.is_any_player_moving = False
