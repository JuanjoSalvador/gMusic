.PHONY: all install update reinstall uninstall clean \

all: install

install:
	./installer.sh --install

update:
	./installer.sh --update

reinstall: uninstall install

uninstall clean:
	./installer.sh --remove
