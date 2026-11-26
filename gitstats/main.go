package main

import (
	"flag"
	"fmt"
)

func main() {
	var folder string
	var email string

	flag.StringVar(&folder, "add", "", "add a new folder to scan for git repositories")
	flag.StringVar(&email, "email", "", "the email to scan commits for")
	flag.Parse()

	if folder != "" {
		scan(folder)
		return
	}

	if email != "" {
		stats(email)
	} else {
		fmt.Println("请使用 -email 参数指定你的 Git 邮箱")
	}
}