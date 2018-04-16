#!/usr/bin/env python3m

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from subprocess import call

class Player():
    def onButtonClose(self, *args):
        print("Close button pressed")
        Gtk.main_quit(*args)

    def onButtonPlay(self, button):
        call(['mocp', '--play'])

    def onButtonPause(self, button):
        call(['mocp', '--toggle-pause'])

    def onButtonBackward(self, button):
        call(['mocp', '--next'])

    def onButtonForward(self, button):
        call(['mocp', '--previous'])

builder = Gtk.Builder()
builder.add_from_file("gui.glade")
builder.connect_signals(Player())

window = builder.get_object("mainWindow")
window.show_all()

Gtk.main()