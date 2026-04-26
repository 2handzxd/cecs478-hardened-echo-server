# 🔐 Hardened Echo Server

## 📌 Overview
This project implements a **secure and observable echo server** for CECS 478.

It demonstrates a full end-to-end pipeline:

echo → validate → rate limit → log → export metrics

The system runs entirely inside Docker and includes:
- Security hardening (input validation + rate limiting)
- Observability (logs + metrics)
- Packet capture (PCAP evidence)
- Automated testing with coverage
- CI pipeline

---

## ⚙️ Quick Start (Required)

From a fresh clone:

```bash
make up && make demo
