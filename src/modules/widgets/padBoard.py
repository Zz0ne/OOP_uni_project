import tkinter
from .pad import Pad


class PadBoard:
    def __init__(self, window, rowSize, columnSize, row, column):
        self.__window = window
        self.__rowSize = rowSize
        self.__columnSize = columnSize
        self.__row = row
        self.__column = column
        self.__pad = tkinter.Frame(window)
        self.__widgets = []
        self.__keyBindings = [
            "1",
            "q",
            "a",
            "z",
            "2",
            "w",
            "s",
            "x",
            "3",
            "e",
            "d",
            "c",
            "4",
            "r",
            "f",
            "v",
        ]

    def __loadWidgets(self):
        keybindingsIndex = 0
        for i in range(self.__rowSize):
            for j in range(self.__columnSize):
                self.__widgets.append(
                    Pad(self.__window, i, j, self.__keyBindings[keybindingsIndex])
                )
                keybindingsIndex += 1

    def __placeWidgets(self):
        for widget in self.__widgets:
            widget.place()

    def place(self):
        self.__loadWidgets()
        self.__placeWidgets()
        self.__pad.grid(row=self.__row, column=self.__column)
