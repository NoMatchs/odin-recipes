package main

import (
	"bufio"
	"flag"
	"fmt"
	"math"
	"math/rand"
	"os"
	"strings"
	"time"

	"golang.org/x/term"
)

var (
	freq   = flag.Float64("freq", 0.1, "色相变化频率")
	spread = flag.Float64("spread", 3.0, "每行色相偏移量")
	force  = flag.Bool("force", false, "强制输出彩色")
	useBg  = flag.Bool("bg", false, "背景色模式")
)

func main() {
	flag.Parse()
	rand.Seed(time.Now().UnixNano())

	useColor := *force || isTerminal()
	files := flag.Args()

	// 核心色相控制（从随机位置开始）
	hue := rand.Float64()

	// 获取标准输入状态，判断是否有管道输入
	stat, _ := os.Stdin.Stat()
	isPiped := (stat.Mode() & os.ModeCharDevice) == 0

	// 1. 如果没有文件参数，且没有管道输入，生成硬件废话
	if len(files) == 0 && !isPiped {
		words := generateHardwareWords(100)
		longText := strings.Join(words, " ")
		termWidth := getTerminalWidth()
		for len(longText) > 0 {
			end := termWidth
			if end > len(longText) {
				end = len(longText)
			}
			line := longText[:end]
			longText = longText[end:]
			line = strings.TrimLeft(line, " ")
			if line == "" {
				continue
			}
			colored, newHue := rainbow(line, hue, useColor, termWidth)
			fmt.Println(colored)
			hue = newHue + *spread
		}
		return
	}

	// 2. 如果有管道输入，处理管道数据（这里就是 cowsay 传过来的图案）
	if isPiped {
		scanner := bufio.NewScanner(os.Stdin)
		for scanner.Scan() {
			colored, newHue := rainbow(scanner.Text(), hue, useColor, 0)
			fmt.Println(colored)
			hue = newHue + *spread
		}
		return
	}

	// 3. 如果传了文件参数，读取文件
	for _, file := range files {
		lines, err := readLines(file)
		if err != nil {
			fmt.Fprintf(os.Stderr, "无法读取文件 %s: %v\n", file, err)
			continue
		}
		for _, line := range lines {
			colored, newHue := rainbow(line, hue, useColor, 0)
			fmt.Println(colored)
			hue = newHue + *spread
		}
	}
}

func rainbow(line string, hue float64, useColor bool, termWidth int) (string, float64) {
	if !useColor {
		return line, hue
	}

	var sb strings.Builder
	if *useBg {
		sb.WriteString("\x1b[30m")
	}

	currentHue := hue
	for _, ch := range line {
		r, g, b := hsvToRgb(math.Mod(currentHue*360, 360), 1.0, 1.0)
		prefix := "38"
		if *useBg {
			prefix = "48"
		}
		sb.WriteString(fmt.Sprintf("\x1b[%s;2;%d;%d;%dm", prefix, r, g, b))
		sb.WriteRune(ch)
		currentHue += *freq / 10.0
	}

	if *useBg && termWidth > 0 && len(line) < termWidth {
		spaces := strings.Repeat(" ", termWidth-len(line))
		sb.WriteString(spaces)
	}

	sb.WriteString("\x1b[0m")
	return sb.String(), currentHue
}

func getTerminalWidth() int {
	width, _, err := term.GetSize(int(os.Stdout.Fd()))
	if err != nil || width <= 0 {
		return 80
	}
	return width
}

func isTerminal() bool {
	return term.IsTerminal(int(os.Stdout.Fd()))
}

func readLines(path string) ([]string, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()
	var lines []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func hsvToRgb(h, s, v float64) (int, int, int) {
	c := v * s
	x := c * (1 - math.Abs(math.Mod(h/60.0, 2)-1))
	m := v - c
	var r, g, b float64
	switch {
	case h >= 0 && h < 60:
		r, g, b = c, x, 0
	case h >= 60 && h < 120:
		r, g, b = x, c, 0
	case h >= 120 && h < 180:
		r, g, b = 0, c, x
	case h >= 180 && h < 240:
		r, g, b = 0, x, c
	case h >= 240 && h < 300:
		r, g, b = x, 0, c
	default:
		r, g, b = c, 0, x
	}
	return int((r+m)*255), int((g+m)*255), int((b+m)*255)
}

var adjectives = []string{"symmetric", "virtual", "optical", "digital", "wireless", "haptic", "solid state", "primary", "back-end", "cross-platform", "open-source", "neural", "quantum"}
var nouns = []string{"hard drive", "SSD", "FTP circuit", "IB capacitor", "HTTP bus", "JBOD hard drive", "SMS array", "SSL bandwidth", "GB protocol", "UX paradigm", "RAM circuit", "AI firewall", "mobile agent"}

func generateHardwareWords(n int) []string {
	var words []string
	for i := 0; i < n; i++ {
		words = append(words, adjectives[rand.Intn(len(adjectives))], nouns[rand.Intn(len(nouns))])
	}
	return words
}