package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	a := bufio.NewScanner(os.Stdin)
	a.Scan()
	name1 := a.Text()

	a.Scan()
	name2 := a.Text()

	a.Scan()
	name3 := a.Text()

	fmt.Println(name1)
	fmt.Println(name2)
	fmt.Println(name3)

}
