import random
import tkinter as tk

from constants import *
from dragon_cards import DragonCard
from player import Player
import tkinter.messagebox as msgbox

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fiery Dragons!")
        self.canvas = tk.Canvas(self , width=SCREEN_WIDTH , height=SCREEN_HEIGHT)
        self.canvas.pack()

        # Load and display the game board image
        self.board = tk.PhotoImage(file=BOARD_PATH)
        self.canvas.create_image(0 , 0 ,image=self.board , anchor=tk.NW)

        # Create Dragon Cards
        self.dragon_cards = []
        self.card_list = DRAGON_CARD_NUM
        for i in CARD_POS:
            # Randomly select a card number and create a Dragon Card object
            random_number_from_list = self.card_list[random.randint(0,len(self.card_list) - 1)]
            self.card_list.remove(random_number_from_list)
            dragon_card = DragonCard(self , self.canvas , i[0] , i[1] , FLIPPED_CARD,random_number_from_list)
            self.dragon_cards.append(dragon_card)

        # Create Player Tokens
        self.players = []
        player_count = 0
        for i in PLAYER_CAVE_POS:
            # Initialize player's path and animal on path
            player_animal_on_path = []
            player_path = []
            player_path.append(i)
            player_animal_on_path.append(PLAYER_CAVE_ANIMAL[player_count])
            start = player_count * 6
            for j in range(24):
                player_path.append(PLAYER_POS[start])
                player_animal_on_path.append(ANIMALS_ON_PATH[start])
                start = start + 1
                start = start % 24
            
            # Create Player object and add it to the players list
            player = Player(self.canvas , player_path , TOKEN_COLOR[player_count] , player_animal_on_path,self)
            self.players.append(player)
            player_count = player_count + 1
        
        # Load and display the skip button image
        self.skip_button_image = tk.PhotoImage(file=SKIP_BUTTON)
        self.skip_button = self.canvas.create_image(SKIP_BUTTON_COORDS[0] , SKIP_BUTTON_COORDS[1] ,image=self.skip_button_image, anchor=tk.NW)

        # Bind the skip button to the on_skip_pressed method
        self.canvas.tag_bind(self.skip_button,"<Button-1>",self.on_skip_pressed)
        self.current_player = 0
        self.is_any_player_moving = False

        # Load player images
        self.player_images = []
        for i in TOKEN_COLOR:
            img = tk.PhotoImage(file=i)
            self.player_images.append(img)

        # Display the current player's token
        x = CURRENT_PLAYER_COORDS[0]
        y = CURRENT_PLAYER_COORDS[1]
        self.current_player_image = self.canvas.create_image(x , y , image=self.player_images[self.current_player] , anchor=tk.NW)

        # Show the current player's token
        self.show_current_player()
        
    def show_current_player(self):
        # Update the image of the current player's token
        self.canvas.itemconfig(self.current_player_image ,image=self.player_images[self.current_player] )

    def reset_all_cards(self ):
        # Reset all Dragon Cards to face down state
        for card in self.dragon_cards:
            card.reset()

    def skip(self):
        # Switch to the next player's turn and reset all cards
        self.current_player = (self.current_player + 1) % 4  
        self.reset_all_cards()
        self.show_current_player()
    
    def on_skip_pressed(self , event):
        # Handle skip button press event
        self.canvas.after(1000 , self.skip)
        
    def move_current_player(self , steps):
        # Move the current player's token by the specified number of steps
        self.players[self.current_player].move(steps)

    def show_winner_message(self):
        # Determine the winner
        winner_index = self.current_player
        if winner_index is not None:
            winner_color = WINNER_COLOR[winner_index]
            self.winner_text = self.canvas.create_text(320, 320, text=f"Player {winner_index + 1} wins!", font=("Arial", 30 , "bold"), fill=winner_color)

            # Create buttons for restart and end game
            self.restart_button = self.canvas.create_text(250, 400, text="Restart", font=("Arial", 30 , "bold"), fill="black")
            self.end_button = self.canvas.create_text(390, 400, text="End", font=("Arial", 30 , "bold"), fill="black")

            # Bind events to the buttons
            self.canvas.tag_bind(self.restart_button, "<Button-1>", self.restart_game)
            self.canvas.tag_bind(self.end_button, "<Button-1>", self.end_game)

    def restart_game(self, event):
        # Remove winner message and buttons
        if self.winner_text:
            self.canvas.delete(self.winner_text)
            self.canvas.delete(self.restart_button)
            self.canvas.delete(self.end_button)
            self.current_player = 0
            self.show_current_player()
            for i in self.players:
                i.reset()
            self.reset_all_cards()
        
        # Your code to reset the game state goes here...

    def end_game(self, event):
        # Display a message box to confirm ending the game
        result = msgbox.askyesno("End Game", "Are you sure you want to end the game?")
        if result:
            # Close the Tkinter window
            self.destroy()
        
    
    def move_if_match(self,animal,steps):
        # Move the current player's token if there is a match between the card's animal and the player's current position
        p = self.players[self.current_player]
        if animal == p.animals_on_path[p.index] or animal == 5:
            self.move_current_player(steps)
        else:
            # If no match, skip the player's turn after a delay
            self.canvas.after(1000 , self.skip)
