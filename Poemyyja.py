# Impordime ja käivitame pygamei
import pygame
pygame.init()

# Loome mänguakna ja lisame nime
aken = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Poemyyja")

# Laeme taustapildi ja salvestame selle muutujasse
taust = pygame.image.load("bg_shop.png")

# Laeme müüja pildi ja seadistame suuruse
mehike = pygame.image.load("seller.png")
mehike = pygame.transform.scale(mehike, (255, 305))

# Laeme jutu mulli pildi ja suuruse
jutu_mull = pygame.image.load("chat.png")
jutu_mull = pygame.transform.scale(jutu_mull, (255, 200))

aken.blit(taust, [0, 0])            # Joonistame taustapildi
aken.blit(mehike, [105, 160])       # Joonistame mehikese
aken.blit(jutu_mull, [247, 67])     # Joonistame jutu mulli

# Loome fondi objekti, mille suurus on 35
font = pygame.font.Font(None, 35)
# Loome tekstipildi valge värviga
jutt = font.render("Anni", True, [255, 255, 255])

# Joonistame teksti ekraanile
aken.blit(jutt, [325, 145])
# Uuendame ekraani
pygame.display.flip()

# Peamine tsükkel
tootab = True
while tootab:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tootab = False