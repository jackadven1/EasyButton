try:
    import pygame
except:
    raise NameError("module 'PyGame' not found")
from pygame.locals import *
import warnings

__version__ = "1.0.0"

def intro():
    print("PyButton — easily create interactive buttons in PyGame. Created by William DeForest Halsted IV; @jackadven on PyPi, @jackadven on Scratch.")
    print("PyButton source website and documentation: https://github.com/jackadven1/PyButton")

'''def blit_text(message, x, y, color, font, size, quality = True):
    font = pygame.font.SysFont(font, size)
    message = font.render(message, quality, color)
    screen.blit(message,(x, y))'''

def blit_text(message, x, y):
    screen.blit(message, (x, y))

def text_object(message, font, size, color, quality):
    font = pygame.font.SysFont(font, size)
    message = font.render(message, quality, color)
    return message


class rect():
    def __init__(self, pos = (0, 0), width = 100, height = 50, text = "", bg = (255, 255, 255), fg = (0, 0, 0), font = "timesnewroman", pixel = False, thickness = 0, command = None, border = 0, margin = 10, bc = (255, 0, 0), hover_bg = None, hover_fg = None, hover_border = 5, hover_bc = (0, 255, 0), hover_text = None, hover_margin = None, hover_font = None, hover_pixel = False, image = None, hover_image = None):
        self.pos = pos
        if(not type(self.pos) == list and not type(self.pos) == tuple):
            raise TypeError("self.pos must be 'list' or 'tuple'")
        if(not type(self.pos[0]) == int or not type(self.pos[1]) == int):
            raise TypeError("self.pos list indice must be 'int'")
        self.width = width
        if(not type(self.width) == int):
            raise TypeError("self.width must be 'int'")
        self.height = height
        if(not type(self.height) == int):
            raise TypeError("self.height must be 'int'")
        self.text = text
        if(not type(self.text) == str):
            raise TypeError("self.text must be 'str'")
        self.image = image
        if(not type(self.image) == pygame.Surface and not type(self.image) == str and not self.image == None):
            raise TypeError("self.image must be pygame 'Surface' object or 'str'; 'Surface' object preferred")
        if(type(self.image) == str):
            try:
                self.image = pygame.image.load(image)
            except:
                raise NameError("could not open '" + image + "'")
            self.image = pygame.image.load(self.image)
        self.image_object = None
        self.bg = bg
        try:
            if(not len(bg) > 3):
                pygame.Color(bg[0], bg[1], bg[2])
            else:
                pygame.Color(bg[0], bg[1], bg[2], bg[3])
        except:
            raise TypeError("self.bg invalid 'Color' argument")
        self.fg = fg
        try:
            if(not len(fg) > 3):
                pygame.Color(fg[0], fg[1], fg[2])
            else:
                pygame.Color(fg[0], fg[1], fg[2], fg[3])
        except:
            raise TypeError("self.fg invalid 'Color' argument")
        self.font = font
        if(not type(self.font) == str):
            raise TypeError("self.font must be 'str'")
        if(self.font not in pygame.font.get_fonts()):
            warnings.warn("'" + self.font + "' not found in PyGame 'fonts'; defaulting to 'timesnewroman'")
            self.font = "timesnewroman"
        self.pixel = not pixel
        if(not type(self.pixel) == bool):
            warnings.warn("self.pixel must be 'bool'")
        self.hover_pixel = not hover_pixel
        if(not type(self.hover_pixel) == bool):
            raise TypeError("self.hover_pixel must be 'bool'")
        self.thickness = thickness
        if(not type(self.thickness) == int):
            raise TypeError("self.thickness must be 'int'")
        self.border = border
        if(not type(self.border) == int):
            raise TypeError("self.border must be 'int'")
        self.text_info = ["", 0, 0, 0, ""]
        self.text_object = None
        self.margin = margin
        if(not type(self.margin) == int):
            raise TypeError("self.margin must be 'int'")
        self.bc = bc
        try:
            if(not len(bc) > 3):
                pygame.Color(bc[0], bc[1], bc[2])
            else:
                pygame.Color(bc[0], bc[1], bc[2], bc[3])
        except:
            raise TypeError("self.bc invalid 'Color' argument")
        self.command = command
        self.hovering = False
        self.hover_border = hover_border
        if(not type(self.hover_border) == int):
            raise TypeError("self.hover_border must be 'int'")
        if(hover_bc == None):
            self.hover_bc = self.bc
        else:
            self.hover_bc = hover_bc
            try:
                if(not len(hover_bc) > 3):
                    pygame.Color(hover_bc[0], hover_bc[1], hover_bc[2])
                else:
                    pygame.Color(hover_bc[0], hover_bc[1], hover_bc[2], hover_bc[3])
            except:
                raise TypeError("self.hover_bc invalid 'Color' argument")
        if(hover_text == None):
            self.hover_text = text
        else:
            self.hover_text = hover_text
            if(not type(self.hover_text) == str):
                raise TypeError("self.hover_text must be 'str'")
        if(hover_image == None):
             self.hover_image = image
        else:
            self.hover_image = hover_image
            if(not type(self.hover_image) == pygame.Surface and not type(self.hover_image) == str):
                raise TypeError("self.image must be pygame 'Surface' object or 'str'; 'Surface' object preferred")
            if(type(self.hover_image) == str):
                try:
                    self.hover_image = pygame.image.load(self.hover_image)
                except:
                    raise NameError("could not open '" + image + "'")
        if(hover_bg == None):
            self.hover_bg = bg
        else:
            self.hover_bg = hover_bg
            try:
                if(not len(hover_bg) > 3):
                    pygame.Color(hover_bg[0], hover_bg[1], hover_bg[2])
                else:
                    pygame.Color(hover_bg[0], hover_bg[1], hover_bg[2], hover_bg[3])
            except:
                raise TypeError("self.hover_bg invalid 'Color' argument")
        if(hover_fg == None):
            self.hover_fg = fg
        else:
            self.hover_fg = hover_fg
            try:
                if(not len(hover_fg) > 3):
                    pygame.Color(hover_fg[0], hover_fg[1], hover_fg[2])
                else:
                    pygame.Color(hover_fg[0], hover_fg[1], hover_fg[2], hover_fg[3])
            except:
                raise TypeError("self.hover_fg invalid 'Color' argument")
        if(hover_margin == None):
            self.hover_margin = margin
        else:
            self.hover_margin = hover_margin
            if(not type(self.hover_margin) == int):
                raise TypeError("self.hover_margin must be 'int'")
        if(hover_font == None):
            self.hover_font = font
        else:
            self.hover_font = hover_font
            if(not type(self.hover_bg) == text):
                raise TypeError("self.hover_text must be 'str'")
            if(self.font not in pygame.font.get_fonts()):
                warnings.warn("'" + self.hover_font + "' not found in PyGame 'fonts'; defaulting to 'timesnewroman'")
                self.hover_font = "timesnewroman"
    def update(self):
            self.image_object = None
            if(self.hovering == True):
                if(self.text_info[4] != self.hover_text):
                    self.text_info[1] = 0
                    self.text_info[2] = 0
                    self.text_info[3] = 0
                    while self.text_info[1] < self.width - self.hover_border * 2 - self.hover_margin and self.text_info[2] < self.height - self.hover_border * 2 - self.hover_margin:
                        self.text_info[3] = self.text_info[3] + 1
                        self.text_object = text_object(self.hover_text, self.hover_font, self.text_info[3], self.hover_fg, self.hover_pixel)
                        self.text_info[1] = self.text_object.get_width()
                        self.text_info[2] = self.text_object.get_height()
                if(self.image != None):
                    scale = 1
                    image = self.image
                    while image.get_width() > self.width - self.hover_border * 2 - self.hover_margin or image.get_height() > self.width - self.hover_border * 2 - self.hover_margin:
                        image = pygame.transform.scale(self.image, (round(scale * self.image.get_width()), round(scale * self.image.get_height())))
                        scale = scale - .05
                    self.image_object = image
            else:
                if(self.text_info[4] != self.text):
                    self.text_info[1] = 0
                    self.text_info[2] = 0
                    self.text_info[3] = 0
                    while self.text_info[1] < self.width - self.border * 2 - self.margin and self.text_info[2] < self.height - self.border * 2 - self.margin:
                        self.text_info[3] = self.text_info[3] + 1
                        self.text_object = text_object(self.text, self.font, self.text_info[3], self.fg, self.pixel)
                        self.text_info[1] = self.text_object.get_width()
                        self.text_info[2] = self.text_object.get_height()
                if(self.hover_image != None):
                    scale = 1
                    image = self.hover_image
                    while image.get_width() > self.width - self.border // 2 - self.margin or image.get_height() > self.width - self.border // 2 - self.margin:
                        image = pygame.transform.scale(self.hover_image, (round(scale * self.hover_image.get_width()), round(scale * self.hover_image.get_height())))
                        scale = scale - .05
                    self.image_object = image
            self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
            if(self.hovering == False):
                pygame.draw.rect(self.surface, self.bg, (0, 0, self.width, self.height), self.thickness)
                pygame.draw.rect(self.surface, self.bc, (0, 0, self.width, self.height), self.border)
            else:
                pygame.draw.rect(self.surface, self.hover_bg, (0, 0, self.width, self.height), self.thickness)
                pygame.draw.rect(self.surface, self.hover_bc, (0, 0, self.width, self.height), self.hover_border)
            if(self.image_object != None):
                self.surface.blit(self.image_object, (self.width // 2 - self.image_object.get_width() // 2, self.height // 2 - self.image_object.get_height() // 2))
            if(self.text_object != None):
                self.surface.blit(self.text_object, (self.width // 2 - self.text_info[1] // 2, self.height // 2 - self.text_info[2] // 2))
    def draw(self, destination):
        self.update()
        destination.blit(self.surface, (self.pos[0], self.pos[1]))
    def hover(self, point):
        if(pygame.Rect(self.pos[0], self.pos[1], self.width, self.height).collidepoint(point) == True):
            if(self.hovering != True):
                self.text_info[4] = None
            self.hovering = True
        else:
            if(self.hovering != False):
                self.text_info[4] = None
            self.hovering = False
    def check_hover(self, point):
        if(pygame.Rect(self.pos[0], self.pos[1], self.width, self.height).collidepoint(point) == True):
            return True
        else:
            return False
    def click(self, point, down):
        if(pygame.Rect(self.pos[0], self.pos[1], self.width, self.height).collidepoint(point) == True and down == True and self.command != None):
            try:
                self.command()
            except:
                raise NameError("self.command " + self.command.__name__ + " not found")
    def check_click(self, point, down = True):
        if(pygame.Rect(self.pos[0], self.pos[1], self.width, self.height).collidepoint(point) == True and down == True):
            return True
        else:
            return False
    def get_fonts(self):
        fonts = []
        for font in pygame.font.get_fonts():
            fonts.append(font)
        return font


if(not __name__ == "__main__"):
    intro()
