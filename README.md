# gMusic

GTK Frontend for Music On Console

![gMusic window on development](https://pbs.twimg.com/media/DbOBgIdX4AIBvJd.png)

## Requeriments

You will need the following requirements:

-   Python 3.4 or higher
-   PyGObject 3.11 or higher

```bash
    sudo apt-get install python3 python3-gi
```

If you're running a Debian or Ubuntu based system, maybe you will have it installed now.

## Download or clone the repo

Download:

```bash
    wget https://github.com/JuanjoSalvador/gMusic/archive/master.zip
```

Clone:

```bash
    git clone https://github.com/JuanjoSalvador/gMusic.git
```

## Automatic installation

This tool includes an installer in the Makefile file:

```bash
    make install
```

Files and settings will be automatically installed inside a `~/.moc/scripts/`
and `~/.moc/config`

## Manual Installation

### Copy Script

Unzip (if needed) and copy `client.py` to `~/.moc/scripts/client.py`

```
    cp client.py ~/.moc/scripts/client.py
```

### Change configuration file

Open your MOC's config file, and locate the line `#OnSongChange`. Uncomment it.

Set the `OnSongChange` event to `/home/<YOUR-USER>/.moc/scripts/client.py`

## Running gMusic

At this moment, I'm working into the possibility to install it using PPA and add a menu entry, but meanwhile...

```python3
    python3 /path/to/gMusic/folder/main.py
```

## Other options
-   **make update** → Update tool from GitHub
-   **make uninstall** → Remove tool and settings
-   **make reinstall** → Uninstall and Install from clean
-   **make help** → This help

Enjoy!
