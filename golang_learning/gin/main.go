package main

import (
	"fmt"
	"io/ioutil"
	"log"

	"github.com/gin-gonic/gin"
	"github.com/ulule/limiter"
	"github.com/ulule/limiter/drivers/store/memory"
	mgin "github.com/ulule/limiter/drivers/middleware/gin"
)


func HomePage(c *gin.Context) {
	c.JSON(200, gin.H{
		"message": "hello world",
	})
}

func PostHomePage(c *gin.Context) {
	
	body := c.Request.Body 

	value, err := ioutil.ReadAll(body)
	if err != nil {
		fmt.Println(err.Error())
	}

	c.JSON(200, gin.H{
		"message": string(value),
	})
}

func QueryStrings(c *gin.Context) {

	name := c.Query("name")
	age := c.Query("age")

	c.JSON(200, gin.H{
		"name": name,
		"age":  age,
	})
}

func PathParameters(c *gin.Context) {

	name := c.Param("name")
	age := c.Param("age")
	
	c.JSON(200, gin.H{
		"name": name,
		"age":  age,
	})
}

func main() {

	// limited to 60 - M
	rate, err := limiter.NewRateFromFormatted("60-M")
	if err != nil {
		log.Fatal(err)
	}
	// ip timeouts stored in memory
	store := memory.NewStore()
	middleware := mgin.NewMiddleware(limiter.New(store, rate))

	fmt.Println("hello world")

	r := gin.Default()
	rLimit := gin.Default()
	rLimit.ForwardedByClientIP = true
	rLimit.Use(middleware)
	

	rLimit.GET("/", HomePage)
	r.POST("/", PostHomePage)
	r.GET("/query", QueryStrings) //query?name=elliot&age=24
	r.GET("/path/:name/:age", PathParameters) //query?name=elliot&age=24

	rLimit.Run()
	r.Run()
}
