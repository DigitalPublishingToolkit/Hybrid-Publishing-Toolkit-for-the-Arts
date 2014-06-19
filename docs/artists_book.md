# Artist's/designer's book

Lately, artists' and designer's books have grown from a niche phenomenon to a major genre within arts and design publishing. It could be argued that the book as an art or design object in its own right has become more prominent now that the function of the book as a generic carrier of information (such as in a telephone directory, a dictionary or a run-of-the-mill novel or non-fiction paperback) is increasingly taken over by the World Wide Web and by e-readers. 

The history of artists' books - or "bookworks", as the Mexican-Dutch writer and visual artist Ulises Carrión called them[^1] - is often traced to the beginnings of concrete poetry, Fluxus and conceptual art, and the artists' books (and book-like objects) made among others by Dieter Roth and Ed Ruscha. But one could just as well include the Bauhaus book series ("Bauhausbücher") of the 1920s, earlier Dadaist and Futurist pamphlets and self-published books, the books made in the 19th century Arts and Crafts movement and even 16th century illustrated books like Sebastian Brant's and Albrecht Dürer's "Ship of Fools" that were crafted in workshop collaborations between writers, visual artists and printmakers.

The common denominator of these books is that they defy easy categorization and genre characteristics, making it difficult to give standard recommendations for their design as electronic books. 

## Transfer from paper to electronic?

The more medium-specific an artist's book is, the less sense it makes to translate it 1:1 into an electronic book. Dieter Roth's sculptural book objects, for example, would change from book art works to mere depictions of book art workds when reproduced electronically. 

On the other hand, many contemporary artists, designers and media activists experimented with electronic publishing as a "poor" (i.e. simple low tech) medium of social sharing rather than a "rich" visual and tactile medium:
- In the 1980s and early 1990s, many makers of zines (do-it-yourself small press periodicals) became makers of _e-zines_, electronic zines that used dial-up computer bulletin boards and the Internet as noncommercial samizdat media. Their typical publication format were simple plain text files. Many e-zines worked around their technical limitations by using ASCII art, typograms as they had also been produced in 1960s and 70s concrete poetry on typewriters, and with homebrew formatting codes ("_" for underlines, "#" for headlines etc.), the immediate precursors of the Markdown format described here in this toolkit.
- In the early 1990s, there also existed a hacker culture of "disk mags" for the Commodore Amiga and Atari ST home computers. These electronic magazines were anonymously published on floppy disks and were based on self-written computer programs (factually, early "apps") that displayed their animated text and visual contents.
- Since the late 1990s, there have been a number of artist-run sites - textz.com, ubu.com, aaaaarg.org, monoskop.org - that offer free downloads of cultural theory and arts-related books, typically in simple formats such as plain text, PDF and epub.
In these examples, the focus is not on the book as a visual object, but on concepts and politics of its sharing and dissemination; in other words, artists' publishing as electronic samizdat. In such scenarios, artists' books as simple 1:1 transfers from print originals to electronic reproductions can make sense.

### Technical solutions for samizdat publications

For such activist or minimalist projects, the lowest technical denominator and most easily readable file formats are advisable:
- plain text (ASCII) as the most simple, compatible and minimalist solution
- single-file HTML. It is possible to directly embed images into an HTML file (without providing them as separate files); technical instructions can be found [here](...).
- PDF. This format is widely readble and best suited for faithfully reproducing print books, but limited in its readability on different devices and hardly editable (more explanation [here](...)).
- epub. This format is factually just HTML for offline reading, with improved publication meta data and improved compatibility to e-readers. Projects can very easily be made and provided both in HTML and epub.
Since the design of most samizdat books does not differ from that of [research publications](...) or other visually simple publishing formats, no special design advice is necessary here, except the principle of "worse is better": the smaller the file size, the most compatible and universally readable the file format, the better, even if this comes at the expense of typographic and visual quality. An plain text files, then, might be preferable to a nicely designed PDF file. 

## How to make visually oriented artists' books

### Pre-history and general issues

There is, factually, a rich tradition of artists' audiovisual electronic books: It began in the 1990s with hypertext and interactive multimedia literary experiments on floppy disk, CD-ROMs, later web sites and mobile apps. The [Electronic Literature Organization](http://eliterature.org) and the international research project [ELMCIP](http://elmcip.net/knowledgebase) document it extensively. Much of this documentation has become media archeology since multimedia formats have become obsolete: CD-ROM applications that no longer run on contemporary computers, websites whose links or plug-ins are no longer working or not compatible to today's browsers anymore. 

This problem was greater in the 1990s and early 2000s when working open, cross-platform multimedia standards barely existed. But even today, the rule explained in chapter ... <!-- cross-reference to Arjen's overview graph of non-visual vs. visual epublishing technologies--> still applies: The more complex the audiovisuality of an electronic book, the less compatible it will be to all kinds of different electronic reading devices, and the more technical updates it will likely need over the course of time. 

### Simple solutions

Electronic visual books can be made in very simple ways:
* As a sequence of images, embedded into an epub file <!-- add reference-->, a self-contained HTML file <!-- add reference--> or a PDF file.
* As a PDF file. PDF generally is the most easy-to-use straightforward format for visual publications in a universally working format.[^2] PDF documents can be graphically designed to work on different screen sizes, and resolution of embedded visuals can be decreased to keep the file size friendly for downloading. Still, the format is essentially limited to fixed document sizes and remains an electronic representation of printed matter. 
* Other standard file formats creatively (ab)used as document formats for visual books: animated GIF graphics files for the digital equivalent of flip books, for example, mp4 video files displaying a real-time book, mp3 audio files triggering abstract art on the volume meter display of an audio player, JPEG files with encoding artefacts of corrupted bits.[^3] 
* Self-contained HTML. <!--- explain the use of self-contained HTML with base64--->

(- iBooks author: medium solution between epub and PDF: example Badlands Unlimited)
(- self-contained HTML5)
(- epub 2, epub 3)
(- plain text: e-zines, BBS era e-books, typograms/typoscripts)


[^1]: Ulises Carrión, "The new art of making books", Aegean editions, 2001
[^2]: For long-time durability, the "PDF/A" format is preferable to run-of-the mill PDF. [PDF/A ](http://en.wikipedia.org/?title=PDF/A) stands for _archival PDF_ and is an ISO standard orginally crafted by Adobe in collaboration with non-profit organizations for information management. As opposed to generic PDF, PDF/A requires that all fonts, references and color profiles are fully embedded into a document.
[^3]: Used as a medium of artistic experimentation among others by net artists since the 1990s and by conceptual poet and Ubuweb founder Kenneth Goldsmith.
