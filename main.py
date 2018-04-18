#!/usr/bin/env python3

import gi
import atexit
from subprocess import call
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from lib.player import Player

class Gmusic():

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("gui.glade")
        builder.connect_signals(Player())

        switch_status = builder.get_object('switch_status')
        if Player.is_server_active(self):
            switch_status.set_active(True)

        window = builder.get_object("mainWindow")
        window.show_all()

        Gtk.main()

Gmusic()