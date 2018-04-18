#!/usr/bin/env python3

import gi
import _thread
from subprocess import call
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from dbus.mainloop.glib import DBusGMainLoop

from lib.player import Player
from lib.session_dbus import Session_DBus

class Gmusic():

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("gui.glade")
        builder.connect_signals(Player())

        switch_status = builder.get_object('switch_status')
        if Player.is_server_active(self):
            switch_status.set_active(True)

        song_label = builder.get_object('song')
        artist_label = builder.get_object('artist')

        window = builder.get_object("mainWindow")
        window.show_all()
        try:
            _thread.start_new_thread(Gtk.main())
        except Exception as ex:
            print(ex)

Gmusic()