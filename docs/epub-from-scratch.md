##EPUB from scratch##
<!-- I would expect an opening explaining why an EPUB from scratch is described here. What is 'from scratch' in this context and in what situation would you make such an EPUB?  -->

The process of creating an EPUB by hand is in part very similar to developing a simple website. A typical EPUB file is a Zip archive without the .zip file extension, which is instead substituted by .epub. In other words, the EPUB file format is basically a compressed collection of HTML files, like on a website, compiled together with some extra files containing descriptive markers regarding the content of the publication. A file archiver <!-- such as... name example(s) ^Miriam--> can easily decompress EPUB files, although the user sometimes has to replace the .epub extension with .zip in order for the file archiver to recognise the EPUB as a compressed archive.

A rudimentary EPUB is used as an example to explain several of its concepts and may be [downloaded here]().

###Layout of an EPUB file <!-- of directory?-->###
Decompressing an EPUB will reveal its directory layout and in that way make clear how an EPUB is set up. As explained above, the EPUB can be seen as a compressed Zip archive, looking as follows after unzipping it:

[[Figure: Screenshot of directory layout]]

The *META-INF* and *OEBPS* directories and *mimetype* should always be present in an EPUB file and form a large part of what constitutes as an EPUB. 

*META-INF* contains an XML file (*container.xml*) which directs EPUB readers to an inventory (an .opf file) of all the files present in the publication. <!-- this sentence is unclear to me, is it the reader as a person or the device? - I presume the last, call it e-readers? How are they then directed to an inventory, what is this inventory, is it just in the backend or on your screen? Is the inventory then a Table of Contents? sorry... -->

*OEBPS* is the location where all the content (HTML files, images, audio, video, etc.) of the publication is stored, (nested) subcategories are possible but not mandatory. The .opf file (traditionally named *content.opf*) is important; this contains the metadata for the EPUB and is in turn referenced by the aforementioned *container.xml*. You might see another file with a .ncx extension (traditionally *toc.ncx*), it holds the hierarchical table of contents for the EPUB and is entirely optional as it isn't part of the EPUB specification.

The file *mimetype* contains a single line describing the EPUB file as `application/epub+zip`, this file allows EPUB readers to check whether the file is actually an EPUB.

When you create an EPUB, these components will all have to be there. <!--some kind of concluding sentence at the end of the subparagraph needed-->

###Creating your own EPUB###
Most of the elements of an EPUB can be produced by hand in a text editor that handles html <!--I added this, is it correct? Otherwise I would think Word, Textedit, NotePad stuff like that-->. Popular text editors include BBEdit, TextWrangler or TextMate for Mac or NotePad++ and PSPad for Windows. Below follows a step by step process of creating a very simple EPUB.


####Creating the required files and directories####
1. Create a directory on your computer to store the files and subdirectories for your EPUB in, e.g. *Example*;
2. Create two directories inside this *Example*, one called *META-INF* and the other *OEBPS*;
3. Create a plain text file using a text editor and add the line `application/epub+zip` to the file;
4. Save the plain text file in the directory *Example*. Name it *mimetype* and don't use a file extension.

Now there are the two directories and one text file, like we saw when we decompressed the EPUB used as an example.


####container.xml####
1. Again using a text editor, create a new file and save it to the *META-INF* directory with the name *container.xml*;
2. *container.xml* contains a simple structure written in XML. Below is a complete version of the document followed by an explanation of its separate parts. You may safely ignore the explanation if its too technical in nature. The important part of this document is what's contained in between the quotes of `full-path` <!--don't understand this--> (*OEBPS/content.opf*). This attribute <!--which attribute?--> should point to an .opf file we'll create later on and will be stored in the *OEBPS* directory. <!--do I understand correctly that you need to copy this little piece of html into your new file? Then I would just name it so: copy the lines below into the file :-)-->

	```
	<?xml version="1.0" encoding="UTF-8"?> 
	<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"> 
		<rootfiles>
			<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
		</rootfiles>
	</container>
	```
	
The first line is a `declaration statement` which should always be present in XML files. This is followed by the `container` which denotes that the publication is based on the *Open Container Format* as specified by the EPUB standard[^epub-standard]. The `rootfiles` tag denotes a collection of rootfiles, viz. the possible starting point(s) for EPUB readers to begin processing and parsing the content. In this case the rootfiles contains only one entry, called `rootfile`, this tag has two attributes - `full-path` and `media-type`. The first attribute holds the path to an inventory file (in this case *Example.opf*) containing metadata regarding the publication and its content. Finally, `media-type` is reaffirmation of the EPUBs mimetype.

<!-- End with something like, Save and close your container.xml document.-->
	

####The OPF file####
The OPF file is an important part of the structure of an EPUB, as it contains the necessary metadata to accurately describe the publication, but also because it may contain a linear reading order which, in combination with the contents of *toc.ncx*, may be used by EPUB readers to build a navigation menu or a table of contents. The OPF file is too long to be included verbatim in this document, but the most important sections are referenced below.
<!--then where can I find it? What do I do with it? Here I miss the 'step-by-step' structure-->

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

The metadata section describes the current publication. It lists information like the title, author, publisher, etc.. Most of these entries are identical to what librarians use to catalogue publications. Parts of the metadata section are used by EPUB readers to organize collections <!-- for example by author, publication year or something-->.
	
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
As stated in the introduction of this section a large part of an EPUB is a collection of HTML files, often interlinked. The process of creating the pages for an EPUB is similar to building a website, but with the particular limitations of EPUB readers in mind - limited support for rich media, colour, etc. <!--see section XX for more details on limitations--> Pages should be written in XHTML, a variant of HTML which was created to make HTML more extensible and increase the interoperability with other data formats. Cascading Style Sheets (CSS) may freely be used, though a lot of EPUB readers ignore or do not parse many of the style definitions.
<!--Here again I miss the 'step-by-step' structure. I think we also need to make clear 'for dummies' how you make the actual html or xhtml files / CSS. or no? Show examples? And where to put the content (which directory)?-->

####Packaging####
Creating an .epub file is as simple as selecting both the *META-INF* and *OEBPS* directories and the *mimetype* file and creating a ZIP archive. This may be done by using the built-in archive utility of the operating system, or an external program like *The Unarchiver* (Mac) or WinZip (Windows) or a custom script.[^epub-zip-unzip] Some of these programs create unnecessary (hidden) files inside the archive which might invalidate your EPUB. Most EPUB readers will safely ignore extraneous files and parse the document properly, though. Validation of EPUBs can be done online using the [EPUB Validator](http://validator.idpf.org) or [a desktop application](http://www.pagina-online.de/produkte/epub-checker/). The .zip extension of the archive may then be renamed to .epub. This file can then be opened in an EPUB reader like Calibre, iBooks or similar applications.

<!--Cool!-->

[^epub-standard]: http://www.idpf.org/epub/30/spec/epub30-ocf.html
[^epub-zip-unzip]: http://www.mobileread.com/forums/showthread.php?t=55681