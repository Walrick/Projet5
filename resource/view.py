#!/usr/bin/python3
# -*- coding: utf8 -*-

import pygame
import resource.constant as constant


class View:
    """ View class to communicate with the user """

    def __init__(self, view_type):

        self.view_type = view_type
        if self.view_type == "graphic":
            # Size of screen
            self.size = [1200, 100]
            pygame.init()
            # Display the screen
            self.screen = pygame.display.set_mode(self.size)
            pygame.display.set_caption('Pur Beurre')
            self.screen.fill((128, 128, 128))
            # Init keydown
            self.keydown = []

    def display(self, data):
        """Display fonction"""

        if self.view_type == "graphic":
            # ecrase the screen
            self.screen.fill((128, 128, 128))
            y = 0
            if "text_header" in data:
                for text in data["text_header"]:
                    font = pygame.font.Font(None, 24)
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                y += 5

            if "text_item_selec" in data:
                for text in data["text_item_selec"]:
                    font = pygame.font.Font(None, 24)
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                y += 5

            if "list_item_category" in data:
                for item in data["list_item_category"]:
                    font = pygame.font.Font(None, 24)
                    text = str(item[0]) + " : " + item[1]
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                y += 5

            if "list_item_products" in data:
                for item in data["list_item_products"]:
                    font = pygame.font.Font(None, 24)
                    text = str(item[0]) + " : " + item[1] + \
                        ", Nutri-Score : " + item[3]
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                y += 5

            if "list_item_substitut" in data:
                for item in data["list_item_substitut"]:
                    font = pygame.font.Font(None, 24)
                    text = str(item[0]) + " : " + item[2] + \
                        ", nombre de substitut : " + str(item[3])
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                y += 5

            if "list_item_products_for_substitut" in data:
                for item in data["list_item_products_for_substitut"]:
                    font = pygame.font.Font(None, 24)
                    text = str(item[0]) + " : " + item[1] + \
                        ", Nutri-Score : " + item[3]
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                    text = "Magasin : " + item[4] + ", Trace : " + \
                        item[5] + ", Allergène : " + item[6]
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                    text = "URL : " + item[7]
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                y += 5

            if "list_item_substitut_display" in data:
                for item in data["list_item_substitut_display"]:
                    font = pygame.font.Font(None, 24)
                    text = "Produit : " + item[1] + ", Nutri-Score : " + \
                        item[2]
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                    text = "Magasin : " + item[3] + ", Trace : " + item[4] + \
                        ", Allergène : " + item[5]
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                    text = "URL : " + item[6]
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                y += 5

            if "text_corp" in data:
                for text in data["text_corp"]:
                    font = pygame.font.Font(None, 24)
                    text = font.render(text, 1, (255, 255, 255))
                    self.screen.blit(text, (0, 5 + y))
                    y += 20
                y += 5

            for event in pygame.event.get():
                # For event type KEYDOWN
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_1) or \
                            (event.key == pygame.K_KP1):
                        self.keydown.append("1")
                    elif (event.key == pygame.K_2) or \
                            (event.key == pygame.K_KP2):
                        self.keydown.append("2")
                    elif (event.key == pygame.K_3) or \
                            (event.key == pygame.K_KP3):
                        self.keydown.append("3")
                    elif (event.key == pygame.K_4) or \
                            (event.key == pygame.K_KP4):
                        self.keydown.append("4")
                    elif (event.key == pygame.K_5) or \
                            (event.key == pygame.K_KP5):
                        self.keydown.append("5")
                    elif (event.key == pygame.K_6) or \
                            (event.key == pygame.K_KP6):
                        self.keydown.append("6")
                    elif (event.key == pygame.K_7) or \
                            (event.key == pygame.K_KP7):
                        self.keydown.append("7")
                    elif (event.key == pygame.K_8) or \
                            (event.key == pygame.K_KP8):
                        self.keydown.append("8")
                    elif (event.key == pygame.K_9) or \
                            (event.key == pygame.K_KP9):
                        self.keydown.append("9")
                    elif (event.key == pygame.K_0) or \
                            (event.key == pygame.K_KP0):
                        self.keydown.append("0")
                    elif event.key == pygame.K_a:
                        self.keydown.append(constant.CHOICE_A)
                    elif event.key == pygame.K_z:
                        self.keydown.append(constant.CHOICE_Z)
                    elif event.key == pygame.K_s:
                        self.keydown.append(constant.CHOICE_S)
                    elif event.key == pygame.K_BACKSPACE:
                        del self.keydown[-1]
                    elif event.key == pygame.K_RETURN:
                        choice = "".join(self.keydown)
                        self.keydown = []
                        return choice

            # Display keydown
            text = "Saisie : " + "".join(self.keydown)
            font = pygame.font.Font(None, 24)
            text = font.render(text, 1, (255, 255, 255))
            self.screen.blit(text, (0, 5 + y))
            y += 20

            # Update the screen
            pygame.display.update()
            # Resize the screen
            self.size[1] = y
            pygame.display.set_mode(self.size)
            pygame.display.set_caption('Pur Beurre')

        else:

            if "text_header" in data:
                for text in data["text_header"]:
                    print(text)

            if "text_item_selec" in data:
                for text in data["text_item_selec"]:
                    print(text)

            if "list_item_category" in data:
                for item in data["list_item_category"]:
                    print(str(item[0]) + " : " + item[1])

            if "list_item_products" in data:
                for item in data["list_item_products"]:
                    print(str(item[0]) + " : " + item[1] +
                          ", Nutri-Score : " + item[3])

            if "list_item_substitut" in data:
                for item in data["list_item_substitut"]:
                    print(str(item[0]) + " : " + item[2] +
                          ", nombre de substitut : " + str(item[3]))

            if "list_item_products_for_substitut" in data:
                for item in data["list_item_products_for_substitut"]:
                    print(str(item[0]) + " : " + item[1] +
                          ", Nutri-Score : " + item[3])
                    print("Magasin : " + item[4] + ", Trace : " +
                          item[5] + ", Allergène : " + item[6])
                    print("URL : " + item[7])

            if "list_item_substitut_display" in data:
                for item in data["list_item_substitut_display"]:
                    print("Produit : " + item[1] +
                          ", Nutri-Score : " + item[2])
                    print("Magasin : " + item[3] + ", Trace : " +
                          item[4] + ", Allergène : " + item[5])
                    print("URL : " + item[6])

            if "text_corp" in data:
                for text in data["text_corp"]:
                    print(text)

            if "choise_text" in data:
                print(data["choise_text"])
                choice = input()
                return choice
