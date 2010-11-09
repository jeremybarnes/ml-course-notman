CHESS := chess-8x8-10.pdf chess-8x8-100.pdf chess-8x8-1000.pdf chess-8x8-10000.pdf

lecture.pdf:	talk.tex $(CHESS) salaries-venn.pdf decision-tree-explain.pdf
	pdflatex talk.tex
	pdflatex talk.tex
	pdflatex talk.tex

$(CHESS): chess.py
	python $<

%.pdf:	%.svg
	inkscape --without-gui --export-dpi=300 --export-pdf $@~ $<
	mv $@~ $@
