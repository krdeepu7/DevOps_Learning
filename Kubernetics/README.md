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

### Components

*   **`flask-frontend`**: A web interface built with Flask that displays a list of students and includes a form to add new ones. It communicates with the backend via its Kubernetes service name (`http://express-service:3000`).
*   **`express-backend`**: A simple REST API built with Express.js. It provides endpoints to get (`/students`) and add (`/students`) student data. The data is stored in-memory for simplicity.
*   **`k8s`**: This directory contains the Kubernetes manifest files (`.yaml`) required to deploy the application, including Deployments and Services for both the frontend and backend.

## Prerequisites

*   Docker
*   A Kubernetes cluster (e.g., Minikube, Docker Desktop, kind)
*   `kubectl` CLI tool

## How to Run

Follow these steps to build the container images and deploy the application to your Kubernetes cluster.

### 1. Clone the Repository

```bash
git clone https://github.com/krdeepu7/devops_learning.git
cd devops_learning/Kubernetics
```

### 2. Build Docker Images

The Kubernetes Deployments are configured with `imagePullPolicy: Never`, which requires the Docker images to be available locally within the cluster's environment.

**Note for Minikube users:** Run the following command first to switch to Minikube's Docker daemon. This ensures the images are built where the cluster can find them.
```bash
eval $(minikube -p minikube docker-env)
```

Now, build the images for the frontend and backend:
```bash
# Build the backend image
docker build -t express-backend:v1 ./express-backend

# Build the frontend image
docker build -t flask-frontend:v1 ./flask-frontend
```

### 3. Apply Kubernetes Manifests

Deploy all the necessary Kubernetes resources using the manifest files in the `k8s` directory.

```bash
kubectl apply -f k8s/
```

This will create the following resources:
*   `express-deployment` and `express-service`
*   `flask-deployment` and `flask-service`

### 4. Verify the Deployment

Check that the pods for both applications are running correctly.

```bash
kubectl get pods
```

You should see output similar to this, with the pods in a `Running` state:
```
NAME                                  READY   STATUS    RESTARTS   AGE
express-deployment-5c688d689b-abcde   1/1     Running   0          60s
flask-deployment-7d99c4b7f-fghij     1/1     Running   0          60s
```

### 5. Access the Application

The Flask frontend is exposed via a `NodePort` service.

**For Minikube users (easiest method):**
Run the following command to automatically open the service URL in your browser.
```bash
minikube service flask-service
```

**For other Kubernetes clusters:**
You can manually construct the URL by finding your node's IP address and the service's assigned `NodePort`.

```bash
# 1. Get the NodePort for the flask-service
NODE_PORT=$(kubectl get svc flask-service -o=jsonpath='{.spec.ports[0].nodePort}')

# 2. Get the IP address of a cluster node (for Minikube, use 'minikube ip')
NODE_IP=$(kubectl get nodes -o=jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}')

# 3. Access the application at http://<NODE_IP>:<NODE_PORT>
echo "Access your application at: http://$NODE_IP:$NODE_PORT"
