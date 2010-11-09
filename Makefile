CHESS := chess-8x8-10.pdf chess-8x8-100.pdf chess-8x8-1000.pdf chess-8x8-10000.pdf

lecture.pdf:	talk.tex $(CHESS) salaries-venn.pdf decision-tree-explain.pdf \
		$(foreach n,1 2 3 4 5 6,telescope$(n).png)
	pdflatex talk.tex
	pdflatex talk.tex
	pdflatex talk.tex

$(CHESS): chess.py
	python $<

%.pdf:	%.svg
	inkscape --without-gui --export-dpi=300 --export-pdf $@~ $<
	mv $@~ $@

telescope%.png:	telescope%.svg
	inkscape -e=$@ -D $< -z -d 500
