# Makefile for Digital Publishing Toolkit
#

allmd = $(wildcard *.md docs/*.md images/*.md)

derivedhtml = $(patsubst %.md,%.html,$(allmd))

all : toolkit.epub

toolkit.epub : $(derivedhtml)
	ebook-convert TOC.html toolkit.epub --cover images/_dpt/cover.png --title "Digital Publishing Toolkit"

%.html: %.md
	# python scripts/chapter.py $< > $@
	pandoc --css=styles.css -s $< > $@

clean:
	rm -f $(derivedhtml)
