import pygame

class SpriteSheet(object):
    def __init__(self, path):
        pass


    def get_frames(self, frame_numbers):
        frames = []
        for frame_number in frame_numbers:
            frames.append(pygame.Rect(0, 0, 40, 40))

        return frames
