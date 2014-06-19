# Makefile for Digital Publishing Toolkit
#

allmd = $(wildcard *.md docs/*.md images/*.md)

derivedhtml = $(patsubst %.md,%.html,$(allmd))

all : toolkit.epub

toolkit.epub :
	pandoc \
	--self-contained \
	--epub-metadata=metadata.xml \
	--epub-stylesheet=styles.css \
	--default-image-extension png \
	--table-of-contents \
	-o toolkit.epub \
	title.txt docs/*.md

toolkit.pdf :
	pandoc \
	--self-contained \
	--epub-metadata=metadata.xml \
	--default-image-extension png \
	--epub-stylesheet=styles.css \
	--table-of-contents \
	-o toolkit.pdf \
	title.txt -H patch.tex docs/*.md

%.html: %.md
	pandoc --css=styles.css -s $< > $@

clean:
	rm -f $(derivedhtml)
