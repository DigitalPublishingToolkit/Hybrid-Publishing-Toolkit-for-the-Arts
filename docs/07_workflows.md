# Workflows


## General

Flow charts: workflows <!-- Loes & Kimmy -->

From single medium to cross-media/hybrid publishing.

From-scratch development of each publication format vs. single source-multi format publishing: advantages, disadvantages

In-house development versus outsourcing to service providers: advantages, disadvantages

Why new workflows are essential for small edition, low budget publishing.


##Structured Workflow //executive management advice /workflow choice

<!--Kimmy was working on this, please take over!-->

<!--executive management advies /keuze van workflow-->

Flow charts: workflows

### Single source cross-media with established software tools (Word, InDesign)

Advantages, limitations

### XML

Advantages, limitations

Does it work for me?

### Markdown

[Advantages, limitations](docs/markdown-advantages.md)

[Is it an easier alternative to XML?](docs/markdown-vs-xml.md)

[Practical tips and tricks](docs/markdown-tips.md)

### Database publishing / Content Management System


Flow charts: workflows

##Single source cross-media with established software tools (Word, InDesign)

###Advantages, limitations
The current workflow of desktop publishing, from Word to inDesign, has certain advantages. It is simple, linear, there are no version branches, you end up with one consolidated manuscript, and What You See Is What you Get in relation to design. In the case of print changing hyphenation is for instance both an editing and a typographic problem. When changing to digital these hyphenations can no longer be determined before going to 'print', they change according to the aspect ratio of the device you are using. <!-- perhaps this is more clear? For example, in the case of analogue print where the page is fixed, changing hyphenation is both an editing and a typographic issue. However when transitioning into digital publishing, these hyphenations will be subject to change as they'll change according to the aspect ratio of the device you are using. --> 


The main disadvantage of this workflow is that you only target one medium and the step to go from here to digital are cumbersome, and do not make full use of it's potential. It tries to implement the print into the digital, keeping the workflow one-dimensional. Working with the established software tools - Word and InDesign - it does this almost literally by allowing you to create quirky and strange 'interactive' publications in PDF, which in the end is a static inDesign document, upgraded with some interactive layers. This is a very limited vision on what the possibilities are for digital publishing. Next to this it is possible to export your publication as an .ePub from InDesign, however it is not developed as a program to produce e.pubs and the results are very messy and requires extra steps for the designer. (For a full description of InDesign to Epub see Elizabeth Castro's Epub Straight to the Point) 

###E-publishing as additional requirement

Before going the hybrid publishing way, another possibility is having a digital publishing workflow as an additional requirement. This is doable <!-- alternative suggestion: 'feasible' --> if e-pub is a secondary market for the publisher. This workflow still starts from Word and, or inDesign documents, and centers around outsourcing the document engineering to external partners, mostly in India. These engineers work with semi-automized software that translate one document format to another, making sure the document is structured. However, the more you use these companies the more problematic it becomes as the costs will explode. For each document, but also every platform you would need to ask these companies to make a translation. 


1. **InDesign** will never become a hybrid publishing tool as it is (too) specifically developed for print design. 

2. **Word** (or any other text editor that uses this approach, for instance Open Office) will never become a structured text processor. It is a hybrid of a text editor, a desktop program with typographic attributes, and something like a semantic mark-up program. <!--perhaps you can describe what 'mark-up program' is, and some other exmaples? also, perhaps a clear definition is something to consider putting in the general introduction to workflows? --> To a certain extent you can work in a structured manner using stylesheets - determining for instance different types of headers. However, the big problem is that these programs don't enforce working in this structured manner. If only one person doesn't use these stylesheets, but uses manual formatting (instead of structuring!), the whole document is messed-up. The problem with these programs is that there is no separation between formatting and structure, as if these two are equal to each-other, but especially in the world of digital publishing this is not the case.


![INC Current Workflow](../_in_progress/workflowINC__Current_v01.svg "INC Current Workflow")



##XML

Advantages, limitations

Does it work for me?

##Markdown

Advantages, limitations

Is it an easier alternative to XML?


##Database publishing / Content Management System

<!--shouldn't we add html and use of tools like calibre / pandoc? A large part of the workflow can stick with Word and use these tools to convert to the necessary output. Or is this part of Single source cross media? Or will these technical things be discussed in the next part - design your own epub?-->




