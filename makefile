F=-O3 -fomit-frame-pointer -march=native
ref:ref.c makefile
	gcc $F ref.c -o ref
run:
	python3 run.py
