package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func int_binary_arr_to_decimal(sigBits []int) (error, int64) {
	binary := strings.Trim(strings.Join(strings.Fields(fmt.Sprint(sigBits)), ""), "[]")

	decimal, err := strconv.ParseInt(binary, 2, 64)
	if err != nil {
		fmt.Println(err)
		return err, -1
	}
	return nil, decimal
}

func main() {
	f, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	s := bufio.NewScanner(f)

	var arr []string
	for s.Scan() {
		var n string
		_, err := fmt.Sscanf(s.Text(), "%s", &n)
		if err != nil {
			log.Fatalf("could not read %s: %v", s.Text(), err)
		}
		arr = append(arr, n)
	}

	lenOfOneWord := len(arr[0])
	lenOfInput := len(arr)
	sigBits := make([]int, lenOfOneWord)

	for i := 0; i < lenOfOneWord; i++ {
		onesCount := 0
		for _, num := range arr {
			numRune := []rune(num)
			if numRune[i] == '1' {
				onesCount++
			}
		}
		if onesCount < lenOfInput/2 {
			sigBits[i] = 1
		}
	}

	err, gamma := int_binary_arr_to_decimal(sigBits)
	if err != nil {
		fmt.Println(err)
		return
	}

	reversedSigBits := make([]int, lenOfOneWord)
	for i := 0; i < len(sigBits); i++ {
		if sigBits[i] == 0 {
			reversedSigBits[i] = 1
		} else if sigBits[i] == 1 {
			reversedSigBits[i] = 0
		}
	}

	err, eps := int_binary_arr_to_decimal(reversedSigBits)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(gamma * eps)

}
