# 10 Software catalogue 

A catalogue of the Free and Open Source software, both used and written in the Hybrid Publishing Toolkit project, with links to the relevant sources. 


### CakePHP 

A piece of web developer software that makes it easy to create web-based applications in the programming language **PHP**. 

[http://cakephp.org/](http://cakephp.org/) 


### epubtrailer.py 

A small program written in the **Python** programming language that automatically generates a visual book trailer from an EPUB file, in the form of an animated (GIF) image. 

[https://github.com/DigitalPublishingToolkit/epubtrailer.py](https://github.com/DigitalPublishingToolkit/epubtrailer.py) 


### EPUBster 

A web application for creating and editing EPUBs, written in **CakePHP**. 

[https://github.com/DigitalPublishingToolkit/epubster](https://github.com/DigitalPublishingToolkit/epubster) 


### expand_toc.py 

A small program written in the **Python** programming language to generate a table of contents for an EPUB that has been created from a **Markdown** document file. 

[https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader/blob/master/scripts/expand_toc.py](https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader/blob/master/scripts/expand_toc.py) 


### Git 

[Git](http://git-scm.com/) is a distributed version control system created for collaborative software development. Similar to popular applications like Dropbox and Google Drive, it allows users to share folders on their computer with others, synchronizing the changes made by different users the files in those folders. Unlike Dropbox or Google Drive however, it stores all previous versions of edited files and automatically resolves inconsistencies when two people edit different parts of the same file. Such shared Git folders may be put on a public website such as [GitHub](http://github.com/) or [Gitorious](http://gitorious.org/), or on a private server. Git is not owned by any company, but is Open Source / Free Software. It was created by the inventor of Linux, Linus Torvalds, is widely used all over the world, and is a very reliable piece of software.

[http://git-scm.com/](http://git-scm.com/) 


### ICML 

ICML is the file format of [InCopy](https://creative.adobe.com/products/incopy), Adobe's word processor built into InDesign. With the application **pandoc**, **Markdown** files can be easily converted into ICML, preserving the logical structure of the document. The resulting file can then be imported into InDesign and be used as the basis of a print design. See the [related blog post on **Make** and its use in one of our projects](http://digitalpublishingtoolkit.org/2014/10/markdown-to-indesign-with-pandoc-via-icml/).


### Make 

The [GNU Make](http://www.gnu.org/software/make/) program helps to automate workflows in which a number of command-line programs and scripts need to be repeatedly used, for example when converting documents. Instead of running a number of such scripts by hand one after another, Make allows to run them in a single batch while applying predefined rules and conditions for this process. See the [related blog post on how Make has been used in one of our projects](http://digitalpublishingtoolkit.org/2014/10/make-book/). A Makefile can be seen as a kind of [a developer's notebook](http://zgp.org/static/scale12x/#) that helps organize one's toolbox of scripts. Make is Open Source / Free Software. 

[http://www.gnu.org/software/make/](http://www.gnu.org/software/make/) 


### Markdown 

[Markdown](http://daringfireball.net/projects/markdown/) is a simple structured text format. It was originally designed to allow writers to use informal, human-readable formatting in blog posts, using writing conventions found in plain-text emails and chats, rather than reader-unfriendly and writer-unfriendly HTML code. Though it [originated from the blogging and coding communities](http://en.wikipedia.org/wiki/Markdown#History), Markdown is gaining popularity and is supported by a wide range of tools and programs (See **Mou** below). This blog post [compares Markdown with HTML](http://digitalpublishingtoolkit.org/2014/04/mark-me-up-mark-me-down/) in the context of one of our own e-book development projects. Most Markdown tools are Open Source / Free Software, and the format is currently in the process of becoming an open [standard](http://blog.codinghorror.com/standard-markdown-is-now-common-markdown/). 

[http://daringfireball.net/projects/markdown/](http://daringfireball.net/projects/markdown/) 


### MacDown 

[MacDown](http://macdown.uranusjr.com/) is a text application for Mac OS X that makes it easy to write **Markdown** text. It offers a split-screen view with an automatic live translation of Markdown to HTML. 

[http://macdown.uranusjr.com/](http://macdown.uranusjr.com/) 


### mmd-meta-validation 

A simple validation tool for checking metadata in a **Markdown** file. 

[https://github.com/DigitalPublishingToolkit/mmd-meta-validation](https://github.com/DigitalPublishingToolkit/mmd-meta-validation) 


### My Highlights 

Our project for nai010 Publishers included two technical components. The first is a mobile web application, called My Highlights, which allows a user to browse a large collection and create an EPUB based on a personal selection of catalogue texts on art works from the collection of the Stedelijk Museum Amsterdam. The other is a set of plug-ins for the popular web content management system WordPress, extending the functionality of the WordPress JSON REST **API** (WP-AP)[^wp-api] and facilitating the generation of EPUBs directly from a WordPress database. (The latter is for the most part a packaged version of the **CakePHP** EPUB component that builds on Asbjørn Grandt's PHPePub.)

[https://github.com/DigitalPublishingToolkit/my-highlights](https://github.com/DigitalPublishingToolkit/my-highlights) 


### Pandoc 

[Pandoc](http://johnmacfarlane.net/pandoc/) is the 'Swiss-army knife' of text converters, an Open Source software application able to convert between a wide variety of document formats. In our projects, Pandoc has been the essential tool for converting documents written in Microsoft Word to Markdown, and then later for converting edited Markdown source documents to EPUB. Pandoc only has a command-line interface and can be run in the Mac OS X Terminal, the Windows Command Prompt and the Linux Terminal. The program has an enormous amount of features such as user-defined design templates and metadata management. It can be used for all kinds of purposes and can be highly customized for one's particular document creation needs. Our Hybrid Workflow How-To Guides (for [editors](http://digitalpublishingtoolkit.org/2014/10/hybrid-workflow-how-to-introduction-editing-steps/), [designers](http://digitalpublishingtoolkit.org/2014/10/markdown-to-indesign-with-pandoc-via-icml/), and [developers](http://digitalpublishingtoolkit.org/2014/10/hybrid-workflow-how-to-making-automated-workflows-part-1/) include various real-world examples for using Pandoc.

[http://johnmacfarlane.net/pandoc/](http://johnmacfarlane.net/pandoc/) 


### PHPePub 

For Valiz Publishers, an online EPUB generator was developed based on **CakePHP** and a set of Open Source software modules, notably Asbjørn Grandt's PHPePub. [^phpepub] The project was developed with relatively low-cost and low-feature [^low-feature-explanation] web hosting in mind. Notable features include support for endnotes and a **WYSIWYG** editor based on HTML5's 'content-editable' mechanism. The platform allows publishers to author and generate EPUBs suitable for distribution in various bookstores. 

[https://github.com/Grandt/PHPePub](https://github.com/Grandt/PHPePub) 


### PHP 

[PHP](http://php.net) is a programming language typically coupled with a web server and used for creating dynamic websites. 

[http://php.net](http://php.net) 

 
### Python 

[Python](https://www.python.org/) is a general-purpose programming (or scripting) language. In one of our projects, Python was used to make small 'helper' programs to clean up HTML, to extract and accumulate metadata from different files, and to create animated GIF book trailers from EPUB files. Python scripts often make use of additional program modules known as libraries. For our project, we made use of the html5lib and images2gif libraries. Python is Free Software / Open Source and comes pre-installed on Mac OS X and all standard flavors of Linux. For all other operating systems, an installer can be [downloaded from the Python website](https://www.python.org/downloads/). 

[http://www.python.org/](http://www.python.org/) 


<!-- ### ReFoot.js -->


[^wp-api]:A JSON-based REST API for WordPress, <a href="https://github.com/WP-API/WP-API">https://github.com/WP-API/WP-API</a>. 

[^low-feature-explanation]: E.g. no command-line access, limited possibilities for executing external programs like Pandoc. 