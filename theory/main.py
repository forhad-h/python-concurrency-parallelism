import run_sleep_tasks
import run_calc_tasks

"""
    Threads are more efficient than serial in I/O bound
    But threads behave same as serial in CPU bound
    Processes have good performance for both
"""
print("\n\nStart sleep tasks")

# run sleep tasks
run_sleep_tasks.run_serially()
run_sleep_tasks.run_threads()
run_sleep_tasks.run_processes()

print("End sleep tasks")

print("\n\nStart calculation tasks")

# run calculation tasks
run_calc_tasks.run_serially()
run_calc_tasks.run_threads()
run_calc_tasks.run_processes()

print("End calculation tasks")
