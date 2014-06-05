Intro-Introduction for newcomers.

<<<<<<< HEAD
Because there exist no stupid questions but only stupid answers. There may be times when you're hesitant to ask questions in a situation where people around seem to know already. The function of this section is to solve your shyness. We explain the fundamentals of digital publishing in order to help the reader to formulate questions more precisely. 

**What is a text? **

A text is a collection of words and words are compositions of letters. In order to read a text we have all kinds of layout helpers. Keep in mind that in the Roman times (when texts were cut in stone) we had continuing writing: no spaces between the words. This was not considered a problem as reading was a craft only a few people mastered. These people knew the words and hence were able to read aloud, just try: Icanreadthiseasilyalound. In time, the craft of reading became a common good and many design helpers were introduced, such spaces between words, capitals at the beginning of new sentences, commas, semicolons, colons and line breaks. Also the notion of paragraphs, chapters, etc. developed into a standardized culture that allowed a smooth transmission between the structure the author endowed their text with and the reader who became familiar to these standards enabling the ease of reading and furthermore to do this silently. 

This whole structure of stratifying words into sentences, sentences into paragraphs and so on, including reading aids such as exclamation marks, bold and underscored text is called **markup**. It goes without saying
that all these **markup** elements demand stable definitions and clear relationships. Everybody is free to invent her/is own rules (e.g., every first letter of a new chapter is a well-decorated small picture). For example, in the time of handwritten manuscripts many “free style” inventions were made. Some of them remained in our time and became part of the expended alphabet. Think of the ampersand “&”, it originated from the conflation of an E and a t – we call this conflations, *ligatures*. Hence,
to be able to handle all vanities and define what we allow and what not, **Markup languages** emerged. 


Grammars that define the markup and the relation between markup elements. With the emergence of computer networks and the increasing need to standardize texts for multiple
usages (think about manuals), in 1982 an international ISO standard was established called: Standardised General Markup Language (SGML). This logically structured markup language was a big step forward, as it made a fundamental split between the text structure as such and the final
representation of that structure. For exmample, contrary to languages used in wordprocessors such as Tex, Latex, Word, MSWord, Wordperfect or ODF (open office document format), where presentation and text structuring are mixed, SGML only defines functions or roles. So, when we type using a word processor a **Bold** word in the text we in fact type “start bold” -\> type the word- \> “end bold”. What is happening here is a mixture of
structure and **Layout** . Layout is the activity of presenting a text onto a medium, such as a paper page. SGML and it derivatives, the easier HTML (hypertext markup languages) and the expanded XML (Extensible Markup Language) make a strict distinction between structure and
representation. A markup language knows notions such as “highlighted word or phrase” and then type 1,2,3... This allows you to equate e.g.: chapter heading with type1 and quotation with type 4. Depending on the output substrate you can then define in the layout phase how this will look like. For instance, a chapter heading is in a certain type font and font size and centred on the page, whilst a quotation is represented in the same corps and font of the running text but now in italics. On a screen we can have things like chapter heading in pink and
quotations are yellow. This layout freedom is then explicated in a so-called **style sheet**, which is a table that connects a layout schema with the markup schema. This way of working is imperative if we want to allow a source text to be represented on many different ways on various media of various size. Note, that in many programs these translations are done fairly invisibly to the user. If we translate a .odt file into a .docx file, in principle all coding is one-to-one translated. As we will see in the following translation between one file
type into another is not always symmetrical. Hence, the golden rule is to always make sure that the source text is as systemically structured as possible.

An important notion is that all text and accompanying coding are all written in simple letters and numerals, it is and remains **Flat text**. In short, a stripped down text without layout — the most elementary token. It goes without saying that the flexibility of this process is limited to the character set for flat text we use. In the “old” days this was ASCII based and limited to the possible number of distinct signs (letter,
numeral, comma, point, ..) of an 8 bit binary computer word. Slowly but firmly a new list of allowed signs is making inroads called: Unicode. It aims to include all alphabets and letter systems including common signs and ligatures. Again, this is step forward to guarantee a clean source file for all kind of usages, even those we don’t consider or even imaging today.

**What is an electronic text? **

An electronic text is normally understood as a text which is represented on a screen of some sort. Of course this is sloppy language. The key issue is that a text became a well-structured file in which the emotions and intentions of the author are translated into notions like
highlighted text of a certain type. Due to this markup, we become able to make different layouts, expressions, onto different media. It is of great importance to realise that electronic publishing introduces a big shift away from our page centred culture of book printing. In book
printing we allow for various sizes depending on the original works of the author. For example, if we make an art book based on a collection of paintings or drawings, we can decide what the ideal book size is and whether or not it will be printed in oblong form. In the world of screens this becomes very difficult as we have very different sizes of screens, but no screen can be cut to the demanded size as with paper book publishing. In electronic books we have to work around things in a completely different way as in the paper world. On the one hand this means that the transposition from an existing work to an electronic representation is rife with difficulties if the structure of the texts
and in particular if the relation between illustrations and running text is important. In the world of novels we normally have only running text. Here the page size is less important and this is the reason why ereaders
are becoming so popular. The text can always be made fitted to the size of the device, this is called** reflowable** text. In all other cases, we have to think deeper into how to design the work and under what conditions do we represent content and meaning. As will be discussed in the following chapters for various outlets we might opt for various versions of the original work. It goes without saying that the coming years, authors and designers will try and develop digitally born works that intrinsically allow for a variety of representations depending on the reading device whether it is electronic
or not.
=======
Because there exist no stupid questions but only stupid answers, this
does not mean that sometimes you may hesitate to ask a question as all
people around you suggest that they know already. The function of this
section is to solve your shyness. We explain the fundamentals of digital
publishing in order to help the reader to formulate questions more
precise.

