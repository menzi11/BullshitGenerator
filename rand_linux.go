// +build linux

package main

import (
	"math/rand"
	"time"
)

//get the random numer in [min, max]
func RandInt(min, max int) int {
	if min >= max || max == 0 {
		return max
	}
	rand.Seed(time.Now().UnixNano())

	//x := r.Intn(max-min) + min
	x := rand.Intn(max-min) + min

	//fmt.Println("RandInt: = ",x)
	return x
}
