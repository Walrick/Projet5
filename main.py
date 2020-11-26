#!/usr/bin/python3
# -*- coding: utf8 -*-


import resource.controller


class Main:

    def __init__(self):
        self.controller = resource.controller.Controller()

    def launch(self):
        self.controller.control()


if __name__ == '__main__':
    main = Main()
    main.launch()
