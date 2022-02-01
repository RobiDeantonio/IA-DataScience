package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

func HandleRoot(w http.ResponseWriter, request *http.Request) {
	fmt.Fprint(w, "hello world")
}

func HandleHome(w http.ResponseWriter, request *http.Request) {
	fmt.Fprint(w, "This is the API Endpoint")
}

func PostRequest(w http.ResponseWriter, request *http.Request) {
	decodificador := json.NewDecoder(request.Body)
	var metadata Metadata
	err := decodificador.Decode(&metadata)
	if err != nil {
		fmt.Fprintf(w, "error %v", err)
		return
	}
	fmt.Fprintf(w, "payload %v\n", metadata)
}

func UserPostRequest(w http.ResponseWriter, request *http.Request) {
	decodificador := json.NewDecoder(request.Body)
	var user User
	err := decodificador.Decode(&user)
	if err != nil {
		fmt.Fprintf(w, "error %v", err)
		return
	}
	response, err := user.ToJson()
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(response)
	//fmt.Fprintf(w, "payload %v\n", user)
}
