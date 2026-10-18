Title: Source Code for Scatterplot Figure in "The Categories Were Made for Man to Make Predictions"
Status: Hidden

Requires [NumPy](http://www.numpy.org/), [Matplotlib](https://matplotlib.org/).

```python
import functools
import itertools

import matplotlib.pyplot as plot
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
from numpy import array
from numpy.random import normal


class Person:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def trait_vector(self):
        return [self.a, self.b, self.c]

    @classmethod
    def generate_cis_male(cls):
        a = normal(0, 1)
        b = normal(0, 1)
        c = normal(0, 1)
        return cls(a, b, c)

    @classmethod
    def generate_cis_female(cls):
        a = normal(3.5, 1)
        b = normal(3.5, 1)
        c = normal(3.5, 1)
        return cls(a, b, c)

    @classmethod
    def generate_agp(cls):
        a = normal(0, 1)
        b = normal(0, 1)
        c = normal(3.8, 1)
        return cls(a, b, c)

def my_plot():
    group_size = 50

    p1 = [Person.generate_cis_female().trait_vector()
          for _ in range(group_size)]
    p2 = [Person.generate_agp().trait_vector()
          for _ in range(group_size)]
    p3 = [Person.generate_cis_male().trait_vector()
          for _ in range(group_size)]

    p = array(p1 + p2 + p3)

    target = list(functools.reduce(itertools.chain,
                                   [itertools.repeat(i, group_size)
                                    for i in range(1, 4)]))

    figure = plot.figure(figsize=(6, 5))
    axes = Axes3D(figure)

    axes.scatter(p[:, 0], p[:, 1], p[:, 2],
                 c=target,
                 cmap=ListedColormap(["#FF1493", "#B000B0", "#1E90FF"]))
    plot.show()


if __name__ == "__main__":
    my_plot()

```