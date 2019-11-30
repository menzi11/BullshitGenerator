package main

import (
	"encoding/json"
	"io/ioutil"
	"os"
)

type BoshJson struct {
	Title  string   `json:"title,omitempty"`
	Famous []string `json:"famous,omitempty"`
	Bosh   []string `json:"bosh,omitempty"`
	After  []string `json:"after,omitempty"`
	Before []string `json:"before,omitempty"`
}

func ReadJson(filename string) BoshJson {
	var BoshJsons BoshJson
	file, err := os.Open(filename)
	checkErr(err)
	b, err := ioutil.ReadAll(file)
	checkErr(err)

	err = json.Unmarshal(b, &BoshJsons)
	checkErr(err)
	return BoshJsons
}

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}
