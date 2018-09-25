PGFOBJS = Figure1.pgf Figure2.pgf

.PHONY: all
all: Answer.pdf

Answer.pdf: Answer.tex $(PGFOBJS)
	lualatex Answer.tex

$(PGFOBJS): $(wildcard Result.dir) Plot.py
	python Plot.py
	sed -i 's/<LABEL1~*>/Estimated $$ \\ope e_N^2 $$/' Figure1.pgf
	sed -i 's/<LABEL2~*>/Estimated $$ \\ope \\abs{e_N} $$/' Figure2.pgf

Result.dir: Problem2.py
	python Problem2.py

%.py: %.ipynb
	jupyter nbconvert --to script $*

.PHONY: report
report: Answer.pdf

.PHONY: run
run: Result.dir
