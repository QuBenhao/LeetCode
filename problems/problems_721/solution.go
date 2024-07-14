package problem721

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func accountsMerge(accounts [][]string) [][]string {
	emailToName := map[string]string{}
	graph := map[string]map[string]struct{}{}

	for _, account := range accounts {
		name := account[0]
		for i := 1; i < len(account); i++ {
			email := account[i]
			if _, ok := graph[email]; !ok {
				graph[email] = map[string]struct{}{}
			}
			if _, ok := graph[account[1]]; !ok {
				graph[account[1]] = map[string]struct{}{}
			}
			graph[account[1]][email] = struct{}{}
			graph[email][account[1]] = struct{}{}
			emailToName[email] = name
		}
	}

	visited := map[string]bool{}
	var dfs func(email string) []string
	dfs = func(email string) []string {
		visited[email] = true
		emails := []string{email}
		for neighbor := range graph[email] {
			if !visited[neighbor] {
				emails = append(emails, dfs(neighbor)...)
			}
		}
		return emails
	}

	var res [][]string
	for email := range graph {
		if !visited[email] {
			emails := dfs(email)
			name := emailToName[email]
			emailList := append([]string{name}, emails...)
			res = append(res, emailList)
		}
	}
	for _, emails := range res {
		sort.Strings(emails[1:])
	}
	return res
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var accounts [][]string

	if err := json.Unmarshal([]byte(inputValues[0]), &accounts); err != nil {
		log.Fatal(err)
	}

	return accountsMerge(accounts)
}
