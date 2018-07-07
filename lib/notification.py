import gi
gi.require_version('Notify', '0.7')

from gi.repository import GObject, Notify

class Notification(GObject.Object):

    def __init__(self):
        super(Notification, self).__init__()
        Notify.init("gmusic")

    def send(self, song, artist):
        notification = Notify.Notification.new(song, artist)
        notification.show()