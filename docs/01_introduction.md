#1 Introduction 

<div class="summary"> 
- Hybrid print and electronic publishing requires new work methods and workflows. 
- Low-budget, small-edition, visually-oriented publications that are designed in-house will require more significant changes in work methods than big-budget publications for which the **ebook** design can be outsourced. 
- Interactive multimedia is still difficult to realize in books. Yet there are new opportunities for entirely new publication formats (such as books with customized content and micro-books). 
- This Toolkit focuses on low-budget, hybrid print and electronic books designed in-house using standard **software** and **Open Source** tools. 
</div> 

'You must change your life' - borrowing from the philosopher Peter Sloterdijk, this could be the summary of our message to art-oriented and design-oriented publishers, writers, editors and designers who are currently transitioning from traditional book making to electronic publishing or - more typically - **hybrid publishing** of print and electronic formats. Hybrid publishing will sooner or later confront them with the need to re-think traditional publication formats, editorial and production workflows, and distribution. The changes required may well be greater and more extensive than initially expected! 

*Change will be minor for scientific publishers and large publishers* 

Having said that, there are exceptions. Workflow changes can be also minor for publishers who already do all their editorial work in highly structured digital document formats such as **XML** or **databases**; but this is typically only the case in scientific and technology-oriented publishing. Changes may also be minor for larger publishers who can afford outsourcing. Generating an electronic (digital) publication in parallel to a printed publication is then simply a matter of paying an external service provider, such as a document engineering company or a media design agency, to turn a Microsoft Word or Adobe InDesign **file** into an ebook. This process can be quick if the book is visually simple - such as a novel or a textbook with few illustrations - and economically worthwhile if many ebooks will be sold. 

*Change will be major for small, arts-oriented publishers* 

