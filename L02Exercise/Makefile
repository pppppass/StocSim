.PHONY: all
all: Answer.pdf

Answer.pdf: Answer.tex Figure1.pgf
	lualatex Answer.tex

Figure1.pgf: Problem7.py
	python Problem7.py

%.py: %.ipynb
	jupyter nbconvert --to script $*

.PHONY: report
report: Answer.pdf

.PHONY: run
run: Figure1.pgf
