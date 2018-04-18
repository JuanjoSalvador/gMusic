import _thread
from subprocess import call, run, PIPE
from gi.repository import Gtk, GLib
from lib.session_dbus import Session_DBus

class Player():

    def is_server_active(self):
        return bool(run(['pidof', 'mocp'], stdout=PIPE).stdout)

    def on_button_close(self, *args):
        if self.is_server_active():
            call(['mocp', '-x'])

        GLib.MainLoop().quit()
        Gtk.main_quit(*args)

    # BUTTONS

    def on_button_play(self, button):
        call(['mocp', '--play'])

    def on_button_toggle_pause(self, button):
        call(['mocp', '--toggle-pause'])

    def on_button_backward(self, button):
        call(['mocp', '--previous'])

    def on_button_forward(self, button):
        call(['mocp', '--next'])

    def on_volumen_change(self, event, value):
        call(['mocp', '--volume={}'.format(round(value * 100))])

    def on_switch_change(self, switch, gparam):
        if switch.get_active():
            if not self.is_server_active():
                call(['mocp', '-S'])

            # CAUSES A GUI FREEZING!
            #Session_DBus.run_dbus_server())
        else:
            #Session_DBus.stop_dbus_server()
            call(['mocp', '-x'])
