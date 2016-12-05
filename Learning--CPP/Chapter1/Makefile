CPPFLAGS=
CFLAGS= -g -Wall
LDFLAGS= 
CC=g++

src = $(wildcard *.cpp)
obj = $(patsubst %.cpp, %.o, $(src))

target=app

$(target):$(obj)
	$(CC) $(obj) $(LDFLAGS) -o $@

%.o:%.cpp
	$(CC) -c $< -o $@

.PHONY:clean

clean:
	-rm -f *.o
	-rm -f app

