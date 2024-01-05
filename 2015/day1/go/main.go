package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	moveInstructions, err := os.ReadFile("input.txt")
	var solutionPart1 int
	if err != nil {
		log.Fatalf("unable to read: %v", err)
	}
	solutionPart1 = strings.Count(string(moveInstructions), "(") - strings.Count(string(moveInstructions), ")")
	fmt.Printf("Solution part1 is: %d", solutionPart1)
}
