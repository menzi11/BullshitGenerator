// +build windows

package main

import (
	"math/rand"
)

//get the random numer in [min, max]
func RandInt(min, max int) int {
	if min >= max || max == 0 {
		return max
	}

	x := rand.Intn(max-min) + min

	//fmt.Println("RandInt: = ",x)
	return x
}
