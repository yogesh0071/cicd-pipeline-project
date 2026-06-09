# 🚀 End-to-End CI/CD Pipeline with Jenkins, Docker & Kubernetes

An automated CI/CD pipeline that builds, containerizes, and deploys a Python Flask application to AWS EC2 using Jenkins — triggered automatically on every GitHub push via webhook.

---

## 📌 Project Overview

This project demonstrates a real-world DevOps workflow where every code push to GitHub automatically triggers a Jenkins pipeline that builds a Docker image, pushes it to DockerHub, and deploys the updated container to an AWS EC2 instance — with zero manual steps.

---

## 🏗️ Architecture

```
Developer → GitHub Push
               ↓
         GitHub Webhook
               ↓
       Jenkins Pipeline
      ┌────────────────┐
      │ 1. Clone Repo  │
      │ 2. Docker Build│
      │ 3. Push Image  │
      │ 4. Deploy EC2  │
      └────────────────┘
               ↓
      Running App on EC2
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Jenkins | CI/CD automation server |
| Docker | Containerization |
| DockerHub | Container image registry |
| Python Flask | Sample web application |
| AWS EC2 | Cloud deployment target |
| GitHub | Source code + webhook trigger |
| Bash | Deployment scripts |

---

## 📋 Prerequisites

- AWS Account (Free Tier works)
- EC2 instance (Ubuntu, t2.micro)
- Jenkins installed on EC2
- Docker installed on EC2
- DockerHub account
- Git installed locally

---

## 🚀 Setup & Run

### Step 1 — Clone this repository
```bash
git clone https://github.com/yogeshnimje071/cicd-pipeline-project.git
cd cicd-pipeline-project
```

### Step 2 — Run the app locally with Docker
```bash
docker build -t yogesh-app .
docker run -p 5000:5000 yogesh-app
```
Open browser → `http://localhost:5000`

### Step 3 — Jenkins Setup on EC2
```bash
# SSH into your EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Install Java and Jenkins
sudo apt update
sudo apt install -y openjdk-11-jdk
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update && sudo apt install -y jenkins docker.io
sudo systemctl start jenkins
```

### Step 4 — Configure Jenkins Pipeline
- Open Jenkins at `http://your-ec2-ip:8080`
- Create a new Pipeline job
- Point it to this GitHub repository
- Jenkins will use the `Jenkinsfile` automatically

### Step 5 — Set Up GitHub Webhook
- Go to your GitHub repo → Settings → Webhooks
- Add webhook: `http://your-ec2-ip:8080/github-webhook/`
- Every push now auto-triggers the pipeline

---

## 📁 Project Structure

```
cicd-pipeline-project/
├── app.py              # Python Flask web application
├── Dockerfile          # Docker container configuration
├── Jenkinsfile         # Jenkins pipeline definition
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🔧 Jenkinsfile Explained

```groovy
pipeline {
  agent any
  stages {
    stage('Clone') {
      steps { git 'https://github.com/yogeshnimje071/cicd-pipeline-project' }
    }
    stage('Build Docker Image') {
      steps { sh 'docker build -t yogesh-app .' }
    }
    stage('Push to DockerHub') {
      steps { sh 'docker push yogeshnimje071/yogesh-app:latest' }
    }
    stage('Deploy to EC2') {
      steps { sh 'docker run -d -p 5000:5000 yogesh-app' }
    }
  }
}
```

---

## 💡 Key Concepts Covered

- Webhook-triggered automated deployments
- Docker image build and registry push
- Jenkins pipeline stages and scripting
- AWS EC2 instance configuration and access
- Zero-touch deployment on code push

---

## 👤 Author

**Yogesh Nimje** — DevOps & Cloud Engineer
- 🔗 [LinkedIn](https://linkedin.com/in/yogeshnimje071)
- 💻 [GitHub](https://github.com/yogeshnimje071)
- 📧 nimje.yogesh1999@gmail.com
