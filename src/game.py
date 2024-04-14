import random
import tkinter as tk

from constants import *
from dragon_cards import DragonCard
from player import Player

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fiery Dragons!")
        self.canvas = tk.Canvas(self , width=SCREEN_WIDTH , height=SCREEN_HEIGHT)
        self.canvas.pack()


        self.board = tk.PhotoImage(file=BOARD_PATH)
        self.canvas.create_image(0 , 0 ,image=self.board , anchor=tk.NW)

        # Create Dragon Card
        self.dragon_cards = []
        self.card_list = DRAGON_CARD_NUM
        for i in CARD_POS:
            random_number_from_list = self.card_list[random.randint(0,len(self.card_list) - 1)]
            self.card_list.remove(random_number_from_list)
            dragon_card = DragonCard(self , self.canvas , i[0] , i[1] , FLIPPED_CARD,random_number_from_list)
            self.dragon_cards.append(dragon_card)

        #Create Player Tokens
        self.players = []
        player_count = 0
        for i in PLAYER_CAVE_POS:
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
            
            player = Player(self.canvas , player_path , TOKEN_COLOR[player_count] , player_animal_on_path,self)
            self.players.append(player)
            player_count = player_count + 1
        
        self.skip_button_image = tk.PhotoImage(file=SKIP_BUTTON)
        self.skip_button = self.canvas.create_image(SKIP_BUTTON_COORDS[0] , SKIP_BUTTON_COORDS[1] ,image=self.skip_button_image, anchor=tk.NW)

        self.canvas.tag_bind(self.skip_button,"<Button-1>",self.on_skip_pressed)
        self.current_player = 0
        self.is_any_player_moving = False


        self.player_images = []
        for i in TOKEN_COLOR:
            # print(i)
            img = tk.PhotoImage(file=i)
            self.player_images.append(img)

        x = CURRENT_PLAYER_COORDS[0]
        y = CURRENT_PLAYER_COORDS[1]

        self.current_player_image = self.canvas.create_image(x , y , image=self.player_images[self.current_player] , anchor=tk.NW)


        self.show_current_player()
        
    def show_current_player(self):
        self.canvas.itemconfig(self.current_player_image ,image=self.player_images[self.current_player] )

    def reset_all_cards(self ):
        for card in self.dragon_cards:
            card.reset()

    def skip(self):
        self.current_player = (self.current_player + 1) % 4
        self.reset_all_cards()
        self.show_current_player()
    
    def on_skip_pressed(self , event):
        self.canvas.after(1000 , self.skip)
        
    def move_current_player(self , steps):
        self.players[self.current_player].move(steps)
        
    
    def move_if_match(self,animal,steps):
        p = self.players[self.current_player]
        # print(animal)
        print(p.animals_on_path[p.index])
        if animal == p.animals_on_path[p.index]:
            self.move_current_player(steps)
        else:
            self.canvas.after(1000 , self.skip)



