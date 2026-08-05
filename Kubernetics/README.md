# Kubernetes Application

This repository contains a simple two-tier web application to demonstrate containerization with Docker and orchestration with Kubernetes. It consists of a Python-based Flask frontend and a Node.js-based Express backend.

## Architecture

The application follows a classic client-server architecture where the frontend communicates with a backend API.

```
Browser
    │
    ▼
Flask Frontend (Service on Port 5000)
    │
    ▼
HTTP API Calls (to express-service)
    │
    ▼
Express Backend (Service on Port 3000)
```

