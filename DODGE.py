from math import sin, cos, pi
import random
import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    #플레이어 객체
    def __init__(self, speed, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([10,10])
        image_surface.fill([255,255,255])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.speed = speed

class Bullet(pygame.sprite.Sprite):
    #총알 객체
    def __init__(self, speed, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([5,5])
        image_surface.fill([150,150,255])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.speed = speed
    
    def move(self, time):
        if self.rect.left < 0 and self.speed[0] < 0:
            self.speed[0] = -self.speed[0]
            self.rect.left = 0
        if self.rect.right > screen.get_width() and self.speed[0] > 0:
            self.speed[0] = -self.speed[0]
            self.rect.right = screen.get_width()
        if self.rect.top < 0 and self.speed[1] < 0:
            self.speed[1] = -self.speed[1]
            self.rect.top = 0
        if self.rect.bottom > screen.get_height() and self.speed[1] > 0:
            self.speed[1] = -self.speed[1]
            self.rect.bottom = screen.get_height()
        self.rect = self.rect.move(self.speed)

def main(bullet_num=50,bullet_speed=3,player_speed=3):
	#파이게임 시작
	global screen
	pygame.init()
	pygame.display.set_caption("DODGE")
	screen = pygame.display.set_mode([640,480])
	clock = pygame.time.Clock()
	time_score_font = pygame.font.Font(None, 30)
	time_score_pos = [10, 10]

	#객체 초기값 설정
	player = Player(player_speed, [screen.get_width()/2,screen.get_height()/2])
	playergroup = pygame.sprite.Group()
	playergroup.add(player)
	bulletgroup = pygame.sprite.Group()

	#총알 추가하는 반복루프
	for topline in range(bullet_num//4 + bullet_num%4):
		ran_angle = random.random()*pi
		bullet = Bullet([bullet_speed*cos(ran_angle)+0.5, bullet_speed*sin(ran_angle)+0.5], [random.randint(10, screen.get_width()-10),10])
		bulletgroup.add(bullet)
	for bottomline in range(bullet_num//4):
		ran_angle = random.random()*pi
		bullet = Bullet([bullet_speed*cos(ran_angle)+0.5, bullet_speed*sin(ran_angle)+0.5], [random.randint(10, screen.get_width()-10),screen.get_width()-10])
		bulletgroup.add(bullet)
	for leftline in range(bullet_num//4):
		ran_angle = random.random()*pi
		bullet = Bullet([bullet_speed*cos(ran_angle)+0.5, bullet_speed*sin(ran_angle)+0.5], [10,random.randint(10, screen.get_height()-10)])
		bulletgroup.add(bullet)
	for rightline in range(bullet_num//4):
		ran_angle = random.random()*pi
		bullet = Bullet([bullet_speed*cos(ran_angle)+0.5, bullet_speed*sin(ran_angle)+0.5], [screen.get_width()-10,random.randint(10, 470)])
		bulletgroup.add(bullet)
		
	pygame.key.set_repeat(100,100)
	running = True
	raw_time = pygame.time.get_ticks()/1000

	while running:  #이벤트 루프
		screen.fill([0,0,0])
		right_switch = 0
		left_switch = 0
		up_switch = 0
		down_switch = 0
		time_score = "%.2f" % (pygame.time.get_ticks()/1000 - raw_time)
		time_score_surf = time_score_font.render(str(time_score) + 's', 1, (255, 255, 255))
		keydown = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
        #플레이어 움직임
		if keydown[pygame.K_RIGHT] and player.rect.right < screen.get_width():
			right_switch = 1
		if keydown[pygame.K_LEFT] and player.rect.left > 0:
			left_switch = 1
		if keydown[pygame.K_UP] and player.rect.top > 0:
			up_switch = 1
		if keydown[pygame.K_DOWN] and player.rect.bottom < screen.get_height():
			down_switch = 1
		if keydown[pygame.K_LSHIFT]:
			player.rect = player.rect.move((player_speed - 1) * (right_switch - left_switch), (player_speed - 1) * (down_switch - up_switch))
		else:
			player.rect = player.rect.move(player_speed * (right_switch - left_switch) , player_speed * (down_switch - up_switch))
		for bullets in pygame.sprite.Group.sprites(bulletgroup):
			bullets.move(float(("%.2f" %(pygame.time.get_ticks()/1000 - raw_time))))
		
		playergroup.draw(screen)
		bulletgroup.draw(screen)
		screen.blit(time_score_surf, time_score_pos)
		pygame.display.flip()
		
		pygame.sprite.groupcollide(playergroup, bulletgroup, True, True)  #충돌판정
		if not playergroup.has(player) == True:
			final_score = "%.2f" %(pygame.time.get_ticks()/1000 - raw_time)
			final_text = "Game Over"
			ft_font = pygame.font.Font(None, 70)
			ft_surf = ft_font.render(final_text, 1, [255,255,255])
			screen.blit(ft_surf, [screen.get_width()/2 - ft_surf.get_width()/2, 200])
			pygame.display.flip()
			pygame.time.delay(1500)
			pygame.quit()
			return final_score
		
		clock.tick(60)

if __name__ == "__main__":
	main()
