import os
import tkinter
import shutil
from tkinter import filedialog

from .buttons import GenericButton
from modules.audio.audio import Audio


class SampleLoader:
    def __init__(self):
        self.__sampleDirectory = "../samples/"
        self.__sampleSelected = False

    def __loadWidgets(self):
        self.__lable = tkinter.Label(self.__loadSampleWindow, text="Samples:")
        self.__addSampleButton = GenericButton(
            self.__loadSampleWindow,
            text="Add",
            row=2,
            column=2,
            callback=self.__addSample,
        )
        self.__confirmButton = GenericButton(
            self.__loadSampleWindow,
            text="Confirm",
            row=3,
            column=1,
            callback=self.__closeWindow,
        )
        self.__sampleList = tkinter.Listbox(self.__loadSampleWindow, height=5, width=52)
        self.__sampleList.bind("<<ListboxSelect>>", self.__setSample)

    def __placeWidgets(self):
        self.__lable.grid(row=1, column=1)
        self.__sampleList.grid(row=2, column=1)
        self.__addSampleButton.place()
        self.__confirmButton.place()

    def __closeWindow(self):
        self.__loadSampleWindow.destroy()

    def __loadSamples(self):
        try:
            for filename in os.listdir(self.__sampleDirectory):
                filePath = os.path.join(self.__sampleDirectory, filename)
                if os.path.isfile(filePath):
                    self.__sampleList.insert(tkinter.END, filePath)
        except FileNotFoundError:
            print("Directory not found:", self.__sampleDirectory)

    def __setSample(self, event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            index = selection[0]
            sampleName = widget.get(index)
            self.__sample = Audio(sampleName)
            self.__sampleSelected = True

    def __addSample(self):
        audioFilePath = filedialog.askopenfilename()
        if audioFilePath:
            filename = os.path.basename(audioFilePath)
            destinationPath = os.path.join(self.__sampleDirectory, filename)
            try:
                shutil.copy(audioFilePath, destinationPath)
                self.__sampleList.insert(tkinter.END, destinationPath)
            except Exception as e:
                print("Error copying file:", e)

    def run(self):
        self.__loadSampleWindow = tkinter.Tk()
        self.__loadSampleWindow.title("SampleLoader")
        self.__loadSampleWindow.attributes("-topmost", True)
        self.__loadWidgets()
        self.__placeWidgets()
        self.__loadSamples()

    def play(self):
        return self.__sample.play()

    @property
    def ready(self):
        return self.__sampleSelected
