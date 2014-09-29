# Makefile for Digital Publishing Toolkit
#

allmd = $(wildcard *.md docs/*.md images/*.md)
svg = $(wildcard images/_in_progress/*.svg)
svgpng = $(patsubst %.svg,%.png,$(svg))

derivedhtml = $(patsubst %.md,%.html,$(allmd))

all : toolkit.epub

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
%.png : %.svg
	convert $< $@

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

toolkit.epub: toolkit.md metadata.xml styles.css images/cover.png
	cd docs && pandoc \
		--from markdown \
		--self-contained \
		--epub-chapter-level=2 \
		--epub-stylesheet=../styles.epub.css \
		--epub-cover-image=../images/cover.png \
		--epub-metadata=../metadata.xml \
		--epub-embed-font=../lib/UbuntuMono-B.ttf \
		--default-image-extension png \
		--toc-depth=2 \
		-o ../toolkit.epub \
		../toolkit.md

toolkit.pdf: toolkit.md $(svgpng)
	cd docs && pandoc \
	--self-contained \
	--epub-metadata=../metadata.xml \
	--default-image-extension png \
	--epub-stylesheet=../styles.epub.css \
	--table-of-contents \
	-o ../toolkit.pdf \
	../title.txt -H ../patch.tex ../toolkit.md