**What is a text? **

A text is a collection of words and words are compositions of letters.
In order to read a text we have all kind of lay out helpers. Be ware
that in the Roman time (when texts were cut in stone) we had continuing
writing: no spaces between the words. This was not considered a problem
as reading was a craft only a few people mastered. These people knew the
words and hence were able to read aloud, just try:
Icanreadthiseasilyalound. In time, the craft of reading became a common
good and many design helpers were introduced, such spaces between words,
capitals at the beginning of new sentences, commas, semicolons, colons,
line breaks. Also the notion of paragraphs, chapters, etc. developed
into a standardised culture that allowed a smooth transmission between
the structure the author endowed her/his text with and the reader who is
used to these standards and can easily read, also silent.

This whole structure of stratifying words into sentences, sentences into
paragraphs and so on, including reading aids such as exclamation marks,
bold and underscored text is called **Markup**. It goes without saying
that all these markup elements demand stable definitions and clear
relationships. Everybody is free to invent her/is own rules (e.g., every
first letter of a new chapter is a well-decorated small picture). In
particular in the time of handwritten manuscripts many “free style”
inventions were made. Some of them remained in our time and became part
of the expended alphabet. Think of the ampersand “&” originated from the
conflation of an E and a t. We call this conflations, ligatures. Hence,
to be able to handle all vanities and define what we allow and what not,
**Markup Languages** emerged. Grammars that define the markup and the
relation between markup elements. With the emergence of computer
networks and the increasing need to standardise texts for multiple
usages (think about manuals), in 1982 an international ISO standard was
established called: Standardised General Markup Language (SGML). This
logically structured markup language was a big step forward, as it made
a fundamental split between the text structure as such and the final
representation of that structure. Contrary to languages used in
wordprocessors such as Tex, Latex, Word, MSWord, Wordperfect or ODF
(open office document format), were presentation and text structuring
are mixed, SGML only defines functions or roles. So, we type using a
word processor a **Bold** word in the text we in fact type “start bold”
-\> type the word- \> “end bold”. What is happening here is a mixture of
structure and **Layout** . Layout is the activity of presenting a text
onto a medium, such as a paper page. SGML and it derivatives, the easier
HTML (hypertext markup languages) and the expanded XML (Extensible
Markup Language) make a strict distinction between structure and
representation. A markup language knows notions such as “highlighted
word or phrase” and then type 1,2, 3... This allows you to equate e.g.:
chapter heading with type1 and quotation with type 4. Depending on the
output substrate you can then define yourself in the layout phase how
this will look like. For instance, a chapter heading is in a certain
type font and corps and centred on the page, whilst a quotation is
represented in the same corps and font of the running text but now in
italics. On a screen we can have things like chapter heading is pink and
quotations are yellow. This layout freedom is then explicated in a
so-called **style sheet**, which is a table that connects a layout
schema with the markup schema. This way of working is imperative if we
want to allow a source text to be represented on many different ways on
various media of various size. Note, that in many programs these
translations are done fairly invisible to the user. If we translate
an.odt file into a .docx file, in principle all coding is one-to-one
translated. As we will see in the following translation between one file
type into another is not always symmetrical. Hence, the golden rule is
to always make sure that the source text is as systemically structured
as possible.

An important notion is that all text and accompanying coding are all
written in simple letters and numerals, it is and remains **Flat text**.
It goes without saying that the flexibility of this process is limited
to the character set for flat text we use. In the “old”days this was
ASCII based and limited on the possible umber of distinct signs (letter,
numeral, comma, point, ..) Of an 8 bit binary computer word. Slowly but
firmly a new list of allowed signs is making inroads called: Unicode.
Unicode aims to include all alphabets and letter systems including
common signs and ligatures. Again, this step forward to guarantee a
clean source file for all kind of usages, even those we don’t consider
or even imaging today.

**What is an electronic text? **

We normally understand with an electronic text, a text which is
represented on a screen of some sort. Of course this is sloppy language.
The key issue is that a text became a well-structured file in which the
emotions and intentions of the author are translated into notions like
highlighted text of a certain type. Due to this markup, we become able
to make different layouts, expressions, onto different media. It is of
great importance to realise that electronic publishing introduces a big
shift away from our page centred culture of book printing. In book
printing we allow for various sizes depending on the original works of
the author. E.g. if we make an art book based on a collection of
paintings or drawings, we can decide what the ideal book size is and if
it will be yes or no printed in oblong form. In the world of screens
this becomes very difficult as we have very different sizes of screens,
but no screen can be cut to the demanded size as with paper book
publishing. In electronic books we have to work around things in a
completely different way as in the paper world. On the one hand this
means that the transposition from an existing work to an electronic
representation is rife with difficulties if the structure of the texts
and in particular if the relation between illustrations and running text
is important. In the world of novels we normally have only running text.
Here the page size is less important and this is the reason why ereaders
are becoming so popular. The text can always be made fitted to the size
of the device, this is called** reflowable** text. In all other cases,
we have to think deep how to design the work and under what conditions
do we represent what. As will be discussed in the following for various
outlets we might opt for various versions of the original work. It goes
without saying that the coming years, authors and designers will try and
develop digitally born works. Works that intrinsically allow for a
variety of representations depending of the reading device (electronic
or not).\
>>>>>>> FETCH_HEAD

