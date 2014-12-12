#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, sys, os


missing_terms=['Acronym', 'Algorithm', 'Android', 'Amazon', 'App', 'App store', 'Anchor', 'Animated GIF', 'Bandwidth', 'Binary', 'Bit', 'Blog', 'Browser', 'Browser extension', 'Byte', 'Compatiblity', 'Compressed files', 'Computer program', 'Content management system', 'Data', 'Database', 'Decompress', 'Device', 'Digital Rights Management', 'Directory', 'Dots per inch', 'E-reader', 'File', 'File extension', 'File format', 'File permissions', 'Folder', 'Formatting', 'Freemium model', 'Graphics Interchange Format', 'GitHub', 'HTTP', 'Hyperlink', 'Hypertext', 'Icon', 'Incompatiblity', 'Interactivity', 'Interface', 'Internet', 'JavaScript', 'JPEG', 'JPG', 'Kindle', 'LaTeX', 'Markup language', 'Monitor', 'MP4', 'MPEG-4', 'OCR', 'Open Source', 'Operating system', 'Pixel', 'Platform', 'Print on demand', 'Program', 'Rich Text Format', 'Server-side scripting', 'Software Development Kit', 'TIFF', 'Tumblr', 'Unix', 'Word processor', 'WWW']

#input_filename=os.path.abspath(sys.argv[1])
#input_file = open(input_filename, "r") # open and parse
#input_file_lines = input_file.readlines()

colophon_file="00_colophon.md"
gloss_file = "11_glossary.md"
avoid_files = [colophon_file, gloss_file, "12_appendix.md", "13_Backcover_text.md" ] 

docs = os.listdir('docs/')
docs.sort()

def find_term(term):    
    exp = "{blog}\s"#.format(term)

    for md_filename in docs:
        if '.md' in md_filename and md_filename not in avoid_files:
            md_file = open("docs/"+md_filename, "r") # open and parse
            md_content = md_file.readlines()
            
            for line in md_content:
                line = line.decode("utf-8")#                print line
                if re.search(r'{}\s'.format(term), line, re.IGNORECASE):                     
                    print [md_filename, line] 
                    print '------'
                    #                    return [md_filename , line]
#                    break



                
for term in missing_terms:
    print '     TERM:', term
    find_term(term)
    print 
