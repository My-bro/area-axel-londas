package main

import (
	"encoding/json"
	"io"
	"net/http"
	"time"
    "fmt"
)

type TriggerRequest struct {
    Hour  string            `json:"hour"`
    State map[string]string `json:"state"`
}

type WorldTimeApi struct {
    DateTime string `json:"datetime"`
}

func getWorldTime() (time.Time, error) {
    url:="http://worldtimeapi.org/api/timezone/Europe/Paris"

    resp, err := http.Get(url)
    if err != nil {
        return time.Time{}, err
    }
    defer resp.Body.Close()

    body, err := io.ReadAll(resp.Body)
    if err != nil {
        return time.Time{}, err
    }

    var worldTime WorldTimeApi
    if err := json.Unmarshal(body, &worldTime); err != nil {
        return time.Time{}, err
    }

    parsedTime, err := time.Parse(time.RFC3339, worldTime.DateTime)
    if err != nil {
        return time.Time{}, err
    }

    return parsedTime, nil
}

func checkTrigger(w http.ResponseWriter, r *http.Request) {
    var req TriggerRequest
    err := json.NewDecoder(r.Body).Decode(&req)
    if err != nil {
        http.Error(w, "Invalid request body", http.StatusBadRequest)
        return
    }

    currentTime, err := getWorldTime()
    if err != nil {
        http.Error(w, "Failed to get current time", http.StatusInternalServerError)
        return
    }

    inputTime, err := time.Parse("15:04", req.Hour)
    if err != nil {
        http.Error(w, "Invalid hour format", http.StatusBadRequest)
        return
    }
    inputTime = time.Date(currentTime.Year(), currentTime.Month(), currentTime.Day(), inputTime.Hour(), inputTime.Minute(), 0, 0, currentTime.Location())

    if currentTime.Before(inputTime) {
        req.State = make(map[string]string)
        json.NewEncoder(w).Encode(map[string]interface{}{
            "triggered": false,
            "state":     req.State,
        })
        return
    }
    if inputTime.Before(currentTime) {
        if len(req.State) == 0 {
            req.State = map[string]string{
                "triggered_at": currentTime.Format("02-01 15:04"),
            }
            json.NewEncoder(w).Encode(map[string]interface{}{
                "triggered": true,
                "state":     req.State,
            })
            return
        }
        if triggeredAt, ok := req.State["triggered_at"]; ok {
            if triggeredAt >= inputTime.Format("02-01 15:04") {
                json.NewEncoder(w).Encode(map[string]interface{}{
                    "triggered": false,
                    "state":     req.State,
                })
                return
            }
            if triggeredAt != currentTime.Format("02-01 15:04") {
                req.State = map[string]string{
                    "triggered_at": currentTime.Format("02-01 15:04"),
                }
                json.NewEncoder(w).Encode(map[string]interface{}{
                    "triggered": true,
                    "state":     req.State,
                })
                return
            }
        }
    }
    json.NewEncoder(w).Encode(map[string]interface{}{
        "triggered": false,
        "state":     req.State,
    })
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, `{"status": "ok"}`)
}

func main() {
    http.HandleFunc("/time/check_trigger", checkTrigger)
    http.HandleFunc("/time/health", healthHandler)
    http.ListenAndServe(":8000", nil)
}