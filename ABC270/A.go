package main

import "fmt"

func A() {
	var A, B int
	ans := 0
	fmt.Scanf("%d %d", &A, &B)
	if A == 1 || A == 3 || A == 5 || A == 7 {
		ans += 1
	} else if A == 2 || A == 3 || A == 6 || A == 7 {
		ans += 2
	} else if A == 4 || A == 5 || A == 6 || A == 7 {
		ans += 4
	}
	if B == 1 || B == 3 || B == 5 || B == 7 {
		ans += 1
	} else if B == 2 || B == 3 || B == 6 || B == 7 {
		ans += 2
	} else if B == 4 || B == 5 || B == 6 || B == 7 {
		ans += 4
	}
	fmt.Println(ans)
}

// 上記間違え。ifでやるのは大変。
// 模範解答
// ビット演算を使うと一瞬で出来る。
// package main

// import "fmt"

// func main() {
// 	var A, B int
// 	fmt.Scan(&A, &B)
// 	fmt.Println(A | B)
// }
