package main

import "testing"

func TestViernes(t *testing.T) {
	valor := isFriday13(1, 2023)
	if valor != true {
		t.Error("No hay viernes 13")
	}
}
