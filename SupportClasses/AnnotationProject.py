import json
import os


class AnnotationProject():
    def __init__(self, modelPath: str, trainingSplit: str):
        self.modelPath = modelPath
        self.trainingSplit = trainingSplit

    def serialize(self, rootPath):
        jsonFilePath = os.path.join(rootPath, 'temp', 'AnnotationProject.JSON')
        with open(jsonFilePath, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, ensure_ascii=False, indent=4)
