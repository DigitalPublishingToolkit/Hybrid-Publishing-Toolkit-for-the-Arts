# Makefile for Digital Publishing Toolkit
#

allmd = $(wildcard *.md docs/*.md images/*.md)

derivedhtml = $(patsubst %.md,%.html,$(allmd))

all : toolkit.epub toolkit.pdf

toolkit.epub : $(derivedhtml)
	ebook-convert TOC.html toolkit.epub --cover images/_dpt/cover.png --title "Digital Publishing Toolkit" --pubdate "01 July 2014" --publisher "Institute of Network Cultures"

toolkit.pdf : $(derivedhtml)
	ebook-convert TOC.html toolkit.pdf --cover images/_dpt/cover.png --title "Digital Publishing Toolkit" --pubdate "01 July 2014" --publisher "Institute of Network Cultures"

%.html: %.md
	# python scripts/chapter.py $< > $@
	pandoc --css=styles.css -s $< > $@

clean:
	rm -f $(derivedhtml)
