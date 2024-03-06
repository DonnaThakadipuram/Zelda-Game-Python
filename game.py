### NAME: DONNA THAKADIPURAM
### DATE: 05/04/2023
### DESCRIPTION: ASSIGNMENT 8 LINK GAME IN PYTHON



import pygame
import time

from pygame.locals import*
from time import sleep

class Sprite():
	def __init__(self, x1, y1, w1, h1):
		self.x = x1
		self.y = y1
		self.w = w1
		self.h = h1
		pass
	
	def isLink(self):
		return False
	
	def isTile(self):
		return False
	
	def isBoomerang(self):
		return False
	
	def isPot(self):
		return False
	

class Link(Sprite):
	def __init__(self, x, y, w, h):
		Sprite.__init__(self, x, y, w, h)
		self.zoomies = 10

		self.y = y
		
		self.prev_x = 0
		self.prev_y = 0

		
		
		self.direction = 0
		self.current_image_index = 0
		
		self.link_images = []
		

		for i in range(0, 52):
			if(i < 9):
				#self.link_images[i] = pygame.image.load("linkImages/link0" + "% s" %(i + 1) +".png")
				self.link_images.append(pygame.image.load("linkImages/link0" + "%s" %(i + 1)+ ".png"))
				#print("link image added")
				pass
			if(i > 9):
				self.link_images.append(pygame.image.load("linkImages/link" + "%s" %(i + 1)+ ".png"))
				#print("link image added")
				pass
			pass
		pass

	def update(self):
		return True
		pass

	def setPrevious(self, x, y):
		self.prev_x = x
		self.prev_y = y

	def isBoomerang(self):
		return False
	
	def isTile(self):
		return False
	
	def isLink(self):
		return True

	def isPot(self):
		return False
	

	def getOut(self, spr):
		if((self.x + self.w >= spr.x) and self.prev_x + self.w <= spr.x):
			self.x = spr.x - self.w
			pass

		if((self.x <= spr.x + spr.w) and (self.prev_x >= spr.x + spr.w)):
			self.x = spr.x + spr.w
			pass

		if((self.y + self.h >= spr.y) and (self.prev_y + self.h <= spr.y)):
			self.y = spr.y - self.h
			pass

		if((self.y <= spr.y + spr.h ) and (self.prev_y >= spr.y +spr.h)):
			self.y = spr.y + spr.h
			pass

	def updateDirection(self, direction):
		self.direction = direction
		self.current_image_index += 1
		if(self.direction == 3):
			if(self.current_image_index >= 11):
				self.current_image_index = 0
				pass
			pass
		if(self.current_image_index >= 11):
			self.current_image_index = 0
			pass
		pass

	def draw(self, screen, scroll_x, scroll_y):
		#self.rect = self.link_images[0].get_rect()
		#screen.clearRect(self.x, self.y, self.w, self.h)
		a = self.current_image_index + self.direction * 13
		transformed = pygame.transform.scale(self.link_images[a], (75, 75))
		screen.blit(transformed, (self.x - scroll_x, self. y- scroll_y))
		pass
	pass
pass

class Pot():
	def __init__(self, x1, y1, w1, h1):
		Sprite.__init__(self, x1, y1, w1, h1)

		self.x_dir = 0
		self.y_dir = 0
		self.speed = 15
		self.broken = False
		self.countdown = 50

		self.pot_image = pygame.image.load("pot.png")
		self.pot_image = pygame.transform.scale(self.pot_image, (50, 50))
		self.pot_broken = pygame.image.load("pot_broken.png")
		self.pot_broken = pygame.transform.scale(self.pot_broken, (50, 50))

	def update(self):
			if(self.countdown <= 0):
				return False
			
			if (self.broken == True):
				self.x_dir = 0
				self.y_dir = 0
				self.speed = 0

				self.countdown -= 1
				pass

			self.x += self.x_dir * self.speed
			self.y += self.y_dir * self.speed

			return True
			pass
		
	def draw(self, screen, scroll_x, scroll_y):
		if(self.broken):
			screen.blit(self.pot_broken, (self.x - scroll_x, self. y- scroll_y))
			pass
		else:
			screen.blit(self.pot_image, (self.x - scroll_x, self. y- scroll_y))
		pass

