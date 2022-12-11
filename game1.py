import pygame
import math

screen = pygame.display.set_mode((500,500))
		
x = 100
y = 250
acceleration = 0
gravity = 0.5
jump = 0
jumpv1 = 0
ground = 400
level = 1
coin1 = 0
coin2 = 0
coin3 = 0
coin4 = 0
coin5 = 0
ice = 0
icev1 = 0


while True:
	
	#Sky
	screen.fill((0,0,200))
	
	#Sun
	pygame.draw.rect(screen,(0,0,0),(25,35,80,80))
	pygame.draw.rect(screen,(235,235,0),(30,40,75,75))
	pygame.draw.rect(screen,(255,255,204),(40,50,55,55))
	
	#Ground
	pygame.draw.rect(screen,(140,70,20),(0,428,500,75))	
	pygame.draw.rect(screen,(0,150,0),(0,428,500,10))	

	#Coin Counter
	pygame.draw.rect(screen,(255,215,0),(20,460,120,30))
	pygame.init()
	text1 = pygame.font.SysFont('Verdana', 20)
	line = f"Coins: {coin1+coin2+coin3+coin4+coin5}"
	text2 = pygame.font.Font.render(text1,line,True, (0,0,0))
	screen.blit(text2,(30,460))


	#Screen 1
	#Coins
	if level == 1:
		if coin1 == 0:
			pygame.draw.circle(screen,(0,0,0),(300,350),13)
			pygame.draw.circle(screen,(255,215,0),(300,350),10)

		if coin2 == 0:
			pygame.draw.circle(screen,(0,0,0),(350,350),13)
			pygame.draw.circle(screen,(255,215,0),(350,350),10)		

		if coin3 == 0:
			pygame.draw.circle(screen,(0,0,0),(325,315),13)
			pygame.draw.circle(screen,(255,215,0),(325,315),10)		
 
		p1 = (300,350)
		p2 = (x+12.5,y+12.5)
		p3 = (350,350)
		p4 = (325,315)
	
		#Using pythagorean theorem
		distance1 = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
		distance2 = math.sqrt(((p3[0]-p2[0])**2)+((p3[1]-p2[1])**2))
		distance3 = math.sqrt(((p4[0]-p2[0])**2)+((p4[1]-p2[1])**2))

		if distance1 < 30:
			coin1 = 1

		if distance2 < 30:
			coin2 = 1

		if distance3 < 30:
			coin3 = 1

	

		#Character
		pygame.draw.rect(screen,(0,0,0),(x-2,y-2,29,29))
		pygame.draw.rect(screen,(160,0,160),(x,y,25,25))
		pygame.draw.arc(screen,(0,0,0),(x+7,y+14,10,8),3,6.1)
		pygame.draw.circle(screen,(0,0,0),(x+7,y+7),4)
		pygame.draw.circle(screen,(0,0,0),(x+18,y+7),4)

	#Screen 2
	#Mushroom jump
	if level == 2:
		ice = 0
		#Mushroom
		pygame.draw.rect(screen,(150,75,0),(180,390,30,40))	
		pygame.draw.rect(screen,(255,255,255),(160,370,70,30))	
		
		if coin1 + coin2 + coin3 + coin4 + coin5 == 5: 
			
			#Secret Door
			pygame.draw.rect(screen,(140,70,20),(175,0,30,10))
			pygame.draw.circle(screen,(0,0,0),(190,8),2)

			p1 = (190,10)
			p2 = (x+12.5,y)

			distanceS = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

			if distanceS < 10:
				level = 8



		#Character
		pygame.draw.rect(screen,(0,0,0),(x-2,y-2,29,29))
		pygame.draw.rect(screen,(160,0,160),(x,y,25,25))
		pygame.draw.arc(screen,(0,0,0),(x+7,y+14,10,8),3,6.1)
		pygame.draw.circle(screen,(0,0,0),(x+7,y+7),4)
		pygame.draw.circle(screen,(0,0,0),(x+18,y+7),4)


		p1 = (180,370)
		p2 = (x+12.5,y+25)
		p3 = (210,370)

		distance4 = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
		distance5 = math.sqrt(((p3[0]-p2[0])**2)+((p3[1]-p2[1])**2))

		#Super Jump
		if distance4 < 20 or distance5 < 20:
			acceleration = 20
			
			if acceleration > 0:
				jumpv1 += 7
				acceleration -= 0.5
				y -= gravity * acceleration + jumpv1
		
			#Falling
			if acceleration <= 0 and y < ground:
				acceleration -= 0.5 
				y -= gravity * acceleration + jumpv1

			if y >= 395:
				y = ground
				acceleration = 0

		if y == ground:
			jumpv1 = 0



		if coin4 == 0:
			pygame.draw.circle(screen,(0,0,0),(195,200),13)
			pygame.draw.circle(screen,(255,215,0),(195,200),10)		
 
		p1 = (195,200)
		p2 = (x+12.5,y+12.5)
	
		#Using pythagorean theorem
		distance6 = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
		
		if distance6 < 30:
			coin4 = 1


	#Screen 3
	#Ice
	if level == 3:
		#Character
		pygame.draw.rect(screen,(0,0,0),(x-2,y-2,29,29))
		pygame.draw.rect(screen,(160,0,160),(x,y,25,25))
		pygame.draw.arc(screen,(0,0,0),(x+7,y+14,10,8),3,6.1)
		pygame.draw.circle(screen,(0,0,0),(x+7,y+7),4)
		pygame.draw.circle(screen,(0,0,0),(x+18,y+7),4)
		
		ice = 1
		#Ice
		pygame.draw.rect(screen,(100,180,255),(0,428,500,10))	

		if coin5 == 0:
			pygame.draw.circle(screen,(0,0,0),(250,350),13)
			pygame.draw.circle(screen,(255,215,0),(250,350),10)		
 
		p1 = (250,350)
		p2 = (x+12.5,y+12.5)
	
		#Using pythagorean theorem
		distance7 = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
		
		if distance7 < 30:
			coin5 = 1

	#Screen 4
	#The End
	if level == 4:		
		#End Text
		text2 = pygame.font.SysFont('Verdana', 100)
		line2 = "The End"
		text2 = pygame.font.Font.render(text2,line2,True, (255,130,0))
		screen.blit(text2,(50,200))

		#Character
		pygame.draw.rect(screen,(0,0,0),(x-2,y-2,29,29))
		pygame.draw.rect(screen,(160,0,160),(x,y,25,25))
		pygame.draw.arc(screen,(0,0,0),(x+7,y+14,10,8),3,6.1)
		pygame.draw.circle(screen,(0,0,0),(x+7,y+7),4)
		pygame.draw.circle(screen,(0,0,0),(x+18,y+7),4)

		ice = 0

	#Screen 5
	#Where are you going
	if level == 5:
		#Error Text
		text3 = pygame.font.SysFont('Verdana', 40)
		line3 = "Where you going?"
		text3 = pygame.font.Font.render(text3,line3,True, (255,0,0))
		screen.blit(text3,(50,200))

		#Character
		pygame.draw.rect(screen,(0,0,0),(x-2,y-2,29,29))
		pygame.draw.rect(screen,(160,0,160),(x,y,25,25))
		pygame.draw.arc(screen,(0,0,0),(x+7,y+14,10,8),3,6.1)
		pygame.draw.circle(screen,(0,0,0),(x+7,y+7),4)
		pygame.draw.circle(screen,(0,0,0),(x+18,y+7),4)

	#Screen 6
	#Go Back
	if level == 6:
		#Error Text
		text4 = pygame.font.SysFont('Verdana', 40)
		line4 = "GO BACK NOW!"
		text4 = pygame.font.Font.render(text4,line4,True, (255,0,0))
		screen.blit(text4,(50,200))

		#Character
		pygame.draw.rect(screen,(0,0,0),(x-2,y-2,29,29))
		pygame.draw.rect(screen,(160,0,160),(x,y,25,25))
		pygame.draw.arc(screen,(0,0,0),(x+7,y+14,10,8),3,6.1)
		pygame.draw.circle(screen,(0,0,0),(x+7,y+7),4)
		pygame.draw.circle(screen,(0,0,0),(x+18,y+7),4)


	#Sends you to the start
	if level == 7:
		x = 5
		level = 1

	#Secret Ending
	if level == 8:
		#Error Text
		text4 = pygame.font.SysFont('Verdana', 60)
		line4 = "YOU WIN!!!"
		text4 = pygame.font.Font.render(text4,line4,True, (255,130,0))
		screen.blit(text4,(50,200))



		#Character
		pygame.draw.rect(screen,(0,0,0),(x-2,y-2,29,29))
		pygame.draw.rect(screen,(255,215,0),(x,y,25,25))
		pygame.draw.arc(screen,(0,0,0),(x+7,y+14,10,8),3,6.1)
		pygame.draw.circle(screen,(0,0,0),(x+7,y+7),4)
		pygame.draw.circle(screen,(0,0,0),(x+18,y+7),4)



	#Movement
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()



	keys = pygame.key.get_pressed()	

	#Left
	if keys[pygame.K_LEFT]:
		
		if ice == 1:
			icev1 = -10

		else:
			x -= 3

		#Trail
		if y == ground:
			pygame.draw.circle(screen,(150,75,0),(x+28,y+25),3)
			pygame.draw.circle(screen,(150,75,0),(x+35,y+25),2)
			pygame.draw.circle(screen,(150,75,0),(x+38,y+25),1)
	
	#Ice left
	if ice == 1:
		if icev1 <= -1:
			x += icev1 * 0.3
			icev1 += 0.1 
	else:
		icev1 = 0

	#Right
	if keys[pygame.K_RIGHT]:
		
		if ice == 1:
			icev1 = 10

		else:
			x += 3
		
		#Tail
		if y == ground:
			pygame.draw.circle(screen,(150,75,0),(x-3,y+25),3)
			pygame.draw.circle(screen,(150,75,0),(x-10,y+25),2)
			pygame.draw.circle(screen,(150,75,0),(x-13,y+25),1)

	#Ice right		
	if ice == 1:
		if icev1 >= 1:
			x += icev1 * 0.3
			icev1 -= 0.1 
	else:
		icev1 = 0

	#Jump
	if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and y == ground: 
		acceleration = 15

	if acceleration > 0:
		acceleration -= 0.5
		y -= gravity * acceleration
		

	#Falling
	if acceleration <= 0 and y < ground:
		acceleration -= 0.5 
		y -= gravity * acceleration

		if y >= 395:
			y = ground
			acceleration = 0


	#Only go right	
	if x >= 475:
		if level != 8:
			x = 5
			level += 1
		else:
			x = 475

	
	if x <= 0:
		if level != 8:
			x = 474
			if level > 1:
				level -= 1
			else:
				level = 1
				x=0
		else:
			x = 0

	#Rest
	if keys[pygame.K_r]:
		x = 0
		y = ground
		level = 1
		coin1 = 0
		coin2 = 0
		coin3 = 0
		coin4 = 0
		coin5 = 0
		ice = 0


	pygame.display.update()



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
