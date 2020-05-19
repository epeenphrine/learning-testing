package main

import (

	"github.com/gin-gonic/gin"

)

func HomePage(c *gin.Context) {
	c.JSON(200, gin.H{
		"message": "hello world",
	})
}
