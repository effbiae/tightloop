F=-O3 -fomit-frame-pointer -march=native
ref:ref.c makefile
	gcc $F ref.c -o ref
eff:eff.c makefile
	gcc $F eff.c -o eff
run:
	python3 run.py
g:ref.c makefile
	gcc -O2 -fomit-frame-pointer  -g ref.c -o refg
