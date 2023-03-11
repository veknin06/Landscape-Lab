import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from pygame import mixer




pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
pygame.display.set_caption("Midnight Boat Ride")


screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Sounds - https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.load
# rain music plays infinitely at a volume of 0.123456789 (volume value of 1 is way to loud)
pygame.mixer.music.load('rain.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.123456789)
# ---------------------------
# Initialize global variables
wave_x = 100
wave_y = 380
wave_radius = 50
wave_x_speed = 1
moon_x = 110
moon_y = 90
moon_radius = 55
moon_x_speed = 0.05
star_x = 0
star_y = 0
star_radius = 1
star_x_speed = 1
# ---------------------------
running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
          
# ---------------------------
    # GAME STATE UPDATES

    wave_x += wave_x_speed
    if wave_x - wave_radius > WIDTH:
     wave_x = - wave_radius
    
    moon_x += moon_x_speed
    if moon_x - moon_radius > WIDTH:
     moon_x = - moon_radius

    wave_x += wave_x_speed

    sky = 57, 32, 51
    sea_colour = 100,132,174
    mountain = 100, 100, 100
    shadow = 50, 50, 50
    mini_wave = 255, 255, 255
    moon = 254, 252, 215
  

# ---------------------------
    # DRAWING
    screen.fill((sky))  

# (Mr. G's code from compound shapes video)

  
  
    def draw_wave(x, y):
      pygame.draw.circle(screen, (sea_colour), (x, y), wave_radius) 
      pygame.draw.circle(screen, (sea_colour), (x + 25, y - 5), wave_radius)
      pygame.draw.circle(screen, (sea_colour), (x + 45, y - 10), wave_radius)

    def draw_fish(x,y):
      pygame.draw.circle(screen, (244, 169, 153), (x, y), 8) 
      pygame.draw.circle(screen, (255, 255, 255), (x + 4, y - 3), 2)
      pygame.draw.circle(screen, (sea_colour), (x - 10, y + 5), 8)
  
# Ocean Base
    pygame.draw.rect(screen, (sea_colour), (0, 340, 640, 200))

  
# Moon + Stars
    pygame.draw.circle(screen, (moon), (moon_x, moon_y), moon_radius)
    pygame.draw.circle(screen, (sky), (moon_x + 20, moon_y - 10), moon_radius - 18)
  
    pygame.draw.circle(screen, (moon), (star_x, star_y), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 105, star_y +34), star_radius + 2)
    pygame.draw.circle(screen, (moon), (star_x + 24, star_y + 91), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 83, star_y + 83), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 46, star_y + 165), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 120, star_y + 116), star_radius + 2)
    pygame.draw.circle(screen, (moon), (star_x + 57, star_y + 238), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 17, star_y + 171), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 44, star_y + 230), star_radius + 2)
    pygame.draw.circle(screen, (moon), (star_x + 26, star_y + 307), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 229, star_y + 185), star_radius + 2)
    pygame.draw.circle(screen, (moon), (star_x + 242, star_y + 155), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 201, star_y + 151), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 155, star_y + 49), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 200, star_y + 15), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 242, star_y + 27), star_radius + 2)
    pygame.draw.circle(screen, (moon), (star_x + 222, star_y + 80), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 256, star_y + 80), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 353, star_y + 19), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 328, star_y + 44), star_radius + 2)
    pygame.draw.circle(screen, (moon), (star_x + 371, star_y + 75), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 443, star_y + 149), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 443, star_y + 71), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 420, star_y + 79), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 289, star_y + 22), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 400, star_y + 150), star_radius + 2)
    pygame.draw.circle(screen, (moon), (star_x + 429, star_y + 190), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 435 , star_y + 190), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 414, star_y + 40), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 398, star_y + 26), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 492, star_y + 210), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 487, star_y + 65), star_radius + 2)
    pygame.draw.circle(screen, (moon), (star_x + 558, star_y + 48), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 628, star_y + 368), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 434, star_y + 79), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 490, star_y + 23), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 611, star_y + 39), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 538, star_y + 95), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 600, star_y + 154), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 622, star_y + 265), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 591, star_y + 229), star_radius + 2)
    pygame.draw.circle(screen, (moon), (star_x + 465, star_y + 25), star_radius)
    pygame.draw.circle(screen, (moon), (star_x + 631, star_y + 131), star_radius + 2)
