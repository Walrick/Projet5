#!/usr/bin/python3
# -*- coding: utf8 -*-


import resource.controller
import os


class Main:

    def __init__(self):
        # open file .env for database connection
        file = open(".env.txt", "r")
        lines = file.readlines()
        for line in lines:
            lg = line.split(" ")
            os.environ[lg[0]] = lg[2]

        self.controller = resource.controller.Controller()

    def launch(self):
        self.controller.control()


if __name__ == '__main__':
    main = Main()
    main.launch()
