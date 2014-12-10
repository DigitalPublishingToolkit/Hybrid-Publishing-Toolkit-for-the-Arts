# 11 Software Catalogue 

A catalogue of the Free and Open Source software both used and written in the context of the Digital Toolkit project with links to the relevant sources. 


### CakePHP 

CakePHP is a web framework that makes it easy to create web based applications using PHP. 

[http://cakephp.org/](http://cakephp.org/) 


### epubtrailer.py 

A Python script that generates a book trailer from an EPUB file as an animated GIF. 

[https://github.com/DigitalPublishingToolkit/epubtrailer.py](https://github.com/DigitalPublishingToolkit/epubtrailer.py) 


### EPUBster 

A web application to create and edit EPUBs, written in CakePHP. 

[https://github.com/DigitalPublishingToolkit/epubster](https://github.com/DigitalPublishingToolkit/epubster) 


### expand_toc.py 

A Python script to generate a Markdown source for an EPUB based on a (Markdown) table of contents source. 

[https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader/blob/master/scripts/expand_toc.py](https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader/blob/master/scripts/expand_toc.py) 


### Git 

[Git](http://git-scm.com/) is a distributed version control system, software that turns a folder into a kind of wiki that tracks the history of changes to files in a way that can then be shared with others. This is done via performing pull and push operations to other copies of the folder (called repositories). The folder may be placed on a public website dedicated to hosting Git repositories such as [GitHub](http://github.com/) or [Gitorious](http://gitorious.org/), or else (also) on a private server. Git is Free Software. 

[http://git-scm.com/](http://git-scm.com/) 


### ICML 

ICML is a file extension generally managed by [InCopy](https://creative.adobe.com/products/incopy), Adobe's own word processor. See the [related blog post on how Make has been used in the INC subgroup](http://digitalpublishingtoolkit.org/2014/10/markdown-to-indesign-with-pandoc-via-icml/) in order to import structured text into Adobe InDesign. 


### Make 

The [GNU Make](http://www.gnu.org/software/make/) program helps automate a workflow made of command-line scripts. See the [related blog post on how Make has been used in the INC subgroup](http://digitalpublishingtoolkit.org/2014/10/make-book/). A Makefile can be seen as a kind of [executable notebook](http://zgp.org/static/scale12x/#) that helps organize ad hoc scripts into a way that records how the pieces fit together as targets and dependencies. Make is Free Software. 

[http://www.gnu.org/software/make/](http://www.gnu.org/software/make/) 


### Markdown 

[Markdown](http://daringfireball.net/projects/markdown/) is a structured text format designed to allow writers to quickly add markup to text using writing conventions found in 'text-only' emails rather than the angle bracket notation of full HTML tags. While [originating from the blogging and coding communities](http://en.wikipedia.org/wiki/Markdown#History), Markdown is gaining increased popularity and is supported in a wide range of tools and programs (See Mou below). This blog post [compares Markdown with HTML](http://digitalpublishingtoolkit.org/2014/04/mark-me-up-mark-me-down/) in the context of the INC work. Most Markdown tools are Free Software, and the format is currently in the process of becoming an open [standard](http://blog.codinghorror.com/standard-markdown-is-now-common-markdown/). 

[http://daringfireball.net/projects/markdown/](http://daringfireball.net/projects/markdown/) 


### MacDown 

[MacDown](http://macdown.uranusjr.com/) is a graphical application for Mac OS X designed for editing 
Markdown text. It offers a split-screen view with a live translation of the Markdown to HTML. 

[http://macdown.uranusjr.com/](http://macdown.uranusjr.com/) 


### mmd-meta-validation 

A simple validation tool to check metadata in a MMD file. 

[https://github.com/DigitalPublishingToolkit/mmd-meta-validation](https://github.com/DigitalPublishingToolkit/mmd-meta-validation) 


### My Highlights 

The project for NAI010 Publishers has two technical components. A mobile web application, called My Highlights, allowing a user to browse a large collection and create an EPUB based on a personal selection of objects from this collection. The other is a set of WordPress plugins, extending the functionality of the WordPress JSON REST **API** (WP-AP)[^wp-api] and facilitating the generation of EPUBs using the content from a WordPress database. The latter is basically a packaged version of the CakePHP EPUB component that builds on Asbjørn Grandt's PHPePub. 

[https://github.com/DigitalPublishingToolkit/my-highlights](https://github.com/DigitalPublishingToolkit/my-highlights) 


### Pandoc 

[Pandoc](http://johnmacfarlane.net/pandoc/) is the 'Swiss-army knife' of text formats, a program able to convert between a wide variety of document formats. In the INC workflow, Pandoc has been essential to convert documents written in Microsoft Word to Markdown, and then later to compile edited Markdown sources to an EPUB. While having a command-line interface, the program supports an enormous amount of features such as templates and metadata meaning that it's quite flexible. See the Hybrid Workflow How-To's (for\ [editors](http://digitalpublishingtoolkit.org/2014/10/hybrid-workflow-how-to-introduction-editing-steps/), [designers](http://digitalpublishingtoolkit.org/2014/10/markdown-to-indesign-with-pandoc-via-icml/), and [developers](http://digitalpublishingtoolkit.org/2014/10/hybrid-workflow-how-to-making-automated workflows-part-1/)) for examples of using Pandoc in the INC workflow. 

[http://johnmacfarlane.net/pandoc/](http://johnmacfarlane.net/pandoc/) 


### PHPePub 

For Valiz Publishers an online EPUB generator was developed using CakePHP and a set of Open Source libraries, notably PHPePub[^phpepub] by Asbjørn Grandt. The project was developed with relatively low-cost and low-feature [^low-feature-explanation] web hosting in mind, allowing it to be run on a broad range of hosting environments. Notable features include support for endnotes and a **WYSIWYG** editor based on HTML5's 'content-editable' mechanism. The platform allows publishers to author and generate EPUBs suitable for distribution in various bookstores. 

[https://github.com/Grandt/PHPePub](https://github.com/Grandt/PHPePub) 

[^wp-api]:A JSON-based REST API for WordPress, https://github.com/WP-API/WP-API. 

[^low-feature-explanation]: E.g. no command line access, limited possibilities of executing external programs like Pandoc. 


### PHP 

[PHP](http://php.net) is a scripting language typically coupled with a web server used to create dynamic websites. 

[http://php.net](http://php.net) 

 
### Python 

[Python](https://www.python.org/) is a general purpose programming (or scripting) language. In the INC project, Python has been used to make small 'helper' programs to: cleanup HTML, extract and accumulate metadata from different files, and to create GIF-format book trailers from an EPUB. Python scripts often make use of additional programs known as libraries. For INC, we made use of the html5lib and images2gif libraries. Python is often pre-installed on many operating systems such as Mac OS X and Debian and Ubuntu GNU/Linux, or otherwise an installer can be [downloaded from the Python website](https://www.python.org/downloads/). 

[http://www.python.org/](http://www.python.org/) 


### ReFoot.js 


