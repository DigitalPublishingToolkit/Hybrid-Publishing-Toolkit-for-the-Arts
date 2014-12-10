# 01 Introduction 

'You must change your life' - borrowing from the philosopher Peter Sloterdijk, this could be the summary of our message to art-oriented and design-oriented publishers, writers, editors and designers who are transitioning from traditional book making to electronic publishing or - more typically - **hybrid** print and electronic publishing. Hybrid publishing will sooner or later confront them with the need to re-think traditional publication formats, editorial and production workflows, and distribution. The changes required may well be greater and more extensive than initially expected! 

*Change will be minor for scientific publishers and large publishers* 

Having said that, there are exceptions. Workflow changes can be minor for publishers who already do all their editorial work in highly structured digital document formats (such as **XML** or databases); but typically, this is only the case in scientific and technology-oriented publishing. Changes may also be minor for larger publishers who can afford outsourcing. Making an electronic (digital) publication in parallel to a printed publication is then simply a matter of paying an external service provider, such as a document engineering company or a media design agency, to turn a Microsoft Word or InDesign file into an **ebook**. This process can be quick if the book is visually simple - such as a novel or a textbook with few illustrations - and economically worthwhile if many ebooks will be sold. 

*Change will be major for small, arts-oriented publishers* 

Since this Toolkit - consisting of this manual and of an online software kit - is meant for publishers who publish visually oriented books in mostly smaller print runs, we propose here an alternative to the route mentioned above. Neither a complex internal IT infrastructure, nor costly outsourcing will be viable solutions for these types of publishers. Unfortunately, there is no magic software button that will turn a print book design into an electronic publication just like that. Since the two media are so different, each with its own specific editorial and visual design needs, such a button will probably not materialize in the future either. Hybrid publishing will ultimately require changes in the way the editorial work is done. The good news is that such change is possible. This Toolkit includes instructions on how to deal with the many issues that arise when making the transition from traditional to hybrid or electronic publishing. 

For art and design publishers, the challenge of going electronic with their publications is greater than that faced by other fields of publishing, for a number of reasons: 

- visually oriented publications are still more difficult to realize technically in the electronic medium, particularly when designing for a multitude of different reading devices and ebook **platforms**; 
- small publishers are under a great deal of pressure to keep project costs low, often due to smaller budgets - however, the need to publish in multiple forms (e.g. print and electronic) will inevitably increase costs, unless one does as much work as possible in a way that is not dependent on the medium; 
- in order to make the investment in an electronic publication durable, electronic publications must be sustainable: they should not require constant investment in technical maintenance and version updates. 

## Industry promises vs. reality 

There is a stark contrast between the promises of the computer industry, and the reality of the new digital medium. On one hand, publishers, editors, designers and artists tend to overestimate the interactive and **multimedia** possibilities of electronic publishing. These extra possibilities do exist, but in most cases bring with them higher development costs, and remain specific to one particular technical reading platform. 

On the other hand, publishers tend to underestimate how even technically simple and seemingly trivial types of electronic publications can lead to a re-thinking of established publishing practices and formats. When traditional publishing formats go electronic or hybrid, there is a real possibility for transformation. Once the book becomes electronic or hybrid, the permanence, immutability and stability typical of physical books is likely to mutate into dynamic, modular, and participative forms, which can benefit from the networked environment in which ebooks exist. 

