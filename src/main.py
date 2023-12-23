import tkinter
from tkinter import messagebox

from modules.widgets.padBoard import PadBoard
from modules.audio.audio import Audio


class App:
    def __init__(self, padBoardSize):
        self.__gui = tkinter.Tk()
        self.__gui.title("SimpleSampler")
        self.__gui.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.__gui.resizable(False, False)
        self.__padGridSize = {"x": padBoardSize[0], "y": padBoardSize[1]}
        self.__widgets = []
        Audio.initAudioPlayer(padBoardSize[0] * padBoardSize[1])

    def __onClosing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            quit()

    def __loadWidgets(self):
        self.__widgets.append(
            PadBoard(self.__gui, self.__padGridSize["x"], self.__padGridSize["y"], 0, 0)
        )

    def __placeWidgets(self):
        for widget in self.__widgets:
            widget.place()

    def run(self):
        self.__loadWidgets()
        self.__placeWidgets()
        self.__gui.mainloop()


if __name__ == "__main__":
    app = App((4, 4))
    app.run()
