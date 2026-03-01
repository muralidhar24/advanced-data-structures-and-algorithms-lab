class Job:
    def __init__(self, id, deadline, profit):
        self.id = id        # Job ID
        self.deadline = deadline  # Deadline of the job
        self.profit = profit  # Profit of the job

def job_sequencing(jobs):
    """
    Solves the Job Sequencing problem using the Greedy strategy.
    
    Parameters:
        jobs: List of Job objects.
        
    Returns:
        Maximum profit and the sequence of jobs.
    """
    # Sort all jobs in descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = max(job.deadline for job in jobs)  # Find the maximum deadline
    result = [None] * n  # Array to store the result sequence of jobs
    slots = [False] * n  # Boolean array to keep track of free time slots
    total_profit = 0

    # Iterate through all jobs
    for job in jobs:
        # Try to schedule the job in the latest available slot before its deadline
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if not slots[j]:
                slots[j] = True  # Mark the slot as occupied
                result[j] = job.id  # Assign the job to the slot
                total_profit += job.profit  # Add the profit of this job
                break

    # Filter out None values from the result (unscheduled slots)
    scheduled_jobs = [job_id for job_id in result if job_id is not None]
    return total_profit, scheduled_jobs

# Example usage
if __name__ == "__main__":
    jobs = [
        Job("J1", 2, 100),
        Job("J2", 1, 19),
        Job("J3", 2, 27),
        Job("J4", 1, 25),
        Job("J5", 3, 15)
    ]

    max_profit, job_sequence = job_sequencing(jobs)
    print("Maximum Profit:", max_profit)
    print("Job Sequence:", job_sequence)

