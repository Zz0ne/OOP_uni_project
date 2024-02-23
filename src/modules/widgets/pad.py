import tkinter

from .buttons import PlayButton, LoadSampleButton
from .sampleLoader import SampleLoader


class Pad:
    """ Classe composta pelo 'PlayButton' e 'LoadSampleButton' """

    def __init__(self, window, row, column, keyBind, feedBackColor, defaultSample):
        self.__row = row
        self.__column = column
        self.__window = window
        self.__pad = tkinter.Frame(window)
        self.__sampleLoader = SampleLoader(window, self.__setSample)
        self.__keyBind = keyBind
        self.__feedBackColor = feedBackColor
        self.__sample = defaultSample

    def __loadWidgets(self):
        """ Cria instancias do 'PlayButton' e do ' LoadSampleButton' """

        self.__playButton = PlayButton(
            self.__window,
            self.__pad,
            self.__keyBind[5],
            0,
            0,
            self.__playAudio,
            self.__keyBind,
            self.__feedBackColor,
        )
        self.__loadSampleButton = LoadSampleButton(
            self.__pad, 120, 1, self.__loadAudioFile
        )

    def __placeWidgets(self):
        """ Posiciona widgets na janela """

        self.__playButton.place()
        self.__loadSampleButton.place()

    def __loadAudioFile(self):
        """ Abre o 'SampleLoader' """

        self.__sampleLoader.run()

    def __playAudio(self):
        """ Reproduz sample """

        self.__sample.play()

    def __setSample(self, sample):
        """ Método usado como callback pelo 'SampleLoader' para estrair o sample selecionado """

        self.__sample = sample

    def place(self):
        """ Posiciona os widgets na janela """

        self.__loadWidgets()
        self.__placeWidgets()
        self.__pad.grid(row=self.__row, column=self.__column)
