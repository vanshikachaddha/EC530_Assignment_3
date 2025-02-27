import concurrency
import time
import matplotlib.pyplot as plt


queue_size = [5, 10, 50, 100, 200, 500, 800, 1000]
num_threads = 10
matrow = 1000
matcol = 1000
num_processor = 10
x_axis = []
thread_time = []
processor_time = []

if __name__ == "__main__":

    for i in queue_size:

        x_axis.append(i)

        start_time = time.time()
        concurrency.test_thread(num_threads, i, matrow, matcol)
        t_time = time.time() - start_time
        print(f"Threading took {t_time:.2f} seconds.")

        thread_time.append(t_time)

        start_time = time.time()
        concurrency.test_processor(num_processor, i, matrow, matcol)
        p_time = time.time() - start_time
        print(f"MicroProcessing took {p_time:.2f} seconds.")

        processor_time.append(p_time)

    plt.figure(figsize=(10, 5))
    plt.plot(x_axis, thread_time, marker='o', label="Threading (🔵)")
    plt.plot(x_axis, processor_time, marker='s', label="Multiprocessing (🔴)")
    plt.xlabel("Iteration (Queue Size Doubles Each Step)")
    plt.ylabel("Time Taken (Seconds)")
    plt.title("Performance Comparison: Threading vs Multiprocessing")
    plt.legend()
    plt.grid()

    # Show and save the plot
    plt.savefig("performance_comparison.png") 
    plt.show()
