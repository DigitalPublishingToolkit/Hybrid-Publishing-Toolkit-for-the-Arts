#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, sys, os


missing_terms=['Amazon', 'Android', 'API', 'AZW', 'Cascading Style Sheets', 'Decompress', 'Ebook', 'EPUB', 'E-reader', 'File', 'GitHub', 'HTML', 'HTML5', 'Hybrid Publishing', 'iBooks', 'Internet', 'iOS', 'KF8', 'Kindle', 'Kobo', 'LCD', 'Linux', 'Markdown', 'Markup', 'Metadata', 'MOBI', 'MultiMarkdown', 'Open Source', 'PDA', 'PDF', 'Reflowable', 'Software', 'Tablet', 'WYSIWYG', 'XHTML', 'XML']

missing_terms=['Acronym', 'Amazon', 'Anchor', 'Android', 'Animated GIF', 'API', 'Application', 'App store', 'ASCII', 'AZW', 'Bandwidth', 'Binary', 'Bit', 'BitTorrent', 'Blog', 'Browser', 'Browser extension', 'Byte', 'Cascading Style Sheets', 'Compatibility', 'Compressed files', 'Computer program', 'Content Management System', 'Data', 'Database', 'Dataset', 'Decompress', 'Desktop Publishing', 'Device', 'Digital Rights Management', 'Dots Per Inch', 'Ebook', 'EPUB', 'E-paper', 'E-reader', 'File', 'Filename extension', 'File permissions', 'Folder', 'Formatting', 'Freemium', 'GitHub', 'Graphical User Interface', 'Graphics Interchange Format', 'HTML', 'HTML5', 'HTTP', 'Hybrid Publishing', 'Hyperlink', 'Hypertext', 'iBooks', 'Icon', 'Incompatibility', 'Interactivity', 'Interface', 'Internet', 'iOS', 'JavaScript', 'JPEG', 'KF8', 'Kindle', 'Kobo', 'LaTeX', 'Layout', 'LCD', 'Linux', 'Markdown', 'Markup', 'Markup language', 'Metadata', 'MOBI', 'Mobipocket', 'Monitor', 'Monochrome', 'MP3', 'MP4', 'MultiMarkdown', 'Multimedia', 'OCR', 'Open Source', 'Operating system', 'PDA', 'PDF', 'Pixel', 'Plain text', 'Platform', 'Print On Demand', 'Program', 'Protocol', 'Reflowable', 'Resolution', 'Rich Text Format', 'Server-side scripting', 'Software', 'Software Development Kit', 'Streaming', 'Style sheet', 'Syntax', 'Tablet', 'Tagging', 'Text editor', 'TIFF', 'Tumblr', 'Unicode', 'Unix', 'Word processor', 'WWW', 'WYSIWYG', 'XHTML', 'XML']

#input_filename=os.path.abspath(sys.argv[1])
#input_file = open(input_filename, "r") # open and parse
#input_file_lines = input_file.readlines()

colophon_file="00_colophon.md"
gloss_file = "11_glossary.md"
avoid_files = [colophon_file, gloss_file, "12_appendix.md", "13_Backcover_text.md" ] 

docs = os.listdir('docs/')
docs.sort()

def find_term(term):
    for md_filename in docs:
        if '.md' in md_filename and md_filename not in avoid_files:
            md_file = open("docs/"+md_filename, "r") # open and parse
            md_content = md_file.readlines()
            
            for line in md_content:
                line = line.decode("utf-8")#                print line

                if re.search(r'\*\*{}.?.?\*\*'.format(term), line, re.IGNORECASE):
                    print md_filename
                    line = line.encode('utf-8')
                    print line
                    #print '------'
#                    return [md_filename , line]
#                   break



                
for term in missing_terms:
    print '   TERM:', term
    find_term(term)
    print ''
    # if found is not None:
    #     print 'File:', found[0] 
    #     print found[1]
    # else:
    #     print 'term Not Found in text'
