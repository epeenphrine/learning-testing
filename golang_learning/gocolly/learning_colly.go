package main

// http://go-colly.org/docs/examples/basic/

import (
	"fmt"
	"github.com/gocolly/colly"
	"strings"
)

func crawl () {
	c := colly.NewCollector(
		// Visit only domains: hackerspaces.org, wiki.hackerspaces.org
		colly.AllowedDomains("scholarships.com", "www.scholarships.com"),
		colly.MaxDepth(4),
		colly.Async(true),
		colly.UserAgent("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"),

	)
	c.Limit(&colly.LimitRule{
		DomainGlob: "*", 
		Parallelism: 4,
		//Delay: 5*time.Second, 
})
	//request
	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL.String())
	})

	//response
	c.OnResponse(func(r *colly.Response) {
		url := r.Ctx.Get("url")
		fmt.Println(url)
	})

	//error handler
	c.OnError(func(r *colly.Response, err error) {
		fmt.Println("Request URL:", r.Request.URL, "failed with response:", r, "\nError:", err)
	})

	
	count := 0
	// On every a element which has href attribute call callback
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		link := e.Attr("href")
		// Print link
		if strings.Contains(link, "/financial-aid/") {
			fmt.Printf("Link found: %q -> %s\n", e.Text, link)
			c.Visit(e.Request.AbsoluteURL(link))
			count += 1
			fmt.Println(count) 
		} else {
			fmt.Println("not a good link")
		}
		// Visit link found on page
		// Only those links are visited which are in AllowedDomains
	})



	// Before making a request print "Visiting ..."

	// Start scraping on https://hackerspaces.org
	c.Visit("https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/")
	c.Wait()
}


func parse() {
	// initiate gocolly
	c := colly.NewCollector(
		// Max depth  of 2 
		colly.MaxDepth(2),
		colly.Async(true),
	)

	c.Visit("https://en.wikipedia.org/")

	c.Limit(&colly.LimitRule{DomainGlob: "*", Parallelism:2})
	// Find and visit all links

	//find h1 element with class attribute
	c.OnHTML("div[id]", func(e *colly.HTMLElement) {
		//e.Attr gives value of whatever attribute
		
		id := e.Attr("id")
		text := e.Text
		//selecting attribute value 

		if id == "mp-tfa"{

			//fmt.Printf("%T\n", id)	
			//fmt.Printf("%T\n", text)

			fmt.Println(id)
			save(text)
		}


		// printing Texts
		//text := e.Text
		//fmt.Println(text)

		// uncomment for crawling
		//e.Request.Visit(class)
	})

	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL)
	})

	c.Wait()
}

func save (s string) {
	fmt.Println("from func save")
	fmt.Println(s)
}

func main() {
	//parse()
	crawl()

}