#!/usr/bin/python3

import gi, threading
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from lib.session_dbus import Session_DBus
from lib.window import ApplicationWindow

"""
Main window for gMusic
"""
app = ApplicationWindow()

# Running DBus server on another thread
thread = threading.Thread(target=Session_DBus.run_dbus_server)
thread.daemon = True
thread.start()

# Main loop
Gtk.main()