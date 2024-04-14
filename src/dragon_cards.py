import tkinter as tk

from constants import *  # Importing constants module which contains paths of card images

class DragonCard:
    def __init__(self,game, canvas, x, y, flipped_image_path , card_num):
        """
        Initialize DragonCard object.

        Args:
            game: Reference to the game object.
            canvas: The canvas on which the card will be displayed.
            x, y: Coordinates of the card on the canvas.
            flipped_image_path: Path to the image displayed when the card is flipped.
            card_num: Number representing the card type and value.
        """
        self.game = game
        self.canvas = canvas
        self.face_down_image_path = flipped_image_path
        self.card_num = card_num
        self.animal = self.get_animal()
        self.steps = self.get_steps()
        self.face_up_image_path = self.get_card_image()

        # Load images
        self.face_down = tk.PhotoImage(file=self.face_down_image_path)
        self.face_up = tk.PhotoImage(file=self.face_up_image_path)

        # Create the card on the canvas
        self.card = canvas.create_image(x, y, image=self.face_down, anchor=tk.NW)
        # Bind a click event to the card
        self.canvas.tag_bind(self.card, "<Button-1>", self.flip_card)
        self.is_flipped = False

    def flip_card(self, event):
        """
        Flip the card when clicked.
        """
        # Check if the card is not flipped and no player is moving
        if not self.is_flipped and not self.game.is_any_player_moving:
            # Flip the card
            self.canvas.itemconfig(self.card, image=self.face_up)
            self.is_flipped = True
            # Check if all cards are flipped
            self.check_all_flipped()
            # Move the player if there is a match
            self.game.move_if_match(self.animal , self.steps)

    def check_all_flipped(self):
        """
        Check if all cards are flipped and trigger reset if so.
        """
        all_flipped = all(card.is_flipped for card in self.game.dragon_cards)
        if all_flipped:
            # Schedule the reset function to be called after a delay of 1000 milliseconds (1 second)
            self.canvas.after(1000, self.game.reset_all_cards)

    def reset(self):
        """
        Reset the card to face down state.
        """
        self.canvas.itemconfig(self.card, image=self.face_down)
        self.is_flipped = False

    def get_card_image(self):
        """
        Get the path of the card image based on the card number.
        """
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
        """
        Get the number of steps based on the card number.
        """
        if(self.animal == 5):
            return -(self.card_num%10)
        return self.card_num%10
    
    def get_animal(self):
        """
        Get the animal type based on the card number.
        """
        return self.card_num//10