# ---------------------------------------

  
# --------------------------------------- 
# Mountains + Shadows
    pygame.draw.polygon(screen, (shadow), ((140, 110),(240, 340),(290, 340)))
    pygame.draw.polygon(screen, (mountain), ((200, 340),(490, 340),(320, 40)))
    pygame.draw.polygon(screen, (shadow), ((450, 340),(490, 340),(320, 40)))
    pygame.draw.polygon(screen, (mountain), ((380, 340),(610, 340),(510, 130)))
    pygame.draw.polygon(screen, (shadow), ((610, 340),(650, 340),(510, 130)))
    pygame.draw.polygon(screen, (shadow), ((430, 340),(490, 340),(320, 40)))
    pygame.draw.polygon(screen, (mountain), ((140, 110),(250, 340),(40, 340)))
    pygame.draw.polygon(screen, (shadow), ((230, 260),(190, 340),(200, 340)))
# ---------------------------------------

  
# ---------------------------------------
  # Boat + Sail

    pygame.draw.polygon(screen, (141, 92, 62), ((40, 300),(280, 300),(190, 370),(80, 370)))
    pygame.draw.polygon(screen, (134, 86, 67), ((110, 150),(130, 160),(130, 300), (110, 300)))
    pygame.draw.polygon(screen, (121, 181, 237), ((129, 280),(129, 170),(220, 240)))
    pygame.draw.circle(screen, (moon), (110, 330), 20)
    pygame.draw.circle(screen, (moon), (190, 330), 20)
# ---------------------------------------


# ---------------------------------------
# Waves (Mr. G's code from compound shapes video)
    draw_wave(wave_x + 600, 380)
    draw_wave(wave_x + 500, 380)
    draw_wave(wave_x + 400, 380)
    draw_wave(wave_x + 300, 380)
    draw_wave(wave_x + 200, 380)
    draw_wave(wave_x + 100, 380)
    draw_wave(wave_x, wave_y)
    draw_wave(wave_x - 100, 380)
    draw_wave(wave_x - 200, 380)
    draw_wave(wave_x - 300, 380)
    draw_wave(wave_x - 400, 380)
    draw_wave(wave_x - 500, 380)
    draw_wave(wave_x - 600, 380)
    draw_wave(wave_x - 700, 380)
    draw_wave(wave_x - 800, 380)
    draw_wave(wave_x - 900, 380)
    draw_wave(wave_x - 1000, 380)
# ---------------------------------------



# ---------------------------------------
# Fish (Mr. G's code from compound shapes video)
    draw_fish(46, 375)
    draw_fish(60, 463)
    draw_fish(207, 409)
    draw_fish(355, 373)
    draw_fish(417, 410)
    draw_fish(571, 462)
    draw_fish(575, 376)

# ---------------------------------------

  
  
# ---------------------------------------
  # Mini waves
    pygame.draw.circle(screen, (mini_wave), (wave_x - 100, wave_y + 45), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x - 100, wave_y + 55), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x - 140, wave_y + 45), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x - 140, wave_y + 55), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x - 120, wave_y + 45), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x - 120, wave_y + 55), wave_radius - 20)

    pygame.draw.circle(screen, (mini_wave), (wave_x - 300, wave_y + 65), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x - 300, wave_y + 75), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x - 340, wave_y + 65), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x - 340, wave_y + 75), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x - 320, wave_y + 65), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x - 320, wave_y + 75), wave_radius - 20)

    pygame.draw.circle(screen, (mini_wave), (wave_x - 450, wave_y + 30), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x - 450, wave_y + 40), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x - 490, wave_y + 30), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x - 490, wave_y + 40), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x - 470, wave_y + 30), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x - 470, wave_y + 40), wave_radius - 20)
  
    pygame.draw.circle(screen, (mini_wave), (wave_x + 100, wave_y + 65), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x + 100, wave_y + 75), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x + 140, wave_y + 65), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x + 140, wave_y + 75), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x + 120, wave_y + 65), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x + 120, wave_y + 75), wave_radius - 20)

    pygame.draw.circle(screen, (mini_wave), (wave_x + 300, wave_y + 45), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x + 300, wave_y + 55), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x + 340, wave_y + 45), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x + 340, wave_y + 55), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x + 320, wave_y + 45), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x + 320, wave_y + 55), wave_radius - 20)

    pygame.draw.circle(screen, (mini_wave), (wave_x + 450, wave_y + 30), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x + 450, wave_y + 40), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x + 490, wave_y + 30), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x + 490, wave_y + 40), wave_radius - 20)
    pygame.draw.circle(screen, (mini_wave), (wave_x + 470, wave_y + 30), wave_radius - 25)
    pygame.draw.circle(screen, (sea_colour), (wave_x + 470, wave_y + 40), wave_radius - 20)
# ---------------------------------------


  
# ---------------------------
    pygame.display.flip()
    clock.tick(30)
#---------------------------


pygame.quit()
