from tkinter import Button
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
BTN_IMG_PATH = os.path.join(BASE_DIR, "assets", "generic_btn.png")


class GenericButton:
    """Botão generico, base dos botões usados neste programa"""

    def __init__(self, window, text: str, row: int, column: int, callback):
        self.__row = row
        self.__column = column
        self._callback = callback
        self._button = Button(window, text=text, command=callback)
        self.__setStyle()

    def __setStyle(self):
        self._button.configure(
            borderwidth=1,
        )

    def place(self):
        """Posiciona botão"""
        self._button.grid(row=self.__row, column=self.__column)


class PlayButton(GenericButton):
    """Botão responsável por reproduzir o audio"""

    def __init__(
        self, window, frame, keybind, row, column, callback, bindKey, feedbackColor
    ):
        super().__init__(frame, keybind, row, column, callback=callback)
        self.__setStyle()
        self.__feedbackColor = feedbackColor
        window.bind(f"{bindKey}", self.__onKeyPress)

    def __setStyle(self):
        """(Polimorfismo) Modificar estilo genérico"""

        self._button.config(
            height=8, width=16, background="grey", activebackground="grey"
        )

    def __pressAnimation(self):
        """Animação reproduzida quando o utilizador usa o teclado"""

        originalColor = self._button.cget("background")
        self._button.config(background=self.__feedbackColor)
        self._button.after(100, lambda: self._button.config(background=originalColor))

    def __onKeyPress(self, event):
        """Método executado quando o utilizador usa o teclado"""

        if event:
            self._callback()
            self.__pressAnimation()


class LoadSampleButton(GenericButton):
    """Botão responsável por abrir o sample loader"""

    def __init__(self, frame, x, y, callback):
        self._x = x
        self._y = y

        super().__init__(frame, "+", 0, 0, callback=callback)
        self.__setStyle()

    def __setStyle(self):
        self._button.configure(
            borderwidth=0,
            background="grey",
        )

    def place(self):
        """(Polimorfismo) Método para posicionar o botão"""

        self._button.place(x=self._x, y=self._y)
