import pygame
pygame.init()


class Score:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.highest_score = 0
        self.font_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Arial", 21, bold=True)

    def __update_score(self):
        return str(self.score)

    def store_highest_score(self):
        # If current score is higher than the saved highest score,
        # the file is overwritten with the current score
        with open("bestscore.txt","r") as f:
            self.highest_score = int(f.read().strip())

        if self.score > self.highest_score:
            with open("bestscore.txt", "w") as f:
                f.write(str(self.score))
                self.highest_score = self.score

            return self.highest_score

    def __get_highest_score(self):
        with open("bestscore.txt","r") as f:
            try:
                self.highest_score = int(f.read().strip())
            except ValueError:
                print("The file is empty.")
                # An initial score 0 should be saved
                # Cannot turn an empty str into int

        return str(self.highest_score)

    def display_score(self):
        text = "Score:" + self.__update_score()
        score_label = self.font.render(text, 1, self.font_color)
        self.screen.blit(score_label, (600, 730))

        best_score = "Best Score:" + self.__get_highest_score()
        score_label2 = self.font.render(best_score, 1, self.font_color)
        self.screen.blit(score_label2, (600, 750))

