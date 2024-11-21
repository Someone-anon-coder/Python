import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chase The Enemy")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

player_size = 50
player_color = GREEN
player_speed = 5

enemy_size = 30
enemy_color = RED
enemy_speed = 2

num_enemies = 5
font = pygame.font.SysFont('Arial', 30)

class Player(pygame.sprite.Sprite):
    """Player class"""
    
    def __init__(self) -> None:
        """Constructor for Player class"""
        
        super().__init__()
        self.image = pygame.Surface((player_size, player_size))
        self.image.fill(player_color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = player_speed
    
    def update(self, keys: list | None = None) -> None:
        """Update player position
        
        Args:
            keys (list): List of keys pressed
        """
        
        if keys is None:
            return
        
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

class Enemy(pygame.sprite.Sprite):
    """Enemy class"""

    def __init__(self) -> None:
        """Constructor for Enemy class"""
        
        super().__init__()
        self.image = pygame.Surface((enemy_size, enemy_size))
        self.image.fill(enemy_color)
        
        pygame.draw.circle(self.image, WHITE, (enemy_size // 3, enemy_size // 3), 5)
        pygame.draw.circle(self.image, WHITE, (2 * enemy_size // 3, enemy_size // 3), 5)
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - enemy_size)
        self.rect.y = random.randint(0, HEIGHT - enemy_size)
        self.speed = enemy_speed
    
    def update(self, player_rect: pygame.Rect | None = None) -> None:
        """Update enemy position"""
        
        if player_rect is None:
            return
        
        if self.rect.x < player_rect.x:
            self.rect.x += self.speed
        if self.rect.x > player_rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player_rect.y:
            self.rect.y += self.speed
        if self.rect.y > player_rect.y:
            self.rect.y -= self.speed

def game_over() -> None:
    """Game over screen"""
    
    game_over_text = font.render('Game Over! Press R to Restart', True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.update()

def main():
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    enemies = pygame.sprite.Group()
    for _ in range(num_enemies):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
    
    clock = pygame.time.Clock()
    
    running = True
    game_running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        player.update(keys)

        for enemy in enemies:
            enemy.update(player.rect)

        if pygame.sprite.spritecollide(player, enemies, False):
            game_running = False
            game_over()
        
        if game_running:
            all_sprites.update()
            all_sprites.draw(screen)
        
        if not game_running and keys[pygame.K_r]:
            main()
        
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    import time

    time.sleep(5)
    main()