package main

import "fmt"

// mapping in golang
//would be in python

func mapping() {

	grades := make(map[string]float32)

	grades["timmy"] = 42
	grades["jess"] = 92
	grades["sam"] = 71

	fmt.Println(grades)

	tims_grade := grades["timmy"]

	fmt.Println(grades)
	fmt.Println(tims_grade)
	fmt.Println(grades["jess"])

	for k, v := range grades {
		fmt.Println(k, ":", v)
	}

	delete(grades, "timmy")
	fmt.Println(grades)

}
