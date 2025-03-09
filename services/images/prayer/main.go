package main

import (
	"net/http"
    "fmt"
)


func healthHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, `{"status": "ok"}`)
}

func main() {
    http.HandleFunc("/prayer/health", healthHandler)
    http.HandleFunc("/prayer/prayer_action", prayerAction)
    http.HandleFunc("/prayer/next_prayer_action", nextPrayerAction)
    http.ListenAndServe(":8000", nil)
}