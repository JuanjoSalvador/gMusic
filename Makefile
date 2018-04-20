.PHONY: all install reinstall uninstall clean \

all: install

install:
	./installer.sh --install

reinstall: uninstall install

uninstall clean:
	./installer.sh --remove
