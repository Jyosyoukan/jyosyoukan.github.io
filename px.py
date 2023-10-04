import pygame 
import math
import threading
class Obj:	
	ws=(1600,2500)	
	pygame.init()
	screen=pygame.display.set_mode((500, 700))
	def __init__(self,pattern):
		self.color=(225,224,24)
		self.pattern=pattern
		self.objrect=(0,0,0,0)
		#screen=pygame.display.set_mode((500, 700))
		#screen.fill((0,0,0))
		for i in range(0,160):
			for b in pattern:
				if b[0]==i:
					self.objrect=(int(b[0]*10),int(b[1]),10,int(b[2]-b[1]))
					pygame.draw.rect(screen,self.color,self.objrect)
	#	for o in pattern:
	#	pygame.display.flip()
	def live(self):
		#screen.fill((0,0,0))
		print(self.pattern)
		pattern=self.pattern
		for b in pattern:
			self.objrect=(b[0]*10,b[1],10,b[2]-b[1])
			pygame.draw.rect(screen,self.color,self.objrect)
		pygame.display.flip()
	def mot(self,pm):
		g=0
		for dot in self.pattern:
			for dotp in pm:
				if dot[0]==pm[0]:
					self.pattern[g]=pm
			g+=1
		self.live()
	def move(self,x,y):
		newp=[]
		for b in self.pattern:
			newp.append((b[0]+x,b[1]+y,b[2]+y))
			print(newp)
		self.pattern=newp
		self.live()
		
		
		
	def click(self):
		def ifclick():
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					print(0)
					mx, my = pygame.mouse.get_pos()
					for b in self.pattern:
						if mx>=b[0]*10 and mx<=b[0]*10+10:
							if my>=b[1] and my<=b[2] and pygame.mouse.get_pressed():
								return True;
			return False;
		return ifclick()

#screen.fill((0, 0, 0))  # 清屏为黑色
  # pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rect_width, rect_height))
   # pygame.display.flip()
	#	pass
#hero=Obj(3)
# 游戏循环
i=0
screen=pygame.display.set_mode((500, 700))
running = True
print(pygame.display.get_surface().get_size())
parm=[
(99,110,230),
(100,100,200),#shou
(101,100,300),(101,52,95),
(102,100,200),(102,50,90),
(103,100,300),(103,52,95),
(104,100,200),
(105,110,230)
]
hero=Obj(parm)
dog=Obj(parm)
d=1
while running:
    mx, my = pygame.mouse.get_pos()
    # 事件处理
    i+=d
    if i>50:
    	d=-1
    if i<1:
    	d=1
    if hero.click():
    	d=(-1)*d
    hero.move(0.2*d,1+d) 
    dog.move(d,d)
    #hero=Obj(parm)
   # hero.mot((100,100,0))
    screen.fill((0,0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   #  pygame.display.flip()
# 退出游戏
pygame.quit()



#def my_function():
    # 执行线程任务的代码

# 创建线程对象my_thread = threading.Thread(target=my_function)

# 启动线程my_thread.start()