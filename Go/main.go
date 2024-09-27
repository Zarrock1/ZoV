package main
	import (
		"fmt"
		"bufio"
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
        
        a.Scan()
		name4 := a.Text()
		
		fmt.Print(name2) 
		fmt.Print(name1) 
		fmt.Print(name3) 
		fmt.Print(name1)
		fmt.Print(name4) 

	}
	
	