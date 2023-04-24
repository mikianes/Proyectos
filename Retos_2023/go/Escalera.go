package main

import "fmt"

func escalera(step int) {
	var stepby = step
	var spaces = stepby * 2

	if stepby > 0 {
		for i := 0; i < step+1; i++ {
			if i == 0 {
				var escalon = " _"
				fmt.Printf("%*s\n", spaces+1, escalon)
			} else {
				var escalon = "_|"
				fmt.Printf("%*s\n", spaces, escalon)
				spaces -= 2

			}

		}
	} else if stepby < 0 {
		var step = step * -1
		var spaces = 2
		for x := 0; x < step+1; x++ {
			if x == 0 {
				var escalon = "_"
				fmt.Printf("%*s\n", spaces, escalon)
				spaces += 2
			} else {
				var escalon = "|_"
				fmt.Printf("%*s\n", spaces, escalon)
				spaces += 2

			}

		}
	} else {
		fmt.Printf("__")
	}

}

func main() {
	escalera(4)
	escalera(-4)
	escalera(0)
}
