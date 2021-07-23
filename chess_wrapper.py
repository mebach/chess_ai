import pygame


class chessWrapper:
    def __init__(self, chess_class, image):
        self.original = chess_class
        self.image = image