// Made by: Shuban Pal

package main

import (
	"fmt"
	"math/rand"
	"os"
	"strings"
)

func main() {
	var wordlist = [9]string{
		"SHARK", "TRAPS", "TRACK", 
		"GRUNT", "AWARD", "SHACK", 
		"HAPPY", "BLACK", "SHARP",
	}
	var builder string
	chances := 5
	word := wordlist[rand.Intn(len(wordlist))]
	for i := 1; i < chances+1; i++ {
		var guess string
		fmt.Printf("Guess %d? ", i)
		fmt.Scanf("%s", &guess)
		guess = strings.ToUpper(guess)
		for j := 0; j < len(word); j++ {
			if strings.Compare(string(guess[j]), string(word[j])) == 0 {
				builder += ("\033[32m" + string(guess[j]) + "\033[0m")
			} else if strings.Contains(word, string(guess[j])) { 
				builder += ("\033[33m" + string(guess[j]) + "\033[0m")
			} else {
				builder += string(guess[j])
			}
		}
		fmt.Println(builder)
		if strings.Compare(guess, word) == 0 {
			fmt.Printf("YOU WIN 🥳!\n")
			os.Exit(0)
		}
		builder = ""
	}
	fmt.Printf("GOOD EFFORT 👍!\n")
	os.Exit(0)
}
