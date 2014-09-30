# 06 Towards a Hybrid Workflow Based on Markdown

Creating a workflow that is both structured and flexible enough to cater for the different choices made is a key step towards an efficient electronic or hybrid publishing strategy. The hybrid workflow we propose here is based on the need for publishing across different mediums, while keeping the majority of the work process in-house instead of outsourcing. 

First describing a more traditional workflow based on desktop publishing via InDesign with a print book as end result, we move to an ideally fitted workflow centered around the strucural file format XML, ending with a Markdown-oriented workflow which is both easy to use and open to many possibilities. Following such a workflow will make the transition from a print-centered publication process to a digital and print - in other words hybrid - publication process viable. 

Instead of ‘adding’ the digital publication at the end of an existing workflow, based on the printed book as end result as is done often by publishers, the workflow should be adjusted and made efficient and practical towards hybrid publishing in an earlier stage. From-scratch development of each publication format is thus replaced by single source-multi format publishing.

However, the description below starts at a point which in reality is not the beginning of the publication trajectory, namely when an author hands in the definitive manuscript - so after the editing and rewriting process has been rounded off. Should the author already be working in Markdown, HTML or even XML format, this will change the workflow. However, in our experience manuscripts are mainly produced in Microsoft Word and delivered in .doc or .docx.

NB: An important step preceding the publication trajectory lies in the formulation of the in-house style guide, where authors and editors can find the requirements for the manuscript. This style guide must be adapted according to the hybrid workflow as an absolute start. See the Guide per genres for pointers regarding adjusting the style guide in this sense.

So how small edition, low budget publishing houses can implement the new workflow is what we will turn to now.

## Three workflows: desktop publishing, XML, Markdown 
![Traditional Workflow](../images/_in_progress/07_workflowOldNewTRADITIONAL "Workflow Traditional")
![Traditional XML](../images/_in_progress/07_workflowOldNewXML "Workflow XML")
<!--![Traditional Markdown](../images/_in_progress/07_workflowOldNewMD "Workflow Markdown") -->
<!-- Loes & Kimmy -->

### Desktop publishing workflow (from Word to InDesign to digital)

Desktop publishing for a lot of publishers presents the current situation. A Microsoft Word file is imported into InDesign and, after designing and editing, exported to PDF, ready to be printed. The traditional, print-oriented workflow can be seen as standard for one-to-one publications: the print book is translated to an electronic version, following the 'original' as close as possible. 

There are certain advantages to this workflow: it is simple, linear, there are no version branches, you end up with one consolidated manuscript, and What You See Is What You Get in relation to design. For example, in the case of a print design where the page is fixed, changing hyphenation is both an editing and a typographic issue: a hyphen must be typed directly into the InDesign document. <!-- maybe this is not formulated very clearly, but there needs to be some explanation here _ Miriam --> However, in digital publishing, hyphenations are not fixed, but will be subject to change as they shift according to the aspect ratio of the device used. So when an editorial correction involves a hyphenation, this need not be adjusted in the digital file. However, this of course also means a limitation in electronic design possibilities.

The main disadvantage of this workflow is that you only target one medium and the steps to go from here to digital are cumbersome, and do not make full use of the potential in electronic publishing. A workflow centered around the paper publication tries to translate print into the digital books, keeping the workflow one-dimensional instead of multi-dimensional. 

Importantly, going from from InDesign to e-publication is not ideal, especially when working with older versions of the software. The results can be messy and may require extra steps in finalizing the publication. InDesign is simply not optimized as a hybrid publishing tool. as it is (too) specifically developed for print design.[^1] The latest version of the InDesign suite is catered more to electronic publishing. For a detailed look at these developments, see XXXXXXX Elisabeth Castro. <!--hopefully a chapter by Liz--> 

In the same way Microsoft Word (or any other text editor that uses a similar approach, for instance Open Office) is not suited for processing structured text. Structured text for example is marking up a title with the tag 'header'. Later on in the design process the structure can be accompanied by a certain formatting, for example headers are 'bold'. To a certain extent these text processing pograms allow working in a structured manner, by using stylesheets which determine for instance different types of headers. The problem is that they do not separate between formatting and structure, while in the world of digital publishing this is especially important.

It is possible to create 'interactive' publications in PDF, working with Microsoft Word and InDesign. In the end however these are also static inDesign documents, upgraded with some interactive layers. This is still a limited vision of what the possibilities are for digital publishing. The second workflow, which centers the file format XML, does precisely that.

### XML 

