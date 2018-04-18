import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from subprocess import call, run, PIPE

class Player():
    def is_server_active(*args):
        return bool(run(['pidof', 'mocp'], stdout=PIPE).stdout)

    def on_button_close(self, *args):
        if self.is_server_active():
            call(['mocp', '-x'])

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
        else:
            call(['mocp', '-x'])
