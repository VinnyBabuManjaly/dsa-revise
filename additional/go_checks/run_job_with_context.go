/*
Implement a function that processes a job with a timeout.
If the job takes longer than the allowed timeout, it should be cancelled and the function should return "timeout".
Otherwise, it should return "completed".

Input parameters:
Duration - Duration for a job to run and complete, sleeping time for simulation
Timeout

Use context to cancel the job after timeout
Go routine to simulate the completion of job with channel
Select to choose between context done or completed job
*/

package main

import (
	"context"
	"fmt"
	"time"
)

func runJobWithContext (duration time.Duration, timeout time.Duration) string {
	ctx, cancel := context.WithTimeout(context.Background(), timeout)
	defer cancel()

	done := make(chan struct{})
	go func() {
		time.Sleep(duration)
		done <- struct{}{}
	}()

	select {
	case <- ctx.Done():
		return "timeout"
	case <- done:
		return "completed"
	}
}

func mainrunJobWithContext () {
	fmt.Println(runJobWithContext(2*time.Second, 3*time.Second))
	fmt.Println(runJobWithContext(3*time.Second, 1*time.Second))
}