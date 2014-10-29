# 06 Towards a Hybrid Workflow Based on Markdown

Creating a workflow that is both structured and flexible enough to cater for the different choices made is a key step towards an efficient electronic or hybrid publishing strategy. The hybrid workflow we propose here is based on the need for publishing across different mediums, while keeping the majority of the work process in-house instead of outsourcing. 

First describing a more traditional workflow based on desktop publishing via InDesign with a print book as end result, we move to an ideally fitted workflow centered around the structural file format XML, ending with a Markdown-oriented workflow which is both easy to use and open to many possibilities. Following such a workflow will make the transition from a print-centered publication process to a digital and print - in other words: hybrid - publication process viable. 

Instead of producing a digital publication based on the printed book at the end of a production process, as is common practice by publishers, the workflow should be adjusted and made efficient and practical towards hybrid publishing at an earlier stage. From-scratch development of each publication format is thus replaced by single source multi-format publishing.

However, the description below starts at a point which in reality is not the beginning of the publishing trajectory, namely when an author hands in the definitive manuscript - so after the editing and rewriting process has passed through its final stages. Should the author already be working in Markdown, HTML or even XML format, this will change the workflow. However, in our experience manuscripts are mainly written in Microsoft Word and delivered in .doc or .docx.

Note: An important step preceding the publication trajectory lies in the formulation of the in-house style guide (see also [![Bloglink](images/dpt_blog_verwijzing.png)](http://networkcultures.org/digitalpublishing/2014/10/21/style-guide-for-hybrid-publishing/ "Link to blog post: Style Guide for Hybrid Publishing")), where authors and editors can find the requirements for the manuscript. This style guide must be adapted according to the hybrid workflow before starting any work on the manuscript itself. For example: specification of the required file format, structuring of the text (headers, styles), image specifications, et cetera. See the Guide per genres <!--Miriam: internal link needed, comment copy edit (Amy or Andre)--> for pointers regarding adjusting the style guide in this sense.

We will now turn to implementing the new workflow for small edition and low budget publishing houses. (See also for a step-to-step guide: [![Bloglink](images/dpt_blog_verwijzing.png)](http://networkcultures.org/digitalpublishing/2014/10/07/hybrid-workflow-how-to-introduction-editing-steps/ "Link to blog post: Hybrid Workflow How-To: Introduction & Editorial Steps"))

## E-publishing workflows: desktop publishing, XML, Markdown 
![Traditional Workflow](images/07_workflow_traditional.png "Workflow Traditional.")


![Traditional XML](images/07_workflowMarkdown.png "Workflow XML.")

<!-- links on the blog: 
* <a href="http://networkcultures.org/digitalpublishing/2014/10/08/markdown-to-indesign-with-pandoc-via-icml/">http://networkcultures.org/digitalpublishing/2014/10/08/markdown-to-indesign-with-pandoc-via-icml/</a>
* <a href="http://networkcultures.org/digitalpublishing/2013/08/30/docx-to-markdown-using-calibre-and-pandoc/">http://networkcultures.org/digitalpublishing/2013/08/30/docx-to-markdown-using-calibre-and-pandoc/</a>
-->

<!-- Silvio: This might be integrated with ICML import from pandoc to have structured text in InDesign to be used by the designer: <a href="http://networkcultures.org/digitalpublishing/2014/10/08/markdown-to-indesign-with-pandoc-via-icml/">http://networkcultures.org/digitalpublishing/2014/10/08/markdown-to-indesign-with-pandoc-via-icml/</a> -->

### Desktop publishing workflow (from Word to InDesign to digital)

Desktop publishing for a lot of publishers presents the current situation: a Microsoft Word file is imported into InDesign and, after designing and editing, exported to PDF, ready to be printed. The traditional, print-oriented workflow can be seen as standard for one-to-one publications: the print book is translated to an electronic version, following the 'original' as close as possible. 

There are certain advantages to this workflow: it is simple, linear, there are no version branches, you end up with one consolidated manuscript, and What You See Is What You Get when it comes to design. For example, in the case of a print design where the page is fixed, changing hyphenation is a laborious process as hyphen indications need to be inserted manually in the InDesign document. <!-- Miram: maybe this is not formulated very clearly, but there needs to be some explanation here --> However, in digital publishing, hyphenations are not fixed, but will be subject to change as they shift according to the aspect ratio and screen size of the device used. So when an editorial correction involves a hyphenation, this need not be adjusted in the digital file. However, this workflow of course also means a limitation in electronic design possibilities. 

The main disadvantage of the DTP workflow is that you only target one medium and the steps to go from here to digital are cumbersome, and do not make full use of the potential in electronic publishing. A workflow with the paper publication as its basis generally tries to translate print into the digital books, keeping the workflow one-dimensional instead of multi-dimensional. 

Importantly, going from InDesign to an electronic publication is not ideal, especially when working with older versions of the software [![Bloglink](images/dpt_blog_verwijzing.png)](http://networkcultures.org/digitalpublishing/2013/05/21/epub-development-in-adobe-indesign-cs6/ "Link to blog post: NOTES ON EPUB DEVELOPMENT IN ADOBE INDESIGN CS6"). The results can be messy in terms of cleanliness of the code and may require extra steps in finalising the publication. InDesign, in its current state, is simply not optimised as a hybrid publishing tool, as it is (too) specifically developed for print design.[^EPUB Straight to the Point] The latest version of the InDesign suite (InDesign CC) is catered more to electronic publishing, but requires very careful structuring and preparation of documents in order to yield good results within manageable work times. It's best suited for projects where the content is generated from databases, imported as XML into InDesign and from there exported to EPUB. For a detailed look at these developments, see XXXXXXX Elisabeth Castro. <!--Margreet: chapter will be added by Liz Castro--> 

In the same way Microsoft Word (or any other text editor that uses a similar approach, for instance Open Office) is not well suited for processing structured text. When working with structured text the author is expected to wrap elements (a heading to emphasise words) in tags, word processors generally apply a visual style to a text, without bothering with tags or any other form of structure. To a certain extent these text processing programs allow working in a structured manner, by using stylesheets which determine for instance different types of headers. The problem is that they do not separate between formatting and structure, while in the world of digital publishing this is especially important.

It is possible to create 'interactive' publications in PDF, working with Microsoft Word and InDesign. In the end however these are also static InDesign documents, upgraded with some interactive layers. This is still a limited vision of what the possibilities are for digital publishing. The second workflow, which centers on the file format XML, does precisely that.

###From Microsoft Word (.docx) to EPUB

There is a viable solution for generating EPUB from Microsoft Word files, using the command line tool pandoc (for more information visit the [Pandoc](http://www.johnmacfarlane.net/pandoc/ 'pandoc website') [^Pandoc] website). The latest versions of pandoc (see below<!---insert cross-reference-->) support document conversion from '.doc' files generated by Microsoft Office 2007 or later, or by comparable programs like OpenOffice/LibreOffice. Since Word does not, as explained above, enforce good structure in a document, the EPUB generated by pandoc will never be perfect and ready for publishing. But it is still a clean enough, usable basis for a designer to produce a the final ebook. Other Word-to-EPUB programs, such as the built-in document converter of Calibre [![Bloglink](images/dpt_blog_verwijzing.png)](http://networkcultures.org/digitalpublishing/2014/03/28/converting-a-docx-directly-to-epub-using-calibre/ "Link to blog post: Converting a DOCX directly to EPUB using Calibre"), produce worse results. <!-- Marc: Needs a reference, I believe. -->

In order to obtain the best possible EPUB file, the Word document should be formatted, solely if possible, with Word's standard paragraph styles such as 'Normal', 'Title', 'Subtitle', 'Quote' and most importantly 'Heading 1', 'Heading 2',  'Heading 3'  for the headings according to their logical hierarchy. For example: 'Heading 1' for chapters, 'Heading 2' for sections, 'Heading 3' for subheadlines. The resulting EPUB document will contain a well-structured table of contents and document navigation menu based on the 'Heading' hierarchy, so well structured headings are of paramount importance. Word footnotes will be appear as linked endnotes in the EPUB, elegantly simplifying an otherwise tedious document redesign task.

Word unfortunately lacks two features that would make it more suitable for hybrid publishing projects:
1). Word does not have a 'strict mode' that would force all writers and editors of a document to only use defined paragraph styles instead of manually formatting. This means, your document will likely contain headlines that haven't been defined as headlines, but are just bold-faced text, quotes that haven't been defined as quotes etc. Unfortunately, if the manual formatting looks the same as the predefined paragraph styles, it is hard to impossible to spot these parts of a text.
2). Word provides no automatic or semi-automatic tools to find manual formatting and replace it with predefined paragraph styles. The only way to achieve this is to manually control and adjust the whole document. 

Often, such inconsistencies in a Word document will only become visible after the EPUB conversion, for example as a missing chapter headline in the table of contents of the electronic book. These are the inherent risks and limitations of using Word in the editorial workflow. Nevertheless, the Word + pandoc solution will likely be the easiest and least painful solution for publishers to adopt. <!-- Florian: We absolutely need to provide a dead-simple GUI or web tool for dropping a Word file to pandoc and obtaining EPUB + Markdown. @Michael and Marc, are you able to create this?-->

We recommend two ways of working with Word + pandoc, and discourage a third one:

1. Direct conversion from Word to EPUB using pandoc. This will require that the Word document is 100% consolidated and no further editorial changes will be applied to it. A graphic designer can take the converted EPUB document and quite painlessly transform it into the final electronic publication (among others, by changing the typographic design to make it suitable for ereaders, by scaling and optimising images for screen reading, by adding bibliographic metadata etc.). 
2. Conversion from Word to Markdown using pandoc. Since pandoc can also convert files _to_ the Markdown format, this often preferable, especially for complex publishing projects. The resulting Markdown file can then be used as the master file for conversions into all kinds of other file formats (such as HTML for websites). Converting to Markdown yields the advantage that any formatting glitch that existed in the Word document becomes clearly visible. For example, a headline erroneously formatted as bold standard text will show up as '\*\*headline\*\*' while a properly formatted headline will show up as '\#'. This makes it much easier to clean up the internal formatting of the document and have a clean master file for all subsequent document conversions. The EPUB file generated from this Markdown file would in most cases be better structured than the EPUB file directly generated from the Word file, and make the subsequent work of the designer easier. It is also possible to customise pandoc with conversion style templates. This even makes it possible to automatically generate complete and well-formatted EPUB files from the Markdown files without hiring a designer, depending on the type of publication. 
3. Not advisable: Using pandoc to go back and forth between Word and EPUB. If the Word document is not consolidated, but subject to further editorial changes, conversion to EPUB (like in the first scenario) would have to be done again, and destroy all work of the designer on the previously exported EPUB file. 
 

###From InDesign to EPUB


####Intro
InDesign is an excellent tool for creating and managing print projects. It also has a powerful EPUB production tool that has continuously improved over time. Its omnipresence and importance in print make it an obvious choice for projects that have both a print and electronic output. It is so powerful that it's useful even if print isn't part of the equation—though cost considerations might preclude its use if print is never a requirement.

InDesign can generate both flowing and fixed layout EPUB files. Flowing EPUB is characterized by text and images than can adapt to fill any size screen and which can be enlarged or shrunk to suit the preferences of the reader. Fixed layout EPUB features text and images that are always shown in the same positions on a page, regardless of the size of the screen. Indeed, they are often reduced in size to fit on smaller screens and are often barely illegible on mobile phones. Finally, flowable EPUB is better supported by a larger range of ereaders, fixed layout is available in only a few. 

InDesigns print features—including master pages and the control of headers and footers, and precise positioning of elements and text—are ignored in flowable EPUB documents. Flowable EPUB does permit choosing (initial) font-size, leading, font, space before and after a paragraph, whether a paragraph should begin on a new page, and more, though the reader may be able to partially or completelly override these settings in individual ereaders. 

You can use InDesign just for EPUB production and not print. In this case, you can simply ignore how the book looks in print and focus on generating flexible EPUB documents that look good across a range of ereaders.

Underneath is a very short guide and InDesign is a very complex and complete software package. There are many more options than those described here.

####Styles 
One of the most effective tools that InDesign offers is the ability to identify different kinds of paragraphs (headers, subheaders, body text, captions, etc)  and apply a whole set of formatting rules to them—called a 'style'—in one fell swoop. These styles can later be exported into EPUB in CSS format, enabling subsequent editing and adjustments, if necessary, in order to adapt to a range of different ereaders and/or offer a different look than in the print document.
You must first create styles, then apply them, then make sure they are properly mapped for export to EPUB.

**Creating styles**

1. Open the Paragraph Styles panel and click the New Style button to create a new style. Any formatting in the active paragraph is incorporated automatically into the new style. 
2. Give the style a name.
3. Choose any additional options from the boxes at left, and save.

Tips: You can also create Character Styles for applying formatting to just a selection of text rather than an entire paragraph. 
Applying all formatting with styles instead of local formatting improves reliability across ereaders and facilitates later editing. 


**Apply styles**

1. Click in a paragraph that you want to style.
Choose the desired style from the Paragraph Styles panel that you wish to apply.
2. Repeat for every paragraph in the document.

Tips: You can style all of the text at once by selecting all and then choosing the Body style. Then apply the less frequent headers and captions and other paragraphs individually.
If you have imported a document with large quantities of existing bold or italic text, you can search and replace to automate applying the character style.


**Map styles to tags**

1. Though InDesign can do this step automatically, you can precisely specify which Paragraph Styles should be mapped to which tags in the resulting CSS to get more control.
2. Choose Edit All Export Tags from the Paragraph Styles Panel menu. 
3. In the dialog box that appears, verify that each style is mapped as desired to the appropriate tag. It's a good idea, for example, for header paragraphs in your book to be output as h1, h2, etc. and for each style to have its own class. 
Tips: If you import XML documents, you can have InDesign automatically map specific XML tags to the desired Paragraph Styles (which later will be mapped to the proper EPUB CSS tags as above).
Earlier versions of InDesign were not as good at exporting all of its styles to CSS. CC is substantially better.
You can apply your own CSS in addition to or in substitution of the formatting from the styles from InDesign through the Export Options dialog box.

####Images
InDesign has three kinds of images: inline, anchored and independent.
 
Inline images are placed or pasted directly within the text. When exported, they are rasterized (and thus if any inline objects contain text, this text is also rasterized), and exported in the flow of the text in which they are placed. Inline images cannot be wrapped with text.

Anchored images are tied to a particular part of the text, and when exported to EPUB will appear just before that text in the code. Anchored images can have text wrapped around them and are properly exported as floating objects in EPUB. Text within anchored groups of objects is not rasterized, but sometimes resizes incorrectly in ereaders.

Independent images are placed on the page adjacent to text and other objects, without any explicit link between the two. InDesign exports text and and independent image objects sequentially according to their location on the page, starting with those objects that are farther up and to the left. Because an entire story is exported before other objects   on the same page, images may often appear several pages after the text in the EPUB than they did in the print version. The order of exported objects can be adjusted in the Articles panel.  

**Anchoring images**

Generally, it's more effective to use anchored images with text that will be exported to EPUB. This gives you more control over where the image appears in the exported EPUB and also permits the use of text wrap. 

1. Place an image on the pasteboard. If desired, you can create a caption, style the caption, and then group the caption with the image
2. Select the image to make its controls visible.
3. Drag the blue box in the upper right corner of the image to the desired location in the text.
4. If the print output is important, adjust the location of the image. This does not affect the image's location in the EPUB. 
5. If you want text to wrap around the image, select the image and then choose Object > Object Export Options.
5.1. Display the EPUB and HTML options panel.
5.2. Check the Custom Layout option and then choose Float Left from the menu. 
5.3. In order to specify the desired amount of space between the image and the text, choose the image, display the Text Wrap box, click the second option, and specify the amount of space in each box. You might also want to do this to adjust how the image appears in the print edition.


**Links and cross references**

One of the main advantages of ebooks over print is that they can contain to additional information, whether it be in the same book, or on a web site somewhere out on the internet. InDesign makes it easy to incorporate links into your ebook.

There are two principal kinds of links: links in which you specify both the destination and the link text, and links that get the link text automatically from the destination. This second kind of links are called cross-references. It's a good idea to apply a character style to all kinds of links.

**Creating links within a book**

1. Create the destination by selecting the point in the book where you want the link to point to, and then choosing New Hyperlink Destination from the Hyperlinks panel menu. Note the name of the Text Anchor, you'll need it later. It's usually the first few words of the destination text.
2. Select the text that you want to convert into a link and choose New Hyperlink from the Hyperlinks panel menu.  
3. Choose Text Anchor next to Link To:, choose the Document that the destination is in and then choose the name of the Text Anchor. It's a good idea to apply a style so that you can format all links later.
4. Click OK to create the link.


**Creating cross references**

1. Cross references are links in which the text you click on is automatically generated from the text in the destination. A typical example for cross references is when you want to link to a different chapter or header name. You can tell InDesign to always use the most up to date text in the Header.
2. To create a cross reference, place the cursor in the text where the link will go.
3. Choose Window > Type & Tables > Cross-References to view the Cross-References panel. 
4. Choose Insert Cross-Reference.
5. Choose the desired document and then the kind of paragraph that you want to link to in the left half of the box. The specific paragraphs tagged with that style will show up on the right so you can choose the one you want for the cross-reference.
6. Select a Format for the Cross-Reference, and click OK.
7. The text from the destination appears in the body of your document. It will be exported as a link in the EPUB document. 


**Table of Contents**

Ebooks have two different kinds of tables of contents, the conventional one that is part of the text, just like any other chapter in your book, but with links to the remaining chapters and sections, and one that is accessed through the menus of the user's ebook reader regardless of which page they're looking at at the moment. InDesign facilitates the creation of both types. 

InDesign generates tables of contents from styled paragraphs. For example, you might want to create a table of contents with all of paragraphs marked with the Heading 1 and Heading 2 styles, or as in this example, with just all of the ChapName elements.


**Creating a Table of Contents Style**

1. Choose Layout > Table of Contents Styles and then click New in the dialog box that appears.
2. Give the table of contents a name, like "Contents" and choose the paragraph style that should be applied to that header in the book. 
3. Choose the kind of paragraphs that should be used to populate the table of contents, like headings or chapter names.
4. Click More Options if it's not already chosen.
5. In the center area, choose the style that should be applied to each kind of element in the table of contents. It's a good idea to create special styles to be applied to these elements.
6. Choose No page number in the Page Number box since these are not necessary in an ebook.
7. Click OK to save the TOC Style. This is the first step to creating both a navigational and in-document table of contents.


**Generate the in-document table of contents**

1. Once you've created a TOC Style, choose Layout > Table of Contents to have InDesign generate the table of contents by extracting the text from the paragraphs marked with the styles you selected.
2. With the "loaded" pointer, place the table of contents in the desired location of the document. You don't have to put the table of contents at the front of the book, or indeed include it all. 

You'll learn how to generate the navigational table of contents in the Export Options section of this guide.

Tips: If you export a multi-document book to EPUB and don't create a Table of contents style, InDesign automatically creates a TOC based on the file names of the individual documents in the book. If you export a single document book to EPUB, InDesign will not automatically generate a table of contents.
You can create a navigational table of contents or an in-document table of contents or both. Most ereaders will throw an error if the navigational TOC is not present. Some ebook stores will complain if you don't include an in-document TOC. 


**Metadata**
Metadata is information about your book, including the names of the author and other creators, the publisher, date of publication, subject matter, and more. It's a good idea to provide as much metadata as possible to make it easy for prospective readers to find your book.  

InDesign gives you two opportunities to add metadata, in the File Info dialog box and when you export your file to EPUB. The two sets of information overlap but are not identical. Further, only empty fields are overwritten by data in the other system. 

1. Go to File > Info to add metadata to your file about the name of your publication, the author, a description, keywords, and copyright status. 

You can add additional metadata as you export the document to EPUB as discussed further ahead. 


**Cover**
The final step before you export to EPUB is to create and add a cover for your ebook. Because ebook covers are often viewed at small sizes, it's important to have large, clear text and to preview the cover at icon size. Most ebook stores ask for images that are at least 1000 pixels on the shortest side. 

1. Save the cover image as a JPEG.

You specify the cover image when you actually export to EPUB in the next section.


**Export options**
Before exporting to EPUB make sure that all formatting is applied with styles, all images are properly placed and anchored, you've created all the links needed, there is a defined Table of Contents style, you've specified as much metadata as necessary and desired, and you've created a high-resolution cover image that can be viewed adequately at small sizes. 

1. Start by choosing File > Export and then choose a filename and destination, and EPUB (Reflowable) in the Format menu. Click OK. The EPUB - Reflowable Layout Export Options box appears with eight separate panels of options.
2. In the General panel, choose EPUB 3.0 next to Version to ensure your document is up to the latest standards.
3. Select Choose image next to Cover, and then click the folder to select the desired cover image that you created earlier. If you choose Rasterize Front Page, InDesign creates a screenshot of the first page of your book and uses that for the cover. 
4. Next to Navigation TOC choose Multi Level (TOC Style) and then choose the Table of Contents Style that you created earlier in the TOC Style menu.
5. Click the Metadata panel
6. Insert the book's ISBN in the Identifier field, if it has one.
7. All the other fields besides the Date field should be automatically populated with data entered in the File Info box earlier. You can add any missing information now. InDesign uses the information in the Date field for the EPUB 2.0 dc:date element but will always automatically set the EPUB 3.0 compatible date format with the export date and time. In other words, you don't have to put anything in the Date field.

There are many other export options, for controlling the way images and text are exported, for adding JavaScript and CSS, and for choosing how the ebook should be previewed. Explore these at your leisure. The CSS is possibly Liz Castro her favorite option since it allows you to override or even completely substitute the sometimes bulky and awkward CSS generated by InDesign with your own carefully crafted CSS. 

8. Finally, click OK to generate the EPUB file. 


**Testing**
Be sure to test the EPUB file in as many ereaders as possible. You can use Kindle Previewer to open the EPUB in a Kindle simulator and/or to convert the EPUB to Kindle format so that you can test it on actual Kindle devices.


**Validating**
It's always a good idea to validate your EPUB documents with ePubCheck [^EpubCheck] before you release them.





### XML 
<!-- Marc: This first paragraph is unclear. XML is not a 'document format' but it's a 'general document format'? Also the whole section appears to be a bit opinionated and lacking references, without providing references (messy XHTML?). -->
The most detailed structuring language developed is XML. It is often confusing for people to understand what XML is because it is not really a document format of its own, but a general document format with which other, specific document formats can be created. HTML (or XHTML), or example, is one XML-based document format, Microsoft Words' .docx is another.

XML is meant for structured documents that clearly separate logical structure from visual formatting, but it has two limitations; 1). since any document format can be constructed with it, messy formats like .docx and .xhtml can be constructed with it, too; 2). because it is itself a toolkit (or actually: a syntax) for defining document formats, it is very complex and quite difficult to work with. 

An XML document works like an archive: from this single document it is possible to create multiple output for different media. Thus, a misspelling or another error is changed in the XML document, which is then used to recreate the output to the different media. Formatting is done in a second step, with for instance **Cascading Style Sheets** (CSS). 

While XML theoretically presents the ideal way of working with single format files which deliver multiple output formats, we do not present it as the most advisable solution for small, independent publishing houses. Because XML is so detailed, with a very complex syntax and hard-to-use software tools, it is difficult to work with.

A good example how to practically use XML for electronic publishing in daily life is demonstrated in our chapter on using InDesign for hybrid paper and electronic publishing. <!--Miriam: this needs adding. Use example -->
<!-- Pia: maybe for the laymen show what xml looks like?-->

### Markdown 

Central in a hybrid publishing workflow, we recommend to use the mark-up language Markdown, as it is an easlier language to use than XML. Markdown is not perfect, but is the most easy to work with and enables the creation of structured texts, thus allowing for hybrid publishing.

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

<!-- Margreet: Would it be possible to also present the result in a visual, like if one is using Mou or Macdown? -->

A short breakdown: '#' signifies a top-level headline, '##' a second-level headline, '_' italic text, ' ** ' bold text, '>' a block quote. Beyond that, Markdown provides conventions for marking up bold text, lists, embedded images and links. Its popular extension **MultiMarkdown** also supports footnotes, tables, mathematical formulas, cross-references, bibliographies and definition lists. With simple open source converter programs, Markdown text like the above can be automatically translated into well-structured HTML, EPUB, PDF, RTF (for importing into InDesign) and other document formats, with a single mouse click or keyboard command, requiring no manual adjustments. <!-- Margreet: Should be take about 'keyboard commands'? Is this clear for a publisher? -->
<!-- pia: clear enough for publishers-->

Markdown is a child of Internet culture. It standardises ad-hoc formatting signs used in e-mail and chats, and became popular in blogging software. There are similar plain text formatting languages to Markdown: the Wiki syntax used in Wikipedia, the language _Textile_ that is used for a number of web content management systems and the language _reStructuredText_ used for writing technical manuals, and many others. 

Markdown and its siblings are human-readable, human-friendly well-structured document formats, excellent for long-term storage and as the basis (or source code) for conversions into present and future document formats. While they are simple, they are also both strict and unambiguous enough in their formatting syntax that multiple writers and editors can work on a single document without introducing weirdness <!-- Amy: What do we mean by 'weirdness'? Can this be more specific? --> into its formatting. Another advantage of Markdown can be written and edited in any computer program capable of processing basic text. Unlike the file formats of Microsoft Word or other classical word processing programs, the file containing the Markdown flavoured text is not bound to specific software, it can be opened using the simplest applications able to parse text.

Why do we recommend Markdown in particular? For particular publishing projects - for example, handbooks or books derived from Wikis, it can be worth considering one the alternatives to Markdown such as _reStructuredText_. There are, however, two reasons why we recommend Markdown as a practical tool for electronic and mixed media publishing:

1. Excellent software support. As the most popular human-readable plain text formatting language, there is a plethora of user-friendly, high quality software for writing and editing documents in Markdown and for converting it into other formats available. While Markdown can be written and edited in any computer program that allows to edit text, there are a number of very user-friendly text programs that make it easier to write and view, think of Mou, Macdown, Texts, MarkdownPad, UberWriter or MdCharm.

2. With Multimarkdown (an extension of Markdown), it provides all the necessary formatting and document syntax needed in arts- and humanities-oriented text publishing. It is perfectly possible to write, for example, a cultural studies Ph.D. thesis in Multimarkdown, or the essay part (complete with footnotes and bibliographical references) of an exhibition catalog.

Markdown/MultiMarkdown is however not a magical one-size-fits-all solution. It is well suited for text-heavy editorial work, but limited when creating visual documents and not really usable for interactive publishing formats. It is also not a layout tool, but a pure manuscript format, excellent for keeping manuscripts in a well-structured, readable, durable, software-independent format. 

Markdown and similar formatting/markup language are meant for workflows in which there is a clear separation between editorial work - involving writers, translators and editors - on the one hand and publication design on the other. For publications requiring lots of interaction between writers/editors and visual designers/artists from the very beginning of the authoring process, these document languages are not the right tool. 


<!-- here. 12 sept.  who is this?  asks Miriam-->
<!-- But which ones should be used then? -->

<!-- Marc: XML again? This section is also highly opinionated and not referenced. Should this be merged with the previous XML section if possible? -->
#### Markdown versus XML

Markdown, and similar human-readable plain text markup languages could be called a 'poor man’s XML'. To summarise XML is complexity hell even by the measures of computer science. It is the holy grail of document processing, and has been deployed by large scale publishers (especially in the academic field) very successfully. For small to medium publishers, it is often overkill. Markdown provides a good middle-of-the-road solution of a format that is easily usable for non-technicians yet much better structured, and a basis for easy document conversion into HTML, EPUB and many other formats, than Microsoft Word and similar classical word processing programs.

Technically speaking, Markdown provides some of the same features and advantages, namely separation of content structure from visual layout, painless translation into multiple output formats. Their relative simplicity and human readability comes, however, at the price of extensibility and universality. XML is, strictly speaking, not a document markup language, but a meta-language (or toolkit) for building domain- and application-specific markup languages such as: a document markup language for exhibition catalogues, a document markup language for restaurant menus, a document markup language for flyers, etc.

Markdown & Co. do not provide this flexibility of building one’s own syntax, but provide only their built-in, hard-wired syntax. For example, if one needs syntax for encoding footnotes and endnotes, MultiMarkdown simply doesn’t provide it. One could think up and use one’s own syntax extension (for example ^^[1] for an endnote), but this would not be supported by the word processing and text conversion programs for Markdown. In XML, there are standard methods of declaring and extending markup languages that can automatically be picked up by XML document converters.

<!--Amy: Seems like there's a lot of repetition in this section: do these last two paragraphs need to be in? -->

However, the declaration of these extensions in the document syntax and conversion rules is highly complex. Even for computer scientists and engineers, XML is often so over-complex that they have resorted to simpler, human-readable language like Markdown, ReStructuredText and ASCIIdoc for software manuals.

They are not as universal and thoroughly structured as XML, but still provide the advantage of separating content structure from visual layout, along with the advantage of painless translation into multiple output formats. And lastly, XML has very complex markup that is hard to read and write for humans. Easy authoring tools for XML and any kind of XML-based document formats do not really exist yet.

#### Practical tips and tricks for working with Markdown 

##### Word Processing / editing programs

For Apple's Mac OS X and iOS, there are nice and very user friendly programs for editing in Markdown. <!--Margreet: What about Windows and Linux. Miriam: I added a Windows option, plus the open source Macdown. I think we should not name all these options but make a choice, for example only name the free ones? Otherwise, what is the criterium? -->

**Linux**
- [UberWriter](http://uberwriter.wolfvollprecht.de) [^UberWriter], this editor also includes built-in support for pandoc
- [MdCharm](http://www.mdcharm.com) [^MdCharm], supports MultiMarkdown

**Mac**
*Freeware:*
- [Mou](http://www.mouapp.com) [^Mou], with features like live preview, sync scroll, auto save, powerful actions, auto pair, custom themes and CSS, HTML and PDF export, enhanced CJK support and more.
- [MacDown](http://macdown.uranusjr.com/) [^MacDown], released under the MIT License and influenced in design and setup by Mou.

*Paid*
- [ByWord](http://bywordapp.com) [^ByWord], a user-friendly, distraction-free text writing program with built-in MultiMarkdown support and export to HTML, RTF, PDF and Microsoft Word. The program runs on Macs, iPhone and iPad.
- [iA Writer](http://www.iawriter.com/mac/) [^iA Writer], a program similar to ByWord. The program runs on Macs, iPhone and iPad.
- [Scrivener](http://www.literatureandlatte.com/scrivener.php) [^Scrivener], a word processing program popular among professional writers, for Mac OS X and Windows. Fully supports MultiMarkdown internally

**Windows**
- [MarkdownPad](http://markdownpad.com/) [^MarkdownPad], free for personal use, with upgrade to MarkdownPad Pro to unlock additional features.


##### Document conversion programs
- [MultiMarkdown](http://fletcherpenney.net/multimarkdown/) [^MultiMarkdown], the original program converts MultiMarkdown files into HTML, PDF, OpenDocument (for later conversion into RTF or Microsoft Word). Open Source, runs on Linux, Mac OS X and Windows.

- [Pandoc](http://johnmacfarlane.net/pandoc/) [^Pandoc], similar in functionality to multimarkdown, but much more powerful. Pandoc reads more input formats (including HTML and reStructuredText) and can output HTML5, XHTML, LaTeX, RTF, Word, EPUB 2 and 3, PDF and many more. Typographic templates for the conversion can be easily customised. 

- [Calibre](http://calibre-ebook.com/) [^Calibre], application suite that allows users to manage ebook collections as well as to create, edit, and read ebooks. It supports a variety of formats (including the common Amazon Kindle and EPUB formats), ebook syncing with a variety of ebook readers, and conversion (within DRM restrictions) from different ebook and non-ebook formats. Open Source, runs on Linux, Mac OS X and Windows.

Pandoc is the tool we recommend for working with Markdown, and has also been extensively used in creating this publication.

<!-- Marc: This is a very practical section all of a sudden. Maybe relocate it to another part of the toolkit? -->

##### Cleaning up Markdown

Since Markdown is a document format and not a word processing program, it does not offer functions like automatic renumbering of footnotes and list items during text editing. In fact, such numbers don't matter since everything will be renumbered during the document conversion anyway. 

However, to also make the Markdown text source coherent and tidy, pandoc can be used to clean it up. The trick is to tell pandoc to convert a document from Markdown to Markdown:

    pandoc -f markdown -t markdown --output markdown-document-clean.txt markdown-document.txt
    
   <!--Pia: why? what happens?--> 

##### A note on limitations

A major downside of Markdown is that it exists in several variants, each with their own extensions of the basic Markdown syntax. In the context of this Toolkit, we recommend the widespread variant 'MultiMarkdown' that includes syntax for footnotes, tables, citations, cross-references, image captions and document meta data. It is also fully supported by pandoc, the recommended software tool.

Another downside is that Markdown allows some formatting to be marked up in different alternative ways (for example, underlines or asterisks for italic text) which can introduce inconsistency in a collaboratively edited document. The trick mentioned above, to use pandoc for converting from Markdown to Markdown, can be used to eliminate such (visual) inconsistencies in a master document. 

At the time of this writing in late 2014, a controversial standardisation effort of Markdown and its extensions is underway, under the name 'CommonMark'. [commonmark-controversy](http://blog.codinghorror.com/standard-markdown-is-now-common-markdown/) [^commonmark-controversy] We will update this Toolkit as soon as CommonMark has been standardised, released, and is supported by the software we recommend.


## Database publishing 
What is gained by a shift to a hybrid publishing workflow? First of all, producing a publication with the possibility to have multiple output formats will be more efficient. However, when the workflow is put into use without restraint and when you really 'change your life', great possibilities will open up. The most important option is shortly discussed here, namely database publishing which uses a so-called content management system.

The ideal database is a collection of independent, but mutually related, objects. These objects can be everything from structured text to pictures of wildlife. The issue at stake is that we need clear grammatical and categorization systems that go beyond the immediate use of the database. Take as an example your mailing list. We can take the full address including the name of the person as one object. But if we want to select per postal code or any other sub category in a full address or want to add more information to the persons name, such as age, email address and previous purchases, we have to make a strict scheme with so-called fields and sub-fields, including their interdependences (a house number demands a street name and vice versa), their indispensability (age might be not crucial), and so on.
What this means is that the holy grail of the all encompassing database is not only almost impossible but also an extremely time consuming operation to build and maintain. 

The best option is therefore to explicate the goals of the publication programmme as well as the practical limitations. The four genres we discuss in this publication all have their own demands in relation to the creation and the dissemination of publications. An art catalog demands clear descriptors about the artist, the materials used, the sizes, the provenance, copyright, keywords according to established list, etc. Other collections of pictures might only need a subset.   

Also in pure text databases we have to be careful. On the one hand we have obviously the data related to the author's name, affiliation, address, etc. But it becomes a different discussion if pictorial illustrations, graphs, etc. are shared between look-alike publications and for that reason we want to identify these objects individually. If such is the case, we might consider a special sector in our database that pertains to illustrations and their specific descriptive sub-field only. The same holds true for bibliographic references and the collection of hyperlinks used in the text.

In conclusion, we can only advise that various objects or in other words pictorial or textual entities are provided with as many consistent metadata (field descriptors) as possible. 






[^EPUB Straight to the Point]: Elizabeth Castro provides a thorough guide for InDesign-to-EPUB publication in her book: EPUB Straight to the Point, San Francisco: Peachpit Press, 2010. 
[^Pandoc]: Pandoc a universal document converter, http://www.johnmacfarlane.net/pandoc/.
[^UberWriter]: UberWriter, http://uberwriter.wolfvollprecht.de/.
[^MdCharm]: MdCharm, http://www.mdcharm.com/.
[^Mou]: Mou, http://25.io/mou/.
[^MacDown]: MacDown, The open source Markdown editor for OS X, http://macdown.uranusjr.com/.
[^ByWord]:ByWord 2, http://bywordapp.com/.
[^iA Writer]: iA Writer, http://www.iawriter.com/mac/.
[^Scrivener]: Scrivener 2, http://www.literatureandlatte.com/scrivener.php.
[^MarkdownPad]: MarkdownPad, http://markdownpad.com/.
[^MultiMarkdown]: MultiMarkdown, http://fletcherpenney.net/multimarkdown/.
[^Calibre]: Calibre ebook management, http://calibre-ebook.com/.
[^commonmark-controversy]: Jeff Atwood, 'Standard Markdown is now Common Markdown', Coding Horror, 05 Sep 2014, http://blog.codinghorror.com/standard-markdown-is-now-common-markdown/.
[^EpubCheck]: EpubCheck is a tool to validate IDPF EPUB files, version 2.0 and later. https://github.com/IDPF/epubcheck

<!--Amy removed it as it didn't appear in text
[^2]: http://daringfireball.net/projects/markdown/
-->

