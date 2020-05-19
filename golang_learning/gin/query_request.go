package main

import (
	"fmt"
	"log"
	"io/ioutil"

	"github.com/gin-gonic/gin"
	"github.com/levigross/grequests"
	//"encoding/json"
	//"github.com/ulule/limiter"
	//"github.com/ulule/limiter/drivers/store/memory"
	//mgin "github.com/ulule/limiter/drivers/middleware/gin"
)

func makeRequest(qStr string) string {

	respStr := ""
	reqURL := fmt.Sprintf("http://localhost:2500/api/%s", qStr)

	log.Println("making request to :", reqURL)
	resp1, err := grequests.Get(string(reqURL), nil)
	respStr = resp1.String()

	if err != nil {
		fmt.Println("error!", err)
	}

	fmt.Println(respStr)
	return respStr

}

func QueryRequest(c *gin.Context) {

	//query from request
	qreq := c.Request.Body
	qBytes, err := ioutil.ReadAll(qreq)
	qStr := string(qBytes)

	if err != nil {
		fmt.Println(err.Error())
	} else {
		fmt.Println(qStr)
	}

	if qStr == "TDA" {

		log.Println(fmt.Sprintf("query: %s", qStr))
		
		resp := makeRequest(qStr)

		c.JSON(200, gin.H{
			"message": resp, 
		})
	} else {
		fmt.Println("didn't match anything")
		c.JSON(200, gin.H{

			"error" :   "query didn't return a match",
			"message" : "did you enter query correctly?",

		})
	}

}