The most detailed structuring language developed is XML. It is very clean, but also quite difficult to work with. A purely semantic language with a clear separation between structure and formatting, it allows you to structure the document in a detailed and thorough manner. An XML document works like an archive: from this single document it's possible to create multiple output for different media. Thus, a misspelling or another error is changed in the XML document, which is then used to recreate the output to the different media. Formatting is done in a second step, with for instance **Cascading Style Sheets** (CSS). 

While XML presents an almost ideal way of working with single format files which deliver multiple output formats, we do not present it as the most advisable solution for small, independent publishing houses. Because XML is so detailed, with a very complex tagging system it is difficult to work with.

It might work for ... <!--this needs adding _ Miriam-->

### Markdown 

Central in a hybrid publishing workflow we recommend to use the mark-up language Markdown, an easier-to-use language than XML. Markdown is not perfect, but is the most easy to work with and enables the creation of structured texts, thus allowing for hybrid publishing.

####Introduction: advantages and limitations
John Gruber, developer of Markdown, describes Markdown on his website as follows: 'Markdown allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML).'^[2] Markdown is a way to process plain, unformatted text with human-readable formatting symbols. That means that Markdown doesn't use HTML style tags to format, such as `<b>` for bold or `<author>` to mark-up the author name. For example, this is what the beginning of *Alice's Adventures in Wonderland* would like in Markdown:

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

'#' signifies a top-level headline, '##' a second-level headline, '_' italic text, '**' bold text, '>' a block quote. Beyond that, Markdown provides conventions for marking up bold text, lists, embedded images, links. Its popular extension MultiMarkdown <!-- add MultiMarkdown to glossary--> also supports footnotes, tables, mathematical formulas, cross-references, bibliographies and definition lists. With simple Open Source converter programs, Markdown text like the above can be automatically translated into well-structured HTML, EPUB, PDF, RTF (for importing into InDesign) and other document formats, with a single mouse click or keyboard command, requiring no manual adjustments.

Markdown is a child of Internet culture. It standardizes ad-hoc formatting signs used in E-Mail and chats, and became popular in blogging software. There are similar plain text formatting languages to Markdown: the Wiki syntax used in Wikipedia, the language _Textile_ that is used for a number of web content management systems and the language _reStructuredText_ used for writing technical manuals, and many others. 

Markdown & Co. are human-readable, human-friendly well-structured document formats, excellent for long-term storage and as the basis (or source code) for conversions into present and future document formats. While they are simple, they are also strict and unambiguous enough in their formatting syntax that multiple writers and editors can work on a document without introducing weirdness into its formatting. Another advantage: Markdown can be written an edited on any text program, even as E-Mail or in an web browser or on a mobile phone. Unlike Word or other classical word processing programs, it is not bound to specific software (just like in graphics, the JPEG format is not dependent on any particular piece of software, but can be edited in any graphics program). 

