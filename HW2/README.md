# HW2

## Problem
Implement N-Queens problem using different heuristics and compare the results for `n` in range `[8, 16]`.

## Summary

### Functionality
All codes are available under `codes` directory. A* and Greedy Search solvers are implemented and also an abstract `State` class which should be implemented for each heuristic. Then an initial state of implemented heuristic must be passed to an instance of solver to find a solution for the state.

### Implemented Heuristics
- `H1`: Number of conflicts, initial state is a n-size **combination** of integers of range `[0, n-1]`, each number representing column of queen on its row. Valid moves are moving each queen one position on its row.
- `H2`: Number of threatened queens,initial state is a n-size **combination** of integers of range `[0, n-1]`,  each number representing column of queen on its row. Valid moves are moving each queen one position on its row.
- `H3`: Number of queens on the same digonal, initial state is a n-size **permutation** of integers of range `[0, n-1]`,  each number representing column of queen on its row and index of each number represents rows of queen on its column. Valid moves are swaping to neighbor numbers (Queens on neighbor rows).

### Results
Finally `H3` had the best performance in terms of computation time and number of iterations. A chart of results is shown below:

![Results](../HW2/images/Comparision%20Graph.png)

`H3` had better performance because intuitively it has encoded more data about final solution into the initial state.

Notice that A* and Greedy Search had same performance for small amount of `n` but lower charts show a small difference between A* and Greedy Search for `n = 16` (red line). In fact by increasing the value of `n`, A* will have a better performance than Greedy Search.

You can reproduce the results by running the code below under `codes` directory:

```bash
 python3 Comparator.py
```

