# 12 Software Catalogue 
A catalogue of open source software written in the context of the project with links to the relevant GitHub repositories.


In the present project we deal with various kinds of products which we combine into five genres: 



## BIS Publishers

## INC
An example of a *research publication* is the Society of Query reader, issued by INC.
<!-- Can be worked out more -->

https://github.com/DigitalPublishingToolkit/epubtrailer.py [^epubtrailer]
https://github.com/DigitalPublishingToolkit/mmd-meta-validation [^mmd-meta-validation]

## NAI/010 Publishers
The project for NAI/010 Publishers has two technical components. A mobile web application, called My Highlights, allowing a user to browse a large collection and create an EPUB based on a personal selection of objects from this collection. The other is a set of WordPress plugins, extending the functionality of the WordPress JSON REST **API** (WP-AP)[^wp-api] and facilitate the generation of EPUBs using the content from a WordPress database. The latter is basically a packaged version of the CakePHP EPUB component that builds on Asbjørn Grandt's PHPePub.

My Highlights on GitHub.[^my-highlights-on-github]

## Valiz
For Valiz Publishers an online EPUB generator was developed using CakePHP and a set of open-source libraries, notably PHPePub[^phpepub] by Asbjørn Grandt. The project was developed with relatively low-cost and low-feature [^low-feature-explanation] webhosting in mind, allowing it to be run on a broad range of hosting environments. Notable features include support for endnotes and a WYSIWYG editor based on HTML5's `contenteditable` mechanism. The platform allows publishers to author and generate EPUBs suitable for distribution in various bookstores.

EPUBster on GitHub.[^EPUBster on GitHub]

[^epubtrailer]: A python script that generates a book trailer from an epub file as an animated gif, https://github.com/DigitalPublishingToolkit/epubtrailer.py.
[^mmd-meta-validation]: A simple validation tool to check metadata in a MMD file, https://github.com/DigitalPublishingToolkit/mmd-meta-validation.
[^wp-api]:A JSON-based REST API for WordPress, https://github.com/WP-API/WP-API.
[^my-highlights-on-github]:A proof-of-contept mobile web application and two Wordpress plugins, https://github.com/DigitalPublishingToolkit/my-highlights.
[^phpepub]:PHP Classes for dynamically generating EPub files, https://github.com/Grandt/PHPePub.
[^low-feature-explanation]: E.g. no command line access, limited possibilities of executing external programs like pandoc.
[^EPUBster on GitHub]:A web application to create and edit EPUBs, written in CakePHP, https://github.com/DigitalPublishingToolkit/epubster.