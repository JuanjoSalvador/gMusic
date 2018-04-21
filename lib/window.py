import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject
from lib.player import Player

class ApplicationWindow(Gtk.Window):
    """
    ApplicationWindow is the main window instance
    """

    builder = Gtk.Builder()

    def __init__(self):
        app_builder = ApplicationWindow.builder
        app_builder.add_from_file("gui.glade")

        app_builder.connect_signals(Player())

        _switch_status = app_builder.get_object('switch_status')
        if Player().is_server_active():
            _switch_status.set_active(True)

        window = app_builder.get_object("mainWindow")
        window.show_all()

    def update_metadata(song=None, artist=None, img=None):
        """
        Updates artist and song labels on UI
        """
        ApplicationWindow.builder.get_object('song').set_text(song)
        ApplicationWindow.builder.get_object('artist').set_text(artist)