OBJS	= sudoku_solver.o test_sudoku_solver.o
SOURCE	= sudoku_solver.cpp test_sudoku_solver.cpp
OUT	    = sudoku.out
CC	    = g++
FLAGS	= -g -c -Wall -std=c++17 -Wshadow -Wno-unused-result -O2
LFLAGS	= -lgtest -lpthread

all: $(OBJS)
	$(CC) -g $(OBJS) -o $(OUT) $(LFLAGS)

sudoku_solver.o: sudoku_solver.cpp
	$(CC) $(FLAGS) sudoku_solver.cpp

test_sudoku_solver.o: test_sudoku_solver.cpp
	$(CC) $(FLAGS) test_sudoku_solver.cpp

clean:
	rm -f $(OBJS) $(OUT)