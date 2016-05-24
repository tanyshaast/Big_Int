all:
	swig -c++ -python Big_integer.i
	g++ -fPIC -c Big_integer.cpp
	g++ -c Big_integer_wrap.cxx -I/usr/include/python3.4m
	g++ Big_integer.o Big_integer_wrap.o -I/usr/include/python3.4m -L/usr/lib/python3.4m -shared -o _Big_integer.pyd
