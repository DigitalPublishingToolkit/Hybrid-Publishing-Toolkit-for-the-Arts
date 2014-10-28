# 01 Introduction 

'You must change your life' - borrowing from philosopher Peter Sloterdijk, this could be the summary of our message for art and design oriented publishers, writers, editors and designers who are transitioning from traditional book making to electronic publishing or - more typically - hybrid print and electronic publishing. Hybrid publishing will sooner or later confront them with the following: (a) rethinking of traditional publication formats, for example, a catalog, (b) rethinking of editorial and production workflows and (c) rethinking of distribution. The changes that need to be made might be greater and more extensive than initially expected! 


*Change is minor for scientific and mass publishers*

With that said, there are exceptions. Workflow changes can be minor for publishers who already accomplish all their editorial work in highly structured digital document formats (such as XML or databases); but typically, this is only the case in scientific and technology-oriented publishing. Changes might also be minor for larger publishers that can afford outsourcing. Making an electronic (digital) publication next to a printed publication then is simply a matter of paying an external service provider such as a document engineering company or a media design bureau for turning a Microsoft Word or InDesign file into an ebook. This process can be quick if the book is visually simple - such as a novel or a textbook with little illustrations - and economic if many ebooks will be sold. 

*Change is major for small, arts-oriented publishers*

Since this Toolkit is for publishers who (a) publish visually oriented books in (b) mostly smaller print runs, it proposes an alternative route. Neither a complex internal IT infrastructure, nor costly outsourcing will be viable solutions for them. But, to disappoint a common expectation, there is no magic software button that will turn a print book design into an electronic publication. Since the two media are so different, with their own specific editorial and visual design needs, such a button will probably not materialize in the future either. Hybrid publishing will ultimately require editorial work to change, both technologically as well as where editorial concepts<!--Amy: what is meant by 'concepts' in this context?--> are concerned.

For art and design publishers, the challenge of going electronic with their publications is greater compared to other fields of publishing for a number of reasons: 

- visually oriented publications are still more difficult to technically realize in the electronic medium when designing for a multitude of different reading devices and ebook platforms; 
- small publishers are under high pressure to keep project costs low due to often smaller budgets - but having to publish in multiple forms (e.g. print and electronic) will increase costs unless one accomplishes as much work as possible in a way that is not the dependent on the medium; 
- To make the investment in a digital publication durable it is necessary that electronic publications are sustainable: they should not need constant investment into technical maintenance and version updates.

## Industry promises versus reality

We face a major contrast between computer industry promises and the reality of the new digital medium. On the one hand, publishers, editors, designers and artists tend to overestimate the interactive and multimedia possibilities of electronic publishing. These extra possibilities do exist, but in most cases cause higher development costs and remain specific to one particular technical reading platform.

On the other hand, publishers tend to underestimate how even technically simple and seemingly banal types of electronic publications can lead us to rethink established publishing practices and formats. When traditional publishing formats go electronic or hybrid, the possibility for transformation is real. Once the book becomes electronic or hybrid, the permanence, immutability and stability typical of physical books, is likely to mutate into dynamic, modular, and participative forms, that can benefit from the networked environment where ebooks exist. 

