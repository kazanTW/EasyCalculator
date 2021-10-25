.POSIX:
.PHONY: all clean
CC = gcc
CFLAGS = -std=c99

all: main

main: Calculator.c
	$(CC) $(CFLAGS) Calculator.c -o EasyCal_gcc

clean:
	rm -rf