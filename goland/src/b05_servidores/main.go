package main

import (
	"fmt"
	"net/http"
	"time"
)

func main() {

	inicio := time.Now()
	servidores := []string{
		"http://platzi.com",
		"http://google.com",
		"http://facebook.com",
		"http://instagram.com",
	}

	canal := make(chan string)

	i := 0

	for {
		if i > 2 {
			break
		}
		for _, servidor := range servidores {
			go revisarServidor(servidor, canal)
		}
		time.Sleep(1 * time.Second)
		fmt.Println(<-canal)
		i++
	}

	//	for i := 0; i < len(servidores); i++ {
	//		fmt.Println(<-canal)
	//	}

	tiempoPaso := time.Since(inicio)
	fmt.Printf("Tiempo de ejecucion %s \n", tiempoPaso)
}

func revisarServidor(servidor string, canal chan string) {
	_, err := http.Get(servidor)
	if err != nil {
		canal <- servidor + " no esta disponible"
	} else {
		canal <- servidor + " funciona correctamente"
	}
}
