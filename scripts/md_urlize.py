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
ULIZES MARKDOWN UNLINKED URLS

Notes: Avoid miss-formatted link in markdown source.
Miss-formatted markdown links like: [link] (http://url.to.link )
will be urlized, like this: [link] (<a href="http://url.to.link">http://url.to.link</a> )

 
Requires: django https://www.djangoproject.com/download/
"""

import re, sys, os
from django.utils.html import urlize

input_filename=os.path.abspath(sys.argv[1])

input_file = open(input_filename, "r") # open and parse
input_file_lines = input_file.readlines()
edited_text = ""

url_regex = '.*http[s]?://.*' # any url 
url_md_regex = '\[.*\]\(http[s]?://.*\)' # url in mardown link ()[http...]


for line in  input_file_lines:
    line = line.decode("utf-8")

    # search url # if is not already a mardown link
    if bool(re.search(url_regex, line)) == True and  bool(re.search(url_md_regex, line)) == False:
        line_urlized = urlize(line, nofollow=False)
        edited_text = edited_text + line_urlized


    else:
        edited_text = edited_text + line


edited_file = open(input_filename, 'w') #write
edited_file.write(edited_text.encode("utf-8"))
edited_file.close()


