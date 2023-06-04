import rumps
import subprocess

class Utility(rumps.App):
    def __init__(self):
        super(Utility, self).__init__("--_--")
        self.menu = ["Text Extraction","Quit"]
        self._quit_button =None

    @rumps.clicked("Text Extraction")
    def prefs(self,_):
        subprocess.run("screencapture -ci ~/Desktop/screenshot.jpg",shell=True)
        subprocess.run("/usr/bin/python3 /Users/paritosh/Documents/GitHub/Text-Extractor-for-mac-os/module1.py",shell=True)

    @rumps.clicked('Quit')
    def quit_Utility(self,_):
        rumps.quit_application()

Utility().run()
