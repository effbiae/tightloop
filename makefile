ref:ref.c makefile
	pip3 install -t . terminaltables
	gcc -O3 -fomit-frame-pointer -march=native ref.c -o ref
run:
	python3 run.py
