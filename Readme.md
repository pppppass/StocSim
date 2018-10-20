# Assignments for Numerical Partial Differential Equations

## Introduction

This is the repository of assignments of the course *Stochastic Simulation* lectured by *Tiejun Li* in Fall 2018. The author of this repository is [Zhihan Li](mailto:lzh2016p@pku.edu.cn).

This repository relies on the personal TeX templates package [ptmpls](https://github.com/pppppass/ptmpls). Remember to specify `--recursive` option when cloning the repository.

## Organization

There are several sub folders in this repository:
1. `ptmpls`: Personal TeX / LaTeX templates;
2. `LxxExercise`: Written exercise for lecture `xx`.

## Environment

All the numerical results are produced in a specific environment. The hardware configuration can be found in `hardware.txt`. An Anaconda environment is set up according to `environment.yml`.

## Usage

There are Makefiles distributed in folders.

To compile reports:
1. Install TeX Live or other TeX utilities with LuaLaTeX and ensure that they can be found by `PATH`;
2. Execute `make` in the root folder to recursively compile all reports;
3. Or proceed down to a folder and execute `make report` to generate one single report;
4. The reports are `Answer.pdf` or `Report.pdf` in each folder.

To reproduce the numerical results:
1. Activate Anaconda and execute `make environment` in the root folder to create a new environment `stocsim`;
2. Activate the environment `stocsim`;
3. Proceed down to a folder and execute `make run` to reproduce numerical results;
4. Execute `make report` or `make` to regenerate the report;
5. The numerical results are updated in the report, i.e., `Answer.pdf` or `Report.pdf`.
