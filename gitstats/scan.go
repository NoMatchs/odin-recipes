package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

const dotFileName = ".gogitlocalstats"

// scan 扫描指定目录下的所有 Git 仓库并保存到本地文件中
func scan(folder string) {
	fmt.Printf("正在扫描目录: %s\n\n", folder)
	repositories := recursiveScanFolder(folder)
	filePath := getDotFilePath()
	addNewSliceElementsToFile(filePath, repositories)
	fmt.Printf("\n成功添加了 %d 个仓库\n\n", len(repositories))
}

// recursiveScanFolder 递归扫描目录
func recursiveScanFolder(folder string) []string {
	return scanGitFolders(make([]string, 0), folder)
}

// scanGitFolders 是递归扫描的核心逻辑
func scanGitFolders(folders []string, folder string) []string {
	// 清理路径格式
	folder = filepath.Clean(folder)

	// 跳过不需要扫描的目录，提升速度
	baseName := filepath.Base(folder)
	if baseName == "node_modules" || baseName == "vendor" || baseName == ".git" {
		return folders
	}

	// 检查当前目录是否包含 .git 文件夹
	gitFolder := filepath.Join(folder, ".git")
	if _, err := os.Stat(gitFolder); err == nil {
		folders = append(folders, folder)
	}

	// 读取当前目录下的所有文件/文件夹
	files, err := os.ReadDir(folder)
	if err != nil {
		return folders
	}

	// 遍历子目录并递归
	for _, file := range files {
		if file.IsDir() {
			// 跳过隐藏目录（如 .git, .idea 等）
			if strings.HasPrefix(file.Name(), ".") {
				continue
			}
			folders = scanGitFolders(folders, filepath.Join(folder, file.Name()))
		}
	}
	return folders
}

// getDotFilePath 获取存储仓库列表的文件路径（位于用户主目录）
func getDotFilePath() string {
	home, err := os.UserHomeDir()
	if err != nil {
		fmt.Println("无法获取用户主目录:", err)
		os.Exit(1)
	}
	return filepath.Join(home, dotFileName)
}

// addNewSliceElementsToFile 将新的仓库路径合并到文件中（去重）
func addNewSliceElementsToFile(filePath string, newRepos []string) {
	existingRepos := parseFileLinesToSlice(filePath)
	repos := joinSlices(newRepos, existingRepos)
	dumpStringsSliceToFile(repos, filePath)
}

// parseFileLinesToSlice 读取文件内容并转为切片
func parseFileLinesToSlice(filePath string) []string {
	f, err := os.Open(filePath)
	if err != nil {
		if os.IsNotExist(err) {
			return []string{}
		}
		return []string{}
	}
	defer f.Close()

	var lines []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

// joinSlices 合并两个切片并去重
func joinSlices(newSlice, existingSlice []string) []string {
	for _, item := range newSlice {
		found := false
		for _, existingItem := range existingSlice {
			if item == existingItem {
				found = true
				break
			}
		}
		if !found {
			existingSlice = append(existingSlice, item)
		}
	}
	return existingSlice
}

// dumpStringsSliceToFile 将切片内容写入文件
func dumpStringsSliceToFile(repos []string, filePath string) {
	content := strings.Join(repos, "\n")
	err := os.WriteFile(filePath, []byte(content), 0644)
	if err != nil {
		fmt.Println("写入文件失败:", err)
	}
}