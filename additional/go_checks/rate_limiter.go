/*
Implement a rate limiter in Go that allows each user to make at most N requests per T time window (e.g., 100 requests per minute).

You may be asked to:
Implement per-user rate limiting
Use Go concurrency primitives (time.Ticker, map, mutex, goroutines)
Make the design thread-safe

🧠 Why This is Asked:
Common in real-world API gateways, load balancers, microservices

Tests:
Understanding of timers, caching, goroutines, mutexes
Clean code organization and correctness under concurrency
Optional: use of token bucket or leaky bucket algorithms

Approach: Fixed window approach
Use a userLogs map to store the recent timestamps for the user
Use a mutex so that only one user updates the map at a given time

Pseudo Code
Filter out the timestamps outside the window, i.e keep only timestamps that are after difference between current time and the window given
If len of timestamps map is >= limit, return the request as denied/false
Append the current timestamp to the map and return true or allowed
*/

package main

import (
	"encoding/json"
	"log"
	"net/http"
	"sync"
	"time"
)

type RateLimiter struct {
	limit int
	window time.Duration
	userLogs map[string][]time.Time
	mu sync.Mutex
}

func NewRateLimiter (limit int, window time.Duration) *RateLimiter {
	return &RateLimiter{
		limit: limit,
		window: window,
		userLogs: make(map[string][]time.Time),
	}
}

func (rl *RateLimiter) Allow (userID string) bool {
	rl.mu.Lock()
	defer rl.mu.Unlock()

	now := time.Now()
	windowStart := now.Add(-rl.window)
	requests := rl.userLogs[userID]

	var recent []time.Time
	for _, t := range requests {
		if t.After(windowStart) {
			recent = append(recent, t)
		}
	}

	if len(recent) >= rl.limit {
		return false
	}

	rl.userLogs[userID] = append(recent, now)
	return true
}

type LimiterRequest struct {
	UserID string `json:"userID"`
}

type LimiterResponse struct {
	Allowed	bool `json:"allowed"`
	Reason string `json:"reason,omitempty"`
}

func (limiter *RateLimiter) handleRateLimit () http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var req LimiterRequest 
		if err:= json.NewDecoder(r.Body).Decode(&req); err != nil || req.UserID == "" {
			http.Error(w, "invalid request", http.StatusBadRequest)
			return
		}
		defer r.Body.Close()

		allow := limiter.Allow(req.UserID)

		var resp LimiterResponse
		resp.Allowed = allow
		if !allow {resp.Reason = "Rate limit exceeded"}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(resp)
	}
}

func mainRateLimiter () {
	limiter := NewRateLimiter(3, 10*time.Second)

	// userID := "vinny"
	// for i := 0; i <= 5; i++ {
	// 	allow := limiter.Allow(userID)
	// 	log.Printf("Request %d allow status = %v\n", i, allow)
	// 	time.Sleep(2*time.Second)
	// }

	http.HandleFunc("/check", limiter.handleRateLimit())

	log.Printf("Server started on 8080")
	http.ListenAndServe(":8080", nil)
}