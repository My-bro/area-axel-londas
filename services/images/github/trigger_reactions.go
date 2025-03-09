package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
)

func triggerReactions(applet_id string, payload interface{}) {
	url := "https://api.skead.fr/applets/trigger_reactions/" + applet_id
	jsonPayload, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error marshalling payload: %s\n", err.Error())
		return
	}
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonPayload))
	if err != nil {
		fmt.Printf("Error creating request: %s\n", err.Error())
		return
	}
	req.Header.Set("Content-Type", "application/json")
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %s\n", err.Error())
		return
	}
	defer resp.Body.Close()
}
