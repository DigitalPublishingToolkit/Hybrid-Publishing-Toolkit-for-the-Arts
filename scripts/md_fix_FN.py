#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(C) 2014 Andre Castro

License: [GPL3](http://www.gnu.org/copyleft/gpl.html)

This code has been developed as part of the [Digital Publishing Toolkit](http://digitalpublishingtoolkit.org).
with the support of Institute for [Network Cultures](http://networkcultures.org)
and [Creating 010](http://creating010.com).

"""

"""
CORRECTS INCORRECT FOOTNOTE REFERENCES,
eg: "or even non-existent. [^bible] Fixed page numbers and in".

NO empty space should come between a word, a fullstop, a semicolon, a comma and the footnote reference.
The correct way for footnotes references are: "word[^FN] other word", ".[^FN] Another sentence", ",[^FN] another thing"
"""

import re, sys, os

input_filename=os.path.abspath(sys.argv[1])
input_file = open(input_filename, "r") # open and parse
input_file_lines = input_file.readlines()
edited_text = ""

messy_FN_regex = '(\S)\s\[\^.*?\]'
messy_FN = re.compile(messy_FN_regex)

for line in  input_file_lines:
    line = line.decode("utf-8")    
    if re.search(messy_FN_regex, line):
        sub1 = re.sub('(?P<punct>\S)\s(?P<note>\[\^.*?\])', r'\g<punct>\g<note>', line)
        edited_text = edited_text + sub1
        print 'SUB', sub1
        print
        print '--------'
    else:
        edited_text = edited_text + line


# order_FN = '(?P<note>\[\^.*?\])(?P<punct>\.|\;|\,)'        
# order_FN_regex = re.compile(order_FN)
        
# for line in edited_text:
#     if re.search(messy_FN_regex, line):
#         print 'ORDER', line
# #         sub2 = re.sub('(?P<note>\[\^.*?\])(?P<punct>\.|\;|\,)', r'\g<punct>\g<note>' ,sub1)
# # #        edited_text2 = edited_text2 + sub2
# #         print 'SUB', sub2
# #         print
# #         print '--------'
# # #    else:
# # #        edited_text = edited_text + line



edited_file = open(input_filename, 'w') #write
edited_file.write(edited_text.encode("utf-8"))
edited_file.close()


## ISSUES
'''
####Calibre 
Calibre is an ebook management suite with a wide variety of features, including a few which are relevant in this particular context. (For a more detailed description of Calibre, see chapter 6.<!--- internal link needed -->) Calibre provides tools for managing large collections of ebooks, converting files to and from various formats (both ebook[^ebook] and other formats)[^calibre-file-formats], viewing all major ebook file formats, and even editing EPUB and AZW documents. 
'''

'''
[^amazon-kf8] ,[^ibooks]
'''

