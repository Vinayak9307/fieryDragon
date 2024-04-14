import tkinter as tk

from constants import *

class DragonCard:
    def __init__(self,game, canvas, x, y, flipped_image_path , card_num):
        self.game = game
        self.canvas = canvas
        self.face_down_image_path = flipped_image_path
        self.card_num = card_num
        self.animal = self.get_animal()
        self.steps = self.get_steps()
        self.face_up_image_path = self.get_card_image()


        self.face_down = tk.PhotoImage(file=self.face_down_image_path)
        self.face_up = tk.PhotoImage(file=self.face_up_image_path)


        self.card = canvas.create_image(x, y, image=self.face_down, anchor=tk.NW)
        self.canvas.tag_bind(self.card, "<Button-1>", self.flip_card)
        self.is_flipped = False

    def flip_card(self, event):
        if not self.is_flipped and not self.game.is_any_player_moving:
            self.canvas.itemconfig(self.card, image=self.face_up)
            self.is_flipped = True    
            self.check_all_flipped()
            # print(self.steps)
            self.game.move_if_match(self.animal , self.steps)

    def check_all_flipped(self):
        all_flipped = all(card.is_flipped for card in self.game.dragon_cards)
        if all_flipped:
            # Schedule the reset function to be called after a delay of 1000 milliseconds (1 second)
            self.canvas.after(1000, self.game.reset_all_cards)

    def reset(self):
        # print('hello')
        self.canvas.itemconfig(self.card, image=self.face_down)
        self.is_flipped = False
    
    def get_card_image(self):
        num = self.card_num
        d = num%10
        if num == 11 or num == 12 or num == 13:
            return SALAMANDER_CARD + str(d) + ".png"
        elif num == 21 or num == 22 or num == 23:
            return BAT_CARD + str(d) + ".png"
        elif num == 31 or num == 32 or num == 33:
            return SPIDER_CARD + str(d) + ".png"
        elif num == 41 or num == 42 or num == 43:
            return DRAGON_EGG_CARD + str(d) + ".png"
        else:
            return SKULL_CARD + str(d) + ".png"


    def get_steps(self):
        if(self.animal == 5):
            return -(self.card_num%10)
        return self.card_num%10
    
    def get_animal(self):
        return self.card_num//10