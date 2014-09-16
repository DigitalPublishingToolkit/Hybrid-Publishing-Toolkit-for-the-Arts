# Guide: How to make a simple ePub

Focus: epub2/3, HTML5 (app) + PDF

<!--example Manifesto, El Lissitzky-->
    

## A simple e-book 
Flow chart: workflow <!-- Loes & Kimmy-->


## Direct conversion to ePub

![Simplest possible case](images/_in_progress/08_markdowntoepub_simple.svg "simple")

Making an epub doesn't have to be complicated. As the epub standard is open and based on HTML (the same format as web pages), there's a large and growing variety of ways to convert and export to an epub from different kinds of sources. For very simple publications, it may be possible to use a tool that directly converts your document to an epub.

Two popular conversion programs that can convert from a wide variety of input formats and produce epub's are ''pandoc''[] and ''ebook-convert''[^1](http://manual.calibre-ebook.com/cli/ebook-convert.html). 

For example, consider Charlotte Bronte's ''Jane Eyre,'' available from Project Gutenberg in a variety of formats (including epub). The ["plain text" version](http://www.gutenberg.org/cache/epub/1260/pg1260.txt), is the complete text of the book in a single file with no styling (no fonts, sizes, or bold etc).

TODO: Give simple example of using markdown + pandoc? to produce a simple epub.




##EPUB from scratch
The process of creating an EPUB from scratch is similar to developing a simple website. The main difference is that while websites can and often link to other websites, an epub is "self-contained", any pages that are linked to, or images that are displayed must be part of the collection. Creating an epub by hand is useful for creating small personal publications, or for making publications that explore the particularities of the epub format in detail.

An epub is a Zip archive typically named with the extension ".epub" instead of ".zip". The epub is a compressed collection of HTML files, stylesheets, and images, like the files found on a website, compiled together with some extra files that mark and structure the files so that an ereader can display them. Any file archiver that works with zip files (Archive Utility, The Unarchiver, WinZip, etc.) can open and decompress an epub file. In some cases, it might simply be necessary to rename the ".epub" with ".zip".

A rudimentary epub is used as an example to explain several of its concepts and may be [downloaded here]().

###Layout of an epub package

Decompressing an epub will reveal its directory layout and in that way make clear how an epub is set up. As explained above, the epub can be seen as a compressed Zip archive, looking as follows after unzipping it:

![Figure: EPUB layout](images/chapterabb_img "Figure: EPUB layout")

The *META-INF* and *OEBPS* directories and *mimetype* should always be present in an epub file and form a large part of what constitutes as an epub. 

*META-INF* contains an XML file (*container.xml*) which directs e-readers to an inventory (an .opf file) of all the files present in the publication.

*OEBPS* is the location where all the content (HTML files, images, audio, video, etc.) of the publication is stored, (nested) subcategories are possible but not mandatory. The .opf file (traditionally named *content.opf*) is important; this contains the metadata for the epub and is in turn referenced by the aforementioned *container.xml*. You might see another file with a .ncx extension (traditionally *toc.ncx*), it holds the hierarchical table of contents for the epub and is entirely optional as it isn't part of the epub specification.

The file *mimetype* contains a single line describing the epub file as `application/epub+zip`, this file allows e-readers to check whether the file is actually an epub and thus if they can read it.

These three components form the basic structure of an epub and are required in order for the file to be a valid epub.


###Creating your own epub

Most of the elements of an epub can be produced by hand in a text editor - not to be confused by a word processor like Microsoft Word or Apple's Pages. Popular text editors include BBEdit, TextWrangler or TextMate for Mac or NotePad++ and PSPad for Windows. Below follows a step by step process of creating a very simple epub.


####Creating the required files and directories

1. Create a directory to store the files and subdirectories for your epub in, e.g. *Example*;
2. Create two more directories inside the one you've just created, one called *META-INF* and the other *OEBPS*;
3. Using a text editor create a plain text file and add the line `application/epub+zip` to the file;
4. Save the plain text file, without a file extension, and name it *mimetype* alongside the two directories you created in step 2.

Now there are the two directories and one text file, like we saw when we decompressed the EPUB used as an example.


####container.xml

1. Again using a text editor, create a new file and save it to the *META-INF* directory with the name *container.xml*;
2. *container.xml* contains a simple structure written in XML. Below is a complete version of the document followed by an explanation of its separate parts. You may ignore the explanation without much consequence if its too technical in nature. The important part of this document is what's contained in between the quotes of the attribute `full-path` (*OEBPS/content.opf*). This attribute should point to an .opf file we'll create later on and will be stored in the *OEBPS* directory.<!--is het the attribute of the file die gestored gaat worden--/>


	```
	<?xml version="1.0" encoding="UTF-8"?> 
	<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"> 
		<rootfiles>
			<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
		</rootfiles>
	</container>
	```
	
	The first line is a `declaration statement` which should always be present in XML files. This is followed by the `container` which denotes that the publication is based on the *Open Container Format* as specified by the epub standard[^epub-standard]. The `rootfiles` tag denotes a collection of rootfiles, viz. the possible starting point(s) for e-readers to begin processing and parsing the content. In this case the rootfiles contains only one entry, called `rootfile`, this tag has two attributes - `full-path` and `media-type`. The first attribute holds the path to an inventory file (in this case *Example.opf*) containing metadata regarding the publication and its content. Finally, `media-type` is reaffirmation of the epubs mimetype.
