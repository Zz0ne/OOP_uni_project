import tkinter


class GenericButton:
    def __init__(self, window, text, row, column, callback):
        self.__row = row
        self.__column = column
        self._callback = callback
        self._button = tkinter.Button(window, text=text, command=callback)

    def __setStyle(self):
        pass

    def place(self):
        self._button.grid(row=self.__row, column=self.__column)


class PlayButton(GenericButton):
    def __init__(self, window, row, column, callback, bindKey):
        super().__init__(window, "", row, column, callback=callback)
        self.__setStyle()
        print(bindKey)
        window.bind(f"<{bindKey}>", self.__onKeyPress)

    def __setStyle(self):
        self._button.config(
            text="", height=8, width=16, background="grey", activebackground="grey"
        )

    def __onKeyPress(self, event):
        if event:
            print(
                f"Key pressed: {event.char}, Key symbol: {event.keysym}, Key code: {event.keycode}"
            )
            self._callback()


class LoadSampleButton(GenericButton):
    def __init__(self, window, x, y, callback):
        self._x = x
        self._y = y

        super().__init__(window, "+", 0, 0, callback=callback)

    def place(self):
        self._button.place(x=self._x, y=self._y)
