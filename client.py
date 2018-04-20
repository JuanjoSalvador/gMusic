#!/usr/bin/python3

import dbus
from subprocess import run, PIPE

bus = dbus.SessionBus()
session = bus.get_object("com.jotadevs.gmusic", "/com/jotadevs/gmusic")

method_message1 = session.get_dbus_method('send_info', 'com.jotadevs.gmusic.SendInfo')

artist = run(['mocp', '-Q', '%artist'], stdout=PIPE).stdout
song   = run(['mocp', '-Q', '%song'], stdout=PIPE).stdout

# Song - Artist
method_message1(song, artist)
