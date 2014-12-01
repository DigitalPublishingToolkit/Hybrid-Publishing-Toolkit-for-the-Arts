#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, html5lib, re
from xml.etree import ElementTree as ET

###
# Adds back hyperlink references and back-references to the terms in the EPUBs glossary.
###

## TODO
# tackle problematic terms
# replace html5lib with built-in module
# integrate code on post_ script 

temp_dir="EPUB/" #temp/
temp_dir_ls=os.listdir(temp_dir)

def add_child(parent, element, myclass, myid, href, text, section):
    if section is 'glossary':
        link_wrap_before = ' [' 
        link_wrap_after = ']'
    else:
        link_wrap_before = '' 
        link_wrap_after = ' '

    child = ET.SubElement(parent, 'span' )
    child.text = link_wrap_before
    child.tail = link_wrap_after

    grandchild = ET.SubElement(child, element, {'class':myclass, 'href': href, 'id':myid})
    grandchild.text = text
#    grandchild.append('span', )
    

def find_unbold_term_in_text(term, gloss_file, search_dir):
    # def only intended to produce lists of terms in body matter that need to become bold
    # looks for files from Glossary outside <strong>
    xhtmls = [f for f in search_dir if f[:2]=='ch' and f[-6:]==".xhtml" and f != gloss_file and f != colophon_file ]  # all content, but glossary or colophon
    xhtmls.sort()
    for f in xhtmls: #try matching glossary term with term in body text
        xhtml_parsed = parse_html(temp_dir, f)
        p = xhtml_parsed.findall('.//p') # glossay terms in text are inside <p>TERM</p>       
        if p:
            for content in p:          
                if content.text is not None:
                    text = (content.text).encode('utf-8')
                    term = term.encode('utf-8')
                    if term in text:
                    # if term in text or term in text.capitalize() or term in text.lower():  # BUG: PROBLEMATIC TERMS
                        title = (xhtml_parsed.find('.//title')).text
                        msg = 'FOUND unbold glossary term: "{}" in file {}, section "{}"'.format(term,f,title)
#                        msg = term +"; "+ title
                        print msg
                        return term, title
                        break

                    
def find_term_in_text(term, gloss_file, search_dir): #find a match for each glossary term
    xhtmls = [f for f in search_dir if f[:2]=='ch' and f[-6:]==".xhtml" and f != gloss_file and f != colophon_file ]  # all content, but glossary or colophon
    xhtmls.sort()
    for f in xhtmls: #try matching glossary term with term in body text
        xhtml_parsed = parse_html(temp_dir, f)
        p_strong = xhtml_parsed.findall('.//p/strong') # glossay terms in text are iside <p>...<strong>TERM</strong>
        if p_strong:
            for content in p_strong:          
                if content.text is not None:
                    text = (content.text).encode('UTF-8')
                    if re.search(r'^{}$'.format(term), text, re.IGNORECASE):                        

#                    if term in text or term in text.capitalize() or term in text.lower():  # BUG: PROBLEMATIC TERMS
                        print 'MATCH TEXT:', text, '-', 'TERM:', term     ## Step 3.3: TEXT LINK: Add link to glossary_term                          
                        return content, xhtml_parsed, f
                        break

def strip_glossary_term(item): #remove whatever is inside parenthesis
    h5 = item.find('./h5')
    h5_text = h5.text
    reg_noparenthesis= re.compile(r'(.*)\s\(.*?\)')
    h5_term = re.sub(reg_noparenthesis, r'\1', h5_text)
    if ' or ' in h5_term:
        term_list=h5_term.split(' or ')
        
    elif ' / ' in h5_term:    
        term_list=h5_term.split(' / ')
    else:        
        term_list=[]
        term_list.append(h5_term)
    return term_list

def parse_html(content_dir, content_file ):
    xhtml = open(content_dir + content_file, "r")
    xhtml_parsed = html5lib.parse(xhtml, namespaceHTMLElements=False)
    return xhtml_parsed

def save_html(content_dir, content_file, tree ):
    doctype = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n'
    html = ET.tostring(tree,  encoding='utf-8', method='xml')
    html = doctype + html
    xhtml_file = open(content_dir + content_file, "w") # open and parse
    xhtml_file.write(html) 
    xhtml_file.close()

def find_chapter(glossary_title, search_dir):    
    # def looks for html file's <title>TITLE</title>
    xhtmls = [f for f in search_dir if f[:2]=='ch' and f[-6:]==".xhtml"]
    for f in xhtmls:
        xhtml_parsed = parse_html(temp_dir, f)
        title = (xhtml_parsed.findall('.//title'))[0].text
        if title in glossary_title:
            return(f, xhtml_parsed)


# files inside unziped EPUB (temp_dir)
glossary=find_chapter("11 Glossary of Technical Terms", temp_dir_ls)
gloss_file = glossary[0]
gloss_tree = glossary[1]
colophon_file=(find_chapter("Colophon", temp_dir_ls))[0]
gloss_terms = gloss_tree.findall('.//section[@class="level5"]') # find glossary terms

# loop through all glossary terms and find them in body text
for gloss_el in gloss_terms:
    gloss_term_list = strip_glossary_term(gloss_el)
    for term in gloss_term_list:
        print 'Glossary Term:', term
        found_term = find_term_in_text(term=term,
                                       gloss_file=gloss_file,
                                       search_dir=temp_dir_ls)
        if found_term is not None:
            text_term_el = found_term[0]
            text_tree = found_term[1]
            text_file = found_term[2]

            # add glossary reference hyperlink
            add_child(parent=text_term_el, 
                      element='a', 
                      myclass='glossref', 
                      myid='glossref_'+gloss_el.get('id'), 
                      href=gloss_file+'#'+gloss_el.get('id'), 
                      text='*',
                      section = 'body'
            )
            save_html(temp_dir, text_file, text_tree ) # save chapter file

            # add glossary term hyperlink
            add_child(parent=(gloss_el.findall('.//h5'))[0], 
                      element='a', 
                      myclass='glossterm', 
                      myid='glossterm_'+gloss_el.get('id'), 
                      href=text_file+'#'+('glossref_'+gloss_el.get('id')), 
                      text=u"back",
                      section = 'glossary'
            ) 

save_html(temp_dir, gloss_file, gloss_tree ) # save GLOSSARY FILE



# # finding unbolded glossary terms
# for gloss_el in gloss_terms:
#     gloss_term = strip_glossary_term(gloss_el) 
# #    print 'Glossary Term:', gloss_term
#     find_unbold_term_in_text(term=gloss_term, 
#                              gloss_file=gloss_file, 
#                              search_dir=temp_dir_ls)
