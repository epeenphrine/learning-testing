package main

import (

	//"fmt"
	"log"

	"github.com/gin-gonic/gin"
	"github.com/ulule/limiter"
	"github.com/ulule/limiter/drivers/store/memory"
	mgin "github.com/ulule/limiter/drivers/middleware/gin"

)

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

	r := gin.Default()
	r.ForwardedByClientIP = true
	
	r.GET("/", HomePage) //limited amoutn of requests
	r.Use(middleware).POST("/", QueryRequest) //limited amoutn of requests
	r.GET("/query", QueryStrings) //query?name=elliot&age=24
	r.GET("/path/:name/:age", PathParameters) //query?name=elliot&age=24

	r.Run(":2000")

}
