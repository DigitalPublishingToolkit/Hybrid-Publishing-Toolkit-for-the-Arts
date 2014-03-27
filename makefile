allmd = $(wildcard *.md docs/*.md)

derivedhtml = $(patsubst %.md,%.html,$(allmd))

all : toolkit.epub

toolkit.epub : $(derivedhtml)
	ebook-convert TOC.html toolkit.epub --cover images/cover.png --title "Digital Publishing Toolkit"

%.html: %.md
	python scripts/chapter.py $< > $@

clean:
	rm -f $(derivedhtml)
