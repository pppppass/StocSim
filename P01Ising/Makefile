PGFOBJS = Figure01.pgf Figure02.pgf Figure03.pgf Figure04.pgf Figure05.pgf Figure06.pgf Figure07.pgf Figure08.pgf Figure09.pgf Figure10.pgf Figure11.pgf Figure12.pgf Figure13.pgf Figure14.pgf Figure15.pgf Figure16.pgf Figure17.pgf Figure18.pgf Figure19.pgf Figure20.pgf Figure21.pgf Figure22.pgf Figure23.pgf Figure24.pgf Figure25.pgf Figure26.pgf Figure27.pgf Figure28.pgf Figure29.pgf Figure30.pgf Figure31.pgf Figure32.pgf Figure33.pgf Figure34.pgf Figure35.pgf Figure36.pgf
RUNOBJS = Problem0.run Problem1.run Problem2.run Problem3.run Problem4.run Problem5.run Problem6.run Problem7.run Problem8.run Problem9.run

.PHONY: all
all: Report.pdf

Report.pdf: Report.tex $(PGFOBJS) | pnote.cls pdef.sty Report.aux
	lualatex Report.tex

Report.aux: Report.tex | pnote.cls pdef.sty
	lualatex Report.tex

pnote.cls pdef.sty:
	ln -s ptmpls/$@ .

.SECONDEXPANSION:
$(PGFOBJS): $(wildcard $(RUNOBJS)) $(if $(wildcard Result.dir), Plot1.py Plot2.py Plot3.py)
	python Plot1.py
	python Plot2.py
	python Plot3.py

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
