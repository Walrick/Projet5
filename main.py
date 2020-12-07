#!/usr/bin/python3
# -*- coding: utf8 -*-

import os
import sys

import resource.controller


class Main:

    def __init__(self):
        # open file .env for database connection
        file = open(".env.txt", "r")
        lines = file.readlines()
        for line in lines:
            lg = line.split(" ")
            os.environ[lg[0]] = lg[2]

        # get the launch options
        arg = sys.argv

        self.controller = resource.controller.Controller(arg)

    def launch(self):
        self.controller.control()


if __name__ == '__main__':
    main = Main()
    main.launch()
