allmd = $(wildcard *.md)

allhtml = $(patsubst %.md,%.html,$(allmd))

all : toolkit.epub

toolkit.epub : $(allhtml)
	ebook-convert toc.html toolkit.epub

%.html: %.md
	python scripts/chapter.py $< > $@

clean:
	rm -f *.html
