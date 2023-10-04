#以下是一个简单的pygame程序，可以显示大量粒子运动的效果：
import pygame
import random
import math
# 初始化pygame
pygame.init()

# 创建游戏窗口
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("099")
# chang
class B:
	def __init__(self,size,posit=(0,0,2500,1500)):
		self.size=size
		self.posit=posit
class F:
	def __init__(self,size,angle):
		#angke jis to x
		self.size=size
		self.angle=angle		
# 定义粒子类
class Particle:
    def __init__(self,x=910,y=910,v0=(0.9,45),q=1,m=1,color=(225,225,225)):
        self.x = x
        self.y =2500- y
        self.vx=v0[0]*math.cos(math.radians(v0[1]))
        self.vy=v0[0]*math.sin(math.radians(v0[1]))
        self.v=v0
        self.q = q
        self.m= m
        self.color = color
    def move(self,f):
        #zhengjiao
        Fx=f.size*math.cos(math.radians(f.angle))#Fx
        Fy=f.size*math.sin(math.radians(f.angle))#Fy
        ax=Fx/self.m
        ay=Fy/self.m
        self.vx+=ax
        self.vy+=ay
        self.x+=self.vx
        #only in position use 2500
        self.y-=self.vy
    def draw(self):
		#ui
        pygame.draw.circle(screen, self.color,(self.x,self.y), 7)
        
        
# 创建粒子列表

particles = []
for i in range(1):
    particles.append(Particle(m=random.randint(1,10)))
#F
E=(0,60)
B=0.03
# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新粒子位置
    for e in particles:
        #Eq
        Eq=F(e.q*E[0],E[1])
        e.move(Eq)
        #B
        v=(e.vx**2+e.vy**2)**0.5
        Bvq=B*v*e.q
        cosFluo=-e.vy/v
        f_angle=math.degrees(math.acos(cosFluo))
        Fluo=F(Bvq,f_angle)
        print((Bvq,f_angle,cosFluo))
        e.move(Fluo)

     
    # 清空屏幕
    screen.fill((0, 0, 0))   
    pygame.draw.rect(screen, (255,255,255), (0,2500,2500,0))    #x   
    pygame.draw.rect(screen, (255,255,255), (0,0,0,2600))   #y
    pygame.draw.rect(screen, (255,255,255), (10,2500,10,10))
    
    # 绘制粒子
    for particle in particles:
        particle.draw()
    
    # 更新屏幕显示
    pygame.display.flip()

# 退出游戏
pygame.quit()


#这个程序创建了一个窗口，然后在窗口中显示大量的小圆点，这些小圆点会随机移动，形成一个粒子运动效果。每个粒子具有随机的位置、颜色和速度。程序使用了pygame库来创建窗口、处理事件和绘制图形。