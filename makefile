.POSIX:
.PHONY: all clean
CC = gcc
CFLAGS = -std=c99
TARGET = ezcalgcc

all: $(TARGET)

$(TARGET): Calculator.c
	$(CC) $(CFLAGS) Calculator.c -o $(TARGET)

clean:
	rm -rf $(TARGET)

install: $(TARGET)
	cp ezcalgcc /usr/local/bin/ezcalgcc