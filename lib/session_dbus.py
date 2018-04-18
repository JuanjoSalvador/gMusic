from gi.repository import GLib, Gtk
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from lib.window import ApplicationWindow

class Session_DBus(dbus.service.Object):

    def __init__(self):
        bus_name = dbus.service.BusName('com.jotadevs.gmusic', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/com/jotadevs/gmusic')

    # Interface and Method
    @dbus.service.method('com.jotadevs.gmusic.SendInfo')
    def send_info(self, song, artist):
        ApplicationWindow.set_song_label(ApplicationWindow, value=song)

    def run_dbus_server():
        DBusGMainLoop(set_as_default=True)
        dbus_service = Session_DBus()
        GLib.MainLoop().run()