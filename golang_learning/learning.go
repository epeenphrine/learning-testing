package main 

import "fmt"

//structs

type car struct {
	gas_pedal uint16 
	brake_pedal uint16
	steering_wheel int16
}


// loopin in go 
func looping() {
	fmt.Println("starting looping function")
	sum := 0 
	for i := 0; i < 10; i++ {
		sum +=i
		fmt.Println(sum)
	}
	fmt.Println("loop ended")
}


func main() {
	fmt.Println("this is from main ")
	looping()
}