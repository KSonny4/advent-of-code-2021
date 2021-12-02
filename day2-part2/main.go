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

	horizontal := 0
	depth := 0
	for s.Scan() {
		var command string
		var n int
		_, err := fmt.Sscanf(s.Text(), "%s %d", &command, &n)
		if err != nil {
			log.Fatalf("could not read %s: %v", s.Text(), err)
		}

		if command == "forward"{
			horizontal += n
		} else if command == "up" {
			depth -= n
		} else if command == "down" {
			depth += n		
		} else {
			panic(fmt.Sprintf("Unknown command: %s", command))
		}
	}

	fmt.Println(horizontal*depth)

}