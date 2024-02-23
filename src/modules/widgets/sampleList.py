import tkinter
import os

class SampleList:
    """ Lista que permite selecionar um sample contido no diretório '../samples/' """
    def __init__(self, window):
        self.__SAMPLE_DIR = "../samples/"
        self.__widget = tkinter.Listbox(window, height=5, width=52)
        self.__widget.bind("<<ListboxSelect>>", self.__setSample)
        self.__selectedSample = ""
 
    @property
    def selectedSample(self):
        """ Getter para recolher o sample selecionado """
        return self.__selectedSample

    def __iadd__(self, sample):
        """ Subrecarga do operador += para adicionar samples novos á lista,
            é feito desta forma por questões de avaliação """

        self.__widget.insert(tkinter.END, sample)

    def __loadSamples(self):
        """ Carrega samples no diretório '../samples/' """
        try:
            for filename in os.listdir(self.__SAMPLE_DIR):
                filePath = os.path.join(self.__SAMPLE_DIR, filename)
                if os.path.isfile(filePath):
                    self.__widget.insert(tkinter.END, filePath)
        except FileNotFoundError:
            print("Directory not found:", self.__SAMPLE_DIR)

    def __setSample(self, event):
        """ Método usado como callback pelo widget 'Listbox' para selecionar um sample """
        widget = event.widget
        selection = widget.curselection()
        if selection:
            index = selection[0]
            sampleName = widget.get(index)
            self.__selectedSample = sampleName

    def place(self):
        """ Posiciona os widgets na janela """

        self.__loadSamples()
        self.__widget.grid(row=2, column=1)

