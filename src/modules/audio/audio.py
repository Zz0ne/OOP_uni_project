import os
from pygame import mixer


class Audio:
    """ Classe composta pelo audio, e nome do ficheiro """
    def __init__(self, file):
        self._audio = mixer.Sound(file)
        self._name = os.path.basename(file)

    @property
    def name(self):
        """ Getter do nome do ficheiro """
        return self._name

    def play(self):
        """ Reproduz o audio """
        self._audio.play()

    @staticmethod
    def initAudioPlayer(numChannels):
        """ A ser usado uma vez para iniciar o mixer """
        mixer.init()
        mixer.set_num_channels(numChannels)
