package main

import (
	"fmt"
	"net/http"
	"time"

	"github.com/dgrijalva/jwt-go"
)

var jwtKey = []byte("my_secret_key")

type Claims struct {
	Username string `json:"username"`
	jwt.StandardClaims
}

func login(w http.ResponseWriter, r *http.Request) {
	// Get the username and password from the request body
	username := r.FormValue("username")
	password := r.FormValue("password")

	// Validate the username and password
	if username != "admin" || password != "password" {
		http.Error(w, "Invalid credentials", http.StatusUnauthorized)
		return
	}

	// Create the JWT
	expiresAt := time.Now().Add(time.Minute * 20).Unix()
	claims := &Claims{
		Username: username,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: expiresAt,
		},
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	tokenString, err := token.SignedString(jwtKey)
	if err != nil {
		http.Error(w, "Failed to create JWT", http.StatusInternalServerError)
		return
	}

	// Send the JWT to the client
	http.SetCookie(w, &http.Cookie{
		Name:    "token",
		Value:   tokenString,
		Expires: time.Unix(expiresAt, 0),
	})
	fmt.Fprint(w, "Login successful!")
}

func welcome(w http.ResponseWriter, r *http.Request) {
	// Get the JWT from the request
	cookie, err := r.Cookie("token")
	if err != nil {
		http.Error(w, "Unauthorized", http.StatusUnauthorized)
		return
	}
	tokenString := cookie.Value

	// Parse the JWT
	token, err := jwt.ParseWithClaims(tokenString, &Claims{}, func(token *jwt.Token) (interface{}, error) {
		return jwtKey, nil
	})
	if err != nil {
		http.Error(w, "Failed to parse JWT", http.StatusBadRequest)
		return
	}

	// Validate the JWT
	if claims, ok := token.Claims.(*Claims); ok && token.Valid {
		fmt.Fprintf(w, "Welcome %s!", claims.Username)
	} else {
		http.Error(w, "Invalid JWT", http.StatusUnauthorized)
	}
}

func main() {
	http.HandleFunc("/login", login)
	http.HandleFunc("/welcome", welcome)
	http.ListenAndServe(":8080", nil)
}