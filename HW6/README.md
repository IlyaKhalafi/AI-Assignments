# HW6

## Problem
Compare the performance of different neural network optimization algorithms on the `IRIS` dataset classification task.

## Resources
The `IRIS` dataset is imported from the `sklearn` library. You can find more information about the dataset [here](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html).

Also, the `keras` library is used to build and optimize neural network models.

A total of 5 optimization algorithms are used to compare performance:

- `Gradient Descent`
- `Stochastic Gradient Descent`
- `Batch Gradient Descent`
- `RMSProp`
- `Adam`

All codes and comparison details are available in the `NNOptimizersComparision.ipynb` file.

## Results
It was not a surprise that the `Adam` optimizer performed the best. The chart below shows information on each optimizer's performance:

![Chart](images/chart.png)
