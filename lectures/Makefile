HTM := $(patsubst %.md,%.html,$(wildcard *.md))
BMR := $(patsubst %.md,%.bmr.pdf,$(wildcard *.md))

mj := $("http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML")

all : $(HTM) $(BMR)

%.html : %.md
	pandoc $^ \
	-t revealjs \
	--slide-level 2 \
	--standalone \
	--mathjax $(mj) \
	--template reveal-code.html \
	--css assets/style.css \
	-L revealjs-codeblock.lua \
	-V highlightjs \
	-V highlightjs-theme=monokai \
	-V theme=night \
	-V margin=0.2 \
	-V slideNumber="'c/t'" \
	-V center=true \
	-V transition=slide \
	-o $@

%.bmr.pdf : %.md
	pandoc $^ \
	-t beamer \
	--slide-level 2 \
	--dpi=96 \
	-L beamer-noincrement.lua \
	-L beamer-media-replace.lua \
	-o $@

clobber : 
	rm -f $(HTM)
	rm -f $(BMR)
