package main 

import (
	"fmt"
	"log"
	"os"
	"os/exec"
)

func bash() {

	fmt.Println("starting")
	cmd := exec.Command("bash","job.sh")
	fmt.Println("starting1")

	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	fmt.Println("starting2")
	log.Println(cmd.Run()) //executes here 
	fmt.Println("finished")

}

func python() {

	python := exec.Command("python3", "job.py")

	python.Stdout = os.Stdout
	python.Stderr = os.Stderr
	log.Println(python.Run())

}


func main () {

	python()
	bash()

}