# 	def updateDirection(self, linkDirection):
# if linkDirection == 0:
#         	self.y_dir = 1
#         	self.x_dir = 0
#     elif linkDirection == 1:
#         self.y_dir = 0
#         self.x_dir = -1
#     elif linkDirection == 2:
#         self.y_dir = 0
#         self.x_dir = 1
#     elif linkDirection == 3:
#         self.y_dir = -1
#         self.x_dir = 0

	def updateDirection(self, linkDirection):
		if linkDirection == 0:
			self.y_dir = 1
			self.x_dir = 0
			pass
		elif linkDirection == 1:
			self.y_dir = 0
			self.x_dir = -1
			pass
		elif linkDirection == 2:
			self.y_dir = 0
			self.x_dir = 1
			pass
		elif linkDirection == 3:
			self.y_dir = -1
			self.x_dir = 0


	def isBoomerang(self):
		return False
	
	def isTile(self):
		return False
	
	def isLink(self):
		return False

	def isPot(self):
		return True


class Boomerang(Sprite):
	def __init__(self, x1, y1, w1, h1):
		Sprite.__init__(self, x1, y1, w1, h1)

		self.x_dir = 0 
		self.y_dir = 0

		self.current_image_index = 0
		self.boomerang_images = []
		self.boomerang_images.append(pygame.image.load("boomerangImages/boomerang1.png"))
		self.boomerang_images.append(pygame.image.load("boomerangImages/boomerang2.png"))
		self.boomerang_images.append(pygame.image.load("boomerangImages/boomerang3.png"))
		self.boomerang_images.append(pygame.image.load("boomerangImages/boomerang4.png"))

		for x in range(0, 4):
			self.boomerang_images[x] = pygame.transform.scale(self.boomerang_images[x], (20, 20))
		pass

	def update(self):
		self.x += self.x_dir * 20
		self.y += self.y_dir * 20

		return True
		pass

	def draw(self, screen, scroll_x, scroll_y):
		screen.blit(self.boomerang_images[self.current_image_index % 4], (self.x - scroll_x, self. y- scroll_y))
		if(self.current_image_index == 3):
			self.current_image_index = 0
			pass
		self.current_image_index += 1
		pass

	def isBoomerang(self):
		return True
	
	def isTile(self):
		return False
	
	def isLink(self):
		return False

	def isPot(self):
		return False

	def move(self, linkDirection):
		if linkDirection == 0:
			self.y_dir = 1
			self.x_dir = 0
		elif linkDirection == 1:
			self.y_dir = 0
			self.x_dir = -1
		elif linkDirection == 2:
			self.y_dir = 0
			self.x_dir = 1
		elif linkDirection == 3:
			self.y_dir = -1
			self.x_dir = 0




class Tile(Sprite):
	def __init__(self, x1, y1, w1, h1):
		Sprite.__init__(self, x1, y1, w1, h1)
		self.tile_image = pygame.image.load("tile.jpg")
		self.tile_image = pygame.transform.scale(self.tile_image, (50, 50))
		self.y = y1
		pass

	def isBoomerang(self):
		return False
	
	def isTile(self):
		return True
	
	def isLink(self):
		return False

	def isPot(self):
		return False


	def update(self):
		return True
		pass

	def draw(self, screen, scroll_x, scroll_y):
		screen.blit(self.tile_image, (self.x - scroll_x, self.y - scroll_y))
		pass
	pass





		
		

