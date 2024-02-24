import os
import shutil

from tkinter import filedialog, messagebox, Frame, Label, Toplevel

from .buttons import GenericButton
from .sampleList import SampleList
from modules.audio.audio import Audio


class SampleLoader:
    """ Classe que representa o sample loader que permite ao utilizador adicionar e carregar novos samples """

    def __init__(self, window, callback):
        self.__window = window
        self.__sampleDirectory = "../samples/"
        self.__setSampleCallback = callback 

    def __loadWidgets(self):
        """ Cria instancias dos widgets necessários """

        self.__lable = Label(self.__loadSampleWindow, text="Samples:")
        self.__addSampleButton = GenericButton(
            self.__loadSampleWindow,
            text="Add",
            row=2,
            column=2,
            callback=self.__addSample,
        )
        self.__confirmCancelFrame = Frame(self.__loadSampleWindow)
        self.__confirmButton = GenericButton(
            self.__confirmCancelFrame,
            text="Confirm",
            row=0,
            column=0,
            callback=self.__onConfirm,
        )
        self.__cancelButton = GenericButton(
            self.__confirmCancelFrame,
            text="Cancel",
            row=0,
            column=1,
            callback=self.__onCancel,
        )
        self.__sampleList = SampleList(self.__loadSampleWindow)

    def __placeWidgets(self):
        """ Posiciona widgets na janela """

        self.__lable.grid(row=1, column=1)
        self.__sampleList.place()
        self.__confirmCancelFrame.grid(row=3, column=1)
        self.__addSampleButton.place()
        self.__confirmButton.place()
        self.__cancelButton.place()

    def __onConfirm(self):
        """ Método executado ao pressionar o botão 'Confirm' """

        sampleName = self.__sampleList.selectedSample
        if (len(sampleName) == 0):
            messagebox.showerror("Error", "Please select a sample.")
            return
        self.__setSampleCallback(Audio(sampleName))
        self.__loadSampleWindow.destroy()

    def __onCancel(self):
        """ Método executado ao pressionar o botão 'Cancel' """

        self.__loadSampleWindow.destroy()

    def __addSample(self):
        """ Método executado ao pressionar o botão 'Add' """

        audioFilePath = filedialog.askopenfilename()
        if audioFilePath:
            filename = os.path.basename(audioFilePath)
            destinationPath = os.path.join(self.__sampleDirectory, filename)
            try:
                shutil.copy(audioFilePath, destinationPath)
                self.__sampleList += destinationPath
            except Exception as e:
                print("Error copying file:", e)

    def run(self):
        """ Cria uma nova janela, bloqueia a janela principal,
        centra a nova janela em relação à janela principal,
        cria e posiciona os widgets """

        self.__loadSampleWindow = Toplevel()
        self.__loadSampleWindow.title("SampleLoader")
        self.__loadSampleWindow.resizable(False, False)
        self.__loadSampleWindow.attributes("-topmost", True)
        self.__loadSampleWindow.grab_set()
        x = self.__window.winfo_x()
        y = self.__window.winfo_y()
        self.__loadSampleWindow.geometry("+%d+%d" % (x + 100, y + 100))
        self.__loadWidgets()
        self.__placeWidgets()
