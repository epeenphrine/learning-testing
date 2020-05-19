package main

import (
	"fmt"
	"time"
)

func say(s string) {
	for i := 0; i < 3; i ++ {
		time.Sleep(100*time.Millisecond)
		fmt.Println(s)
	}
}



func concurrency() {
	go say("hey")
	go say ("there")
	time.Sleep(1000*time.Millisecond)
}