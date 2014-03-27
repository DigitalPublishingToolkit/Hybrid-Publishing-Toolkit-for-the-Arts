Digitial Publishing Toolkit
===========================

Meeting in Amsterdam 27 March 2014

The [github](https://github.com/DigitalPublishingToolkit) account.

Workshop in using interchangable tools in a (static file) based (e)publishing workflow.

Assemble sources to a convincing epub with styles + svg figures (and an index ?!)


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
An ssh key is in a nutshell a password-alternative. Rather than entering a password every time you login, or storing a password in a cookie, ssh keys have a private and a public part. You then upload (for once and forever) the public part to the servers you want to login to, and from that point on, your computer is able to login. Note that the system works because at login, the private half of the key stored on your computer is used so that no one else could steal your identity if they only have the public half of the key.

Step one is creating your own "ssh key" and adding the public half to either the github DPT account, or your own github account (if you have one). This then gives your computer permission to upload changes. If you use multiple computers, generate a key on each one, and add each to the server (github in this case).

    [Generating SSH Keys](http://help.github.com/articles/generating-ssh-keys)

Secondly, you tell git tool the name and email address you'd like to use:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

If you want to set this to be different per repository, just omit the --global option and make sure you are inside the directory when you do the command.


Add, Commit, Push
------------------

Standard procedure: Add, Commit (close file without saving), (and Push)
Faster: Quick commit a single file, (and Push)


Alternatively
--------------
github distributes an "easier" application that merges bit with access to their (closed-source) platform. Advantages: works without separate git install, Disadvantages: sublime plugin won't work (unless git is also installed) ... so commits and syncing should be done with the github app. [Github for mac](http://mac.github.com/).

