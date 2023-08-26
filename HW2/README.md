# HW2

## Problem
Implement the N-Queens problem using different heuristics and compare the results for `n` in range `[8, 16]`.

## Summary

### Functionality
All codes are available under the `codes` directory. A* and Greedy Search solvers are implemented, and an abstract `State` class should be implemented for each heuristic. Then, an initial state of the implemented heuristic must be passed to an instance of the solver to find a solution for the state.

### Implemented Heuristics
- `H1`: Number of conflicts, the initial state is a n-size **combination** of integers of range `[0, n-1]`, each number representing a column of queen on its row. Valid moves are moving each queen in one position on its row.
- `H2`: Number of threatened queens, the initial state is an n-size **combination** of integers of range `[0, n-1]`,  each number representing the column of queen on its row. Valid moves are moving each queen in one position on its row.
- `H3`: The number of queens on the same diagonal, initial state is an n-size **permutation** of integers of range `[0, n-1]`,  each number representing the column of a queen on its row and index of each number represents rows of the queen on its column. Valid moves are swapping to neighbor numbers (Queens on neighbor rows).

### Results
Finally, `H3` had the best performance in terms of computation time and number of iterations. A chart of results is shown below:

![Results](./images/Comparision%20Graph.png)

`H3` had better performance because, intuitively, it encoded more data about the final solution into the initial state.

Notice that A* and Greedy Search had the same performance for a small amount of `n`, but lower charts show a small difference between A* and Greedy Search for `n = 16` (red line). In fact, by increasing the value of `n`, A* will have a better performance than Greedy Search.

You can reproduce the results by running the code below under the `codes` directory:

```bash
 python3 Comparator.py
```

