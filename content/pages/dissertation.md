Title: Dissertation
Category: Dissertation
Tags: Art History, Archaeology, Material Culture, Women's History, PhD, Textiles, Open Access
Slug: dissertation
Author: Dr. Morgan Lemmer-Webber

# Women and Wool Working in the Roman Empire

## Dr. Morgan A Lemmer Webber, University of Wisconsin Madison, Spring 2021 

### Abstract

This dissertation looks at women’s roles in textile production in the Roman
Empire, from the first through third centuries C.E., utilizing archaeological,
epigraphic, literary, administrative, and visual evidence. The sites of Karanis, Trier,
and Ephesus are used as case studies to focus analysis alongside domestic,
commercial, and performative lines. Scholars have often viewed the domestic and
commercial divide in textile production along gendered lines, associating domestic
production with women in the context of the ideal of feminine virtue and
commercial production with men working in centralized production centers. This
study uses the cottage industry model to explore the role of women’s labor in the
Roman textile industry, exploring the links between domestic production and
commercial distribution.

### License

Released under the Creative Commons Attribution-ShareAlike 4.0 International license by Morgan Lemmer-Webber 2021

### Links to Full Text

* [Full Text PDF (official version)]({static}/dissertation/Dissertation-official.pdf)
* [Full Text PDF (latest version)]({static}/dissertation/Dissertation.pdf)
* [ODT (latest version)]({static}/dissertation/Dissertation.odt)
* HTML (coming soon)

### Source

My dissertation is done in
[Scribble](https://docs.racket-lang.org/scribble/),
which is a combination programming and markdup language built on top of
[Racket](https://racket-lang.org/).

You can [browse the source files](https://mlemmer.org/git/dissertation/)
or even check out and compile the dissertation yourself by checking it
out via [git](https://git-scm.com/) and [git-annex](https://git-annex.branchable.com/):

```
$ git clone https://mlemmer.org/git/dissertation/.git/
$ cd dissertation
$ git-annex init
$ git-annex sync
```

From there you can pull down binary files, eg:

```
$ git-annex get WeavingTutorial.odt
```

Note a few things:

* The repository is kind of a mess.  I hope to clean it up eventually.
* [Christine](https://dustycloud.org/) did a lot of the work on the technical tooling including the ODT exporter, but the text is all me.  However there are some commits where Christine committed on my behalf because I had a migraine and she was typing as I dictated.  Just be aware of that (and thanks Christine)!
* Note that I was fairly new to both git and git-annex when we started this.  Because of that, I mostly was letting git-annex assistant commit files on my behalf.  Therefore, many of the commit messages from me are automated and aren't that helpful.  These days I use [Emacs](https://www.gnu.org/software/emacs/) and [Magit](https://magit.vc/) to manage git repositories (I didn't know Emacs at the time, so I was using DrRacket, which is a good place to start but a bit more limited).  If I were to do it over I'd probably start there first.
* I still need to copy up a bunch of the images and some of the other binary files to the publicly hosted git-annex repo.  It's a bit complicated because I dumped a bunch of stuff in here, and not all of it are files I'm legally allowed to publish.  I have to sort that out... hopefully soon.
