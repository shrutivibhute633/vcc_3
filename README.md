# 🚀 Auto-Scaling Flask App

This project demonstrates how to deploy a Flask application on a local virtual machine (VM) and automatically scale it to Google Cloud Platform (GCP) when CPU usage exceeds a defined threshold (75%).

---

## 📌 Overview

The system continuously monitors CPU utilization on a local machine. When the CPU usage goes beyond **75%**, an automated script triggers scaling by deploying or shifting workload to GCP.

This setup is useful for:

* Learning auto-scaling concepts
* Simulating real-world cloud scaling behavior
* Understanding resource monitoring and automation

---

## 📂 Project Structure

* **app.py**
  A Flask application that simulates high CPU usage for testing auto-scaling behavior.

* **monitor_resource.sh**
  A shell script that monitors CPU usage and triggers auto-scaling to GCP when the threshold is exceeded.

---

## ⚙️ Usage

### 1️⃣ Run the Flask Application

Start the Flask app locally:

```bash
python3 app.py
```

---

### 2️⃣ Start Resource Monitoring & Auto-Scaling

Give execution permission and run the monitoring script:

```bash
chmod +x monitor_resource.sh
./monitor_resource.sh
```

---

## 🧠 How It Works

1. The Flask app generates CPU load.
2. The monitoring script continuously checks CPU usage.
3. If CPU usage exceeds **75%**, the script triggers auto-scaling to GCP.
4. The system ensures better performance by offloading workload.

---

## 📈 Key Features

* Automatic CPU monitoring
* Threshold-based scaling (75%)
* Local-to-cloud workload transition
* Simple and easy-to-understand implementation

---

## 🛠️ Requirements

* Python 3
* Flask
* Bash (Linux/Mac terminal)
* Google Cloud Platform (GCP) setup

---

