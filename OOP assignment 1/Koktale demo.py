import pygame
import random

pygame.init()

# Screen setup
screen_width = 1366
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Koktale")

#Load Sound
bg_music = pygame.mixer.Sound('Whispers in the Twilight.mp3')
bg_music.play(loops=-1)
bg_music.set_volume(0.3)
hit = pygame.mixer.Sound('undertale-damage-taken.mp3')

# Load images
bg = pygame.image.load("background battle.png").convert_alpha()
bg2 = pygame.transform.scale(bg, (1370, 385))
bg_surface = bg2.get_rect()

heart = pygame.image.load("heart.png").convert_alpha()
heart2 = pygame.transform.scale_by(heart, 0.025)

kok = pygame.image.load("kok.png").convert_alpha()
kok2 = pygame.transform.scale_by(kok, 0.4)

rect_1 = heart2.get_rect()
rect_1.center = (683, 580)

kok_enemy = kok2.get_rect()
kok_enemy.center = (683, 200)

bullet = pygame.image.load("jellyfish_.png")
bullet2 = pygame.transform.scale_by(bullet, 0.1)
bullet2 = pygame.transform.flip(bullet2, False, True)

Fight = pygame.image.load("Fight.png").convert_alpha()
Fight_hover = pygame.image.load("FightHover.png").convert_alpha()

# Bullet class
class Bullet:
    def __init__(self, x, y, speed):
        self.image = bullet2
        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed  # Move downward

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw bullet

    def is_off_screen(self):
        return self.rect.bottom > 750  # Remove bullet when it leaves the white box

bullets = []
bullets_falls = False

class HealthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def DrawHp(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface,"red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "yellow", (self.x, self.y, self.w * ratio, self.h))

health_bar = HealthBar(800, 780, 100, 90, 20)

text_font = pygame.font.SysFont("Pixel Operator", 85, True)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, font, text_col)
    screen.blit(img, (x, y))

# Button class
class Button():
    def __init__(self, x, y, image, hover_image, scale):
        width = image.get_width()
        height = image.get_height()

        # Store both normal and hover images
        self.normal_image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.hover_image = pygame.transform.scale(hover_image, (int(width * scale), int(height * scale)))

        # Default to normal image
        self.image = self.normal_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        # Check if mouse is hovering
        if self.rect.collidepoint(pos):
            self.image = self.hover_image  # Switch to hover image
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        else:
            self.image = self.normal_image  # Switch back to normal image

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


fight_button = Button(150, 770, Fight, Fight_hover, 0.7)

# Game Scoring
survival_time = 0
start_time = 0

#enemy movement
kok_speed = 5  # Adjust speed
kok_direction = random.choice(["left", "right"])  # Initial random direction

# Game loop
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)

    # Draw background and elements
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (150, 400, 1066, 350), width=5)
    screen.blit(heart2, rect_1)
    screen.blit(bg2, bg_surface)
    screen.blit(kok2, kok_enemy)
    health_bar.DrawHp(screen)
    draw_text("Dave LV 1", text_font, (255, 255, 255), 450, 780)
    draw_text(f"HP {health_bar.hp}/20", text_font, (255, 255, 255), 915, 780)

    if fight_button.draw(screen):
        bullets_falls = True
        health_bar.hp = health_bar.max_hp
        start_time = pygame.time.get_ticks()
        survival_time = 0

    # Player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_a]: rect_1.move_ip(-5, 0)
    if rect_1.x < 156: rect_1.x = 155
    if key[pygame.K_d]: rect_1.move_ip(5, 0)
    if rect_1.x > 1172: rect_1.x = 1171
    if key[pygame.K_w]: rect_1.move_ip(0, -5)
    if rect_1.y < 406: rect_1.y = 405
    if key[pygame.K_s]: rect_1.move_ip(0, 5)
    if rect_1.y > 706: rect_1.y = 705

    #enemy movement
    # Inside the game loop
    if random.randint(1, 30) == 1:  # Change direction randomly every 30 frames
        kok_direction = random.choice(["left", "right"])

    # Move enemy based on direction
    if kok_direction == "left":
        kok_enemy.x -= kok_speed
        if kok_enemy.left < 156:  # Prevent leaving the box
            kok_enemy.left = 156
            kok_direction = "right"  # Change direction

    elif kok_direction == "right":
        kok_enemy.x += kok_speed
        if kok_enemy.right > 1216:  # Prevent leaving the box
            kok_enemy.right = 1216
            kok_direction = "left"  # Change direction

    # Bullet spawning
    if bullets_falls:
        survival_time = (pygame.time.get_ticks() - start_time) // 1000
        if random.randint(1, 10) == 1:  # Adjust spawn frequency
            x_pos = random.randint(160, 1200)
            bullets.append(Bullet(x_pos, 400, random.uniform(2, 6)))
        draw_text(f"Time Survived: {survival_time}s", pygame.font.SysFont("Pixel Operator", 50, True), (255, 255, 255), 900, 50)

    # Update and draw bullets
    for bullet in bullets[:]:
        bullet.update()
        bullet.draw(screen)
        #pygame.draw.rect(screen, (255, 0, 0), bullet.rect, width=2)  # Draw hitbox

        if rect_1.colliderect(bullet.rect):
            print("Player hit!")
            hit.play()
            hit.set_volume(0.03)
            health_bar.hp -= 1
            bullets.remove(bullet)
        if health_bar.hp == 0:
            bullets_falls = False

        if health_bar.hp < 0:
            health_bar.hp = 0

        elif bullet.is_off_screen():
            bullets.remove(bullet)

    if health_bar.hp == 0 and bullets_falls == False:
        draw_text("You Died", text_font, (255, 255, 255), 520, 450)
        draw_text(f"You Survived: {survival_time} Seconds", text_font, (255, 255, 255), 250, 530)
        draw_text("Press Fight to try again", text_font, (255, 255, 255), 250, 600)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #used for positioning the images
        #pos = pygame.mouse.get_pos()
        #print (pos)

    pygame.display.flip()

pygame.quit()
