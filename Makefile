prefix=/usr/local
DESTDIR=

all: doc

doc/getopt-enhanced.1: doc/getopt-enhanced.1.txt
	a2x -f manpage -L doc/getopt-enhanced.1.txt

doc/getopt-enhanced.1.html: doc/getopt-enhanced.1.txt
	asciidoc doc/getopt-enhanced.1.txt

doc/getopt-enhanced.txt: doc/getopt-enhanced.1
	groff -t -e -Tutf8 -P -c -mandoc doc/getopt-enhanced.1 | \
	col -bx > doc/getopt-enhanced.txt

doc: doc/getopt-enhanced.1 doc/getopt-enhanced.1.html doc/getopt-enhanced.txt

clean:
	rm -f doc/getopt-enhanced.1 doc/getopt-enhanced.1.html

install-docs: doc/getopt-enhanced.1 doc/getopt-enhanced.1.html doc/getopt-enhanced.txt
	install -d -m 0755 $(DESTDIR)$(prefix)/share/man/man1
	install -m 0644 doc/getopt-enhanced.1 $(DESTDIR)$(prefix)/share/man/man1/
	install -m 0644 doc/getopt-enhanced.1.html $(DESTDIR)$(prefix)/share/man/man1/
	install -d -m 0755 $(DESTDIR)$(prefix)/share/doc/getopt-enhanced/
	install -m 0644 doc/getopt-enhanced.txt $(DESTDIR)$(prefix)/share/doc/getopt-enhanced/

install-doc: install-docs

