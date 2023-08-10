import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time

def animate(sorting_alg, 
            max_value: int, 
            arr_size: int, 
            title: str="Sorting Algorithm", 
            frame_interval: int=50):
    """ Function to animate sorting algorithms.

    ** NOTE THAT SORTING ALGS NEED TO USE YIELD FOR UPDATE, NOT RETURN **

    Args:
        sorting_alg: function sorting algorithm
        max_value: the highest value you want for your sort array
        array_size: the size of the array to be sorted
        frame_interval: ms for animation refresh 
    """
    # Generate array to be sorted
    array = np.random.randint(0, max_value, arr_size)
    fig, ax = plt.subplots()

    # Configure bars
    bars = ax.bar(range(len(array)), array, align="edge")
    ax.set_xlim(0, len(array))
    ax.set_ylim(0, int(1.1 * max(array)))
    ax.axis('off')

    start_time = time.time()

    def update_fig(array, bars, start_time):
        for bar, height in zip(bars, array):
            bar.set_height(height)
        elapsed_time = time.time() - start_time
        ax.set_title(f"{title} - Time Elapsed: {elapsed_time:.2f}s")

    # Configure the animation
    animation = FuncAnimation(
        fig, # figure
        func=update_fig, # update function 
        fargs=(bars, start_time), # figure bars
        frames=sorting_alg(array, 0, len(array) - 1), # sorting algorithm
        repeat=False, blit=False, interval=frame_interval, # animation variables
        cache_frame_data=False # frame cache off
    )
    plt.title(title)
    plt.show()

# Sorting algorithms

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot_idx = start
    pivot = array[end]
    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
            pivot_idx += 1
        yield array
    array[end], array[pivot_idx] = array[pivot_idx], array[end]
    yield array

    yield from quick_sort(array, start, pivot_idx - 1)
    yield from quick_sort(array, pivot_idx + 1, end)

def bubble_sort(array, start, end):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j+1], array[j]
                swapped = True
                yield array
                
        if not swapped:
            break









