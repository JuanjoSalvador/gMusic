#!/usr/bin/env bash
# -*- ENCODING: UTF-8 -*-

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

    exit 0
fi

## Uninstall tool
if [[ '--remove' = "$1" ]]; then

    if [[ -f "$HOME/.moc/scripts/client.py" ]]; then
        echo 'Borrando client.py'
        rm -f "$HOME/.moc/scripts/client.py"
        echo 'Desinstalación Terminada'
    else
        echo 'No hay nada que desinstalar'
    fi

    exit 0
fi
