.SUFFIXES:
SHELL = /bin/sh

PREFIX=/usr/local
DESTDIR=

A2X ?= a2x
ASCIIDOC ?= asciidoc
GROFF ?= groff
COL ?= col
RM ?= rm -f
INSTALL_DIR ?= install -d -m 0755
INSTALL_DATA ?= install -m 0644

help:
	@echo "Targets: doc install-doc clean"

all: doc

doc/getopt-enhanced.1: doc/getopt-enhanced.1.txt
	$(A2X) -f manpage -L doc/getopt-enhanced.1.txt

doc/getopt-enhanced.1.html: doc/getopt-enhanced.1.txt
	$(ASCIIDOC) doc/getopt-enhanced.1.txt

doc/getopt-enhanced.txt: doc/getopt-enhanced.1
	$(GROFF) -t -e -Tutf8 -P -c -mandoc doc/getopt-enhanced.1 | \
	$(COL) -bx > doc/getopt-enhanced.txt

doc: doc/getopt-enhanced.1 doc/getopt-enhanced.1.html doc/getopt-enhanced.txt
docs: doc

clean:
	$(RM) doc/getopt-enhanced.1 doc/getopt-enhanced.1.html

install-docs: doc/getopt-enhanced.1 doc/getopt-enhanced.1.html doc/getopt-enhanced.txt
	@$(INSTALL_DIR) $(DESTDIR)$(PREFIX)/share/man/man1
	$(INSTALL_DATA) doc/getopt-enhanced.1 $(DESTDIR)$(PREFIX)/share/man/man1/
	$(INSTALL_DATA) doc/getopt-enhanced.1.html $(DESTDIR)$(PREFIX)/share/man/man1/
	@$(INSTALL_DIR) $(DESTDIR)$(PREFIX)/share/doc/getopt-enhanced/
	$(INSTALL_DATA) doc/getopt-enhanced.txt $(DESTDIR)$(PREFIX)/share/doc/getopt-enhanced/
install-doc: install-docs

.PHONY: help all doc docs clean install-docs install-doc
