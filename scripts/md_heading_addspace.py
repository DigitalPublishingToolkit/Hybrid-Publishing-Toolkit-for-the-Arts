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
ADDS AN EMPTY SPACE TO MARKDOWN HEADERS THAT AREN'T FOLLOW BY EMPTY SPACE
eg: "###3) One-to-database"  --> "### 3) One-to-database"

"""
h
import re, sys, os

input_filename=os.path.abspath(sys.argv[1])
input_file = open(input_filename, "r") # open and parse
input_file_lines = input_file.readlines()
edited_text = ""

h_nospace_regex = '(^#{1,5})(\w.*)'


for line in  input_file_lines:
    line = line.decode("utf-8")
    if re.search(h_nospace_regex, line):
        print line
        match = re.match(h_nospace_regex, line)
        replacement = "{} {}".format(match.groups()[0], match.groups()[1])
        edited_text = edited_text + replacement
        print 'REPLACEMENT:', edited_text
    else:
        edited_text = edited_text + line

    
        
for line in  input_file_lines:
    line = line.decode("utf-8")

edited_file = open(input_filename, 'w') #write
edited_file.write(edited_text.encode("utf-8"))
edited_file.close()


