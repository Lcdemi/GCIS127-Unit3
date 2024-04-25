import plotter
import time

def fibonacci_naive(n):
	if n <= 0:
		return None
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibonacci_naive(n-1) + fibonacci_naive(n-2)

def naive_timer(n):
	plotter.new_series("Naive")
	for i in range(n):
		start = time.perf_counter()
		fibonacci_naive(i)
		end = time.perf_counter()
		elapsed = end - start
		plotter.add_data_point(elapsed)
	plotter.plot()
	
def fibonacci_fast(n, fn_minus_1=1, fn_minus_2=0):
	if n <= 0:
		return None
	elif n == 1:
		return fn_minus_2
	elif n == 2:
		return fn_minus_1
	else:
		return fibonacci_fast(n-1, fn_minus_1 + fn_minus_2, fn_minus_1)
	#https://stackoverflow.com/questions/76834978/python-recursive-function-to-calculate-the-sum-of-fibonacci-numbers

def fast_timer(n):
	plotter.new_series("Fast")
	for i in range(n):
		start = time.perf_counter()
		fibonacci_fast(i)
		end = time.perf_counter()
		elapsed = end - start
		plotter.add_data_point(elapsed)
	plotter.plot()

def main():
	n_value1 = int(input("Enter a value for N: "))
	#print(fibonacci_naive(9))
	plotter.init("Naive Fibonacci", "N", "Time")
	naive_timer(n_value1)
	n_value2 = int(input("Enter another value for N: "))
	#print(fibonacci_fast(9))
	plotter.init("Fast Fibonacci", "N", "Time")
	fast_timer(n_value2)
	n_value3 = int(input("Enter a final value for N: "))
	plotter.init("Naive vs. Fast", "N", "Time")
	naive_timer(n_value3)
	fast_timer(n_value3)

if __name__ == "__main__":
	main()