3. Save and close *container.xml*.
	

####The OPF file

The OPF file is an important part of the structure of an epub. It is located in the *OEBPS* directory and contains the necessary metadata to accurately describe the publication, but also because it can contain the linear reading order which, in combination with the contents of *toc.ncx*, may be used by e-readers to build navigation menus or a table of contents. The OPF file is too long to be included verbatim in this document, but the most important sections are referenced below.

```
	<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"
		xmlns:opf="http://www.idpf.org/2007/opf"
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
		<dc:title>Example EPUB</dc:title>
		<dc:language>en</dc:language>
		<dc:identifier id="BookId">http://digitalpublishingtoolkit.org/ExampleEPUB.html</dc:identifier>
    	<meta property="dcterms:modified">2014-03-28T14:11:50Z</meta>
    	...
	</metadata>
```

The metadata section describes the current publication. It lists information such as the title, author, publisher, etc. Most of these entries are identical to what librarians use to catalogue publications. Parts of the metadata section are used by e-readers to organize collections.
	
```	
  <manifest>
    <item href="styles.css" id="css1" media-type="text/css"/>
    <item href="cover.png" id="cover" media-type="image/png" properties="cover-image"/>
	<item id="chapter1" href="Cover.html" media-type="application/xhtml+xml" />
	<item id="chapter2" href="Page-01.html" media-type="application/xhtml+xml" />
	<item properties="nav" id="toc" href="toc.html" media-type="application/xhtml+xml" />
    <item href="toc.ncx" id="ncx" media-type="application/x-dtbncx+xml"/>
  </manifest>
```

A manifest lists all the resources available in the EPUB package, with the exception of directories, the *mimetype* file, the contents of *META-INF* and the .opf file itself. A manifest file can be a pain to produce by hand for large epubs, as the list of resources utilised in the publication is bound to be long. Every resource has a unique `id` and should be referenced by a relative path in the `href` tag and described in the `media-type` attribute. The entry with the *cover.png* is of special interest, as the attribute `properties` describes the fact that the image may be used by e-readers as the cover image for the publication - e.g. for use in collection overviews.

```
  <spine toc="ncx">
  	<itemref idref="chapter1" />
  	<itemref idref="chapter2" />
  </spine>
```
Lastly, the `spine` lists all the pages present in the publication and it's listing arrangement tells an e-reader the linear reading order of the publication. The `spine` may only contain (X)HTML pages, not images or other content. The `toc` attribute refers to the `id`  of the `toc.ncx` in the manifest.
	

####The Content

As stated in the introduction of this section a large part of an epub is a collection of HTML files which are often interlinked. The process of creating the pages of an epub is similar to building a website, but with the particular limitations of e-readers in mind - limited support for rich media, colour, etc. An overview of the limitations can [be found here]().
Pages should be written in XHTML, a variant of HTML which was created to make HTML more extensible and increase the interoperability with other data formats. Cascading Style Sheets (CSS) may freely be used, though a lot of e-readers ignore or do not parse many of the style definitions.


####Packaging

Creating an .epub file is as simple as selecting both the *META-INF* and *OEBPS* directories and the *mimetype* file and creating a ZIP archive. This may be done by using the built-in archive utility of the operating system, or an external program like *The Unarchiver* (Mac) or WinZip (Windows) or a special purpose utility.[^epub-zip-unzip] Some of these programs create unnecessary (hidden) files inside the archive which might invalidate your epub. Most e-readers will safely ignore extraneous files, though parse the document properly. Validation of epubs can be done online using the [EPUB Validator](http://validator.idpf.org) or [a desktop application](http://www.pagina-online.de/produkte/epub-checker/). The .zip extension of the archive may then be renamed to .epub. This file can then be opened in an e-reader like Calibre, iBooks or similar applications.<!--mischien nog even uitleggen wat dat valideren dan is en waarom het er toe doet?--/>



[^epub-standard]: [http://www.idpf.org/epub/30/spec/epub30-ocf.html](http://www.idpf.org/epub/30/spec/epub30-ocf.html)
[^epub-zip-unzip]: [http://www.mobileread.com/forums/showthread.php?t=55681](http://www.mobileread.com/forums/showthread.php?t=55681)





