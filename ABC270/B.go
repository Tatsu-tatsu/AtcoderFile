package main

import "fmt"

func B() {
	var X, Y, Z int
	ans := 0
	fmt.Scan(&X, &Y, &Z)
	if 0 < X {
		if Y < 0 {
			ans += X
		} else if 0 < Y {
			if Y < Z {
				ans -= 1
			} else if 0 < Z {
				ans += X
			} else {
				ans += -Z*2 + X
			}
		}
	} else if X < 0 {
		if 0 < Y {
			ans += -X
		} else if Y < 0 {
			if Z < Y {
				ans -= 1
			} else if Z < 0 {
				ans += -X
			} else {
				ans += 2*Z + -X
			}
		}
	}
	fmt.Println(ans)
}
