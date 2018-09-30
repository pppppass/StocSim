DIRS = $(shell ls -d */ | grep -v ptmpls)

.PHONY: all
all: recursive environment.yml

environment.yml:
	conda env export > environment.yml

.PHONY: recursive
recursive: template
	for DIR in $(DIRS);\
	do\
		$(MAKE) -C $${DIR};\
	done

.PHONY: template
template:
	$(MAKE) -C ptmpls

.PHONY: environment
environment: environment.yml
	conda env create -f envorinment.yml
