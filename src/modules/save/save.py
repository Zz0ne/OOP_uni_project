import json
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
SAVE_FILE_PATH = os.path.join(BASE_DIR, "saves", "saves.json")
SAMPLE_BASE_PATH = os.path.join(BASE_DIR, "samples")


def getJsonFile(path: str):
    saveFile = open(path, "r", encoding="utf-8")
    return json.load(saveFile)


def saveJsonFile(path: str, jsonFile: dict):
    jsonStr = json.dumps(jsonFile, ensure_ascii=False, indent=4)
    with open(path, "w", encoding="utf-8") as outFile:
        outFile.write(jsonStr)


class Save:
    """Classe estática feita para encapsular as funcionalidadesrelacionadas
    relacionadas com gravar e carregar o ultimo estado do programa"""

    @staticmethod
    def save(keyBind: str, sample: str):
        """Grava o sample num ficheiro json"""
        jsonFile = getJsonFile(SAVE_FILE_PATH)
        jsonFile["userSave"][keyBind] = sample
        saveJsonFile(SAVE_FILE_PATH, jsonFile)

    @staticmethod
    def load(keyBind: str):
        saveJson = getJsonFile(SAVE_FILE_PATH)
        sample = SAMPLE_BASE_PATH + "/" + saveJson["userSave"][keyBind]

        if os.path.isfile(sample):
            return sample
        else:
            return SAMPLE_BASE_PATH + "/default/" + saveJson["default"][keyBind]
