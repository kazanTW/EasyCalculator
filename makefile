.POSIX:
.PHONY: all clean
CC = gcc
CFLAGS = -std=c99
TARGET = EasyCal_gcc

all: $(TARGET)

$(TARGET): Calculator.c
	$(CC) $(CFLAGS) Calculator.c -o $(TARGET)

clean:
	rm -rf $(TARGET)

install: $(TARGET)
	cp ~/EasyCal_gcc /usr/bin/ezcalgcc