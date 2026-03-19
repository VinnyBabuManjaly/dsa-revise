// Writing a function that return Content-Type header
package main

import (
	"fmt"
	"net/http"
)

func contentType(url string) (string, error) {
	resp, err := http.Get(url)
	if err != nil {
		return "", err
	}

	defer resp.Body.Close()

	ctype := resp.Header.Get("Content-Type")
	if ctype == "" {
		return "", fmt.Errorf("cant find content-type header")
	}

	return ctype, nil
}

func main() {
	ctype, err := contentType("https://www.linkedin.com")
	if err != nil {
		fmt.Printf("Error: %s\n", err)
	} else {
		fmt.Printf("Content-Type: %s", ctype)
	}
}
