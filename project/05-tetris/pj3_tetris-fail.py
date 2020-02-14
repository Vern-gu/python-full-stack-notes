# coding:utf8

import sys
import random
import pygame
from pygame.locals import *


class CubeShape:
    # 骨牌形状、坐标定义
    SHAPES = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
    I = [[(0, -1), (0, 0), (0, 1), (0, 2)],  # (y,x)(行，列)
         [(-1, 0), (0, 0), (1, 0), (2, 0)]]
    J = [[(-2, 0), (-1, 0), (0, 0), (0, -1)],
         [(-1, 0), (0, 0), (0, 1), (0, 2)],
         [(0, 1), (0, 0), (1, 0), (2, 0)],
         [(0, -2), (0, -1), (0, 0), (1, 0)]]
    L = [[(-2, 0), (-1, 0), (0, 0), (0, 1)],
         [(1, 0), (0, 0), (0, 1), (0, 2)],
         [(0, -1), (0, 0), (1, 0), (2, 0)],
         [(0, -2), (0, -1), (0, 0), (-1, 0)]]
    O = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
    S = [[(-1, 0), (0, 0), (0, 1), (1, 1)],
         [(1, -1), (1, 0), (0, 0), (0, 1)]]
    T = [[(0, -1), (0, 0), (0, 1), (-1, 0)],
         [(-1, 0), (0, 0), (1, 0), (0, 1)],
         [(0, -1), (0, 0), (0, 1), (1, 0)],
         [(-1, 0), (0, 0), (1, 0), (0, -1)]]
    Z = [[(0, -1), (0, 0), (1, 0), (1, 1)],
         [(-1, 0), (0, 0), (0, -1), (1, -1)]]
    SHAPES_WITH_DIR = {'I': I, 'J': J, 'L': L, 'O': O, 'S': S, 'T': T, 'Z': Z}

    def __init__(self):  # 初始化骨牌特征
        self.shape = self.SHAPES[random.randint(0, len(self.SHAPES) - 1)]
        # 骨牌所在的行列
        self.center = (2, 7 // 2)
        self.dir = random.randint(0, len(self.SHAPES_WITH_DIR[self.shape]) - 1)
        self.color = Surface.shapes_color[random.randint(0, len(Surface.shapes_color) - 1)]

    def get_all_gridpos(self, center=None):  # 获取当前的骨牌形状位置
        curr_shape = self.SHAPES_WITH_DIR[self.shape][self.dir]
        if center is None:
            center = [self.center[0], self.center[1]]
        return [(cube[0] + center[0], cube[1] + center[1])
                for cube in curr_shape]

    def draw(self):  # 画出骨牌
        for cube in self.get_all_gridpos():
            pygame.draw.rect(frame.screen, self.color,
                             (cube[1] * 20, cube[0] * 20,
                              20, 20))
            # pygame.draw.rect(screen, WHITE,
            #                  (cube[1] * GRID_WIDTH, cube[0] * GRID_WIDTH,
            #                   GRID_WIDTH, GRID_WIDTH),
            #                  1)

    def conflict(self, center):  # 判断方块位置是否合法
        for cube in self.get_all_gridpos(center):
            # 超出屏幕之外，说明不合法
            if cube[0] < 0 or cube[1] < 0 or cube[0] >= frame.cube_width_num or \
                    cube[1] >= frame.cube_height_num:
                return True
            # 不为None，说明之前已经有小方块存在了，也不合法
            if frame.screen_color_matrix[cube[0]][cube[1]] is not None:
                return True
        return False

    def rotate(self):
        new_dir = self.dir + 1  # 下一个方向
        new_dir %= len(self.SHAPES_WITH_DIR[self.shape])
        old_dir = self.dir
        self.dir = new_dir
        if self.conflict(self.center):
            self.dir = old_dir
            return False

    def down(self):
        center = (self.center[0] + 1, self.center[1])
        if self.conflict(center):
            return False
        self.center = center
        return True

    def left(self):
        center = (self.center[0], self.center[1] - 1)
        if self.conflict(center):
            return False
        self.center = center
        return True

    def right(self):
        center = (self.center[0], self.center[1] + 1)
        if self.conflict(center):
            return False
        self.center = center
        return True


class Surface:
    red = (220, 20, 60)
    purple = (128, 0, 128)
    blue = (0, 0, 255)
    steelblue = (70, 130, 180)
    green = (0, 128, 0)
    yellow = (255, 255, 0)
    tomato = (255, 99, 71)
    maroon = (128, 0, 0)
    shapes_color = [red, purple, blue, steelblue, green, yellow, tomato, maroon]
    def __init__(self):
        self.cube_width_num, self.cube_height_num = 15,25
        self.screen_color_matrix = [[None] * int(self.cube_width_num)for i in range(int(self.cube_height_num))]
        self.gray = (20, 20, 20)
        self.black = (0, 0, 0)
        pygame.init()
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((480, 500), 0, 32)
        self.score = 0
        self.level = 1

    def remove_full_line(self):
        new_matrix = [[None] * int(frame.cube_width_num) for i in range(int(frame.cube_height_num))]
        index = frame.cube_height_num - 1
        n_full_line = 0
        for i in range(frame.cube_height_num-1, -1, -1):
            is_full = True
            for j in range(frame.cube_width_num):
                if frame.screen_color_matrix[i][j] is None:
                    is_full = False
                    continue
            if not is_full:
                new_matrix[index] = frame.screen_color_matrix[i]
                index -= 1
            else:
                n_full_line += 1
        self.score += n_full_line
        self.level = self.score // 20 + 1
        frame.screen_color_matrix = new_matrix

    def draw_grid(self):
        self.screen.fill(self.black)
        for i in range(int(self.cube_width_num)):  # 画出网格线
            pygame.draw.line(self.screen, self.gray, (20 * i, 0), (20 * i, 500))  # 后两坐标代表直线始末点
        for i in range(int(self.cube_height_num)):
            pygame.draw.line(self.screen, self.gray, (0, 20 * i), (280, 20 * i))

    def main_loop(self):
        gameover = True
        counter = 0
        cube_shape = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if gameover:
                        gameover = False
                        cube_shape = CubeShape()
                        break
                    if event.key == pygame.K_LEFT:
                        cube_shape.left()
                    elif event.key == pygame.K_RIGHT:
                        cube_shape.right()
                    elif event.key == pygame.K_UP:
                        cube_shape.rotate()
                    elif event.key == pygame.K_DOWN:
                        cube_shape.down()
                    elif event.key == pygame.K_SPACE:
                        while cube_shape.down():
                            pass
                    frame.remove_full_line()
            # level 是为了方便游戏的难度，level 越高 FPS // level 的值越小
            # 这样屏幕刷新的就越快，难度就越大
            if gameover is False and counter % (30 // frame.level) == 0:
                # down 表示下移骨牌，返回False表示下移不成功，可能超过了屏幕或者和之前固定的
                # 小方块冲突了
                if not cube_shape.down():
                    for cube in cube_shape.get_all_gridpos():
                        frame.screen_color_matrix[cube[0]][cube[1]] = cube_shape.color
                    live_cube = CubeShape()
                    if live_cube.conflict(cube_shape.center):
                        gameover = True
                        cube_shape.score = 0
                        cube_shape = None
                        frame.screen_color_matrix = [[None] * frame.cube_width_num for i in range(frame.cube_height_num)]
                # 消除满行
                frame.remove_full_line()
            counter += 1
            self.clock.tick(30)
            frame.draw_grid()
            if cube_shape is not None:
                cube_shape.draw()
            # if gameover:
            #     show_welcome(frame.screen)
            pygame.display.update()


frame = Surface()

if __name__ == "__main__":
    frame.draw_grid()
    frame.main_loop()


