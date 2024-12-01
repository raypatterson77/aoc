package main

import (
	"reflect"
	"testing"
)

func TestParseInput(t *testing.T) {
	input_test := []byte(`3   4
4   3
2   5
1   3
3   9
3   3`)

	input := ParseInput()

	if len(input) != len(input_test) {
		t.Errorf("got %d lines, wanted %d lines", len(input), len(input_test))
	}
}

func TestConvert(t *testing.T) {
	leftListTest := []int{3, 4, 2, 1, 3, 3}
	rightListTest := []int{4, 3, 5, 3, 9, 3}
	input := ParseInput()
	leftList, rightList := ConvertInputToIntSlices(input)

	if reflect.DeepEqual(leftListTest, leftList) != true {
		t.Errorf("left list wrong, got %v, wanted %v", leftList, leftListTest)
	}
	if reflect.DeepEqual(rightListTest, rightList) != true {
		t.Errorf("left list wrong, got %v, wanted %v", rightList, rightListTest)
	}
}

func TestSorting(t *testing.T) {
	sortedTest := []int{1, 2, 3}
	sorted := SortSlice([]int{2, 1, 3})

	if reflect.DeepEqual(sortedTest, sorted) != true {
		t.Errorf("sorting wrong: got: %v, wanted %v", sorted, sortedTest)
	}
}

func TestComputeAwnser(t *testing.T) {
	awnserTest := 11
	input := ParseInput()
	leftList, rightList := ConvertInputToIntSlices(input)
	awnser := ComputeAwnser(SortSlice(leftList), SortSlice(rightList))

	if reflect.DeepEqual(awnserTest, awnser) != true {
		t.Errorf("sorting wrong: got: %d, wanted %d", awnser, awnserTest)
	}
}
