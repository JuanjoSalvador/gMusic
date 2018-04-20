# gMusic

GTK Frontend for Music On Console

![gMusic window on development](https://pbs.twimg.com/media/DbOBgIdX4AIBvJd.png)

### Basic installation

You will need the following requirements:

* Python 3.4 or higher
* PyGObject 3.11 or higher

    $ sudo apt-get install python3 python3-gi

If you're running a Debian or Ubuntu based system, maybe you will have it installed now.

1. Download or clone the repo.
2. Unzip (if needed) and move `client.py` to `~/.moc/scripts/client.py`
3. Open your MOC's config file, and locate the line `#OnSongChange`. Uncomment it.
4. Set the `OnSongChange` event to `/home/<YOUR-USER>/.moc/scripts/client.py`

### Running gMusic

At this moment, I'm working into the possibility to install it using PPA and add a menu entry, but meanwhile...

    python3 /path/to/gMusic/folder/main.py
    
Enjoy!

