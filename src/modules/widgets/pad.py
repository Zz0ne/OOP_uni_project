import tkinter

from .buttons import PlayButton, LoadSampleButton
from .sampleLoader import SampleLoader


class Pad:
    def __init__(self, window, row, column, keyBind, feedBackColor):
        self.__row = row
        self.__column = column
        self.__window = window
        self.__pad = tkinter.Frame(window)
        self.__sampleLoader = SampleLoader()
        self.__keyBind = keyBind
        self.__feedBackColor = feedBackColor

    def __loadWidgets(self):
        self.__playButton = PlayButton(
            self.__window,
            self.__pad,
            0,
            0,
            self.__playAudio,
            self.__keyBind,
            self.__feedBackColor,
        )
        self.__setSampleButton = LoadSampleButton(
            self.__pad, 120, 1, self.__loadAudioFile
        )

    def __gridWidgets(self):
        self.__playButton.place()
        self.__setSampleButton.place()

    def __loadAudioFile(self):
        self.__sampleLoader.run()

    def __playAudio(self):
        if self.__sampleLoader.ready:
            self.__sampleLoader.play()
        else:
            print("No sample loaded")

    def place(self):
        self.__loadWidgets()
        self.__gridWidgets()
        self.__pad.grid(row=self.__row, column=self.__column)
