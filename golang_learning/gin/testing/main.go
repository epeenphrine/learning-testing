package main

import (
	"fmt"
	//"github.com/levigross/grequests"
)

//func funcName(input data type) return datatype {
		//logics go here 
//}

func pass(s2 string) string {

	something := s2

	return something

}

func main() {

	s := "hello world!"

	ss := fmt.Sprintf("%s what up", s)

	fmt.Println(ss)
	
	fmt.Println(pass(ss))
}
