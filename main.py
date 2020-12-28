import random
import time
import pygame
import sys

print("0:简单模式\n1:普通模式\n2:困难模式\n")
mode = int(input("选择模式"))
size = 500
count = 20
p_size = int(size / count)

if mode == 0:
    size = 400
    count = 5
    p_size = int(size / count)
    pass
elif mode == 1:
    size = 400
    count = 10
    p_size = int(size / count)
    pass
elif mode == 2:
    size = 500
    count = 20
    p_size = int(size / count)
    pass
else:
    size = 400
    count = 10
    p_size = int(size / count)
    pass

# 360 = (count - 1) * p_size
# 40 = p_size
score = 0
pic_number = 1
pygame.init()
screen = pygame.display.set_mode((size, size))
pic = str(pic_number) + ".png"
pic_obj = pygame.image.load(pic)
pic_obj_rect = pic_obj.get_rect()
pics = {}
pic_rects = {}
pic_numbers = {}


def get_pos(x: int):
    j = 0
    while j <= (count - 1) * p_size:
        if j <= x < j + p_size:
            return j
        j += p_size


i = 0
j = 0
while j <= (count - 1) * p_size:
    i = 0
    while i <= (count - 1) * p_size:
        pic_number = random.randint(1, 4)
        pic = str(pic_number) + ".png"
        pic_obj = pygame.image.load(pic, str(pic_number))
        pic_obj = pygame.transform.scale(pic_obj, (p_size, p_size))
        pic_obj_rect = pic_obj.get_rect()
        screen.blit(pic_obj, (i, j))
        pics[str(i) + str(j)] = pic_obj
        pic_rects[str(i) + str(j)] = pic_obj_rect
        pic_numbers[pic_obj] = pic_number
        # print(str(i) + str(j))
        pygame.display.flip()
        i += p_size
    j += p_size

start = time.time()
while True:
    if time.time() - start >= 6:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            m0 = get_pos(pygame.mouse.get_pos()[0])
            m1 = get_pos(pygame.mouse.get_pos()[1])
            if not pics.__contains__((str(m0) + str(m1))):
                break
            if pic_numbers[pics[(str(m0) + str(m1))]] == 4:
                score += 1
                BLACK = 0, 0, 0
                tmp = pics[(str(m0) + str(m1))]
                screen.blit(tmp, (m0, m1), tmp.fill(BLACK))
                pics.pop((str(m0) + str(m1)))
    pygame.display.set_caption("找到笑脸 Score: " + str(score))
    pygame.display.update()

print("你的得分: " + str(score))
