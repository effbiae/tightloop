ref:ref.c makefile
	gcc -O3 -fomit-frame-pointer -march=native ref.c -o ref
	make -C contrib/jfa
	make -C contrib/cpp
setup:
	sudo pip3 install -t . terminaltables
run:
	python3 run.py
