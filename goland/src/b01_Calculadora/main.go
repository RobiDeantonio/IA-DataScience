package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {

	entrada := leerEntrada()
	operador := leerEntrada()

	c := calc{}
	fmt.Println(c.operate(entrada, operador))

}

type calc struct{}

func parsear(entrada string) int {
	operador, _ := strconv.Atoi(entrada)
	return operador
}

func leerEntrada() string {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	return scanner.Text()
}

func (calc) operate(entrada string, operator string) int {

	entradalimpia := strings.Split(entrada, operator)
	operador1 := parsear(entradalimpia[0])
	operador2 := parsear(entradalimpia[1])

	switch operator {
	case "+":
		return operador1 + operador2
	case "-":
		return operador1 - operador2
	case "*":
		return operador1 * operador2
	case "/":
		return operador1 / operador2
	default:
		fmt.Println(operator, "no es un operador valido")
		return 0
	}
}
