# Constants for screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

# Directory for texture assets
TEX_DIR = "../assets/textures/"

# Paths for different types of dragon cards
FLIPPED_CARD = TEX_DIR + "flipped_dragon.png"
SALAMANDER_CARD = TEX_DIR + "salamander"
BAT_CARD = TEX_DIR + "bat"
SPIDER_CARD = TEX_DIR + "spider"
DRAGON_EGG_CARD = TEX_DIR + "dragon_egg"
SKULL_CARD = TEX_DIR + "skull"

# Positions for each dragon card on the game board
CARD_POS = [[214, 192], [281,162], [348,177], [395,224], [411,289], [391,353], [336,400], [271,403],
            [206,379], [167,319], [171,246], [238,260], [300,228], [348,281], [246,324], [309,339]]

# Numbers representing each type of dragon card
DRAGON_CARD_NUM = [11,12,13,21,22,23,31,32,33,41,42,43,51,52,51,52]

# Positions for each player token along the path
PLAYER_POS = [[299,89],[351,96],[403,113],[447,146],[486,189],[504,240],[509,295],[509,355],[486,405],[449,447],
              [403,485],[352,504],[296,510],[239,499],[190,479],[149,444],[118,399],[97,350],[85,296],[85,237],
              [112,189],[151,149],[193,114],[244,98]]

# Starting positions for players in their respective caves
PLAYER_CAVE_POS = [[299,2],[592,294] ,[297,593] ,[1,294]]
# Animal types in each player's cave
PLAYER_CAVE_ANIMAL = [1,2,3,4]
# Animal types on the path
ANIMALS_ON_PATH = [3,2,1,3,4,2,1,4,3,2,1,2,4,3,2,1,4,1,3,2,4,1,3,4]

# Paths to player token images
TOKEN_COLOR = [TEX_DIR + "red.png" , TEX_DIR + "green.png" , TEX_DIR + "blue.png" , TEX_DIR + "yellow.png"]
WINNER_COLOR = ["red" , "green" , "blue" , "yellow"]

# Coordinates of the skip button
SKIP_BUTTON_COORDS = [516 , 519]
SKIP_BUTTON = TEX_DIR + "skip_button.png"

# Coordinates of the current player indicator
CURRENT_PLAYER_COORDS = [52,554]

# Path to the game board image
BOARD_PATH = TEX_DIR + "board.png"
