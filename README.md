Digitial Publishing Toolkit
===========================

**THIS IS A TEST PROJECT and may not actually be accurate or useful**

Workshop in using interchangable tools in a (static file) based (e)publishing workflow.

Assemble sources to a convincing epub with styles + svg figures (and an index ?!)

* Fun way to share (with version control ?!)


Sublime + Markdown
----------------------------

* [Sublime Text](http://www.sublimetext.com/)
* [Sublime Package Control](http://sublime.wbond.net) -- installable via the Sublime console! (make sure to use the version of Sublime 2)...
* *Markdown Preview* plugin

In Sublime, a very powerful feature is the "Command Palette". It's in the Tools menu, but it's handiest to open with the keyboard shortcut: Command-Shift-P (mac) or Ctrl-Shift-p (windows, linux).

To install a package with "package control", open the command palette, and type package install. Hit Enter to pick the command: "Package Control: Install Package". In the status bar at the bottom of the window, you can see that the command is busy loading a list of available packages from the "repositories". A Repository is like an "app store" for software plugins.

Type Markdown, and select the plugin called "Markdown Preview".


Sublime + Git
---------------

* [Installing git](http://git-scm.com/download/)
* Sublime *Git* plugin (by [kenmayo](http://github.com/kemayo/sublime-text-git/wiki))


Calibre
-----------

* [Calibre conversion](http://manual.calibre-ebook.com/conversion.html)
* [Calibre commandline tools](http://manual.calibre-ebook.com/cli/cli-index.html)

* Custom sublime / python scripts ?


Setting your git identity
------------

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

When Using git pull, you need to revert files (kind of weird)

Add, Commit, Push
------------------

Standard procedure: Add, Commit (close file without saving), (and Push)
Faster: Quick commit a single file, (and Push)


Alternatively
--------------
github distributes an "easier" application that merges bit with access to their (closed-source) platform. Advantages: works without separate git install, Disadvantages: sublime plugin won't work (unless git is also installed) ... so commits and syncing should be done with the github app. [Github for mac](http://mac.github.com/).

