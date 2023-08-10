import numpy as np

from animate import animate
import algs

np.random.seed(1)

animate(algs.quick_sort, 100, 20, "Quick Sort", 10)
# animate(algs.bubble_sort, 100, 20, "Bubble Sort", 10)
# animate(algs.bogo_sort, 100, 5, "Bogo Sort", 10)

