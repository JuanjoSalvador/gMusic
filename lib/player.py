from subprocess import call

class Player():

    def __init__(self):
        pass

    def closeWindow(self, *args):
        print("Close button pressed")
        Gtk.main_quit(*args)

    def play():
        print("Close button pressed")
        call(['mocp', '--play'])

    def pause():
        call(['mocp', '--pause'])

    def unpause():
        call(['mocp', '--unpause'])