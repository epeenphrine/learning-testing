package main 

import (
	"fmt"
)


func looping() {
	fmt.Println("starting looping function")
	sum := 0 
	for i := 0; i < 10; i++ {
		sum +=i
		fmt.Println(sum)
	}
	fmt.Println("loop ended")
}