Why do we recommend Markdown in particular? For particular publishing projects - for example, handbooks or books derived from Wikis -, it can be worth considering one the alternatives to Markdown such as _reStructuredText_. (It's also quite easy to convert those into Markdown and vice versa.) There are, however, two reasons why we recommend Markdown as a practical tool for electronic and mixed media publishing:

1. Excellent software support. As the most popular human-readable plain text formatting language, there is plethora of available user-friendly, high quality software for writing and editing documents in Markdown and for converting it into other formats. While Markdown can be written and edited in any computer program that allows to edit text, there are a number of very user-friendly text programs that make it easier to write and view. <!-- some  examples of programs here? -->

2. With Multimarkdown (an extended version of Markdown), it provides all the necessary formatting and document syntax needed in arts- and humanities-oriented text publishing. It is perfectly possible to write, for example, a cultural studies Ph.D. thesis in Multimarkdown, or the essay part (complete with footnotes and bibliographical references) of an exhibition catalog.

Markdown/MultiMarkdown is however not a magic one-size-fits-all solution. It is excellent for text-heavy editorial work, but limited for visual document creation and not really usable for interactive publishing formats. It is not a layout tool, but a pure manuscript format, excellent for keeping manuscripts in a well-structured, readable, durable, software-independent format. 

Markdown (and similar formatting/markup language) are meant for workflows in which there is a clear separation between editorial work - involving writers, translators and editors - on the one hand and publication design on the other. For publications where there is a high degree of interaction between writers/editors and visual designers/artists from the very beginning of the authoring process, these document languages are not the right tool. 


<!-- here. 12 sept --  who is this _ asks Miriam-->

#### Markdown versus XML

Markdown, and similar human-readable plain text markup languages could be called a “poor man’s XML”. To summarize XML is complexity hell even by the measures of computer science. It’s the holy grail of document processing, and has been deployed by large scale publishers (especially in the academic field) very successfully. For small to medium publishers, it is often overkill. Markdown provides a good middle-of-the-road solution of a format that is easily usable for non-technicians yet much better structured, and a basis for easy document conversion into HTML, EPUB and many other formats, than Microsoft Word and similar classical word processing programs.

Technically speaking, Markdown provides some of the same features and advantages: separation of content structure from visual layout, painless translation into multiple output formats. Their relative simplicity and human readability comes, however, at the price of extensibility and universality. XML is, strictly speaking, not a document markup language, but a meta-language (or toolkit) for building domain- and application-specific markup languages such as: a document markup language for exhibition catalogues, a document markup language for restaurant menus, a document markup language for flyers, etc.

Markdown & Co. do not provide this flexibility of building one’s own syntax, but provide only their built-in, hard-wired syntax. For example, if one needs syntax for encoding footnotes and endnotes, MultiMarkdown simply doesn’t provide it. One could think up and use one’s own syntax extension (for example ^^[1] for an endnote), but this would not be supported by the word processing and text conversion programs for Markdown. In XML, there are standard methods of declaring and extending markup languages that can automatically be picked up by XML document converters.

However, the declaration of these extensions in the document syntax and conversion rules is highly complex. Even for computer scientists and engineers, XML is often so over-complex that they have resorted to simpler, human-readable language like Markdown, ReStructuredText and ASCIIdoc for software manuals.

They are not as universal and thoroughly structured as XML, but still provide the advantage of separating content structure from visual layout, along with the advantage of painless translation into multiple output formats. And lastly, XML has very complex markup that is hard to read and write for humans. Easy authoring tools for XML and any kind of XML-based document formats do not really exist yet.

#### Practical tips and tricks for working with Markdown 

##### Word Processing / editing programs

For Apple's Mac OS X and iOS, there are nice and very user friendly programs
for editing in Markdown. None of them, however, are Open Source:

- [ByWord](http://bywordapp.com), a very user-friendly, distraction-free text writing program with built-in MultiMarkdown support and export to HTML, RTF, PDF and Microsoft Word. The program runs on Macs, iPhone and iPad.

- [iA Writer](http://www.iawriter.com/mac/), a program similar to ByWord. The program runs on Macs, iPhone and iPad.

- [Scrivener](http://www.literatureandlatte.com/scrivener.php), a word processing program popular among professional writers, for Mac OS X and Windows. Fully supports MultiMarkdown internally.

- [Mou](http://www.mouapp.com), is a Markdown editor that funds on Mac OS X. It consists of features like live preview, sync scroll, auto save, powerful actions, auto pair, custom themes and CSS, HTML and PDF export, enhanced CJK support and more.


##### Document conversion programs
- [multimarkdown](http://fletcherpenney.net/multimarkdown/), the original program convert MultiMarkdown files into HTML, PDF, OpenDocument (for later conversion into RTF or Microsoft Word). Open Source, runs on Linux, Mac OS X and Windows.

- [pandoc](http://johnmacfarlane.net/pandoc/), similar in functionality to multimarkdown, but much more powerful. Pandoc reads more input formats (including HTML and reStructuredText) and can output HTML5, XHTML, LaTeX, RTF, Word, EPUB 2 and 3, PDF and many more. Typographic templates for the conversion can be easily customized. 

- [Calibre](http://http://calibre-ebook.com/), application suite that allows users to manage ebook collections as well as to create, edit, and read ebooks. It supports a variety of formats (including the common Amazon Kindle and EPUB formats), ebook syncing with a variety of ebook readers, and conversion (within DRM restrictions) from different ebook and non-ebook formats. Open Source, runs on Linux, Mac OS X and Windows.

Pandoc is the tool we recommend for working with Multimarkdown, and has also been extensively used in creating this publication.


##### Practical tips

Cleaning up Markdown

Since Markdown is a document format and not a word processing program, it does not offer functions like automatic renumbering of footnotes and list items during text editing. In fact, such numbers don't matter since everything will be renumbered during the document conversion anyway. 

However, to also make the Markdown text source coherent and tidy, pandoc can be used to clean it up. The trick is to tell pandoc to convert a document from Markdown to Markdown:

    pandoc -f markdown -t markdown --output markdown-document-clean.txt markdown-document.txt




### Database publishing / Content Management System
<!-- the extra possibilities / what you win by changing your life-->




<!-- comments from Amy: perhaps some definitions or descriptions of what 'mark-up', 'semantic langauge' and 'restructured text' is after this part? --><!-- Miriam: are they not in the Glossary yet? -->


[^1]: A thorough guide for InDesign-to-EPUB publication is Elizabeth Castro, *EPUB Straight to the Point*. San Francisco: Peachpit Press, 2010. 

^[2]: http://daringfireball.net/projects/markdown/