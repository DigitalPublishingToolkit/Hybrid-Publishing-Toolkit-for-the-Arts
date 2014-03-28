##EPUB from scratch

Part of the process of creating an EPUB by hand is very similar to developing a simple website. The EPUB file format is basically a compressed collection of HTML files, compiled together with some extra files containing descriptive markers regarding the content of the publication. A typical EPUB file is just a Zip archive without the .zip file extension, which is instead substituted by .epub. A file archiver can easily decompress EPUB files, although the user sometimes has to replace the .epub extension with .zip in order for the file archiver to recognise the EPUB as a compressed archive.

A rudimentary EPUB is used as an example to explain several concepts and may be [downloaded here]().


###Layout of an EPUB file###
After decompressing an EPUB the following directory layout is revealed:

[[Screenshot of directory layout]]

The *META-INF* and *OEBPS* directories and *mimetype* should always be present in an EPUB file and form a large part of what constitutes as an EPUB. 

*META-INF* contains an XML file (*container.xml*) which directs EPUB readers to an inventory (an .opf file) of all the files present in the publication. 

The file *mimetype* contains a single line describing the EPUB file as `application/epub+zip`, this file allows EPUB readers to check whether the file is actually an EPUB.

*OEBPS* is the location where all the content (HTML files, images, audio, video, etc) of publication is stored, (nested) subcategories are a possibility but not mandatory. One file is important. it has an .opf file extension (traditionally named *content.opf*) and contains the metadata for the EPUB, this file is in turn referenced by the aforementioned *container.xml*. You might see another file with a .ncx extension (traditionally *toc.ncx*), it holds the hierarchical table of contents for the EPUB and is entirely optional as it isn't part of the EPUB specification.


###Creating your own EPUB###
Most of the elements of an EPUB can be produced by hand in a text editor. Popular text editors include BBEdit, TextWrangler or TextMate for Mac or NotePad++ and PSPad for Windows. Below follows a step by step process of creating a very simple EPUB.


####Creating the required files and directories####
1. Create a directory to store the files and subdirectories for your EPUB in, e.g. *Example*;
2. Create two directories, one called *META-INF* and the other *OEBPS*, inside the one you've just created;
3. Using a text editor create a plain text file and add the line `application/epub+zip` to the file;
4. Save the plain text file, without a file extension, and name it *mimetype* alongside the two directories you created earlier;


####container.xml####
1. Again using a text editor, create a file inside the *META-INF* directory and name it *container.xml*;
2. *container.xml* contains a simple structure written in XML. Below is a complete version of the document followed by an explanation of its separate parts. You may safely ignore the explanation if its too technical in nature, the important part of this document is what's contained in between the quotes of `full-path` (*OEBPS/content.opf*). This attribute should point to an .opf file we'll create later on and will be stored in the *OEBPS* directory.

	```
	<?xml version="1.0" encoding="UTF-8"?> 
	<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"> 
		<rootfiles>
			<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
		</rootfiles>
	</container>
	```
	
	The first line is a 'declaration statement' which should always be present in XML files. This is followed by the 'container' which denotes that the publication is based on the *Open Container Format* as specified by the EPUB standard[^epub-standard]. The `rootfiles` tag denotes a collection of rootfiles, viz. the possible starting point(s) for EPUB readers to begin processing and parsing the content. In this case the rootfiles contains only one entry, called `rootfile`, this tag has two attributes - `full-path` and `media-type`. The first attribute holds the path to an inventory file (in this case *Example.opf*) containing metadata regarding the publication and its content. Finally, `media-type` is reaffirmation of the EPUBs mimetype.
	

####The OPF file####
The OPF file is an important part of the structure of an EPUB, as it contains the necessary metadata to accurately describe the publication, but also because it may contain a linear reading order which, in combination with the contents of *toc.ncx*, may be used by EPUB readers to build a navigation menus or a table of contents. The OPF file is too long to be included verbatim in this document, but the most important sections are referenced below.

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

The metadata section describes the current publication. It lists information like the title, author, publisher, etc., most of these entries are identical to what librarians use to catalogue publications. Parts of the metadata section are used by EPUB readers to organise collections.
	
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

A manifest lists all the resources available in the EPUB package, with the exception of directories, the *mimetype* file, the contents of *META-INF* and the .opf file itself. A manifest file can be a pain to produce by hand for large EPUBs, as the list of resources utilised in the publication is bound to be long. Every resource has a unique `id` and should be referenced by a relative path in the `href` tag and described in the `media-type` attribute. The entry with the *cover.png* is of special interest, as the attribute `properties` describes the fact that the image may be used by EPUB readers as the cover image for the publication - e.g. for use in collection overviews.

```
  <spine toc="ncx">
  	<itemref idref="chapter1" />
  	<itemref idref="chapter2" />
  </spine>
```
Lastly, the `spine` lists all the pages present in the publication and it's listing arrangement tells an EPUB reader the linear reading order of the publication. The `spine` may only contain (X)HTML pages, not images or other content. The `toc` attribute refers to the `id`  of the `toc.ncx` in the manifest.
	

####The Content####
As stated in the introduction of this section a large part of an EPUB is a collection of HTML files, often interlinked. The process of creating the pages for an EPUB is similar to building a website, but with the particular limitations of EPUB readers in mind - limited support for rich media, colour, etc. Pages should be written in XHTML a variant of HTML which was created to make HTML more extensible and increase the interoperability with other data formats. Cascading Style Sheets (CSS) may freely be used, though a lot of EPUB readers ignore or do not parse many of the style definitions.


####Packaging####
Creating an .epub file is as simple as selecting both the *META-INF* and *OEBPS* directories and the *mimetype* file and creating a ZIP archive. This may be done by using the built-in archive utility of the operating system, or an external program like *The Unarchiver* (Mac) or WinZip (Windows) or a custom script.[^epub-zip-unzip] Some of these programs create unnecessary (hidden) files inside the archive which might invalidate your EPUB. Most EPUB readers will safely ignore extraneous files and parse the document properly, though. Validation of EPUBs can be done online using the [EPUB Validator](http://validator.idpf.org) or [a desktop application](http://www.pagina-online.de/produkte/epub-checker/). The .zip extension of the archive may then be renamed to .epub. This file can then be opened in an EPUB reader like Calibre, iBooks or similar applications.

[^epub-standard]: http://www.idpf.org/epub/30/spec/epub30-ocf.html
[^epub-zip-unzip]: http://www.mobileread.com/forums/showthread.php?t=55681