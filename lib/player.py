from subprocess import call
from gi.repository import Gtk

class Player():
    def initializer(self):
        call(['mocp', '-S'])

    def onButtonClose(self, *args):
        call(['mocp', '-x'])
        Gtk.main_quit(*args)

    def onButtonPlay(self, button):
        call(['mocp', '--play'])

    def onButtonPause(self, button):
        call(['mocp', '--toggle-pause'])

    def onButtonBackward(self, button):
        call(['mocp', '--previous'])

    def onButtonForward(self, button):
        call(['mocp', '--next'])