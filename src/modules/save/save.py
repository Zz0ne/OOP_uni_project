import json
import os

saveFilePath = "../../../saves/saves.json"
sampleBasePath = "../../../samples/"

def getJsonFile(path:str):
    saveFile = open(path, "r", encoding="utf-8")
    return json.load(saveFile)

def saveJsonFile(path:str, jsonFile: dict):
    jsonStr = json.dumps(jsonFile, ensure_ascii=False, indent=4)
    with open(path, "w", encoding="utf-8") as outFile:
        outFile.write(jsonStr)

class Save:
    @staticmethod
    def save(keyBind: str, sample: str):
        jsonFile = getJsonFile(saveFilePath)
        jsonFile["userSave"][keyBind] = sample
        saveJsonFile(saveFilePath, jsonFile)

    @staticmethod
    def load(keyBind: str):
        saveJson = getJsonFile(saveFilePath)
        sample = sampleBasePath + saveJson["userSave"][keyBind]

        if os.path.exists(sample):
                return sample
        else:
            return  sampleBasePath + "default" + saveJson["default"][keyBind]
