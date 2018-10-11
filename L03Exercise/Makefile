PGFOBJS = Figure1.pgf Figure2.pgf Figure3.pgf
TBLOBJS = Table1.tbl
RUNOBJS = Problem2.run

.PHONY: all
all: Answer.pdf

Answer.pdf: Answer.tex $(PGFOBJS) | Answer.aux
	lualatex Answer.tex

Answer.aux: Answer.tex
	lualatex Answer.tex

.SECONDEXPANSION:
$(PGFOBJS) $(TBLOBJS): $(wildcard $(RUNOBJS)) Plot.py
	python Plot.py

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
