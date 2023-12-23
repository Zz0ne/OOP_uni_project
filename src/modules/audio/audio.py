import os
from pygame import mixer


class Audio:
    def __init__(self, file):
        _, extention = os.path.splitext(file)
        extention = extention[1:]  # Remover "." da extenção

        self._audio = mixer.Sound(file)
        self._name = os.path.basename(file)

    @property
    def name(self):
        return self._name

    def play(self):
        self._audio.play()

    @staticmethod
    def initAudioPlayer(numChannels):
        mixer.init()
        mixer.set_num_channels(numChannels)
