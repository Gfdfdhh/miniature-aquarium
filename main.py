import random, pygame
from pprint import pprint
import time as tima

class GameSprite(pygame.sprite.Sprite):
    cache = {}
    def __init__(self, player_image, player_x, player_y, width, height):
        super().__init__()
        if player_image not in GameSprite.cache:
            GameSprite.cache[player_image] = pygame.transform.scale(pygame.image.load(player_image), (width, height))
            print(f'Картинка {player_image} прогружена!')
        self.image = GameSprite.cache[player_image]
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 500
win_height = 500
dirt_weights = [55, 40, 2.5, 2.5]
sand_weights = [55, 30, 2.5, 2.5]
block_size = 50

class Fish(GameSprite):
    def __init__(self, player_image, player_x, player_y, width, height, speed):
        super().__init__(player_image, player_x, player_y, width, height)
        self.speed = speed
        

    def update_go(self):
        self.rect.x += self.speed
        if self.rect.x > win_width:
            new_fish.remove(self)
        if random.randint(0,50) ==0:
            for bubl in bubul:
                bu = Fish('Images/'+bubl,
                self.rect.x,
                self.rect.y,
                random.randint(10,30),
                random.randint(10,30),
                random.uniform(2,4))
                fish_bubu.append(bu)

    def up_bubl(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            if self in new_bubl:
                new_bubl.remove(self)
            else:
                fish_bubu.remove(self)
    

        
    
fishs = ['fish_blue_outline.png','fish_green.png',
'fish_green_outline.png','fish_pink_outline.png',
'fish_orange_outline.png','fish_red.png']

bubul = ['bubble_c.png','bubble_b.png','bubble_a.png']
plants = ['seaweed_orange_b_outline.png','seaweed_pink_a.png','seaweed_grass_a_outline.png']
stone = ['rock_b.png','rock_a.png']
old_time = tima.time()

width_blocks_count = win_width // block_size
height_blocks_count = win_height // block_size

matrix = []
for y in range(height_blocks_count):
    matrix.append([])
    for x in range(width_blocks_count):
        matrix[y].append('background_terrain.png')


for x in range(width_blocks_count):
    matrix[height_blocks_count - 1][x] = random.choices(['terrain_dirt_a.png', 'terrain_dirt_b.png', 'terrain_dirt_c.png', 'terrain_dirt_d.png'], weights=dirt_weights, k=1)[0]

for x in range(width_blocks_count):
    matrix[height_blocks_count - 2][x] = random.choices(['terrain_sand_a.png', 'terrain_sand_b.png', 'terrain_sand_c.png', 'terrain_sand_d.png'], weights=sand_weights, k=1)[0]

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        matrix[y][x] = GameSprite(
            player_image='Images/'+matrix[y][x],
            player_x=block_size * x,
            player_y=block_size * y,
            width=block_size,
            height=block_size,
        )

window = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

pygame.display.set_caption("Аквариум")


new_fish = []
new_bubl = []
fish_bubu = []
game_over = False
while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    for y in range(height_blocks_count):
        for x in range(width_blocks_count):
            matrix[y][x].draw()
    if len(new_bubl) <= 100:
        for bubl in bubul:
            bu = Fish('Images/'+bubl,
            random.randint(4,win_height - 4),
            400,
            random.randint(10,30),
            random.randint(10,30),
            random.uniform(2,4))
            new_bubl.append(bu)
    for bu in new_bubl+fish_bubu:
        bu.draw()
        bu.up_bubl()

    if len(new_fish) <= 90:
        for fish in fishs:
            fi = Fish('Images/'+fish,
            0 - 90,
            random.randint(20 ,win_height - 180),
            random.randint(30,60),
            random.randint(30,40),
            random.uniform(0.5,5))
            new_fish.append(fi)
    for fi in new_fish:
        fi.draw()
        fi.update_go()

    pygame.display.update()
    clock.tick(60)