# Hardened Echo Server

## Project Summary
This project demonstrates how a simple echo server can be insecure when using plaintext communication and how it can be improved using basic security protections.

The project compares an insecure echo server with a hardened version that includes:
- TLS encryption
- input validation
- logging
- rate limiting

## Goals
- Show how plaintext traffic can be captured
- Harden the service against interception and abuse
- Provide a reproducible Docker-based setup and evaluation process

## Repository Structure
- `src/` - source code for client and server
- `scripts/` - helper scripts for capture and demo runs
- `pcaps/` - packet captures for evaluation
- `docs/` - proposal and final report files

## Setup
Build the project with:

```bash
make bootstrap
