package main

import (
	"encoding/json"
	"fmt"
	"log"
	"reflect"

	"github.com/levigross/grequests"
)


type Data struct {
	State     string `json: "state"`
	Positive  uint32 `json: "positive"`
	Recovered uint32 `json: "recovered"`
}

func makeRequest() string {
	// decode to a slice of DAta
	var d []Data

	res, err := grequests.Get("https://covidtracking.com/api/states", nil)
	fmt.Println(reflect.TypeOf(res.Bytes()))

	resBytes := res.Bytes()

	json.Unmarshal(resBytes, &d)

	fmt.Println(d)
	if err != nil {
		log.Println("error happened ", err)
	}

	return res.String()
}

func jsonParse() {

}

type Testings struct {
	Testing string `json: "testing"`
}

func main() {
	
	//convert json to struct to work with it 
	var v []Testings
	//log.Println(makeRequest())
	example := `[{"testing": "this is the first item"}, {"testing":"this is the second item"}]`
	fmt.Println(example)
	fmt.Println(reflect.TypeOf(example))
	json.Unmarshal([]byte(example), &v)
	fmt.Println(v)
	fmt.Println(reflect.TypeOf(v))

	//turn back struct to json


}
