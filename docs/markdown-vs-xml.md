# Markdown versus XML

Markdown, and similar human-readable plain text markup languages could be called a "poor man's XML". They provide some of the same features and advantages: separation of content structure from visual layout, painless translation into multiple output formats. Their relative simplicity and human readability comes, however, at the price of extensibility and universality. XML is, strictly speaking, not a document markup language, but a meta-language (or toolkit) for building domain- and application-specific markup languages such as: a document markup language for exhibition catalogues, a document markup language for restaurant menus, a document markup language for flyers, etc. 

Markdown & Co. do not provide this flexibility of building one's own syntax, but provide only their built-in, hard-wired syntax. For example, if one needs syntax for encoding footnotes _and_ endnotes, MultiMarkdown simply doesn't provide it. One could think up and use one's own syntax extension (for example ^^[1] for an endnote), but this would not be supported by the word processing and text conversion programs for Markdown. In XML, there are standard methods of declaring and extending markup languages that can automatically be picked up by XML document converters.

However, the declaration of these extensions in the document syntax and conversion rules is highly complex. Even for computer scientists and engineers, XML is often so over-complex that they have resorted to simpler, human-readable language like Markdown, ReStructuredText and ASCIIdoc for software manuals.  

They are not as universal and thoroughly structured as XML, but still provide the advantage of separating content structure from visual layout, along with the advantage of painless translation into multiple output formats. And lastly, XML has very complex markup that is hard to read and write for humans. Easy authoring tools for XML and any kind of XML-based document formats do not really exist yet.

In short, and if the above sounded too cryptically technical: XML is complexity hell even by the measures of computer science. It's the holy grail of document processing, and has been deployed by large scale publishers (especially in the academic field) very successfully. For small to medium publishers, it is often overkill. Markdown provides a good middle-of-the-road solution of a format that is easily usable for non-technicians yet much better structured, and a basis for easy document conversion into HTML, epub and many other formats, than Microsoft Word and similar classical word processing programs.





