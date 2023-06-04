import rumps
import subprocess

class Screen_time(rumps.App):
    def __init__(self):
        super(Screen_time, self).__init__("Screen Time")
        self.menu = ["Usage","Quit"]
        self._quit_button =None

    @rumps.clicked("Usage")
    def prefs(self,_):
        subprocess.run("screencapture -ci ~/Desktop/screenshot.jpg",shell=True)
        subprocess.run("/usr/bin/python3 /Users/paritosh/Desktop/CS/Screen-usage-widget-main/1.py",shell=True)

    @rumps.clicked('Quit')
    def quit_Screen_time(self,_):
        rumps.quit_application()

Screen_time().run()
