package main

import (
	"fmt"
	"sort"
	"time"
)

type column []int

const (
	weeksInLastSixMonths = 52
)

func printCommitsStats(commits map[int]int) {
	keys := sortMapIntoSlice(commits)
	cols := buildCols(keys, commits)
	printCells(cols)
}

func sortMapIntoSlice(m map[int]int) []int {
	var keys []int
	for k := range m {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	return keys
}

func buildCols(keys []int, commits map[int]int) map[int]column {
	cols := make(map[int]column)
	col := make(column, 0)

	for _, k := range keys {
		// 计算是第几周（列）
		week := int(k / 7)
		// 计算是星期几（行）
		dayInWeek := k % 7

		if dayInWeek == 0 {
			// 新的一周开始
			col = make(column, 0)
			cols[week] = col
		}
		cols[week] = append(cols[week], commits[k])
	}
	return cols
}

func printCells(cols map[int]column) {
	printMonths()
	for j := 6; j >= 0; j-- {
		for i := 0; i < weeksInLastSixMonths+1; i++ {
			if i == weeksInLastSixMonths {
				printDayCol(j)
			}
			if col, ok := cols[i]; ok {
				if len(col) > j {
					printCommitChar(col[j])
				} else {
					printCommitChar(0)
				}
			} else {
				printCommitChar(0)
			}
		}
		fmt.Printf("\n")
	}
	printLegend()
}

func printMonths() {
	week := getBeginningOfWeek(time.Now())
	month := week.Month()
	fmt.Printf("  ")
	for {
		if week.Month() != month {
			fmt.Printf("%s ", week.Month().String()[:3])
			month = week.Month()
		} else {
			fmt.Printf("   ")
		}
		week = week.Add(7 * 24 * time.Hour)
		if week.After(time.Now()) {
			break
		}
	}
	fmt.Printf("\n")
}

func printDayCol(day int) {
	out := " "
	switch day {
	case 1:
		out = " Mon "
	case 3:
		out = " Wed "
	case 5:
		out = " Fri "
	}
	fmt.Printf(out)
}

func printCommitChar(commits int) {
	if commits > 4 {
		fmt.Printf("▓")
	} else if commits > 0 {
		fmt.Printf("▒")
	} else {
		fmt.Printf("░")
	}
}

func printLegend() {
	fmt.Printf("\n")
	fmt.Printf("░ = 无提交    ▒ = 1-4 次提交    ▓ = 5 次以上提交\n")
}

func getBeginningOfWeek(t time.Time) time.Time {
	// 将时间调整到周日的 0 点
	offset := (int(t.Weekday()) + 6) % 7
	return t.AddDate(0, 0, -offset).Truncate(24 * time.Hour)
}