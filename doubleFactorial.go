func doubleFactorial(n int) int {
	if n <= 0 {
		return 1
	}
	return n * doubleFactorial(n-2)
}
