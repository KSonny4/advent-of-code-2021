package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	
)

func binary_to_decimal(str string) (int64, error) {
	decimal, err := strconv.ParseInt(str, 2, 64)
	if err != nil {
		fmt.Println(err)
		return -1, err
	}
	return decimal, nil
}

func filter(arr []string, position int, keep byte) []string {
	// Filters out all values that are not keep
	var filtered []string

	for _, num := range arr {
		if num[position] == keep {
			filtered = append(filtered, num)
		}
	}
	return filtered

}


func compute(arr []string, oxygenOrCO2 string, equalKeep byte) string {
	position := 0
	for len(arr) != 1 {
		ones := 0
		zeros := 0

		for _, num := range arr {
			if num[position] == '0' {
				zeros++
			} else {
				ones++
			}
		}

		var keep byte = '0'
		if ones == zeros {
			arr = filter(arr, position, equalKeep)
		} else if ones > zeros {
			// o2 == delete 0	; co2 == delete 1
			if oxygenOrCO2 == "O2" {
				keep = '1'
			}
			arr = filter(arr, position, keep)
		} else {
			// o2 == delete 1; co2 == delete 0
			if oxygenOrCO2 == "CO2" {
				keep = '1'
			}
			arr = filter(arr, position, keep)
		}
		fmt.Println("=====")
		fmt.Printf("%s: zeros: %d ones: %d\n",oxygenOrCO2, zeros,ones)
		fmt.Println(arr)		
		fmt.Println("=====")

		position++

	}
	return arr[0]
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
	
	o2_b := compute(arr, "O2", '1')
	fmt.Println(o2_b)
	oxygen, err := binary_to_decimal(o2_b)
	if err != nil {
		panic(err)
	}
	fmt.Println(oxygen)
	
	co2_b := compute(arr,"CO2", '0')
	fmt.Println(co2_b)
	co2, err := binary_to_decimal(co2_b)
	if err != nil {
		panic(err)
	}
	fmt.Println(co2)

	fmt.Println(oxygen*co2)
	
}
