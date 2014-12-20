#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys, zipfile, os, shutil, glob, textwrap
from os.path import join
from xml.etree import ElementTree as ET
import html5lib
import argparse
"""
(C) 2014 Andre Castro

License: [GPL3](http://www.gnu.org/copyleft/gpl.html)
"""

"""
Script enhances the EPUB created from from Pandoc conversion to EPUB3, namely:

* Removes <sub> from footnotes, since these interferes with the iPad response; relies on CSS instead 
* Replaces back arrows - '↩' - with work 'back'
* add class='bloglink' to blog icon images - for CSS a:hover
* makes cover linear inside content.opf <spine>

"""

filename = sys.argv[1]
# unzip ePub
fh = open(str(filename), 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    outpath = "temp"
    z.extract(name, outpath)
fh.close()
temp_dir="temp/"
os.remove(temp_dir+'mimetype') # delete mimetype (will be added later with epub.writestr)



def fn_rm_sup(tree, element): # Removes Footnotes <sub>
    for fn in tree.findall(element):
        for child in list(fn):
            if child.tag == 'sup':                
                number = child.text
                fn.remove(child)
                fn.text=number


def replace_fn_links(tree, element): #replace back arrows with work "back"
    for tag in tree.findall(element):
        if tag.text is not None:
            text=(tag.text).encode('utf-8')
            if text == '↩':#'&#8617;':
                tag.text = 'back'


def addclass_bloglink(tree, element): # add class=bloglink to blog icon images
    for tag in tree.findall(element):
        tag.set('class', 'bloglink')

def figure(tree, element): # insert <div> inside <figure> tp wrap <img>
    for tag in tree.findall(element):
        figure = tag.find('./figure')
        img = tag.find('./img')  # find child elements' atrib
        img_src = img.get('src')
        figcaption = tag.find('./figcaption') #to img alt & figcaption text
        if figcaption is not None:
            figcaption_txt = figcaption.text
        else:
            figcaption_txt = ""
        tag.clear() # clear child elements
        new_fig = ''' <figure>
  <div class="fig">	      
  <img class="fig" src="{src}"
  alt="{caption}" />
  </div>
  <figcaption>{caption}</figcaption>
</figure>
'''.format(src=(img_src.encode('utf-8')), caption=(figcaption_txt.encode('utf-8'))) # new children
        new_fig = new_fig.replace('&', '&amp;')
        new_fig_tag = ET.fromstring(new_fig)
        tag.extend(new_fig_tag) # insert into figure

def spine(filename): # makes cover linear is <spine>
    tree = ET.parse(filename)
    ET.register_namespace('epub', 'http://www.idpf.org/2007/ops')
    spine = tree.find('.//{http://www.idpf.org/2007/opf}spine')
    manifest = tree.find('.//{http://www.idpf.org/2007/opf}manifest')
    for child in spine.getchildren():
        if child.attrib['idref'] == 'cover_xhtml':            
            child.attrib['linear'] = 'yes'
    return tree

        
def save_html(content_dir, content_file, tree ):
    doctype = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n'
    html = ET.tostring(tree,  encoding='utf-8', method='xml')
    html = doctype + html
    xhtml_file = open(content_dir + content_file, "w") 
    xhtml_file.write(html) 
    xhtml_file.close()


temp_ls=os.listdir("temp/")
temp_ls.sort()

for f in temp_ls: 
    if f[:2]=='ch' and f[-6:]==".xhtml": # all ch*.xhtml        
        filename = "temp/"+f
        xhtml = open(filename, "r") 
        xhtml_parsed = html5lib.parse(xhtml, namespaceHTMLElements=False)
        fn_rm_sup(xhtml_parsed, './/a[@class="footnoteRef"]')
        replace_fn_links(xhtml_parsed, './/li/p/a')
        addclass_bloglink(xhtml_parsed, './/img[@alt="Bloglink"]')
#        figure(xhtml_parsed, './/figure')
        save_html(
            content_dir=temp_dir,
            content_file=f,
            tree=xhtml_parsed )
        
    elif f == 'content.opf':
        filename = "temp/"+f
        xhtml = open("temp/"+f, "r")
        tree = spine(filename)
        ET.register_namespace('', 'http://www.idpf.org/2007/opf')
        tree.write(filename, encoding='utf-8', xml_declaration='True' )

        
# Step 3: zip epub
epub = zipfile.ZipFile("FromPrintToEbooks.epub", "w")
epub.writestr("mimetype", "application/epub+zip")
temp_dir = "temp"

def fileList(source):
    matches = []
    for root, dirnames, filenames in os.walk(source):
        for filename in filenames:
            matches.append(os.path.join(root, filename))
    return matches

dirlist=fileList(temp_dir)

for name in dirlist:
    path = name[5:] # removes 'temp/'
    epub.write(name, path, zipfile.ZIP_DEFLATED)
epub.close()


# Step 4: clean up: rm temp zipname
shutil.rmtree(temp_dir)

print
print "** FromPrintToEbooks.epub was generated without errors **"

