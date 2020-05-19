package main

import (

	"github.com/gin-gonic/gin"

)

func main() {
	// limited to 60 - M

	r := gin.Default()

	r.GET("/api/TDA", tda)
	r.Run(":2500")
}
