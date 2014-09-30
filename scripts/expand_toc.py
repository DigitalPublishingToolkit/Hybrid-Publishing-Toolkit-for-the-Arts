#!/usr/bin/env python
# Process a TOC to a set of links
"""
(C) 2014 Michael Murtaugh / contributors to the Digital Publishing Toolkit

License: [GPL3](http://www.gnu.org/copyleft/gpl.html)

This code has been developed as part of the [Digital Publishing Toolkit](http://digitalpublishingtoolkit.org).
with the support of Institute for [Network Cultures](http://networkcultures.org)
and [Creating 010](http://creating010.com).

"""

from __future__ import print_function
import sys, re, argparse, sys, os
from subprocess import Popen, check_output, PIPE
from itertools import izip

"""

sotq style:

# Theorizing Web Search

* [ **Kylie Jarrett**  
A Database of Intention?](source/Kylie-Jarrett.md)
* [ **Andrea Miconi**  
Dialectic of Google ](source/Andrea_Miconi.md)
* [ **Vito Campanelli**  
Frictionless Sharing: The Rise of Automatic Criticism ](source/Vito_Campanelli.md)



toolkit style:

# [01 Introduction](docs/01_introduction.md)
<!--status: Joost adds a few things, then it's ready for copy edit.-->

## [Industry promises versus reality](#industry-promises-versus-reality)
## [What this Toolkit provides](#what-this-toolkit-provides)


Headers / Levels / Includes/Links
1. Rewrite the TOC
a. Headers to divs
b. Link Header if not already <! new >, otherwise patch/include the link

"""
def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

def grouped(iterable, n):
    """
    http://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list
    s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ...
    """
    return izip(*[iter(iterable)]*n)

parser = argparse.ArgumentParser(description='Table of contents Tools')
parser.add_argument('toc', help='toc file')
parser.add_argument('--list', dest='list', action='store_true', help='output makefile friendly list of linked files')
parser.add_argument('--ignore-missing', dest='ignoreMissing', action='store_true', help='')
parser.add_argument('--filter', dest="filter", default="cat", help='script to run on each linked chapter')
parser.add_argument('--section-pages', action='store_true', help='Output TOC headers as pages')
parser.add_argument('--no-toc', action='store_true', help='')

# parser.add_argument('--section-level', help='level from which to generate sections')
# parser.add_argument('--section-template', help='template to generate sections')

args = parser.parse_args()

## in fact filter markdown links, return original targets when list is requested
## otherwise return toc with links replaced to links to titles

markdown_link_pattern = re.compile(r"\[(.*?)\]\((.*?)\)", re.DOTALL)
markdown_header_pattern = re.compile(r"^(#+)(.*)$", re.M)

def _join (a, b):
    ret = u""
    if a:
        ret += a + "\n\n"
    if b:
        ret += b
    return ret

toc = args.toc
with open(toc) as f:
    if args.list:
        # OUTPUT LIST ONLY
        srcs = []
        toctext = f.read().decode("utf-8")
        for m in markdown_link_pattern.finditer(toctext):
            srcs.append(m.groups()[1])
        for s in srcs:
            if args.ignoreMissing:
                if os.path.exists(s):
                    print (s)
                else:
                    print ("MISSING", s, file=sys.stderr)
            else:
                print (s)
    else:
        # OUTPUT TOC + BOOK
        toctext = f.read().decode("utf-8")
        split = markdown_header_pattern.split(toctext)
        split.insert(0, None)
        split.insert(0, None)


        # from pprint import pprint
        # print ("START")
        # pprint(split)
        # sys.exit(0)
        ## PART 1: Output the TOC with transformed headings & mapped links,
        ## NB: Cache the (filtered) sources for PART 2
        sources_text = {}

        def id_for_source (src):
            """
            converts the (filtered) src to html with pandoc
            and searches for the first id attribute to use as a link
            """
            # cmd = [args.sectionID, src]
            # return check_output(cmd).strip()
            markdown_src = check_output([args.filter, src])
            # cache filtered src!
            sources_text[src] = markdown_src
            p = Popen(["pandoc", "--to", "html", "--from", "markdown"], stdin = PIPE, stdout=PIPE)
            (html, err) = p.communicate(markdown_src)
            idpat = re.compile(r"id=\"(.*?)\"")
            for m in idpat.finditer(html):
                return m.group(1)

        def toc_link_sub(m):
            label, link = m.groups()
            return u"[{0}]({1})".format(label,"#"+id_for_source(link))

        for header_hashes, header, text in grouped(split, 3):
            if header:
                # Up the h-level of > 1's by 1 (so 2 ==> 3)
                n = len(header_hashes)
                # if n > 1:
                #     n += 1
                # print (((u"#"*n)+header).encode("utf-8"))
                if not args.no_toc:
                    print (u"""<div class="toc_h{0}">{1}</div>\n""".format(n,header.lstrip()).encode("utf-8"))
            # OUTPUT TEXT WITH REPLACED LINKS
            repl = markdown_link_pattern.sub(toc_link_sub, _join(header, text))
            if not args.no_toc:
                print (repl.encode("utf-8"))
        if not args.no_toc:
            print ()

        ## PART 2: Output the (filtered) sections markdown in order
        ## with TOC headers at the right spots (section pages)
        ##
        for header_hashes, header, text in grouped(split, 3):
            if header and args.section_pages:
                n = len(header_hashes)
                print (((u"#"*n)+header).encode("utf-8"))
                print ()
            for m in markdown_link_pattern.finditer(_join(header, text)):
                src = m.groups()[1]
                print (sources_text[src])
                print () 

