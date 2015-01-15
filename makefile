# Makefile for Digital Publishing Toolkit
#

allmd = $(wildcard *.md docs/*.md images/*.md)
# svg = $(wildcard images/_in_progress/*.svg)
# svgpng = $(patsubst %.svg,%.png,$(svg))

derivedhtml = $(patsubst %.md,%.html,$(allmd))

all : toolkit.epub
trailer: toolkit-trailer.gif

# toolkit.epub : title.txt $(allmd)
# 	cd docs && pandoc \
# 	--self-contained \
# 	--epub-metadata=../metadata.xml \
# 	--epub-stylesheet=../styles.css \
# 	--default-image-extension svg \
# 	--table-of-contents \
# 	--epub-embed-font=fonts/FreeUniversal-Regular.ttf \
# 	--epub-embed-font=fonts/FreeUniversal-Bold.ttf \
# 	-o ../toolkit.epub \
# 	../title.txt *.md

# toolkit.pdf : $(svgpng) $(allmd)
# 	cd docs && pandoc \
# 	--self-contained \
# 	--epub-metadata=../metadata.xml \
# 	--default-image-extension png \
# 	--epub-stylesheet=../styles.css \
# 	--table-of-contents \
# 	-o ../toolkit.pdf \
# 	../title.txt -H ../patch.tex *.md

# Use pandoc to convert markdown to HTML
%.html: %.md
	pandoc --css=styles.css -s $< > $@

# Use ImageMagick to convert svg's to png
# MM: Automatic image conversion isn't working
# on both technical and design grounds (event when it *works* the results are often not right)
# Images need to be commited in both SVG and (directly exported) PNG.
# %.png : %.svg
# 	convert $< $@

clean:
	rm -f $(derivedhtml)
	rm toolkit.epub
	rm toolkit.pdf

# markdown sources
sources=$(shell scripts/expand_toc.py --list TOC.md)

# Rule to build the entire book as a single markdown file from the table of contents file using expand_toc.py
toolkit.md: TOC.md $(sources)
	# scripts/expand_toc.py TOC.md --section-pages --filter scripts/chapter.sh > $@
	scripts/expand_toc.py TOC.md --no-toc > $@

toolkit.epub: toolkit.md metadata.xml styles.css docs/images/cover.png
	cd docs && pandoc \
		--from markdown \
		--to epub3 \
		--self-contained \
		--epub-chapter-level=2 \
		--epub-stylesheet=../styles.epub.css \
		--epub-cover-image=images/cover.png \
		--epub-metadata=../metadata.xml \
		--epub-embed-font=../lib/UbuntuMono-B.ttf \
		--epub-embed-font=../lib/OpenSans-Bold.ttf \
		--epub-embed-font=../lib/OpenSans-BoldItalic.ttf \
		--epub-embed-font=../lib/OpenSans-Italic.ttf \
		--epub-embed-font=../lib/OpenSans-Light.ttf \
		--epub-embed-font=../lib/OpenSans-LightItalic.ttf \
		--epub-embed-font=../lib/OpenSans-Regular.ttf \
		--default-image-extension png \
		--toc-depth=2 \
		-o ../toolkit.epub \
		../toolkit.md

# Epub post production - and and enhancements to toolkit.epub
FromPrintToEbooks.epub: toolkit.epub
	python scripts/glossary.py toolkit.epub && \
	python scripts/epub_post.py FromPrintToEbooks.epub

# 

# needs wkhtmltopdf installed http://wkhtmltopdf.org/
toolkit.pdf: toolkit.md
	cd docs && pandoc --from markdown \
	-t html5 \
	-s \
	--css=styles.pdf.css \
	--default-image-extension png \
	-o toolkit.html ../toolkit.md && \
	wkhtmltopdf --user-style-sheet styles.pdf.css toolkit.html ../toolkit.pdf 



toolkit.docx: toolkit.md
	cd docs && pandoc --default-image-extension png --table-of-contents -o ../toolkit.docx ../toolkit.md

toolkit.odf: toolkit.md
	cd docs && pandoc --default-image-extension png --table-of-contents -o ../toolkit.odf ../toolkit.md


# Trailer (this rule works for any epub)
%-trailer.gif: %.epub
	python scripts/epubtrailer.py $< --width 320 --height 240 --duration=0.5 -o $@


toolkit.icml: toolkit.md
	cd docs && pandoc \
		--from markdown \
		--to icml \
		--self-contained \
		-o ../toolkit.icml \
		../toolkit.md
