# Workflows

## Why change your life
From single medium to cross-media/hybrid publishing.

From-scratch development of each publication format vs. single source-multi format publishing: advantages, disadvantages

In-house development versus outsourcing to service providers: advantages, disadvantages

Why new workflows are essential for small edition, low budget publishing.

## Towards a hybrid workflow   
<!--executive management advies /keuze van workflow-->

### One flowchart of all the three "flows": Traditional, XML, Markdown <!-- Loes & Kimmy -->

### Desktop publishing workflow (from Word to InDesign to digital)

Advantages, limitations <!-- current situation, from InDesign to epub, not ideal-->

The current workflow of desktop publishing, from Word to inDesign, has certain advantages. It is simple, linear, there are no version branches, you end up with one consolidated manuscript, and What You See Is What you Get in relation to design. In the case of print changing hyphenation is for instance both an editing and a typographic problem. When changing to digital these hyphenations can no longer be determined before going to 'print', they change according to the aspect ratio of the device you are using. <!-- perhaps this is more clear? For example, in the case of analogue print where the page is fixed, changing hyphenation is both an editing and a typographic issue. However when transitioning into digital publishing, these hyphenations will be subject to change as they'll change according to the aspect ratio of the device you are using. --> 


The main disadvantage of this workflow is that you only target one medium and the step to go from here to digital are cumbersome, and do not make full use of it's potential. It tries to implement the print into the digital, keeping the workflow one-dimensional. Working with the established software tools - Word and InDesign - it does this almost literally by allowing you to create quirky and strange 'interactive' publications in PDF, which in the end is a static inDesign document, upgraded with some interactive layers. This is a very limited vision on what the possibilities are for digital publishing. Next to this it is possible to export your publication as an .ePub from InDesign, however it is not developed as a program to produce e.pubs and the results are very messy and requires extra steps for the designer. (For a full description of InDesign to Epub see Elizabeth Castro's Epub Straight to the Point) 

1. **InDesign** will never become a hybrid publishing tool as it is (too) specifically developed for print design. 

2. **Word** (or any other text editor that uses this approach, for instance Open Office) will never become a structured text processor. It is a hybrid of a text editor, a desktop program with typographic attributes, and something like a semantic mark-up program. <!--perhaps you can describe what 'mark-up program' is, and some other exmaples? also, perhaps a clear definition is something to consider putting in the general introduction to workflows? --> To a certain extent you can work in a structured manner using stylesheets - determining for instance different types of headers. However, the big problem is that these programs don't enforce working in this structured manner. If only one person doesn't use these stylesheets, but uses manual formatting (instead of structuring!), the whole document is messed-up. The problem with these programs is that there is no separation between formatting and structure, as if these two are equal to each-other, but especially in the world of digital publishing this is not the case.


### XML 

The most detailed structuring language developed is XML. The advantage is that it is very clean, but on the other hand it is very difficult to work with. It is a purely semantic language - with a clear separation with formatting - allowing you to structure the document in a very detailed and thorough manner. These documents work like a database. The original XML document is your fundament, your manuscript, and from there you can create translations for every medium. Thus, if there is a misspelling or another error - you change this in your XML document and you make new translation to the different media that you have produced. For formatting you would need to add a second step, like for instance CSS stylesheets. However, because XML is so detailed it becomes too difficult to work with as the tagging systems become very complex.

Advantages, limitations

Does it work for me?

### Markdown <!-- not perfect, but the most easy to work with and creates structured texts hat allow for hybrid publishing-->

