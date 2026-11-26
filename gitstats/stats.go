package main

import (
	"fmt"
	"time"

	git "github.com/go-git/go-git/v5"
	"github.com/go-git/go-git/v5/plumbing/object"
)

// daysInLastSixMonths 统计最近 6 个月（约 183 天）
const daysInLastSixMonths = 365

// stats 是 main.go 调用的入口函数
func stats(email string) {
	commits := processRepositories(email)
	printCommitsStats(commits)
}

// processRepositories 遍历所有已记录的仓库，统计提交
func processRepositories(email string) map[int]int {
	filePath := getDotFilePath()
	repos := parseFileLinesToSlice(filePath)
	daysMap := make(map[int]int)

	for _, repo := range repos {
		fmt.Printf("正在统计仓库: %s\n", repo)
		fillCommits(email, repo, daysMap)
	}
	return daysMap
}

// fillCommits 读取单个仓库的提交历史并填充到 daysMap
func fillCommits(email string, path string, commits map[int]int) {
	repo, err := git.PlainOpen(path)
	if err != nil {
		fmt.Println("无法打开仓库:", path, err)
		return
	}

	ref, err := repo.Head()
	if err != nil {
		return
	}

	iterator, err := repo.Log(&git.LogOptions{From: ref.Hash()})
	if err != nil {
		return
	}

	err = iterator.ForEach(func(c *object.Commit) error {
		if c.Author.Email != email {
			return nil
		}

		daysAgo := int(time.Since(c.Author.When).Hours() / 24)
		if daysAgo < daysInLastSixMonths {
			commits[daysAgo]++
		}
		return nil
	})
	if err != nil {
		fmt.Println("遍历提交记录时出错:", err)
	}
}