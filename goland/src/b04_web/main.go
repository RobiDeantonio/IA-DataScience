package main

import (
	"fmt"
	"io"
	"net/http"
)

type writerWeb struct{}

func (writerWeb) Write(p []byte) (int, error) {
	fmt.Println(string(p))
	return len(p), nil
}

func main() {
	answer, err := http.Get(("http://google.com"))
	if err != nil {
		fmt.Println(err)
	}

	e := writerWeb{}
	io.Copy(e, answer.Body)

}
