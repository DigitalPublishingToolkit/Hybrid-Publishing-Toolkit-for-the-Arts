##EPUB from scratch

Part of the process of creating an EPUB by hand is very similar to developing a simple website. The EPUB file format is basically a compressed collection of HTML files, compiled together with some extra files containing descriptive markers regarding the content of the publication. A typical EPUB file is just a Zip archive without the .zip file extension, which is instead substituted by .epub. A file archiver can easily decompress EPUB files, although the user sometimes has to replace the .epub extension with .zip in order for the file archiver to recognise the EPUB as a compressed archive.


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
2. *container.xml* contains a simple structure written in XML. Below is a complete version of the document followed by an explanation of its separate parts. You may safely ignore the explanation if its too technical in nature, the important part of this document is what's contained in between the quotes of *full-path* (`OEBPS/content.opf`). This attribute should point to an .opf file we'll create later on and will be stored in the *OEBPS* directory.

	```
	<?xml version="1.0" encoding="UTF-8"?> 
	<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"> 
		<rootfiles>
			<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
		</rootfiles>
	</container>
	```
	
	The first line is a 'declaration statement' which should always be present in XML files. This is followed by the 'container' which denotes that the publication is based on the *Open Container Format* as specified by the EPUB standard[^epub-standard]. The *rootfiles* tag denotes a collection of rootfiles, viz. the possible starting point(s) for EPUB readers to begin processing and parsing the content. In this case the rootfiles contains only one entry, called *rootfile*, this tag has two attributes - *full-path* and *media-type*. The first attribute holds the path to an inventory file (in this case *Example.opf*) containing metadata regarding the publication and its content. Finally, *media-type* is reaffirmation of the EPUBs mimetype.
	

####The OPF file####
The OPF file is an important part of the structure of an EPUB, as it contains the necessary metadata to accurately describe the publication, but also because it may contain a linear reading order which, in combination with the contents of *toc.ncx*, may be used by EPUB readers to build a navigation menus or a table of contents. The OPF file is too long to be included verbatim in this document, but the most important sections are referenced below.

```
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title id="title">Example</dc:title>
    <meta refines="#title" property="title-type">main</meta>
    ...
  </metadata>
```

The metadata section covers 
	
```	
  <manifest>
    <item href="css/style.css" id="css1" media-type="text/css"/>
    <item href="cover.png" id="cover" media-type="image/png" properties="cover-image"/>
    <item href="pages/page-01.xhtml" id="page1" media-type="application/xhtml+xml"/>
    <item href="pages/toc.ncx" id="ncx" media-type="application/x-dtbncx+xml"/>
  </manifest>
```

A manifest.

```
  <spine toc="ncx">
    <itemref idref="page1" />
  </spine>
```

[^epub-standard]: http://www.idpf.org/epub/30/spec/epub30-ocf.html