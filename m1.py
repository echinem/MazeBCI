import pygame
import sys
import csv

pygame.init()

width, height = 400, 280
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Maze')

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 223, 0)

player_size = 20
player_x = 20
player_y = 20
player_speed = 5

walls = [
    pygame.Rect(0, 0, width, 20),          # Top border
    pygame.Rect(0, 0, 20, height),         # Left border
    pygame.Rect(0, height - 20, width, 20),# Bottom border
    pygame.Rect(width - 20, 0, 20, height),# Right border
    pygame.Rect(0, 50, 200, 20),  #1
    pygame.Rect(250, 0, 20, 80),  #2
    pygame.Rect(270, 60, 50, 20), #3
    pygame.Rect(180, 50, 20, 80), #4
    pygame.Rect(180, 110, 140, 20), #5
    pygame.Rect(60, 160, 100, 20), #6
    pygame.Rect(100, 100, 20, 70), #7
    pygame.Rect(160, 160, 100, 20), #8
    pygame.Rect(300, 160, 20, 60), #9
    pygame.Rect(0, 200, 120, 25), #10
    pygame.Rect(230, 210, 90, 20),
    pygame.Rect(320, 180, 100, 20),
    pygame.Rect(160, 160, 20, 100), #11
    pygame.Rect(52, 50, 20, 80)
]

keys_disp = [
    pygame.Rect(45, height-40, 5, 20),
    pygame.Rect(40, height-50, 15, 15)
]

key_rect3 = pygame.Rect(45, height-45, 5, 5)

key = pygame.Rect(45, height-50, 15, 15)
exit_rect = pygame.Rect(width - 40, height - 40, 20, 20)
font = pygame.font.SysFont(None, 55)

key_collected = False

dataset = []
with open('emotions.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        dataset.append([float(row[i]) for i in range(2)])  # Only first two columns

def display_message(message):
    text = font.render(message, True, white)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

data_index = 0

# move when current - neutral > 2 (threshold)
neutral_x, neutral_y = 20, 25 
threshold = 2 

last_collision = {"x": 0, "y": 0}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    data_row = dataset[data_index]
    print(f"Data Row: {data_row}")

    prev_x, prev_y = player_x, player_y

    # Movement
    if abs(data_row[0] - neutral_x) > threshold:
        if data_row[0] > neutral_x and last_collision["x"] != 1:
            player_x += player_speed
            #print("Moving right")
            last_collision["x"] = 0
        elif data_row[0] < neutral_x and last_collision["x"] != -1:
            player_x -= player_speed
            #print("Moving left")
            last_collision["x"] = 0

    if abs(data_row[1] - neutral_y) > threshold:
        if data_row[1] > neutral_y and last_collision["y"] != 1:
            player_y += player_speed
            #print("Moving down")
            last_collision["y"] = 0
        elif data_row[1] < neutral_y and last_collision["y"] != -1:
            player_y -= player_speed
            #print("Moving up")
            last_collision["y"] = 0

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    # Collision with Wall
    collided = False
    for wall in walls:
        if player_rect.colliderect(wall):
            player_x, player_y = prev_x, prev_y
            #print("Collision with wall")
            collided = True
            break

    if collided:
        data_index = (data_index + 1) % len(dataset)

        if player_x > prev_x:
            last_collision["x"] = 1  # Right collision
        elif player_x < prev_x:
            last_collision["x"] = -1 # Left collision
        if player_y > prev_y:
            last_collision["y"] = 1  # Down collision
        elif player_y < prev_y:
            last_collision["y"] = -1 # Up collision

    # Collision with Key
    if player_rect.colliderect(key):
        key_collected = True

    screen.fill(black)

    for wall in walls:
        pygame.draw.rect(screen, blue, wall)

    if not key_collected:
        pygame.draw.rect(screen, yellow, key)
        for k in keys_disp:
            pygame.draw.rect(screen, yellow, k)

    pygame.draw.rect(screen, black, key_rect3)
    pygame.draw.rect(screen, white, player_rect)

    if key_collected:
        pygame.draw.rect(screen, red, exit_rect)

    if key_collected and player_rect.colliderect(exit_rect):
        display_message("You Win!")
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()

    # Frame rate control
    pygame.time.Clock().tick(30)
