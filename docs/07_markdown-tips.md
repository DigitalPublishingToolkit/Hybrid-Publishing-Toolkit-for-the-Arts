# Practical tips and tricks for working with Markdown 

## Word Processing / editing programs

For Apple's Mac OS X and iOS, there are nice and very user friendly programs
for editing in Markdown. None of them, however, are Open Source:

- [ByWord](http://bywordapp.com), a very user-friendly, distraction-free text writing program with built-in MultiMarkdown support and export to HTML, RTF, PDF and Microsoft Word. The program runs on Macs, iPhone and iPad.

- [iA Writer](http://www.iawriter.com/mac/), a program similar to ByWord. The program runs on Macs, iPhone and iPad.

- [Scrivener](http://www.literatureandlatte.com/scrivener.php), a word processing program popular among professional writers, for Mac OS X and Windows. Fully supports MultiMarkdown internally.


## Document conversion programs

- [multimarkdown](http://fletcherpenney.net/multimarkdown/), the original program convert MultiMarkdown files into HTML, PDF, OpenDocument (for later conversion into RTF or Microsoft Word). Open Source, runs on Linux, Mac OS X and Windows.

- [pandoc](http://johnmacfarlane.net/pandoc/), similar in functionality to multimarkdown, but much more powerful. Pandoc reads more input formats (including HTML and reStructuredText) and can output HTML5, XHTML, LaTeX, RTF, Word, Epub 2 and 3, PDF and many more. Typographic templates for the conversion can be easily customized. 

Pandoc is the tool we recommend for working with Multimarkdown, and has also been extensively used in creating this publication.


## Practical tips

### Cleaning up Markdown

Since Markdown is a document format and not a word processing program, it does not offer functions like automatic renumbering of footnotes and list items during text editing. In fact, such numbers don't matter since everything will be renumbered during the document conversion anyway. 

However, to also make the Markdown text source coherent and tidy, pandoc can be used to clean it up. The trick is to tell pandoc to convert a document from Markdown to Markdown:

    pandoc -f markdown -t markdown --output markdown-document-clean.txt markdown-document.txt





