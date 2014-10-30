# 09 Guide: Alternative ways of publishing
<!-- Miriam: in chapter 7 there is also a small section on Calibre (how to make a simple ebook) - what is the difference with this chapter?-->

<!-- Kimmy: there indeed seems to be a strange division between chapter 07 and 09. Maybe this chapter should come after 07 as a more advanced version? Or we should first explain the workflows and than the guides?. so you get:

Chapter 06_workflows.md
Chapter 07_guide workflow.md
chapter 08_guide_DIY.md
Chapter 09_guide_advanced.md
-->

<!--Margreet:Chapter 09 should talk about existing authoring suites and enahancers, i.e. ADE, Mag+ -->

<!-- Silvio: Adobe Digital Editions is the software used to read and manage e-books: <a href="http://www.adobe.com/it/solutions/ebook/digital-editions.html">http://www.adobe.com/it/solutions/ebook/digital-editions.html</a>
- the Adobe Digital Publishing Suite is a sort of extension of InDesign that allows to produce 'enhanced' magazines and publications for iPad, etc: <a href="http://www.adobe.com/it/products/digital-publishing-suite-enterprise.html">http://www.adobe.com/it/products/digital-publishing-suite-enterprise.html</a> -->


A consistent design and uniform interactivity across devices could be a requirement, in which case a reflowable document might not be the ideal solution. Some publishers opt to develop their own (mobile) applications, like The Guardian's iOS [^guardian-ios] version of their newspaper, the amplified ebooks by Penguin [^penguin-amplified] or the children's book by Purple Carrot [^purple-carrot-publication].
These solutions offer fine-grained control over user interaction and consistency of design, but come with the extra cost of hiring a development team to engineer the application. Also, publishing for different platforms is not that straightforward. Code written specifically with the iOS **SDK (Software Development Kit)** in mind will likely require a lot of editing before it's ready to run on the Android platform. Portability is another issue, it's fairly easy to transfer an EPUB to another device, however application binaries are not that easily passed around, mostly due to the relatively closed nature of mobile operating systems.

Lastly, why not just publish essays, articles or even whole books on a website? The wealth of weblogs and other publishing platforms shows that this is a viable form of publishing. Monetising is less straightforward, most websites generate income by showing advertisements or sponsored articles. Paid membership is also used as a business model by some websites, like *De Correspondent* [^de-correspondent]. One of the major downsides is that content will only be available online and cannot be easily passed around as a single unit of information like an EPUB or a PDF.


##Authoring Suites
A range of publishing suites is available as well, which roughly fall into two categories. One can be described as full-blown editors, the other allows publishers to enhance existing publications with interactive features.

###Editors: Calibre
<!-- Miriam: why is Calibre called an editor here?-->
Calibre [^calibre] is a 'swiss army knife' for reading, converting, authoring and cataloging e-books. It is open source, runs on Windows, Mac OS X, and Linux (with identical graphical interfaces on all these platforms) and is under very active development with frequent version updates. We recommend it as a standard tool for all ebook publishers next to pandoc and consider it superior to (older) alternatives like Sigil.[^Sigil] The inexpensive commercial program Jutoh[^Jutoh], which also runs on Windows, Mac OS X and Linux, is superior as an easy-to-use graphical editor for ebooks since it gives writers and editors a user interface similar to that of Microsoft Word. Jutoh is less powerful as a document converter and ebook database.

Calibre can be used to:

* open and read EPUB files on a personal computer;

* import various documents in various ebook and electronic text formats (including .docx, rtf, HTML and plain text) and convert them into EPUB; export to other document formats including Amazon Kindle, PDF and RTF.

* manage a local library/database of all imported ebooks, with easy editing of the bibliographic meta data of each ebook;

* synchronize the user's ebook library with ereading devices;

* edit ebooks in HTML source code, with live graphical preview.

Calibre calls itself 'the one stop solution to all your ebook needs'. And indeed, (small) publishers could use it as their single, one-size-fits-all tool for ebook production. If one wants to create text-oriented, standard-compliant ebooks, Calibre is the most accessible and straightforward authoring software currently available.

However, at its current version 2.5, Calibre is not perfect. For some aspects, other programs provide better functionality:

* Calibre's user interface is cluttered and can be confusing. The program has so many features and modules that it can feel like several programs jammed into one.

* The editor only supports EPUB 2.0 and is meant for tweaking the HTML and CSS code of imported documents, not for editing ebooks from scratch. That said, it provides good live graphical previews of the formatted document. Still, the editor is not the right tool for visual/multimedia-oriented publications. 

* The import/document conversion function is inferior to pandoc. In our tests, we obtained clearly better results converting Microsoft Word .docx and Markdown files to epub with pandoc than with Calibre. Calibre has the advantage of easy graphical operation, as opposed to the non-graphical command line interface of pandoc.

* Calibre's graphical viewer uses a simple HTML engine that is insufficient for testing and evaluating the visual design of an ebook. 

* Calibre's PDF export provides no real alternative to a PDF document carefully designed in a program like InDesign, or with custom templates using XML or other document formats. Here, pandoc is superior to Calibre as well.

Despite these limitations, Calibre is a capable program for importing simple text documents, tweaking them into an ebook  and exporting it to the most common ebook formats.  

Currently, the technically easiest and least expensive way of hybrid publishing is to transform a book into Markdown, edit the Markdown into a structurally clean document, use pandoc for converting Markdown to EPUB , and import the EPUB into Calibre for final tweaks and conversion into other e-book formats (including Amazon Kindle).

![Calibre Workflow](images/09_calibre.png)
<!-- image is still in progress, will be finished after go on content about calibre -->

In a perfect future, Calibre would use pandoc as its import and document conversion engine, Readium for displaying e-books, and its document editor would be on par with iBooks Author for multimedia design while maintaining full compliance to the EPUB3 standard.  


###Enhancers: Adobe Digital Publishing Suite, Mag+
These applications mostly integrate (as plugins) in an existing Adobe InDesign and allow designers to define interactive content (media, animations, etc.) in a traditional print design. As such these tools are often used to convert print magazines into their digital counterparts suitable for sale in Apple's Newsstand, for example.


[^guardian-ios]: Guardian app for iOS and Android, http://www.theguardian.com/global/ng-interactive/2014/may/29/-sp-the-guardian-app-for-ios-and-android.
[^penguin-amplified]: For example: Jack Kerouac's On the Road (A Penguin Books Amplified Edition), July 2, 2011, http://www.penguin.com/static/pages/features/amplified_editions/on_the_road.php and Ayn Rand's Atlas Shrugged (An NAL Amplified Edition), October 12, 2013, Ayn Rand's Atlas Shrugged (An NAL Amplified Edition)http://www.penguin.com/static/pages/features/amplified_editions/atlas_shrugged.php.
[^purple-carrot-publication]: The Prisoner of Carrot Castle, November 19, 2013, https://itunes.apple.com/us/app/the-prisoner-of-carrot-castle/id499981407?mt=8&ign-mpt=uo%3D4.
[^de-correspondent]: De Correspondent, https://decorrespondent.nl.
[^calibre]: Calibre ebook management: http://calibre-ebook.com/.
[^Sigil]: Sigil, The EPUB Editor, http://code.google.com/p/sigil.
[^Jutoh]: Jutoh, epublishing made easy, http://www.jutoh.com.