class Model():
	def __init__(self):
		# self.dest_x = 0
		# self.dest_y = 0
		self.sprites = []

		self.tile = Tile(0, 0, 50, 50)
		self.sprites.append(self.tile)
		#print(self.tile.y)
		
		self.link = Link(150, 150, 75, 75)
		self.sprites.append(self.link)
		#print(self.link.y)

		for x in range(0, 1400, 50):
			self.tile = Tile(x, 0, 50, 50)
			self.sprites.append(self.tile)
			pass
		for y in range(0, 1000, 50):
			self.tile = Tile(0, y, 50, 50)
			self.sprites.append(self.tile)
			pass

		for x in range (0, 1400, 50):
			self.tile = Tile(x, 950, 50, 50)
			self.sprites.append(self.tile)
			pass

		for y in range (0, 1000, 50):
			self.tile = Tile(1350, y, 50, 50)
			self.sprites.append(self.tile)
			pass

		self.tile = Tile(0, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(50, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(100, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(150, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(200, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(400, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(450, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(500, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(550, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(600, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(650, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(700, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(750, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(800, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(850, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(900, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(950, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(1000, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(1050, 450, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(1100, 450, 50, 50)
		self.sprites.append(self.tile)




		self.tile = Tile(0, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(50, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(100, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(150, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(200, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(400, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(450, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(500, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(550, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(600, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(650, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(700, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(750, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(800, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(850, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(900, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(950, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(1000, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(1050, 500, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(1100, 500, 50, 50)
		self.sprites.append(self.tile)


		self.tile = Tile(650, 200, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(650, 250, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(650, 300, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(650, 350, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(650, 400, 50, 50)
		self.sprites.append(self.tile)


		self.tile = Tile(700, 200, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(700, 250, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(700, 300, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(700, 350, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(700, 400, 50, 50)
		self.sprites.append(self.tile)


		self.tile = Tile(650, 550, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(650, 600, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(650, 650, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(650, 700, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(650, 750, 50, 50)
		self.sprites.append(self.tile)

		# self.tile = Tile(650, 800, 50, 50)
		# self.sprites.append(self.tile)

		
		self.tile = Tile(700, 550, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(700, 600, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(700, 650, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(700, 700, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(700, 750, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(450, 400, 50,50)
		self.sprites.append(self.tile)

		self.tile = Tile(500, 400, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(550, 400, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(600, 400, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(500, 350, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(550, 350, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(600, 350, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(550, 300, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(600, 300, 50, 50)
		self.sprites.append(self.tile)


		self.tile = Tile(600, 250, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(1050, 300, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(800, 700, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(750, 700, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(850, 700, 50, 50)
		self.sprites.append(self.tile)

		self.tile = Tile(900, 700, 50, 50)
		self.sprites.append(self.tile)

		self.pot = Pot(900, 650, 50, 50)
		self.sprites.append(self.pot)

		self.pot = Pot(600, 100, 50, 50)
		self.sprites.append(self.pot)

		self.pot = Pot(1050, 400, 50, 50)
		self.sprites.append(self.pot)

		self.pot = Pot(1050, 750, 50, 50)
		self.sprites.append(self.pot)

		self.pot = Pot(100, 600, 50, 50)
		self.sprites.append(self.pot)

		pass


	def addBoomerang(self):
		self.boomerang = Boomerang(self.link.x, self.link.y, 20, 20)
		self.sprites.append(self.boomerang)

		direction = self.link.direction
		self.boomerang.move(direction)
		self.boomerang.update()
		pass


	def collision(self, spr):
		if((self.link.x + self.link.w < spr.x )or (self.link.x > spr.x + spr.w)):
			return False
		
		if((self.link.y + self.link.h < spr.y) or (self.link.y > spr.y + spr.h)):
			return False
		
		return True
	
	def collision2(self, s, d):
		if s.x + s.w <= d.x:
			return False
		if s.x >= d.x + d.w: # + s.width
			return False
		if s.y + s.h <= d.y: # assumes bigger is downward
			return False
		if s.y >= d.y + d.h: # + s.height
			return False
		return True

		


	def update(self):
		for Sprite in self.sprites:
			Sprite.update()
			if(self.collision(Sprite)):
				if(Sprite.isTile()):
					#print("link x: " + str(self.link.x))
					self.link.getOut(Sprite)
					pass

				if(Sprite.isPot()):
					Sprite.updateDirection(self.link.direction)
				pass
			pass
		i = 0
		while i < len(self.sprites):
			if not self.sprites[i].update():
				self.sprites.pop(i)
				continue
			j = 0
			while j < len(self.sprites):
				if(self.collision2(self.sprites[i], self.sprites[j])):
					if self.sprites[i].isBoomerang() and self.sprites[j].isTile():
						self.sprites.pop(i)
						break
					if self.sprites[i].isBoomerang() and self.sprites[j].isPot():
						self.sprites[j].broken = True
						self.sprites.pop(i)
						break
					if self.sprites[i].isTile() and self.sprites[j].isPot():
						self.sprites[j].broken = True
						break

					if self.sprites[i].isBoomerang() and self.sprites[j].isLink():
						pass
					pass
				j+=1
				pass
			i+=1

		
		pass




	# def set_dest(self, pos):
	# 	pass
	# 	# self.dest_x = pos[0]
	# 	# self.dest_y = pos[1]

class View():
	def __init__(self, model):
		self.scroll_x = 0
		self.scroll_y = 0
		screen_size = (700,500)
		self.screen = pygame.display.set_mode(screen_size, 32)
		#self.turtle_image = pygame.image.load("linkImages/link01.png")
		self.model = model
		self.model.rect = pygame.Rect(0,0,0,0)
		#self.model.rect = self.turtle_image.get_rect()

	def update(self):
		self.screen.fill([228, 199, 255])
		for Sprite in self.model.sprites:
			Sprite.draw(self.screen, self.scroll_x, self.scroll_y)
		pygame.display.flip()
			#pygame.display.flip()

		#self.screen.fill([0,200,100])
		#self.screen.blit(self.turtle_image, self.model.rect)
		#pygame.display.flip()

class Controller():
	def __init__(self, model, view):
		self.model = model
		self.view = view
		self.truemerang = False
		self.keep_going = True

	def update(self):
		self.model.link.setPrevious(self.model.link.x, self.model.link.y)
		for event in pygame.event.get():
			if event.type == QUIT:
				self.keep_going = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.keep_going = False
					pass
				if event.key == K_LCTRL or event.key == K_RCTRL:
					self.truemerang = True
				pass
			elif event.type == KEYUP:
				pass

			# elif event.type == pygame.MOUSEBUTTONUP:
			# 	self.model.set_dest(pygame.mouse.get_pos())
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			if(self.model.link.x < 700 and self.view.scroll_x != 0):
				self.view.scroll_x -= 700
				pass
			self.model.link.updateDirection(1)
			self.model.link.x -= self.model.link.zoomies
			pass

		if keys[K_RIGHT]:
			if(self.model.link.x > 700 and self.view.scroll_x != 700):
				pass
				self.view.scroll_x += 700
			self.model.link.updateDirection(2)
			self.model.link.x += self.model.link.zoomies
			pass

		if keys[K_UP]:
			if(self.model.link.y < 500 and self.view.scroll_y != 0):
				self.view.scroll_y -= 500
				pass
			self.model.link.updateDirection(3)
			self.model.link.y -= self.model.link.zoomies
			pass

		if keys[K_DOWN]:
			if(self.model.link.y > 500 and self.view.scroll_y != 500):
				self.view.scroll_y += 500
				pass
			self.model.link.updateDirection(0)
			self.model.link.y += self.model.link.zoomies
			pass
		if self.truemerang:
			#print("boom")
			self.model.addBoomerang()
			self.truemerang = False
			pass

		if keys[K_q]:
			self.keep_going = False

print("Use the arrow keys to move. Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m, v)
while c.keep_going:
	c.update()
	m.update()
	v.update()
	sleep(0.04)
#print("Goodbye")