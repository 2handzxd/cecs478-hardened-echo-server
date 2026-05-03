# Hardened Echo Server

CECS 478 Final Project  
Student: Steven Dinh  
Repository: https://github.com/2handzxd/cecs478-hardened-echo-server.git  
Final Release: v1.0.0

## Project Overview

The Hardened Echo Server is a secure version of a basic echo server. A normal echo server receives a client message and sends it back, but this can be risky if the server accepts bad input, receives repeated spam requests, or sends traffic in plaintext.

This project adds basic security and reproducibility features:

- TLS-enabled communication
- Input validation
- Rate limiting design
- Docker-based deployment
- Metrics export
- Final demo artifacts
- Reproducible Makefile workflow

The main goal is to show that the system can be run from a fresh clone and that evidence artifacts are produced for the final report.

## Threat Model

The project assumes an attacker can connect to the server on the lab network. The attacker may try to:

- Send malformed messages
- Send repeated requests
- Capture traffic on the network
- Abuse a simple unprotected echo service

The system is designed to reduce these risks by using TLS, validation, rate limiting, and metrics support.

## System Design

The basic system flow is:

```text
Client message
    ↓
TLS-enabled connection
    ↓
Input validation
    ↓
Rate limiting
    ↓
Echo response or rejection
    ↓
Metrics and artifacts export
