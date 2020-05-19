package main 

import "fmt"

/// pointers in go
func pointer() {

	x := 15
	a := &x // & point to x

	fmt.Println(a)  // memory address
	fmt.Println(*a) // asterisk reads the memory addres

	*a = 5 //sets the value pointed at to 5, so x is modified

	fmt.Println(x)

	*a = *a * *a //

	fmt.Println(*a)
	fmt.Println(x)

	fmt.Println(&x) //memory address
	fmt.Println(a)  //memory address

}