NOTES FROM FLORIAN'S TALK
##Desktop Publishing
The current workflow of desktop publishing, from Word to inDesign, has certain advantages. It is simple, linear, there are no version branches, you end up with one consolidated manuscript, and What You See Is What you Get in relation to design. In the case of print changing hyphenation is for instance both an editing and a typographic problem. When changing to digital these hyphenations can no longer be determined before going to 'print', they change according to the aspect ratio of the device you are using. 

The main disadvantage of this workflow is that you only target one medium and the step to go from here to digital are cumbersome, and do not make full use of it's potential. 

####Adobe's vision
Adobe's vision on digital publishing leans too much on this old workflow. It tries to implement the digital into the print, keeping the workflow one-dimensional. It does this almost literally by allowing you to create quirky and strange 'interactive' publications in PDF. (The static inDesign document, upgraded with some interactive layers. `maybe elaborate a bit further on why these documents are so quirky / why they do not take full advantage of 'being digital'.`) This is a very limited vision on what the possibilities are for digital publishing. Essentially, it allows you to put your PDF publication in iTunes so you can get it on your iPad. However, as Florian emphasizes, you shoot yourself in the foot when only publishing to Apple's platform. The market is becoming more and more diverse, and Apple no longer has a monopoly over it. It went from 30% to an 11% market share. (`what was the source of these numbers?`)

####E-publishing as additional requirement
Another possible workflow, before going the hybrid publishing way, is having digital publishing as an additional requirement. This is doable if e-pub is a secondary market for the publisher. This workflow still starts from Word and, or inDesign documents, and centers around outsourcing the document engineering to external partners, mostly in India. These engineers work with semi-automized software that translate one document format to another, making sure the document is structured. However, the more you use these companies the more problematic it becomes as the costs will explode. For each document, but also every platform you would need to ask these companies to make a translation. 

##Hybrid Publishing!
Hybrid publishing is a way to overcome these endless conversions and high costs. In this workflow you make a version of the document that can be changed to all publishing platforms.

####Problems of Technology
In relation to this shift of workflows it is important to acknowledge the limitations of the computer programs publishers currently work with and have designed their workflows around.

1. **InDesign** will never become a hybrid publishing tool as it is (too) specifically developed for print design. (`can you elaborate a little on this?`)
2. **Word **(or any other text editor that uses this approach, for instance Open Office) will never become a structured text processor. It is a hybrid of a text editor, a desktop program with typographic attributes, and something like a semantic mark-up program. To a certain extend you can work in a structured manner using stylesheets - determining for instance different types of headers. However, the big problem is that these programs don't enforce to work in this structured manner.  If only one person doesn't use these stylesheets, but uses manual formatting (instead of structuring!), the whole document is messed-up. ( `maybe explain a bit further what gets messed-up? why is it such a big deal to do this correctly and separate formatting and structure`)The problem with these programs is that there is no separation between formatting and structure, as if these two are equal to each-other, but especially in the world of digital publishing this is not the case.

####Solution
`*I missed this - can you expand on this?*`

You wrote: 
Solution
From the IT textbook:
1.	abstracting content from formatting
2.	i.e. abstracting information from display
3.	translating information to various displays

####Problems
`*I missed this - can you expand on this?*`

Problems
•	Easier for highly formal publications (research papers)
•	Difficult for visual publications
•	Visuals will always require made-to-measure design

