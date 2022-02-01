package main

import "fmt"

type animal interface {
	move() string
}
type dog struct{}
type fish struct{}
type bird struct{}

func (dog) move() string {
	return "soy un perro y camino"
}
func (fish) move() string {
	return "soy un pez y nado"
}
func (bird) move() string {
	return "soy un pajaro y vuelo"
}

func moveAnimal(a animal) {
	fmt.Println(a.move())
}

func main() {
	perro := dog{}
	moveAnimal(perro)
	pez := fish{}
	moveAnimal(pez)
	pajaro := bird{}
	moveAnimal(pajaro)
}
