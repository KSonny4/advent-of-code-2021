package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	f, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()	
	
	s := bufio.NewScanner(f)

	last := -1
	increased := 0
	for s.Scan() {
		var n int
		_, err := fmt.Sscanf(s.Text(), "%d", &n)
		if err != nil {
			log.Fatalf("could not read %s: %v", s.Text(), err)
		}
		
		if n > last {
			increased++
		}

		last = n
	}
	if err := s.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Println(increased - 1) // The first number has no predecesor
}