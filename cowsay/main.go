package main

import (
	"bufio"
	"flag"
	"fmt"
	"io"
	"os"
	"strings"
	"unicode/utf8"
)

// 默认的奶牛画 (内置)
const cowArt = `
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
`

func main() {
	// -f 参数指定动物文件
	animal := flag.String("f", "cow", "选择动物文件 (例如: xia.cow)")
	flag.Parse()

	// 1. 检查输入是否来自管道
	info, _ := os.Stdin.Stat()
	if info.Mode()&os.ModeCharDevice != 0 {
		fmt.Println("这个命令需要配合管道使用。")
		fmt.Println("用法示例: echo 'Hello' | gocowsay -f xia.cow")
		return
	}

	// 2. 读取管道输入
	reader := bufio.NewReader(os.Stdin)
	var output []rune
	for {
		input, _, err := reader.ReadRune()
		if err != nil && err == io.EOF {
			break
		}
		output = append(output, input)
	}

	// 3. 处理文字
	text := strings.TrimSpace(string(output))
	lines := strings.Split(text, "\n")

	// 4. 画气泡
	fmt.Println(buildBalloon(lines))

	// 5. 决定显示什么动物
	if *animal == "cow" {
		fmt.Println(cowArt)
	} else {
		// 尝试作为外部文件读取
		art, err := loadArtFromFile(*animal)
		if err != nil {
			// 如果读取失败，强制打印错误，不糊弄自己
			fmt.Printf("\n[严重错误] 无法读取文件 %s: %v\n", *animal, err)
		} else {
			// 读取成功，直接打印图案
			fmt.Print(art)
			// 确保最后有一个换行
			if !strings.HasSuffix(art, "\n") {
				fmt.Println()
			}
		}
	}
}

// buildBalloon 生成 ASCII 气泡
func buildBalloon(lines []string) string {
	maxLen := 0
	for _, line := range lines {
		l := utf8.RuneCountInString(line)
		if l > maxLen {
			maxLen = l
		}
	}

	var sb strings.Builder
	sb.WriteString(" " + strings.Repeat("_", maxLen+2) + "\n")

	for i, line := range lines {
		lineLen := utf8.RuneCountInString(line)
		padding := strings.Repeat(" ", maxLen-lineLen)

		if len(lines) == 1 {
			sb.WriteString(fmt.Sprintf("< %s%s >\n", line, padding))
		} else if i == 0 {
			sb.WriteString(fmt.Sprintf("/ %s%s \\\n", line, padding))
		} else if i == len(lines)-1 {
			sb.WriteString(fmt.Sprintf("\\ %s%s /\n", line, padding))
		} else {
			sb.WriteString(fmt.Sprintf("| %s%s |\n", line, padding))
		}
	}
	sb.WriteString(" " + strings.Repeat("-", maxLen+2))
	return sb.String()
}

// loadArtFromFile 读取外部图案文件
func loadArtFromFile(filename string) (string, error) {
	// 如果没有指定后缀，默认加上 .cow
	if !strings.Contains(filename, ".") {
		filename += ".cow"
	}

	content, err := os.ReadFile(filename)
	if err != nil {
		return "", err
	}

	// 直接返回文件内容
	return string(content), nil
}