#!/usr/bin/perl

chdir ('../docs');
opendir (DIR, '.');
@files = readdir (DIR);
closedir (DIR);

@files = sort(@files);

foreach $file(@files) {
	if ($file =~ /\.md$/i) {
		print "\n<!-- $file -->\n";
		open (FILE, $file);
		while (<FILE>) {
			chomp; 
			if (/^[\s]*#[ \t]*.[^#]/) {print $_,"\n" }
			}
		close (FILE);
		}
	}
