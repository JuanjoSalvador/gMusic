import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from subprocess import call, run, PIPE

class Player():
    """
    GMusic button handler
    """

    def is_server_active(*args):
        """
        Check if the server is running
        :return: boolean if server is running or not
        """
        return bool(run(['pidof', 'mocp'], stdout=PIPE).stdout)

    def on_button_close(self, *args):
        """
        Close the server and client.
        """
        if self.is_server_active():
            call(['mocp', '-x'])

        Gtk.main_quit(*args)

    # BUTTONS

    def on_button_play(self, button):
        """
        Starts playing the music
        """
        call(['mocp', '--play'])

    def on_button_toggle_pause(self, button):
        """
        Pause/unpause music
        """
        call(['mocp', '--toggle-pause'])

    def on_button_backward(self, button):
        """
        Call the previous song
        """
        call(['mocp', '--previous'])

    def on_button_forward(self, button):
        """
        Call the next song
        """
        call(['mocp', '--next'])

    def on_volumen_change(self, event, value):
        """
        Changes MOC's volume
        """
        call(['mocp', '--volume={}'.format(round(value * 100))])

    def on_switch_change(self, switch, gparam):
        """
        Starts or stops the server using the UI Switch
        """
        if switch.get_active():
            if not self.is_server_active():
                call(['mocp', '-S'])
        else:
            call(['mocp', '-x'])
