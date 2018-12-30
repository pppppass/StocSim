PGFOBJS = Figure01.pgf Figure02.pgf Figure03.pgf Figure04.pgf Figure05.pgf Figure06.pgf Figure07.pgf Figure08.pgf Figure09.pgf Figure10.pgf Figure11.pgf Figure12.pgf Figure13.pgf Figure14.pgf Figure15.pgf Figure16.pgf Figure17.pgf Figure18.pgf Figure19.pgf Figure20.pgf Figure21.pgf
TBLOBJS = Table1.tbl Table2.tbl Table3.tbl Table4.tbl Table5.tbl Table6.tbl
RUNOBJS = Problem0.run Problem1.run Problem2.run Problem3.run

.PHONY: all
all: Report.pdf

Report.pdf: Report.tex Report.bbl $(PGFOBJS) $(TBLOBJS) | pnote.cls pdef.sty Report.aux
	lualatex Report.tex

Report.aux: Report.tex Report.bbl | pnote.cls pdef.sty
	lualatex Report.tex

Report.bbl: Report.tex | pnote.cls pdef.sty
	lualatex Report.tex
	biber Report

pnote.cls pdef.sty:
	ln -s ptmpls/$@ .

.SECONDEXPANSION:
$(PGFOBJS) $(TBLOBJS): $(wildcard $(RUNOBJS))
	touch $@

setup.cfg:
	if [ -z "$$CONDA_PREFIX" ];\
	then\
		echo "Anaconda not found";\
		exit 1;\
	fi
	echo "[build_ext]" > setup.cfg
	echo "include_dirs=${CONDA_PREFIX}/include" >> setup.cfg
	echo "library_dirs=${CONDA_PREFIX}/lib" >> setup.cfg

samp.so: setup.py setup.cfg samp/samplers.c samp/utils.c samp/wrappers.c samp/samp.h
	python setup.py build_ext --inplace
	FILENAMES=`ls | grep 'samp.*\.so' | grep -v 'samp.so'`;\
	for FILE in $${FILENAMES};\
	do\
		mv $${FILE} samp.so;\
	done

.PRECIOUS: %.py
%.py: %.ipynb
	jupyter nbconvert --to script $*

%.run: %.py samp.so
	python $<
	touch $@

.PHONY: run
run: $(RUNOBJS)
