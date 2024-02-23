import tkinter
from tkinter import messagebox

from modules.widgets.padBoard import PadBoard
from modules.audio.audio import Audio


class App:
    """ Classe principal, a raiz do programa. """

    def __init__(self):
        self.__gui = tkinter.Tk()
        self.__gui.title("SimpleSampler")
        self.__gui.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.__gui.resizable(False, False)
        self.__padGridSize = {"x": 4, "y": 4}
        self.__widgets = []

        # iniciar as funcionalidade de reproduzir audio
        numChannles = self.__padGridSize["x"] * self.__padGridSize["y"]
        Audio.initAudioPlayer(numChannles)

    def __onClosing(self):
        """ Callback que executa quando o utilizador pressiona o 'x' na janela principal """

        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            quit()

    def __loadWidgets(self):
        """ Cria instancia do 'PadBoard' """

        self.__widgets.append(
            PadBoard(self.__gui, self.__padGridSize["x"], self.__padGridSize["y"], 0, 0)
        )

    def __placeWidgets(self):
        """ Posiciona widgets na janela """

        for widget in self.__widgets:
            widget.place()

    def run(self):
        """ Cria e posiciona os widgets na janela e corre a aplicação """

        self.__loadWidgets()
        self.__placeWidgets()
        self.__gui.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
