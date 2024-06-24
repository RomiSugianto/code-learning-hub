package heist

import (
	"fmt"
	"math/rand"
	"time"
)

package main

import (
"fmt"
"math/rand"
"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	isHeistOn := true
	eludedGuards := rand.Intn(100)
	openedVault := rand.Intn(100)
	leftSafely := rand.Intn(5)

	if eludedGuards >=50 {
		fmt.Println("Looks like you've managed to make it past the guards. Good job, but remember, this is the first step.")
	} else {
		isHeistOn = false
		fmt.Println("Plan a better disguise next time?")
	}

	if isHeistOn == true && openedVault >= 70 {
		fmt.Println("Grab and GO!")
	} else if isHeistOn {
		isHeistOn = false
		fmt.Println("vault cant be opened")
	}

	fmt.Println(isHeistOn)

	if isHeistOn {
		switch leftSafely {
		case 0:
			isHeistOn = false
			fmt.Println("Heist failed, cant get out safely")
		case 1:
			isHeistOn = false
			fmt.Print("Turns out vault doors don't open from the inside...")
		case 2:
			isHeistOn = false
			fmt.Println("Heist failed, our drivers get caught")
		case 3:
			isHeistOn = false
			fmt.Println("Heist failed, the plan has been compromised")
		case 4:
			isHeistOn = false
			fmt.Println("Heist failed, all team has been killed")
		default :
			fmt.Println("Start the getaway car!")
		}
	}
	if isHeistOn {
		amtStolen := rand.Intn(1000000)
		fmt.Println("Stolen amount is %d", amtStolen)
	}
}

