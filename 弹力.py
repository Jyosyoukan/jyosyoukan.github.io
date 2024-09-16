import pygame
import random as r

pygame.init()
k=r.randint(0,1000)
# 设置窗口大小和标题
size = (1600, 2600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rectangle Motion")

# 设置矩形的初始位置和速度
rect_x = 400
rect_y = 400
rect_speed_x = 0
rect_speed_y = 0

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 如果鼠标左键被按下，则减少矩形速度
            mx, my = pygame.mouse.get_pos()
            rect_speed_x+=(mx-800)/300
            rect_speed_y+=(my-1300)/400


    # 移动矩形
    rect_x += rect_speed_x
    rect_y += rect_speed_y
    rect_speed_x-=0
    rect_speed_y+=0.09
    if rect_x in range(0,400):
    	done=True

    # 检查矩形是否超出屏幕边界
    if rect_x < 0 or rect_x > size[0] - 50:
    	rect_speed_x = -rect_speed_x 
    if rect_y < 0 or rect_y > size[1] - 400:
        if rect_x<k or rect_x>k+200:
         	rect_speed_y = -rect_speed_y

    # 填充背景色
    screen.fill((255, 255, 255))

    # 绘制矩形
    pygame.draw.rect(screen, (0, 0, 255), [rect_x, rect_y, 50, 50])

    # 刷新屏幕
    pygame.display.flip()

# 退出程序
pygame.quit()