Various types of electronic publications may be subject to different kinds of significant change. An exhibition catalog for instance can be split up into interrelated micro-monographs which readers can download and read as individual ebooks. An ebook can be assembled from a variety of sources selected by individual readers, as is currently the case with Wikipedia, where visitors to the website can compile their own collection of Wikipedia articles and export this compilation to an **EPUB** or PDF using the [Book Creator tool](http://en.wikipedia.org/wiki/Help:Books). 

The possibilities for change can go beyond the rethinking of publishing formats, eventually going so far as to redefine what a book actually is. 


## What this Toolkit provides 

Going electronic - or going hybrid - means that you need to change the way you work in the publishing process, from manuscript to publication. The software tools currently in use, from **word processors** such as Microsoft Word to **desktop publishing** suites such as Adobe InDesign, were created for the analog or desktop-publishing world. Although it's possible to create electronic publications from Microsoft Word [![Bloglink](images/dpt_blog_verwijzing.png)](http://networkcultures.org/digitalpublishing/2014/03/28/converting-a-docx-directly-to-epub-using-calibre/ "Link to blog post: Converting a Docx directly to EPUB using Calibre")( Converting a Docx directly to EPUB using Calibre) and InDesign [![Bloglink](images/dpt_blog_verwijzing.png)](http://networkcultures.org/digitalpublishing/2013/05/21/epub-development-in-adobe-indesign-cs6/ "Link to blog post: NOTES ON EPUB DEVELOPMENT IN ADOBE INDESIGN CS6")(Notes on EPUB Development in Adobe InDesign CS6) documents, which are likely to be the standard format used in current publishing workflows, in most cases this will be a painful, slow, inefficient and expensive process. This Toolkit focuses on technical do-it-yourself (DIY) alternatives, in the first place because the Toolkit is primarily aimed at publishers who, in most cases, cannot afford to outsource ebook design to external service providers, and also because it is aimed at those who want to keep the process in their own hands. 

This Toolkit focuses particularly (but not exclusively) on EPUB3 as an electronic publication format, and on Markdown as a word processing format, because of the specific needs of small-edition publishers in the field of art and design: low costs, ease of use, sustainability and platform independence. The recommendations stem from our practical experience in collaborating with four Dutch art, design and research publishers on electronic publication projects: BIS Publishers, Valiz, NAI010 and Institute of Network Cultures. 


## Whom is this Toolkit written for 

You may be a publisher, a designer, or someone who is just starting out with making books. You probably identify with or work in the arts. You may hope to find answers, gain knowledge, pick up some tips, and consult various resources. This Toolkit intends to provide all of that. The overall focus is on pragmatic solutions for publishers within the sector of art and culture. No prior knowledge of creating an ebook is required - having said that, a familiarity with various computer software applications is helpful, as is the willingness to learn and the inquisitive curiosity to look beyond this guide for specific answers. This publication is not a tutorial on how to make an electronic publication, it merely intends to provide the reader with guidance on how to make a first attempt at creating an electronic publication. 

As we said at the beginning of this introduction, 'you must change your life', so there may be something of a culture shock while reading through this document. If electronic publishing is to be no more than an afterthought in the production chain and the product portfolio, the amount of change may be relatively small. However, if electronic publishing is to become just as important as print, the change may be radical. What this means is that if you wish to make visual electronic publications, you should be willing to change your current way of working, and to gradually get used to the less mainstream alternatives offered here. 


## How to use this Toolkit 

The Toolkit aims to provide a practical guide on how to develop electronic publications, for publishers as well as for anyone else interested in this subject matter. The Toolkit will attempt to provide insight into the preconditions of electronic publishing, providing Open Source tools where possible, and to allow publishers active in the art and culture sector to navigate the diverse and complex landscape of digital publishing in a more informed way. 

Furthermore, the Toolkit will help the reader to develop e-publications, specifically art and design 
publications, which generally make use of a greater variety of fonts, graphics and layout than publications focused exclusively or mainly on text. 

After going into the basics of (electronic) publishing in Chapter 2, Chapter 3 will provide a general introduction to these publications, sketching out various scenarios on how to develop e-publications. We will discuss a number of issues and opportunities in going electronic. In Chapter 4 we focus on the strengths and limitations of specific types of e-reader hardware and software, different file formats, moving on to describe a number of distribution platforms in Chapter 5. In Chapter 6 we give a step-by-step guide to creating your own EPUB, Chapter 7 offers a practical, how-to guide for workflows (both structured and specific to each scenario) and finally in Chapter 8 we go into designing electronic publications for the various scenarios addressed earlier. In Chapter 9 we look into the future of e-publishing. The manual ends with a glossary and a description of the developed software within the different project groups. 

We wish to stress here that the structure of the manual isn't as linear as this outline may suggest. Particularly further on in the manual, some of the terminology may seem confusing at first, but will be explained in more detail later. We chose to focus on delivering a practical how-to guide for e-publishing, starting with the step-by-step guide to creating an ebook (in Chapter 6) and leaving the more detailed argumentation for the next chapters (particularly Chapter 7). 


## Who worked on this Toolkit 

This publication is part of the Digital Publishing Toolkit [^DPT-blog] RAAK-MKB [^RAAK-MKB] research project. The following research question was stated: *'In what way can a platform be created with new tools for Open Source publishing, which will allow publishers in the sector of art and culture to produce interactive e-publications by themselves?'* 

To answer this research question, the Institute of Network Cultures (lectoraat Netwerkcultuur) of the Amsterdam University of Applied Sciences, and the Research Centre Creating 010 (kenniscentrum Creating 010) of the Rotterdam University of Applied Sciences jointly conducted state-of-the-art research. In collaboration with an already existing consortium [^DPT-Consortium] of eleven small businesses including publishers, designers and developers, five sub-projects were formulated. Within these sub-groups, publishers, designers and developers, researchers and students of the participating applied universities collaborated. 

The result is the present publication, as well as a software repository consisting of tools for electronic publishing, based on Open Source software of which the source code is published and freely accessible[^DPT-GitHub]. With a single command, one can get hold of the code repository, downloading not only the current state of 'source' files for the book, but also the full history of changes and comments made by each collaborator to the Toolkit up to that point. With another command, the various 'sources' are pulled together into an EPUB produced at that moment. In this way both the 'content' and the 'machine' used for making the book are bundled and shared. 

We are not claiming that all ebooks will follow, or should follow this path. We are simply laying out one of the many directions ebook creators can already take with their publications, by using simple and inexpensive tools, and without needing to buy into the industry's glossy scenarios of multimedia and interactivity. 

[^DPT-blog]: *Blog of the Digital Publishing Toolkit research program*, http://networkcultures.org/digitalpublishing. 
[^RAAK-MKB]: http://www.innovatie-alliantie.nl/stimuleringsregeling/regeling/item/54-raak-mkb.html. 
[^DPT-GitHub]: http://networkcultures.org/digitalpublishing/github/. 
