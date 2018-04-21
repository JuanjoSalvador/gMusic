from gi.repository import GLib, Gtk
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from lib.window import ApplicationWindow

class Session_DBus(dbus.service.Object):
    """
    DBus server for gMusic
    """
    def __init__(self):
        bus_name = dbus.service.BusName('com.jotadevs.gmusic', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/com/jotadevs/gmusic')

    @dbus.service.method('com.jotadevs.gmusic.SendInfo')
    def send_info(self, song, artist):
        """
        Sends metadata from DBus Client to Server.
        :param song: name of the playing song
        :param artist: name of the playing artist
        """

        GLib.idle_add(ApplicationWindow.update_metadata, song, artist)

    def run_dbus_server():
        """
        Starts the DBus server
        """
        DBusGMainLoop(set_as_default=True)
        dbus_service = Session_DBus()
        GLib.MainLoop().run()