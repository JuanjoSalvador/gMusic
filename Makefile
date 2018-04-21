.PHONY: all install update reinstall uninstall clean help \

all: install

install:
	./installer.sh --install

update:
	./installer.sh --update

reinstall: uninstall install

uninstall clean:
	./installer.sh --remove

help:
	./installer.sh --help