Since this Toolkit - consisting of this manual and an [online software kit](http://networkcultures.org/digitalpublishing/github/) - is meant for publishers who publish visually oriented books in mostly smaller print runs, we propose here an alternative to the process mentioned above. Neither a complex internal IT infrastructure, nor costly outsourcing will be viable solutions for these types of publishers. Unfortunately, there is no 'magic' software button that will turn a print book design into an electronic publication just like that. Since the two media are so different, each with its own specific editorial and visual design needs, such a button is unlikely to materialize in the future either. Hybrid publishing will ultimately require changes in the way the editorial work is done. The good news is that such change is possible. This Toolkit includes instructions on how to deal with the many issues that arise when making the transition from traditional to hybrid or electronic publishing. 

For art and design publishers, the challenge of 'going electronic' with their publications is greater than that faced by other fields of publishing, for a number of reasons: 

- Visually oriented publications are still more difficult to realize technically in the electronic medium, particularly when designing for a multitude of different reading **devices** and ebook **platforms**; 
- Small publishers are under a great deal of pressure to keep project costs low, often due to smaller budgets. However, the need to publish in multiple forms (print and electronic) will inevitably increase costs, unless one does as much work as possible in a way that is not dependent on the medium; 
- In order to make the investment in an electronic publication durable, electronic publications must be sustainable: they should not require constant investment in technical maintenance and version updates. 

##Industry promises vs. reality 

There is a stark contrast between the fanciful promises of the computer industry and the often harsh reality of the new digital medium. On one hand, publishers, editors, designers and artists tend to overestimate the interactive and **multimedia** possibilities of electronic publishing. These extra possibilities do exist, but in most cases bring with them higher development costs and remain specific to one particular technical platform. 

On the other hand, publishers tend to underestimate how even technically simple and seemingly trivial types of electronic publications can in fact lead to a re-thinking of established publishing practices and formats. When traditional publishing formats are replaced by electronic or hybrid formats, there is a real possibility for transformation. Once the book becomes electronic or hybrid, the permanence, immutability and stability typical of physical books is likely to mutate into dynamic, modular, and participative forms. Such publications can greatly benefit from the networked environment in which ebooks exist. 

Various types of electronic publications may be subject to different kinds of change. Still, the change will always radical. An exhibition catalog for instance can be split up into interrelated micro-monographs which readers can download and read as individual ebooks. An ebook can be assembled from a variety of sources selected by individual readers, as is currently the case with Wikipedia, where visitors to the website can compile their own collection of Wikipedia articles and export this compilation to an **EPUB** or **PDF** document using the [Book Creator tool](http://en.wikipedia.org/wiki/Help:Books). 

The possibilities for change can go beyond the rethinking of existing publishing formats, eventually even redefining what a book actually is. 


##What this Toolkit provides 

'Going electronic' - or going hybrid - requires changing the way you work during the publishing process, from delivered manuscript to final publication. The software tools currently in use, from **word processors** such as Microsoft Word to **desktop publishing** suites such as Adobe InDesign, were created for the world of analog print and desktop publishing. Although it is entirely possible to create electronic publications from Microsoft Word documents [![Bloglink](images/dpt_blog_verwijzing.png)](http://networkcultures.org/digitalpublishing/2014/03/28/converting-a-docx-directly-to-epub-using-calibre/ "Link to blog post: Converting a Docx directly to EPUB using Calibre")(*Converting a Docx directly to EPUB using Calibre*) or InDesign documents [![Bloglink](images/dpt_blog_verwijzing.png)](http://networkcultures.org/digitalpublishing/2013/05/21/epub-development-in-adobe-indesign-cs6/ "Link to blog post: NOTES ON EPUB DEVELOPMENT IN ADOBE INDESIGN CS6")(*Notes on EPUB Development in Adobe InDesign CS6*), which are likely to be the standard format used in existing publishing workflows, in most cases this will be a painful, slow, inefficient and expensive process. This Toolkit focuses instead on do-it-yourself (DIY) technical alternatives. Firstly because the Toolkit is primarily aimed at publishers who, in most cases, cannot afford to outsource ebook design to external service providers; secondly because it is aimed at those who wish to keep the design process in their own hands. 

This Toolkit focuses particularly (but not exclusively) on EPUB3 as an electronic publication format, and on **Markdown** as a word processing format, because of the specific needs of small-edition publishers in the field of art and design: low costs, ease of use, sustainability, and platform independence. The recommendations stem from our practical experience in collaborating on electronic publication projects with four Dutch art, design and research publishers: BIS Publishers, Valiz, nai010 Publishers and the Institute of Network Cultures. 


##Who is this Toolkit written for 

You may be a publisher, a designer, or someone who is just starting out with making books. You probably identify with, or work in, the arts. You may be hoping to find answers, gain knowledge, pick up some tips, and consult various resources. This Toolkit intends to provide all of that. The overall focus is on pragmatic solutions for publishers within the sector of art and culture. No prior knowledge of creating an ebook is required. Having said that, a familiarity with various computer software **applications** is certainly helpful, as is the willingness to learn, and an inquisitive curiosity to look beyond this guide for specific answers. This publication is not meant as a complete tutorial on how to create an electronic publication; rather, it intends to provide the reader with basic guidance on how to make a first attempt at creating such a publication. 

As we said at the beginning of this introduction, 'you must change your life'; therefore, you may experience something of a culture shock as you read through this document. If electronic publishing is to be merely an afterthought in the production chain and the product portfolio, the amount of change may be relatively small. However, if electronic publishing is to become just as important as print, the change may be quite radical. In other words, if you are seriously interested in electronic publishing, you must be willing to change your current way of working, and to gradually familiarize yourself with the less mainstream alternatives offered here. 


##How to use this Toolkit 

The Toolkit aims to provide a practical guide on how to develop electronic publications, for publishers as well as for anyone else interested in this subject matter. The Toolkit will attempt to provide insight into the prerequisite conditions of electronic publishing, to suggest Open Source tools whenever possible, and to allow publishers active in the art and culture sector to navigate the diverse and complex landscape of digital publishing in a more informed way. 

Furthermore, the Toolkit will help the reader to develop electronic publications - specifically art and design publications, which generally make use of a greater variety of fonts, graphics and **layout** than publications focused exclusively or mainly on text. 

After a basic exploration in Chapter 2 of publishing in general and electronic publishing in particular, in Chapter 3 we provide a general introduction to electronic publishing, sketching out various scenarios on how to develop electronic publications and discussing a number of issues and opportunities in 'going electronic'. In Chapter 4 we focus on the strengths and limitations of various specific types of **e-reader** hardware and software as well as different file formats, before moving on to describe in Chapter 5 a number of distribution platforms. In Chapter 6 we provide a step-by-step guide to creating your own EPUB. Chapter 7 offers a practical, how-to guide for workflows (both generally structured and specific to each scenario) and finally in Chapter 8 we explore the design of electronic publications for the various scenarios addressed earlier. Finally, in Chapter 9 we look into the future of electronic publishing. The manual also includes a description of the software developed within the different project groups, and a glossary of terms. 

We wish to stress here that the structure of the manual is not as linear as the above outline may suggest. Particularly further on in the manual, some of the terminology may seem confusing at first, but will be explained in more detail later. 

##Who worked on this Toolkit 

This publication is an outcome of the two-year research and development project *Digital Publishing Toolkit* funded by the Dutch Stichting Innovatie Alliantie (SIA) as part of its[^DPT-blog] RAAK-MKB[^RAAK-MKB] program for innovation in small and medium-sized businesses. The project was based on the following research question: *In what way can a platform be created with new tools for Open Source publishing that will allow publishers in the sector of art and culture to produce interactive e-publications themselves?* 

To answer this research question, the Institute of Network Cultures (lectoraat Netwerkcultuur) of the Amsterdam University of Applied Sciences, together with the Research Centre Creating 010 (kenniscentrum Creating 010) of the Rotterdam University of Applied Sciences jointly conducted state-of-the-practice-oriented design research. In collaboration with an already existing consortium[^DPT-Consortium] of eleven small businesses including publishers, designers and developers, four sub-projects were formulated. Within these sub-projects, a number of collaborations took place between publishers, designers, developers, researchers, and students of the participating universities of applied sciences. 

The result is the present publication, as well as a software repository consisting of tools for electronic publishing, based on Open Source software of which the source code is published and freely accessible.[^DPT-GitHub] With a single command line, one can get hold of the code repository, downloading not only the current state of 'source' files for the book, but also the full history of changes and comments made by each collaborator to the Toolkit up to that point. With another command, the various 'sources' can be pulled together into an instantly produced EPUB document. In this way both the 'content' and the 'machine' used for making the book are bundled and shared. 

We are not claiming that all ebooks will follow, or indeed should follow this path. We are simply laying out one of the many directions ebook creators can now take with their publications, by using simple and inexpensive tools, and without having to buy into the industry's glossy promises of multimedia and interactivity. 

[^DPT-blog]: *Blog of the Digital Publishing Toolkit research program*, <a href="http://networkcultures.org/digitalpublishing">http://networkcultures.org/digitalpublishing</a>. 
[^RAAK-MKB]: Nationaal Regieorgaan Praktijkgericht Onderzoek SIA, <a href="http://www.regieorgaan-sia.nl">http://www.regieorgaan-sia.nl</a>. 
[^DPT-GitHub]: Digital Publishing Toolkit GitHub, <a href="http://networkcultures.org/digitalpublishing/github/">http://networkcultures.org/digitalpublishing/github/</a>. 
[^DPT-Consortium]: Digital Publishing Toolkit consortium, http://networkcultures.org/digitalpublishing/consortium/.
