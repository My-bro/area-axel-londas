package main

import (
	"os"
	"encoding/json"
	"net/http"
	"github.com/twilio/twilio-go"
	twilioApi "github.com/twilio/twilio-go/rest/api/v2010"
)

type SendSmsReactionInput struct {
	PhoneNumber string `json:"phone_number"`
	Content     string `json:"content"`
}

func sendSmsReaction(w http.ResponseWriter, r *http.Request) {
	var input SendSmsReactionInput
	err := json.NewDecoder(r.Body).Decode(&input)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	accountSid := "AC2d283ee548018c0c65240c57b466b673"
	authToken := os.Getenv("API_KEY")
	client := twilio.NewRestClientWithParams(twilio.ClientParams{
		Username: accountSid,
		Password: authToken,
	})
	params := &twilioApi.CreateMessageParams{}
	params.SetTo(input.PhoneNumber)
	params.SetFrom("+17013532489")
	params.SetBody(input.Content)
	_, err = client.Api.CreateMessage(params)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}
