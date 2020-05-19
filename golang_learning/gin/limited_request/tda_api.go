package main

import (
	"github.com/gin-gonic/gin"
)

func tda(c *gin.Context) {
	c.JSON(200, gin.H{
		"message": "this is a reroute from 2000",
	})
}
