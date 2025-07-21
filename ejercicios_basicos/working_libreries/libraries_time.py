"""[summary]

    Using sleep to pause the execution of a program.
    
    It is often necessary to optimize code and analyze performance metrics. Here, the time library comes to help. We can measure the runtime of our code and optimize it. We can also use it to measure the runtime of two pieces of code doing the same work so that we can choose the most optimized one.

"""

from time import sleep, time

lista = [3, 4, 8, 2, 1, 9, 7, 5, 6]

for item in lista:
    print(item)
    sleep(1)

# ------------------------------------------------------------------
print("Calculating Execution Time")
start_time: float = time()

# print all even numbers till 20
for i in range(10):
    if i % 2 == 0:
        print(i, end="")

end_time: float = time()
time_taken: float = end_time - start_time
print(f"\nTime taken to execute the code is {time_taken} seconds")

# ------------------------------------------------------------------
# Countdown Timer


def countdown(time_number):
    while time_number:
        mins, secs = divmod(time_number, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        sleep(1)
        time_number -= 1
    print("Time's up!")


time_input = input("Enter the time in seconds: ")
countdown(int(time_input))
