#!/usr/bin/env bash
# -*- ENCODING: UTF-8 -*-

## Help Options
if [[ '--help' = "$1" ]] || [[ '-h' = "$1" ]]; then
    echo ''
    echo 'OPTIONS script:'
    echo ''
    echo -e "$0 --install\tInstall tool"
    echo -e "$0 --update\tUpdate tool from GitHub"
    echo -e "$0 --uninstall\tRemove tool and settings"
    echo -e "$0 --help\tThis Help"
    echo -e "$0 -h\tThis Help"
    echo ''
    echo -e "make install\tInstall tool"
    echo -e "make update\tUpdate tool from GitHub"
    echo -e "make uninstall\tRemove tool and settings"
    echo -e "make reinstall\tUninstall and Install from clean"
    echo -e "make help\tThis help"

    exit 0
fi


## Install Tool
if [[ '--install' = "$1" ]]; then
    echo 'Instalando'

    ## Crear directorio si no existiera
    if [[ ! -d "$HOME/.moc/scripts" ]]; then
        echo 'Creando el directorio ~/.moc/scripts'
        mkdir -p "$HOME/.moc/scripts"
    fi

    ## Copiar cliente si no existe
    if [[ ! -f "$HOME/.moc/scripts/client.py" ]]; then
        echo 'Creando el cliente en ~/.moc/scripts/client.py'
        cp 'client.py' "$HOME/.moc/scripts/client.py"
    fi

    if [[ -f "$HOME/.moc/config" ]]; then
        script="OnSongChange = ${HOME}/.moc/scripts/client\.py"
        sed -r -i "s,^\#?\s*OnSongChange\s*=*.*$,$script," "$HOME/.moc/config"
    else
        echo 'No existe el archivo "~/.moc/config", generando uno nuevo'
        echo "OnSongChange = $HOME/.moc/scripts/client.py" > "$HOME/.moc/config"
    fi

    exit 0
fi

## Update Tool
if [[ '--update' = "$1" ]] && [[ -f /usr/bin/git ]]; then
    git pull
    exit 0
elif [[ '--update' = "$1" ]]; then
    echo 'Para actualizar se necesita la herramienta "git"'
    echo 'En Debian GNU/Linux puedes instalarlo con "sudo apt install git"'
    exit 1
fi


## Uninstall Tool
if [[ '--remove' = "$1" ]]; then

    if [[ -f "$HOME/.moc/scripts/client.py" ]]; then
        echo 'Borrando client.py'
        rm -f "$HOME/.moc/scripts/client.py"
        echo 'Desinstalación Terminada'
    else
        echo 'No hay nada que desinstalar'
    fi

    echo 'Limpiando configuraciones'
    sed -r -i "s,^\#?\s*OnSongChange\s*=*.*$,#OnSongChange =," "$HOME/.moc/config"

    exit 0
fi

exit 0
