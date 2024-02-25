import tkinter
from tkinter import messagebox
from .pad import Pad
import os


def getListOfDefaultSamplePaths():
    """Retorna a lista de samples presentes no diretório '../samples/default'"""

    defaultFolderPath = "../samples/default"
    return [
        os.path.join(defaultFolderPath, path) for path in os.listdir(defaultFolderPath)
    ]


class PadBoard:
    """Classe composta por varias instâncias da classe 'Pad'"""

    def __init__(self, window, rowSize, columnSize, row, column):
        self.__window = window
        self.__rowSize = rowSize
        self.__columnSize = columnSize
        self.__row = row
        self.__column = column
        self.__pad = tkinter.Frame(window)
        self.__widgets = []
        self.__keyBindings = [
            ["<Key-1>", "<Key-2>", "<Key-3>", "<Key-4>"],
            ["<Key-q>", "<Key-w>", "<Key-e>", "<Key-r>"],
            ["<Key-a>", "<Key-s>", "<Key-d>", "<Key-f>"],
            ["<Key-z>", "<Key-x>", "<Key-c>", "<Key-v>"],
        ]
        self.__feedbackColors = [
            ["red", "green", "blue", "yellow"],
            ["orange", "purple", "brown", "pink"],
            ["cyan", "magenta", "lime", "maroon"],
            ["navy", "olive", "teal", "white"],
        ]
        self.__defaultSamples = getListOfDefaultSamplePaths()
        # Verifica se existem samples suficientes para a quantidade de pads
        if len(self.__defaultSamples) != rowSize * columnSize:
            self.__onClosing()

    def __loadWidgets(self):
        """Cria as instâncias dos Pad's especificando as keybinds e as cores de feedback"""

        for i in range(self.__rowSize):
            for j in range(self.__columnSize):
                self.__widgets.append(
                    Pad(
                        self.__window,
                        i,
                        j,
                        self.__keyBindings[i][j],
                        self.__feedbackColors[i][j],
                    )
                )

    def __placeWidgets(self):
        """Posiciona os widgets na janela"""

        for widget in self.__widgets:
            widget.place()

    def __onClosing(self):
        """Mostra uma mensagem de erro quando não ecistem samples suficientes para od pads"""
        if messagebox.showerror("Error", "Not enought default samples."):
            quit()

    def place(self):
        """Posiciona os widgets na janela"""

        self.__loadWidgets()
        self.__placeWidgets()
        self.__pad.grid(row=self.__row, column=self.__column)