Seemingly banal types of electronic publications can be subject to significant change. An exhibition catalogue, can for instances be split up into interrelated micro-monographs that readers can download and read as individual ebooks. An ebook can be assembled from a variety of sources selected by the reader, as currently happens in Wikipedia, where the visitor can compile her own collection of Wikipedia articles and export them to an EPUB or PDF using the [Book creator tool](http://en.wikipedia.org/wiki/Help:Books).  Or an anthology of essays might allow annotations from all its readers to grow around its contents.

The possibility for change can also go beyond rethinking publishing formats and expand to redefine what the book is. As in the case of this publication, the adopted workflow brings into question aspects often seen as inherit and essential to books. For instances, instead of a single author, its authorship is shared by a number of collaborating authors. Several writers, designers, developers and editors, sometimes under more than one hat, actively contribute to this publication. They write, edit, design, create illustrations, comment, and develop scripts, that collectively lead the publication into its final from, which you are likely to be reading at this very moment. Each single contribution is entrusted to eyes and hands of the other co-authors by being uploaded to publication's [code repository](https://github.com/DigitalPublishingToolkit/Hybrid-Publishing-Toolkit-for-the-Arts) — an online pool, where all the files essential to the publication are stored and tracked over time. The public availability such files, not only provide a window on to the book's development, since it began, but in tandem with the book's free-culture license — [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/) —, they give carte blanche for anyone to alter its content, or even publish it ahead of its *original* publisher. All one has to do is type into a command-line interpreter:

`git clone https://github.com/DigitalPublishingToolkit/Hybrid-Publishing-Toolkit-for-the-Arts` 

By doing so all source files and scripts that constitute the publication will be downloaded. Following that first step one can invoke the command:

`make toolkit.epub` 

Consequently this publication will be compiled into its digital publishable form, ready to be read, sent around, or uploaded to somewhere on the Web.

We are not claiming that all ebooks will follow, or must follow this path. We are simply laying out one of the many directions ebook creators can already undertake with their publications, by using with simple and inexpensive tools, and without needing to get into the industry's glossy scenarios of multimedia and interactivity. 


## What this Toolkit provides

Going electronic - or going hybrid - means that you need to change the way you work in the publishing process from manuscript to publication. The software tools currently in use, from word processors like Microsoft Word to desktop publishing suites like InDesign, were created for the analog or desktop-publishing world. Although it's possible to create electronic publications from Microsoft Word [![Bloglink](images/dpt_blog_verwijzing.png)](http://networkcultures.org/digitalpublishing/2014/03/28/converting-a-docx-directly-to-epub-using-calibre/ "Link to blog post: Converting a DOCX directly to EPUB using Calibre") and InDesign [![Bloglink](images/dpt_blog_verwijzing.png)](http://networkcultures.org/digitalpublishing/2013/05/21/epub-development-in-adobe-indesign-cs6/ "Link to blog post: NOTES ON EPUB DEVELOPMENT IN ADOBE INDESIGN CS6") files that are likely the standard in the current publishing workflow, it will be painful, slow, inefficient and expensive in most cases. This Toolkit describes technical Do It Yourself (DIY) alternatives because it is primarily aimed at publishers who, in most cases, cannot afford to outsource ebook design to external service providers and furthermore it is aimed at those who want to keep the process in their own hands. 

This Toolkit has a particular (but not exclusive) focus on EPUB3 as an electronic publication format and on Markdown as a word processing format because of the specific needs of small edition publishers in the art and design field: low cost, ease of use, sustainability and
platform-independence. The recommendations stem from our practical experience in collaborating with four Dutch art, design and research publishers on electronic publication projects.



## Whom is this Toolkit written for

You may be a publisher, a designer or someone who is just starting out with making books. You probably identify with or work in the arts. You may hope to gain answers, knowledge, get tips, and consult various resources. This Toolkit intends to provide them all. The overall focus is on pragmatic solutions for publishers within the art and cultural sector. No prior knowledge of creating an ebook is required – with that said, a familiarity of various computer software is helpful, as is the willingness to learn and the inquisitive curiosity to look beyond this guide for certain answers. This publication is not a tutorial on how to make an electronic publication, it merely intends to give the reader guidance on how to make a first attempt at creating an electronic publication.

As mentioned before 'you must change your life', so there might a little culture shock reading through this document. If electronic publishing will merely remain an afterthought in the production chain and product portfolio, the change might be light. If electronic publishing will become just as important as print, the change may be radical. What this means is that if you want to make visual electronic publications, you should be willing to change your current way of working and gradually get used to the offered but less common alternatives.



## How to use this Toolkit 

The Toolkit aims to provide a practical guide on how to develop electronic publications
for publishers as well as for anyone else interested in this subject matter. It will attempt to give insight into the preconditions of electronic publishing, providing open-source tools where possible, and allow publishers of the art and culture sector to navigate the diverse and complex landscape of digital publishing in a more informed way.
Furthermore, the Toolkit will help the reader to develop e-publications, specifically art and design
publications, which generally make more use of different fonts, graphics and layout than text-dominant publications. 
Chapter 3 will give a general introduction of these publications and sketches out various scenarios on how to develop e-publications. Issues and opportunities of going electronic will be discussed, as well as strengths and limitations of particular reader hardwares and softwares, file formats and lastly distribution platforms. Chapters 4 offers a practical, how-to guide to workflows (both structured and per scenario) and designing electronic publications for the various scenarios addressed earlier in Chapter 3. Chapter 5 illustrates the concepts with concrete examples from the The Hybrid Publishing Toolkit For The Arts, A Guide From Print To Ebooks project.


## Who worked on this Toolkit

This publication is part of the Digital Publishing Toolkit [^DPT-blog] RAAK-MKB [^RAAK-MKB] research project. The following research questions was stated: *'In what way can a platform be created with new tools for open source-publishing, by which publishers in the art- and cultural sector can produce interactive e-publications by themselves?'*

To answer this research question, the Institute of Network Cultures (lectoraat Netwerkcultuur) of the Amsterdam University of Applied Sciences and knowledge centre creating 010 of the Rotterdam University of Applied Sciences executed state-of-the-art research. In collaboration with an already existing consortium [^DPT-consortium] of eleven MKB-companies consisting of publishers, designers and developers, a fivesome subprojects were formulated. Within these subgroups publishers, designers and developers, (research)lecturers and students of the participating applied universities collaborated.

The result is this publication and a toolkit that exists of tools for digital publishing, based on open source-software of which the source code is published and freely accessible[^DPT-GitHub]. As a result everyone can freely copy, adjust and distribute the tools. Five e-publications of titles of the art- and culture books fund of the participating publishers were produced and presented on a platform that is developed for that purpose. 


[^DPT-blog]: Blog of the Digital Publishing Toolkit research program, http://networkcultures.org/digitalpublishing
[^RAAK-MKB]: http://www.innovatie-alliantie.nl/stimuleringsregeling/regeling/item/54-raak-mkb.html.
[^DPT-GitHub]: http://networkcultures.org/digitalpublishing/github/
[^DPT-Consortium]: http://networkcultures.org/digitalpublishing/consortium/

