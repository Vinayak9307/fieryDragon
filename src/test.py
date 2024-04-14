# import tkinter as tk
# import random

# from constants import TEX_DIR

# class DragonCard:
#     def __init__(self, canvas, x, y, image_path, reset_callback):
#         self.canvas = canvas
#         self.image_path = image_path
#         self.photo = tk.PhotoImage(file=image_path)
#         self.card = canvas.create_image(x, y, image=self.photo, anchor=tk.NW)
#         self.canvas.tag_bind(self.card, "<Button-1>", self.flip_card)
#         self.is_flipped = False
#         self.reset_callback = reset_callback

#     def flip_card(self, event):
#         if not self.is_flipped:
#             self.photo = tk.PhotoImage(file=TEX_DIR + "flipped_dragon.png")  # Change to your flipped image path
#             self.canvas.itemconfig(self.card, image=self.photo)
#             self.is_flipped = True
#             self.check_all_flipped()

#     def check_all_flipped(self):
#         all_flipped = all(card.is_flipped for card in dragon_cards)
#         if all_flipped:
#             # Schedule the reset function to be called after a delay of 1000 milliseconds (1 second)
#             self.canvas.after(1000, self.reset_callback)

# class Player:
#     def __init__(self, canvas, x, y):
#         self.canvas = canvas
#         self.player = canvas.create_rectangle(x, y, x+10, y+10, fill="green")
#         self.steps = 0
#         self.moving = False

    # def move(self, steps):
    #     self.steps = steps
    #     self.moving = True
    #     self.move_step()

    # def move_step(self):
    #     if self.steps > 0:
    #         self.canvas.move(self.player, 10, 0)
    #         self.steps -= 1
    #         self.canvas.after(1000, self.move_step)
    #     else:
    #         self.moving = False

# root = tk.Tk()
# root.title("Dragon Card Game")

# canvas = tk.Canvas(root, width=400, height=400)
# canvas.pack()

# dragon_card_images = [TEX_DIR + "bat1.png", TEX_DIR + "bat2.png", TEX_DIR + "bat3.png",TEX_DIR +  "spider1.png"]
# dragon_cards = []

# def reset_game():
#     player_move()
#     # Reset all cards to their initial state
#     for card in dragon_cards:
#         card.photo = tk.PhotoImage(file=card.image_path)
#         card.canvas.itemconfig(card.card, image=card.photo)
#         card.is_flipped = False
#     # Shuffle the cards
#     random.shuffle(dragon_cards)

# # Create Dragon Card instances
# x, y = 50, 50
# for image_path in dragon_card_images:
#     dragon_card = DragonCard(canvas, x, y, image_path, reset_game)
#     dragon_cards.append(dragon_card)
#     x += 100  # Move to the next position

# # Shuffle the cards initially
# random.shuffle(dragon_cards)

# player = Player(canvas, 10, 10)



# def player_move():
#     if not player.moving:
#         player.move(random.randint(1, 5))

# root.mainloop()
for i in range(24):
    print(i)
