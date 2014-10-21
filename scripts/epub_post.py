#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys, zipfile, os, shutil, glob, textwrap
from os.path import join
from xml.etree import ElementTree as ET
import html5lib
import argparse
#####
# EDITING TOOLKIT.EPUB AFTER ITS CREATION, TO:
# * introduce classes to BLOG LINKS
# *
###

## STEP 1: unzip epub
filename = sys.argv[1]


# unzip ePub
fh = open(str(filename), 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    outpath = "temp"
    z.extract(name, outpath)
fh.close()

## STEP 2:  Do Changes

### Changes defs
def addclass_bloglink(tree, element): # add class=bloglink to blog icon images
    for tag in tree.findall(element):
        tag.set('class', 'bloglink')


temp_ls=os.listdir("temp/")

for f in temp_ls: # 2.1: Do loop content files
    if f[:2]=='ch' and f[-6:]==".xhtml": # all ch*.xhtml
#        print f
        filename = "temp/"+f
        # 2.2 Parse each file
        xhtml = open("temp/"+f, "r") # open and parse
        xhtml_parsed = html5lib.parse(xhtml, namespaceHTMLElements=False)

        addclass_bloglink(xhtml_parsed, './/img[@alt="Bloglink"]')

        html = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n' + ET.tostring(xhtml_parsed, method="xml", encoding="utf-8")
        edited = open(filename, 'w') #write
        edited.write(html)

# Step 3: zip epub
epub = zipfile.ZipFile("toolkit_post.epub", "w")
#epub.writestr("mimetype", "application/epub+zip")
temp_dir = "temp"

def fileList(source):
    matches = []
    for root, dirnames, filenames in os.walk(source):
        for filename in filenames:
            matches.append(os.path.join(root, filename))
    return matches
dirlist=fileList(temp_dir)

for name in dirlist:
    path = name[5:] # removes temp/
#    print path
    epub.write(name, path, zipfile.ZIP_DEFLATED)
epub.close()


# Step 4: clean up: rm temp zipname
shutil.rmtree(temp_dir)



