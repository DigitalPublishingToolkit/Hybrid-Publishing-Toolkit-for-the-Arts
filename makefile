# Makefile for Digital Publishing Toolkit
#

allmd = $(wildcard *.md docs/*.md images/*.md)

derivedhtml = $(patsubst %.md,%.html,$(allmd))

all : toolkit.epub

toolkit.epub : $(derivedhtml)
	pandoc -S --epub-metadata=metadata.xml --epub-stylesheet=styles.css -o toolkit.epub title.txt docs/*.md
	# pandoc -o toolkit.epub --cover images/_dpt/cover.png --title "Digital Publishing Toolkit" --pubdate "01 July 2014" --publisher "Institute of Network Cultures" *

toolkit.pdf : $(derivedhtml)
	pandoc -S --epub-metadata=metadata.xml --epub-stylesheet=styles.css -o toolkit.pdf title.txt -H patch.tex docs/*.md

%.html: %.md
	pandoc --css=styles.css -s $< > $@

clean:
	rm -f $(derivedhtml)
