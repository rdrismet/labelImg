import json
import os


class ConfigManager:
    def __init__(self, filename=None):
        self.configFilePath = os.path.join(str(os.getcwd()).split("libs")[0], "data", "config.json")
        with open(self.configFilePath) as file:
            self.data = json.load(file)
        self.bannedKeyboardShortcutsList = []
        self.modifiableKeyboardShortcutsList = []

        for keyboarShortcut in self.data["shortcuts"]:
            if keyboarShortcut["isModifiable"]:
                self.modifiableKeyboardShortcutsList.append(keyboarShortcut)
            else:
                self.bannedKeyboardShortcutsList.append(keyboarShortcut)

    def getConfigData(self):
        with open(self.configFilePath) as file:
            data = json.load(file)
        return data

    def getKeyboardShortcutsList(self):
        configData = self.getConfigData()
        return configData["shortcuts"]

    def getBannedKeyboardShortcutsList(self):
        return self.bannedKeyboardShortcutsList

    def getModifiableKeyboardShortcutsList(self):
        return self.modifiableKeyboardShortcutsList

    def setKeyboardShortcut(self, pName, pValue):
        i = 0
        for shortcut in self.data["shortcuts"]:
            if shortcut["name"] == pName:
                self.data["shortcuts"][i]["value"] = pValue
                a_file = open(self.configFilePath, "w", encoding='utf-8')
                json.dump(self.data, a_file, ensure_ascii=False, indent=4)
                a_file.close()
            i = i+1

    def getShortcutsProperties(self, pName):
        shortcutList = self.getKeyboardShortcutsList()
        for properties in shortcutList:
            if properties["name"] == pName:
                return properties
        return "There is no such name" #or 0

    def getPredefinedClasses(self):
        configData = self.getConfigData()
        return configData["predefinedClasses"]

    def getQuitShortcut(self):
        return self.data["shortcuts"][0]["value"]

    def getSaveShortcut(self):
        return self.data["shortcuts"][1]["value"]

    def getDeleteImageShortcut(self):
        return self.data["shortcuts"][2]["value"]

    def getDeleteBoxShortcut(self):
        return self.data["shortcuts"][3]["value"]

    def getCreateBoxShortcut(self):
        return self.data["shortcuts"][4]["value"]

    def getNextImageShortcut(self):
        return self.data["shortcuts"][5]["value"]

    def getPreviousImageShortcut(self):
        return self.data["shortcuts"][6]["value"]

    def getZoomInShortcut(self):
        return self.data["shortcuts"][7]["value"]

    def getZoomOutShortcut(self):
        return self.data["shortcuts"][8]["value"]

    def getOpenFileShortcut(self):
        return self.data["shortcuts"][9]["value"]

    def getVerifyImageShortcut(self):
        return self.data["shortcuts"][10]["value"]

    def getDuplicateBoxShortcut(self):
        return self.data["shortcuts"][11]["value"]

def main():
    cm = ConfigManager()


if __name__ == '__main__':
    main()
