ref:ref.c makefile
	gcc -O3 -fomit-frame-pointer -march=native ref.c -o ref
run:
	python3 run.py
