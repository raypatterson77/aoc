package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func ParseInput() []byte {
	fileInput, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	return fileInput
}

func ConvertInputToIntSlices(input []byte) ([]int, []int) {
	var left, right []int
	inputString := string(input)
	for i, number := range strings.Fields(inputString) {
		numberInt, err := strconv.Atoi(number)
		if err != nil {
			panic(err)
		}
		switch i % 2 {
		case 0:

			left = append(left, numberInt)
		default:
			right = append(right, numberInt)
		}
	}
	return left, right
}

func SortSlice(unsorted []int) []int {
	sorted := make([]int, len(unsorted))
	copy(sorted, unsorted)
	sort.Ints(sorted)
	return sorted
}

func abs(i int) int {
	if i < 0 {
		return -i
	}
	return i
}

func ComputeAwnser(l, r []int) int {
	var awnser int = 0
	if len(l) != len(r) {
		fmt.Println("needs to be equal")
	}
	for i := range l {
		a := l[i] - r[i]
		awnser = awnser + abs(a)
	}
	return awnser

}

func main() {
	byteInput := ParseInput()
	leftList, rightList := ConvertInputToIntSlices(byteInput)
	fmt.Printf("the awnser is: %d\n", ComputeAwnser(SortSlice(leftList), SortSlice(rightList)))
}
