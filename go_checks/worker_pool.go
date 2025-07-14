/*
Concurrency: Worker Pool in Go
Problem Statement:
Implement a worker pool in Go.

You are given:
A slice of jobs (e.g., job IDs or durations).
A fixed number of workers (N).

Each worker:
Picks up jobs from a shared queue.
Simulates job processing using time.Sleep(...).
Once all jobs are completed, the program exits.


Input:
jobs := []int{1000, 500, 300, 1200, 800} // durations in ms
numWorkers := 3

Output:
Worker 1 started job 0
Worker 2 started job 1
Worker 3 started job 2
Worker 2 finished job 1
Worker 2 started job 3
Worker 1 finished job 0
Worker 1 started job 4
...

Goroutines used to call the workers concurrently
Channels can be used to send the jobs to the goroutines
Waitgroups can be used to make sure all jobs are executed before the program exits

- Make jobs channel of size len(jobs), buffered channel, upto the mentioned the goroutines/workers can be created without a deadlock
- Wait group can be created
- For the specific number of workers given as input, that many goroutines an be kept ready to simulate job execution, whenever the job is sent through the channel
	- Loop over the wokers
	- Log messages
	- Simulate the job being executed using the time sleep
	- wait group done
- Loop over jobs to send in the job ids to be executed
	- wait groups to be added for each job
	- job can be sent to the channel
	- log a meesage as well
- Let wait group wait until all jobs are done
- Close the jobs channel


*/

package main

import (
	"fmt"
	"context"
	"sync"
	"time"
)

func worker(ctx context.Context, id int, jobs <-chan int, wg *sync.WaitGroup) {
	for {
		select {
		case <- ctx.Done():
			fmt.Printf("Worker %d received shutdown signal\n", id)
			return
		case job, ok := <-jobs:
			if !ok {return}
			start := time.Now()
			fmt.Printf("Worker %d started job %d\n", id, job)
			time.Sleep(time.Duration(job) * time.Millisecond)
			duration := time.Since(start)
			fmt.Printf("Worker %d completed job %d took %v\n", id, job, duration)
			wg.Done()
		}
	}
}

func processJobs (ctx context.Context, jobsList []int, numWorkers int) {
	jobs := make(chan int, len(jobsList))
	var wg sync.WaitGroup

	for i := 1; i <= numWorkers; i++ {
		go worker(ctx, i, jobs, &wg)
	}

	for job := range jobsList {
		select {
		case <- ctx.Done():
			fmt.Printf("Main: Context cancelled, cancelling job submission")
			break
		default:
			wg.Add(1)
			jobs <- job
			fmt.Printf("Main: Job queued %d\n", job) 
		}
	}

	close(jobs)
	wg.Wait()
}

func mainWorkerPool () {
	ctx, cancel := context.WithTimeout(context.Background(), 1*time.Nanosecond)
	defer cancel()
	jobs := []int{1000, 500, 300, 1200, 800} // durations in ms
	numWorkers := 3
	processJobs(ctx, jobs, numWorkers)
}