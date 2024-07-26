import pygame

class SokobanGame:
    def __init__(self):
        pygame.init()

        self.font = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption("Sokoban")

        self.load_images()

        self.map_data = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                         [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                         [1, 2, 3, 0, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1],
                         [1, 0, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 1, 0, 0, 0, 1],
                         [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.height = len(self.map_data)
        self.width = len(self.map_data[0])
        self.scale = self.images[0].get_width()

        screen_height = self.scale * self.height
        screen_width = self.scale * self.width
        self.screen = pygame.display.set_mode((screen_width, screen_height + self.scale))

        self.start_new_game()

        self.game_loop()

    def load_images(self):
        self.images = []
        for name in ["floor", "wall", "target", "box", "robot", "completed", "targeted_robot"]:
            self.images.append(pygame.image.load("src\\" + name + ".png"))

    def start_new_game(self):
        self.moves_count = 0

    def game_loop(self):
        while True:
            self.handle_events()
            self.draw_game()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_robot(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.move_robot(0, 1)
                if event.key == pygame.K_UP:
                    self.move_robot(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.move_robot(1, 0)

                if event.key == pygame.K_F2:
                    self.start_new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.QUIT:
                exit()

    def move_robot(self, move_y, move_x):
        if self.is_game_over():
            return

        old_robot_y, old_robot_x = self.find_robot()
        new_robot_y = old_robot_y + move_y
        new_robot_x = old_robot_x + move_x

        if self.map_data[new_robot_y][new_robot_x] == 1:
            return

        if self.map_data[new_robot_y][new_robot_x] in [3, 5]:
            box_new_y = new_robot_y + move_y
            box_new_x = new_robot_x + move_x

            if self.map_data[box_new_y][box_new_x] in [1, 3, 5]:
                return

            self.map_data[new_robot_y][new_robot_x] -= 3
            self.map_data[box_new_y][box_new_x] += 3

        self.map_data[old_robot_y][old_robot_x] -= 4
        self.map_data[new_robot_y][new_robot_x] += 4

        self.moves_count += 1

    def find_robot(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map_data[y][x] in [4, 6]:
                    return (y, x)

    def draw_game(self):
        self.screen.fill((0, 0, 0))

        for y in range(self.height):
            for x in range(self.width):
                tile = self.map_data[y][x]
                self.screen.blit(self.images[tile], (x * self.scale, y * self.scale))

        text = self.font.render("Moves: " + str(self.moves_count), True, (255, 0, 0))
        self.screen.blit(text, (25, self.height * self.scale + 10))

        text = self.font.render("F2 = new game", True, (255, 0, 0))
        self.screen.blit(text, (200, self.height * self.scale + 10))

        text = self.font.render("Esc = close game", True, (255, 0, 0))
        self.screen.blit(text, (400, self.height * self.scale + 10))

        if self.is_game_over():
            text = self.font.render("Congratulations, you completed the game!", True, (255, 0, 0))
            text_x = self.scale * self.width / 2 - text.get_width() / 2
            text_y = self.scale * self.height / 2 - text.get_height() / 2
            pygame.draw.rect(self.screen, (0, 0, 0), (text_x, text_y, text.get_width(), text.get_height()))
            self.screen.blit(text, (text_x, text_y))

        pygame.display.flip()

    def is_game_over(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map_data[y][x] in [2, 6]:
                    return False
        return True

if __name__ == "__main__":
    SokobanGame()
