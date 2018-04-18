#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject
from lib.player import Player

class ApplicationWindow(Gtk.Window):

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gui.glade")
        self.builder.connect_signals(Player())

        self.song_label = self.builder.get_object('song')

        _switch_status = self.builder.get_object('switch_status')
        if Player().is_server_active():
            _switch_status.set_active(True)

        window = self.builder.get_object("mainWindow")
        window.show_all()