####Technological considerations
In the digital publishing landscape there are certain technological consideration you should keep in mind. (For a more comprehensive overview of these issues see the post [Landscape Digital Publishing](http://digitalpublishingtoolkit.org/2013/07/landscape-digital-publishing-research-pdf/) and [Digital Publishing in Practice](http://digitalpublishingtoolkit.org/2013/06/digital-publications-in-practice/)). 

- **Screen sizes and ratios**: There are several devices with all their different sizes and aspect ratio's. 
- **Resolution and color**: They have their own resolutions and for instance do not always allow the use of color. 
- **File sizes**: The question here is how media-rich can you make an ebook before it exceeds your bandwidths or space on your reader?
- **File format requirements of distribution**: Several distribution platforms demand you create your ebook in a certain [file format](http://en.wikipedia.org/wiki/Comparison_of_e-book_formats). Apple for instance uses the .iBook format, forcing you to comply with their terms of use, which mean you can only sell your beautifully designed .ibooks through Apple's iBook store. But Amazon also developed their own .kf8 format. There is thus no standardization of file formats, and as a result you need to adjust your ebook to match the specifications of these different distribution platforms.

####The holy grail - XML extended markup language
The most detailed structuring language developed is XML. The advantage is that it is very clean, but on the other hand it is very difficult to work with. It is a purely semantic language - with a clear separation with formatting - allowing you to structure the document in a very detailed and thorough manner. These documents work like a database. The original XML document is your fundament, your manuscript, and from there you can create translations for every medium. Thus, if there is a misspelling or another error - you change this in your XML document and you make new translation to the different media that you have produced. For formatting you would need to add a second step, like for instance CSS stylesheets. However, because XML is so detailed it becomes too difficult to work with as the tagging systems become very complex.

####Pragmatic solutions
**CMS, or wiki's** also allow you to structure documents. Even Wordpress puts in certain semantics like a header, tag and comments. Moreover, from these platforms it is very easy to translate the content to other media. A disadvantage of these platforms is that it works with commercially owned databases. You do not have the source document on your own server, but you have to extract it from the service database. XML on the other hand can for instance be edited in any text editor, you can open it always and everywhere.

Another example that is more like XML, is **[xHTML](http://en.wikipedia.org/wiki/XHTML)** as solution. It has a proper separation between syntax, formatting and semantics. However the syntax is not very rich, you for instance don't have semantics for footnotes. (it is however possible to work around this). As a result you need strict discipline to write properly structured html.

**[Booktype](http://www.sourcefabric.org/en/booktype/)** is an open source platform developed by Adam Hyde to "help you publish and print digital books." It is comparable to Wordpress or Wiki, but developed for producing text heavy books. This would thus more be a pre-production tool; grooming the source document, and than give it to the designers who can make it esthetically appealing. But just like Wiki and Wordpress the source document is in their database.

**(Multi)markdown** seems to be the most pragmatic solution. It reads like normal text, it is popular, it has richer semantics than xhtml, and it separates structure from formatting. In a way you can see it as XML for dummies as it is more user friendly to use without loosing too much 'structuring power'. One disadvantage however is that you cannot make your own tags, you are stuck with what is given. Examples of MultiMarkdown tools for mac are [iawriter](http://iawriter.com), [mou app](http://mouapp.com) and [bywordapp](http://bywordapp.com). And for Windows you for instance have [Markdownpad](http://markdownpad.com).


##Conclusion
1. There is no holy grail, but there are better ones than the common used.
2. When you are forced to work with hybrid publications you have a problem if you don't change your workflow.


<!-- comments from Amy: perhaps some definitions or descriptions of what 'mark-up', 'semantic langauge' and 'restructured text' is after this part? -->



## Per scenario


### art/design catalogue like

traditional workflow vs. new workflow

###  artist's/designer's book

traditional workflow vs. new workflow

### research publication

Traditional, print oriented workflow for text-centred works, with additional illustrations / videos / resources online, and extended referencing and/or indexing  
See Kimmy's visualized workflow for the INC, which will be generalized for [research-type publications](researchlikepub.html)

* Editor works with author(s) on manuscript  
* Several versions going back and forth between different people in different roles (editor, author, copyeditor, designer)  
* Final version of the text will be in a text editor or Word format  
* This is then designed in InDesign  
* Corrections made on the print proof and added in the InDesign file  
* Certified PDF goes to printer  
* How to make an e-publication from InDesign - this is the big problem. Going from InDesign to ePub is not easy and needs a lot of manual work

*New workflow*  
This is why the new workflow is directed towards **hybrid input** and **hybrid output** - which leads to a **workflow that is also hybrid**, but centered around **a single 'archive format'** - the definitive version that enables multiple output. 

So instead of having a final text file (e.g. Word) which is changed in InDesign - both of which are not good formats to convert to an ePub, the storage / archive file has to be in a format that can translate into InDesign for the print edition and ePub / mobi / web for the e-publication. The most suitable format for this is **html** - because it allows footnotes (which Markdown does not). The html can easily be converted to ePub, though not so easily to InDesign... (working on this)

### arts/design periodical

traditional workflow vs. new workflow