####Advantages and Limitations
Markdown is nothing but plain, unformatted text with human-readable formatting symbols. For example, this is what the beginning of "Alice's Adventures in Wonderland" would like in Markdown:

    # Alice's Adventures in Wonderland
    
    ## Chapter I. Down the Rabbit-Hole

    There was nothing so _very_ remarkable in that; nor did Alice think
    it so VERY much out of the way to hear the Rabbit say to itself,

    > Oh dear! Oh dear! 
    > I shall be late!

    (when she thought it over afterwards, it occurred to her that she
    ought to have wondered at this, but at the time it all seemed quite
    natural); but when the Rabbit actually **took a watch out of its
    waistcoat-pocket**, and looked at it, and then hurried on, Alice
    started to her feet, for it flashed across her mind that she had
    never before seen a rabbit with either a waistcoat-pocket, or a
    watch to take out of it, and burning with curiosity, she ran across
    the field after it, and fortunately was just in time to see it pop
    down a large rabbit-hole under the hedge.

"#" signifies a top-level headline, "##" a second-level headline, "_" italic text, "**" bold text, "> " a long quote. Beyond that, Markdown provides conventions for marking up bold text, lists, embedded images, links. Its popular extension MultiMarkdown also supports footnotes, tables, mathematical formulas, cross-references, bibliographies and definition lists. With simple Open Source converter programs, Markdown text like the above can be automatically translated into well-structured HTML, ePub, PDF, RTF (for importing into InDesign) and other document formats, with a single mouse click or keyboard command, requiring no manual adjustments.

Markdown is a child of Internet culture. It standardizes ad-hoc formatting signs used in E-Mail and chats, and became popular in blogging software. There are similar plain text formatting languages to Markdown: the Wiki syntax used in Wikipedia, the language _Textile_ that is used for a number of web content management systems and the language _reStructuredText_ used for writing technical manuals, and many others. 

Markdown & Co. are human-readable, human-friendly well-structured document formats, excellent for long-term storage and as the basis (or source code) for conversions into present and future document formats. While they are simple, they are also strict and unambiguous enough in their formatting syntax that multiple writers and editors can work on a document without introducing weirdness into its formatting. Another advantage: Markdown can be written an edited on any text program, even as E-Mail or in an web browser or on a mobile phone. Unlike Word or other classical word processing programs, it is not bound to specific software (just like in graphics, the JPEG format is not dependent on any particular piece of software, but can be edited in any graphics program). 

