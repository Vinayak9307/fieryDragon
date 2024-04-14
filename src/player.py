import tkinter as tk

class Player:
    def __init__(self, canvas , path , color , animals , game):
        """
        Initialize Player object.

        Args:
            canvas: The canvas on which the player token will be displayed.
            path: List of coordinates representing the path on which the player token moves.
            color: Color of the player token.
            animals: List of animals on the path (not used in current implementation).
            game: Reference to the game object.
        """
        self.canvas = canvas
        self.game = game
        self.index = 0
        self.path = path
        self.animals_on_path = animals
        self.color = color
        self.player_token_image = tk.PhotoImage(file=self.color)

        # Set initial position of player token
        x = path[self.index][0]
        y = path[self.index][1]
        self.steps = 0
        self.player_token = self.canvas.create_image(x, y, image=self.player_token_image, anchor=tk.NW)
        self.moving = False

        self.total_moves = 0
        self.has_won = False
    
    def move(self, steps):
        """
        Move the player token by the specified number of steps.

        Args:
            steps: Number of steps to move (positive for forward, negative for backward).
        """
        self.game.is_any_player_moving = True
        self.steps = steps
        self.moving = True
        if self.steps < 0:
            self.move_step_backward()
        else:
            self.move_step_forward()
        
        
    def move_step_backward(self):
        """
        Move the player token backward one step.

        """
        if self.steps < 0:
            self.index = (self.index - 1)

            if self.total_moves < 5:
                if self.index < 0:
                    self.index = 0
                    self.game.is_any_player_moving = False
            else:
                if self.index == 0:
                    self.index = 24
            self.canvas.coords(self.player_token, self.path[self.index][0], self.path[self.index][1])
            self.steps += 1
            self.total_moves -= 1
            self.canvas.after(1000 , self.move_step_backward)
        else:
            self.game.is_any_player_moving = False

    def move_step_forward(self):
        """
        Move the player token forward one step.
        """
        if self.steps > 0:
            self.index = (self.index + 1) % len(self.path)
            
            self.steps -= 1

            if self.index == 0:
                self.index = 1

            # print(f"index : {self.index} , total moves : {self.total_moves} , steps : {self.steps}")


            if self.index == 1 and self.total_moves > 20 and self.steps == 0:
                self.game.show_winner_message()
        
            self.canvas.coords(self.player_token, self.path[self.index][0], self.path[self.index][1])
            self.total_moves += 1
            self.canvas.after(1000, self.move_step_forward)
        else:
            self.game.is_any_player_moving = False

    def reset(self):
        self.index = 0
        self.total_moves = 0
        self.canvas.coords(self.player_token, self.path[self.index][0], self.path[self.index][1])

        self.moving = False
        self.has_won = False