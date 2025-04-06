import pygame
import sys

# Initsialiseeri Pygame
pygame.init()

# Mänguakna seaded
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne 1")

# Lae pildid
bg = pygame.image.load("bgshop.jpg")
seller = pygame.image.load("seller.png")
chat = pygame.image.load("chat.png")

# Skaali pildid (valikuline, kui vaja mahutada ekraanile)
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# Font ja tekst
font = pygame.font.SysFont("arial", 24)
text = font.render("Minu Nimi", True, (255, 255, 255))  # Valge tekst

# Põhiloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Joonista kõik ekraanile
    screen.blit(bg, (0, 0))                  # Taust
    screen.blit(seller, (50, 200))           # Poemüüja
    screen.blit(chat, (250, 100))            # Jutumull
    screen.blit(text, (270, 130))            # Tekst jutumulli sees

    pygame.display.flip()

# Lõpeta mäng
pygame.quit()
sys.exit()