Why do we recommend Markdown in particular? For particular publishing projects - for example, handbooks or books derived from Wikis -, it can be worth considering one the alternatives to Markdown such as _reStructuredText_. (It's also quite easy to convert those into Markdown and vice versa.) There are, however, two reasons why we recommend Markdown as a practical tool for electronic and mixed media publishing:

1. Excellent software support. As the most popular human-readable plain text formatting language, there is plethora of available user-friendly, high quality software for writing and editing documents in Markdown and for converting it into other formats. While Markdown can be written and edited in any computer program that allows to edit text, there are a number of very user-friendly text programs that make it easier to write and view. <!-- some  examples of programs here? -->

2. With Multimarkdown (an extended version of Markdown), it provides all the necessary formatting and document syntax needed in arts- and humanities-oriented text publishing. It is perfectly possible to write, for example, a cultural studies Ph.D. thesis in Multimarkdown, or the essay part (complete with footnotes and bibliographical references) of an exhibition catalog.

Markdown/MultiMarkdown is however not a magic one-size-fits-all solution. It is excellent for text-heavy editorial work, but limited for visual document creation and not really usable for interactive publishing formats. It is not a layout tool, but a pure manuscript format, excellent for keeping manuscripts in a well-structured, readable, durable, software-independent format. 

Markdown (and similar formatting/markup language) are meant for workflows in which there is a clear separation between editorial work - involving writers, translators and editors - on the one hand and publication design on the other. For publications where there is a high degree of interaction between writers/editors and visual designers/artists from the very beginning of the authoring process, these document languages are not the right tool. 


#### Markdown versus XML

Markdown, and similar human-readable plain text markup languages could be called a "poor man's XML". They provide some of the same features and advantages: separation of content structure from visual layout, painless translation into multiple output formats. Their relative simplicity and human readability comes, however, at the price of extensibility and universality. XML is, strictly speaking, not a document markup language, but a meta-language (or toolkit) for building domain- and application-specific markup languages such as: a document markup language for exhibition catalogues, a document markup language for restaurant menus, a document markup language for flyers, etc. 

Markdown & Co. do not provide this flexibility of building one's own syntax, but provide only their built-in, hard-wired syntax. For example, if one needs syntax for encoding footnotes _and_ endnotes, MultiMarkdown simply doesn't provide it. One could think up and use one's own syntax extension (for example ^^[1] for an endnote), but this would not be supported by the word processing and text conversion programs for Markdown. In XML, there are standard methods of declaring and extending markup languages that can automatically be picked up by XML document converters.

However, the declaration of these extensions in the document syntax and conversion rules is highly complex. Even for computer scientists and engineers, XML is often so over-complex that they have resorted to simpler, human-readable language like Markdown, ReStructuredText and ASCIIdoc for software manuals.  

They are not as universal and thoroughly structured as XML, but still provide the advantage of separating content structure from visual layout, along with the advantage of painless translation into multiple output formats. And lastly, XML has very complex markup that is hard to read and write for humans. Easy authoring tools for XML and any kind of XML-based document formats do not really exist yet.

In short, and if the above sounded too cryptically technical: XML is complexity hell even by the measures of computer science. It's the holy grail of document processing, and has been deployed by large scale publishers (especially in the academic field) very successfully. For small to medium publishers, it is often overkill. Markdown provides a good middle-of-the-road solution of a format that is easily usable for non-technicians yet much better structured, and a basis for easy document conversion into HTML, epub and many other formats, than Microsoft Word and similar classical word processing programs.

#### Practical tips and tricks for working with Markdown 

##### Word Processing / editing programs

For Apple's Mac OS X and iOS, there are nice and very user friendly programs
for editing in Markdown. None of them, however, are Open Source:

- [ByWord](http://bywordapp.com), a very user-friendly, distraction-free text writing program with built-in MultiMarkdown support and export to HTML, RTF, PDF and Microsoft Word. The program runs on Macs, iPhone and iPad.

- [iA Writer](http://www.iawriter.com/mac/), a program similar to ByWord. The program runs on Macs, iPhone and iPad.

- [Scrivener](http://www.literatureandlatte.com/scrivener.php), a word processing program popular among professional writers, for Mac OS X and Windows. Fully supports MultiMarkdown internally.


##### Document conversion programs
<!-- why is calibre not mentioned here? Question by kimmy-->

- [multimarkdown](http://fletcherpenney.net/multimarkdown/), the original program convert MultiMarkdown files into HTML, PDF, OpenDocument (for later conversion into RTF or Microsoft Word). Open Source, runs on Linux, Mac OS X and Windows.

- [pandoc](http://johnmacfarlane.net/pandoc/), similar in functionality to multimarkdown, but much more powerful. Pandoc reads more input formats (including HTML and reStructuredText) and can output HTML5, XHTML, LaTeX, RTF, Word, Epub 2 and 3, PDF and many more. Typographic templates for the conversion can be easily customized. 

Pandoc is the tool we recommend for working with Multimarkdown, and has also been extensively used in creating this publication.


##### Practical tips

###### Cleaning up Markdown

Since Markdown is a document format and not a word processing program, it does not offer functions like automatic renumbering of footnotes and list items during text editing. In fact, such numbers don't matter since everything will be renumbered during the document conversion anyway. 

However, to also make the Markdown text source coherent and tidy, pandoc can be used to clean it up. The trick is to tell pandoc to convert a document from Markdown to Markdown:

    pandoc -f markdown -t markdown --output markdown-document-clean.txt markdown-document.txt




### Database publishing / Content Management System
<!-- the extra possibilities / what you win by changing your life-->




<!-- comments from Amy: perhaps some definitions or descriptions of what 'mark-up', 'semantic langauge' and 'restructured text' is after this part? -->




