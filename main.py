#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from lib.player import Player

Player().initializer()

builder = Gtk.Builder()
builder.add_from_file("gui.glade")
builder.connect_signals(Player())

window = builder.get_object("mainWindow")
window.show_all()

Gtk.main()