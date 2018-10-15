PGFOBJS = Figure1.pgf Figure2.pgf
RUNOBJS = Problem2.run

.PHONY: all
all: Answer.pdf

Answer.pdf: Answer.tex $(PGFOBJS) | Answer.aux
	lualatex Answer.tex

Answer.aux: Answer.tex
	lualatex Answer.tex

$(PGFOBJS): $(wildcard $(RUNOBJS)) $(if $(wildcard Result.dir), Plot.py)
	python Plot.py
	sed -i 's/<LABEL1~*>/Estimated $$ \\ope e_N^2 $$/' Figure1.pgf
	sed -i 's/<LABEL2~*>/Estimated $$ \\ope \\abs{e_N} $$/' Figure2.pgf

.PRECIOUS: %.py
%.py: %.ipynb
	jupyter nbconvert --to script $*

%.run: %.py
	python $<
	touch $@

.PHONY: report
report: Answer.pdf

.PHONY: run
run: $(RUNOBJS)
