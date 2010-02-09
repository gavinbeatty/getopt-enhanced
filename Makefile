prefix=/usr/local
DESTDIR=

all: doc

doc/getopt-enhanced.1: doc/getopt-enhanced.1.txt
	a2x -f manpage -L doc/getopt-enhanced.1.txt

doc/getopt-enhanced.1.html: doc/getopt-enhanced.1.txt
	asciidoc doc/getopt-enhanced.1.txt

doc: doc/getopt-enhanced.1 doc/getopt-enhanced.1.html

clean:
	rm -f doc/getopt-enhanced.1 doc/getopt-enhanced.1.html

install-docs: doc/getopt-enhanced.1 doc/getopt-enhanced.1.html
	install -d -m 0755 $(DESTDIR)$(prefix)/share/man/man1
	install -m 0644 doc/getopt-enhanced.1 $(DESTDIR)$(prefix)/share/man/man1/
	install -m 0644 doc/getopt-enhanced.1.html $(DESTDIR)$(prefix)/share/man/man1/

install-doc: install-docs

