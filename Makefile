CC = gcc
CFLAGS = -Wall -g -Iinclude
SRCS = src/wal.c src/memtable.c src/sstable.c src/lsm_tree.c src/bloom_filter.c src/utils.c
OBJS = $(SRCS:.c=.o)
EXEC = lsm-tree

all: $(EXEC)

$(EXEC): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^ -lm

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@