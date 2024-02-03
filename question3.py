class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_burst_time = burst_time
        self.start_time = 0
        self.finish_time = 0

def round_robin(processes, time_quantum):
    current_time = 0
    while True:
        all_processes_finished = True  # Flag to check if all processes have finished
        for process in processes:
            if process.remaining_burst_time > 0:
                all_processes_finished = False
                if process.remaining_burst_time > time_quantum:
                    # Execute the process for the time quantum
                    process.start_time = current_time
                    current_time += time_quantum
                    process.remaining_burst_time -= time_quantum
                else:
                    # Execute the remaining burst time of the process
                    process.start_time = current_time
                    current_time += process.remaining_burst_time
                    process.remaining_burst_time = 0
                    process.finish_time = current_time

        if all_processes_finished:
            break

def calculate_metrics(processes):
    total_turnaround_time = sum(process.finish_time - process.arrival_time for process in processes)
    total_response_time = sum(process.start_time - process.arrival_time for process in processes)
    total_waiting_time = sum((process.finish_time - process.arrival_time - process.burst_time) for process in processes)
    
    average_turnaround_time = total_turnaround_time / len(processes)
    average_response_time = total_response_time / len(processes)
    average_waiting_time = total_waiting_time / len(processes)

    return average_turnaround_time, average_response_time, average_waiting_time

if __name__ == "__main__":
    processes = [
        Process(1, 0, 2),
        Process(2, 1, 8),
        Process(3, 2, 3),
        Process(4, 5, 1),
        Process(5, 7, 2)
    ]

    time_quantum = 4
    round_robin(processes, time_quantum)
    avg_turnaround, avg_response, avg_waiting = calculate_metrics(processes)

    print("Round Robin (q=1) Scheduling:")
    print(f"Average Turnaround Time: {avg_turnaround}")
    print(f"Average Response Time: {avg_response}")
    print(f"Average Waiting Time: {avg_waiting}")
