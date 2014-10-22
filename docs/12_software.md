# 12 Software Catalogue 
A catalogue of open source software written in the context of the project with links to the relevant GitHub repositories.

## BIS Publishers

## INC

<a href="https://github.com/DigitalPublishingToolkit/epubtrailer.py">https://github.com/DigitalPublishingToolkit/epubtrailer.py</a>
<a href="https://github.com/DigitalPublishingToolkit/mmd-meta-validation">https://github.com/DigitalPublishingToolkit/mmd-meta-validation</a>

## NAI/010 Publishers
The project for NAI/010 Publishers has two technical components. A mobile web application, called My Highlights, allowing a user to browse a large collection and create an EPUB based on a personal selection of objects from this collection. The other is a set of WordPress plugins, extending the functionality of the WordPress JSON REST API ([WP-API](https://github.com/WP-API/WP-API)) and facilitate the generation of EPUBs using the content from a WordPress database. The latter is basically a packaged version of the CakePHP EPUB component that builds on Asbjørn Grandt's PHPePub.

[My Highlights on GitHub](https://github.com/DigitalPublishingToolkit/my-highlights)


## Valiz
For Valiz Publishers an online EPUB generator was developed using CakePHP and a set of open-source libraries, notably [PHPePub](https://github.com/Grandt/PHPePub) by Asbjørn Grandt. The project was developed with relatively low-cost and low-feature [^low-feature-explanation] webhosting in mind, allowing it to be run on a broad range of hosting environments. Notable features include support for endnotes and a WYSIWYG editor based on HTML5's `contenteditable` mechanism. The platform allows publishers to author and generate EPUBs suitable for distribution in various bookstores.

[EPUBster on GitHub](https://github.com/DigitalPublishingToolkit/epubster)


[^low-feature-explanation]: E.g. no command line access, limited possibilities of executing external programs like pandoc.