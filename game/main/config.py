# Class to create, check, load and save the differents configurations

from sys import exit
import json

from game.util.logger import Logger


class Config:
    # Set the different paths of configuration files
    DATA_FOLDER = "data"
    MAIN_CONFIG_PATH = "data/config/config.json"
    KEYBOARD_CONFIG_PATH = "data/config/inputs.json"

    ratio = 0
    server = []
    inputs = {}
    values = {}

    @staticmethod
    def check():

        import os

        # Check if the "data" folder exists (and create it if necessary)
        path = Config.DATA_FOLDER
        if not (os.path.exists(path)) and not (os.path.isdir(path)):
            Logger.info("Config", "Creating '%s' folder..." % path)
            try:
                os.mkdir(path)
                Logger.success("Config", "Done !")
            except OSError:
                Logger.error("Config", "Creation of the directory %s failed" % path)
                exit()

        # Check if the "data/config" folder exists (and create it if necessary)
        path = Config.DATA_FOLDER + "/config"
        if not (os.path.exists(path)) and not (os.path.isdir(path)):
            Logger.info("Config", "Creating '%s' folder..." % path)
            try:
                os.mkdir(path)
                Logger.success("Config", "Done !")
            except OSError:
                Logger.error("Config", "Creation of the directory %s failed" % path)
                exit()

        # Check if the main configuration file exists (and create it if necessary)
        path = Config.MAIN_CONFIG_PATH
        if not (os.path.exists(path)):
            Logger.info("Config", "Creating the user-specific configuration file...")
            Config.createDefaultConfig()

        # Check if the keyboard configuration file exists (and create it if necessary)
        path = Config.KEYBOARD_CONFIG_PATH
        if not (os.path.exists(path)):
            Logger.info("Config", "Creating the user-specific key configuration file...")
            Config.createDefaultInputs()

    @staticmethod
    def load():
        Config.check()
        Config.loadConfig()
        Config.loadInputs()
        Config.ratio = Config.values["window"]["width"] / Config.values["window"]["height"]

    @staticmethod
    def createDefaultConfig(overwrite=True):

        # We retrieve the user's screen resolution using the GLFW library
        width = 576
        height = 384
        import glfw
        glfw.init()
        vm = glfw.get_video_modes(glfw.get_primary_monitor())
        nvm = len(vm) - 1
        monitorRes = [vm[nvm][0][0], vm[nvm][0][1]]

        # We choose the highest resolution that can support the screen
        baseRes = [576, 384]  # The minimum game display resolution (18 tiles * 32 pixels and 12 tiles * 32 pixels)
        for factor in range(1, 10):  # Test differents zoom factors to find the maximum that can be used
            if (baseRes[0] * factor < monitorRes[0] and baseRes[1] * factor < monitorRes[1]):
                width = baseRes[0] * factor
                height = baseRes[1] * factor

        # We retrieve the user's locale
        import locale
        userLanguage = locale.getdefaultlocale()[0][:2]
        languages = [['en', 'English'], ['fr', 'Français']]
        language = "en"
        # We choose the locale if present in the game, otherwise, we take the default one (English)
        for lang in languages:
            if lang[0] == userLanguage: language = lang[0]

        # We set the values for the configuration
        Config.values = {
            "general": {
                "language": language,
                "debug": False
            },
            "window": {
                "limFrameRate": 0,
                "fullScreen": 0,
                "width": width,
                "height": height
            },
            "audio": {
                "musicVolume": 0.5,
                "soundsVolume": 0.5
            }
        }

        # We overwrite the configuration if needed
        if overwrite: Config.saveConfig()

    @staticmethod
    def createDefaultInputs(overwrite=True):

        # We set default values for the keyboard configuration
        Config.inputs = {
            "ECHAP": [[0, 256]]
        }

        # We overwrite the keyboard configuration if needed
        if overwrite: Config.saveInputs()

    # Method to save the configuration into a file
    @staticmethod
    def saveConfig():

        ConfigToSave = {
            "config": Config.values
        }

        with open(Config.MAIN_CONFIG_PATH, 'w') as outfile:
            json.dump(ConfigToSave, outfile, indent="	")
            Logger.success("Config", "Configuration file saved successfully !")

    # Method to save the keyboard configuration into a file
    @staticmethod
    def saveInputs():

        InputsToSave = {
            "inputs": Config.inputs
        }

        with open(Config.KEYBOARD_CONFIG_PATH, 'w') as outfile:
            json.dump(InputsToSave, outfile, indent="	")
            Logger.success("Config", "Key configuration file saved successfully !")

    @staticmethod
    def loadConfig():

        try:  # Try to load the configuration from file
            configFile = json.load(open(Config.MAIN_CONFIG_PATH))['config']
            Config.values = configFile
        except json.decoder.JSONDecodeError:  # If it fails, ask for overwrite (or it will use a default configuration)
            Config.createDefaultConfig(Config.yes(Logger.format("Config",
                                                                "Failed to parse the config file ! Do you want to recreate it and delete the old one ?")))

    @staticmethod
    def loadInputs():

        try:  # Try to load the keyboard configuration from file
            inputsFile = json.load(open(Config.KEYBOARD_CONFIG_PATH))['inputs']
            Config.inputs = inputsFile
        except json.decoder.JSONDecodeError:  # If it fails, ask for overwrite (or it will use a default keyboard configuration)
            Config.createDefaultInputs(Config.yes(Logger.format("Config",
                                                                "Failed to parse the key config file ! Do you want to recreate it and delete the old one ?")))

    # Simple method that allow to ask questions to the user
    @staticmethod
    def yes(sentence):

        choice = input(sentence + " (Answer \"yes\") : ").lower()

        if choice == "yes":
            return True
        else:
            return False
