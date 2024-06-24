package main

import "fmt"

func returnsTen() int {
	return 10
}
func main() {
	coolVariable := returnsTen()
	fmt.Println(coolVariable + 10)

}