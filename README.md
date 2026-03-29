# Auto-Scaling Local VM to Google Cloud Platform (GCP)

## Project Overview

This project demonstrates a **hybrid cloud auto-scaling system** where a local virtual machine (VM) is monitored continuously, and when CPU usage exceeds a defined threshold (75%), a new VM is automatically provisioned on **Google Cloud Platform (GCP)**.

The system also deploys a sample application automatically on the cloud VM using a startup script.

---

## 🎯 Objectives

- Create a local VM using VirtualBox  
- Monitor CPU usage using Python  
- Trigger scaling when CPU > 75%  
- Automatically create a VM in GCP  
- Deploy application on the cloud VM  

---

## 🧱 Architecture

```

Local VM (VirtualBox)
│
▼
Monitoring Script (Python + psutil)
│
CPU > 75%
│
▼
Trigger gcloud CLI
│
▼
GCP Compute Engine VM
│
Startup Script Execution
│
▼
Application Running on Cloud

```

---

## 🛠️ Technologies Used

- VirtualBox
- Ubuntu Server 22.04
- Python 3
- psutil
- Google Cloud Platform (GCP)
- gcloud CLI

---

## 📂 Project Structure

```

autoscale-project/
│
├── monitor.py      # Monitoring + scaling logic
├── stress.py       # CPU load generator
├── startup.sh      # Cloud VM startup script
└── app.py          # application

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <repo-link>
````

---

### 2️⃣ Install Dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install psutil
```

---

### 3️⃣ Configure GCP

```bash
gcloud auth login
gcloud config set project <PROJECT_ID>
gcloud config set compute/zone asia-south1-a
```

---

### 4️⃣ Enable Compute Engine API

Go to:

```
GCP Console → APIs & Services → Enable Compute Engine API
```

---

## ▶️ How to Run

### Step 1: Start Monitoring

```bash
python3 monitor.py
```

---

### Step 2: Generate CPU Load

```bash
python3 stress.py
python3 stress.py
```

---

### Step 3: Auto Scaling Trigger

When CPU > 75%:

* New VM is created on GCP
* Application is deployed automatically

---

### Step 4: Access Application

```bash
gcloud compute instances list
```

Open in browser:

```
http://<EXTERNAL_IP>:8000
```

---

## 📸 Output

* CPU monitoring logs
* Auto-scaling trigger message
* GCP VM instance created
* Application accessible via public IP

---

## ✅ Features

* Real-time CPU monitoring
* Automatic cloud scaling
* Automatic app deployment
* Hybrid cloud implementation

---

## 👨‍💻 Author

**Sourabh Tyagi**

M.Tech - Data Engineering
