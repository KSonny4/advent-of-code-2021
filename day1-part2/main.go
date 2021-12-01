package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func sum(nums []int, start_index int) int {
	sum := 0
	for j := 0; j <= 2; j += 1 {
		sum += nums[start_index+j]
	}
	return sum
}

func main() {
	f, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	s := bufio.NewScanner(f)

	var nums []int

	for s.Scan() {
		var n int
		_, err := fmt.Sscanf(s.Text(), "%d", &n)
		if err != nil {
			log.Fatalf("could not read %s: %v", s.Text(), err)
		}

		nums = append(nums, n)
	}
	if err := s.Err(); err != nil {
		log.Fatal(err)
	}

	inc := 0
	last_sum := -1
	for i := 0; i <= len(nums)-3; i += 1 {
		sum_for_triplet := sum(nums, i)
		if sum_for_triplet > last_sum {
			inc++
		}
		last_sum = sum_for_triplet
	}
	fmt.Println(inc - 1)
}
