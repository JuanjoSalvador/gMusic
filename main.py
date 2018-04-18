#!/usr/bin/env python3

import gi, threading
from subprocess import call
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject
from lib.player import Player
from lib.session_dbus import Session_DBus

def gmusic_main():
    builder = Gtk.Builder()
    builder.add_from_file("gui.glade")
    builder.connect_signals(Player())

    switch_status = builder.get_object('switch_status')
    if Player().is_server_active():
        switch_status.set_active(True)

    song_label = builder.get_object('song')
    artist_label = builder.get_object('artist')

    window = builder.get_object("mainWindow")
    window.show_all()

    thread = threading.Thread(target=Session_DBus.run_dbus_server)
    thread.daemon = True
    thread.start()

gmusic_main()
Gtk.main()