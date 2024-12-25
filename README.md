# Network Traffic Analyzer Web Application

This is a **Django-based web application** for analyzing network traffic using PCAP files. The application is capable of detecting port scanning activities, analyzing protocol distribution, and visualizing communication between IPs.

---

## Features

- **Upload PCAP Files:** Analyze uploaded PCAP files to detect port scans, identify top communicators, and calculate protocol distribution.
- **Live Traffic Capture:** Capture live network traffic using selected network interfaces.
- **Visualizations:** View graphical representations of network protocol usage, communication matrices, and more.

---

## Setup Instructions

### Prerequisites

Ensure the following are installed:
- Docker and Docker Compose
- Python (if running locally without Docker)

---

### Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/aegusten/Network-Traffic-Analyzer-Web-Application.git
   cd Network-Traffic-Analyzer-Web-Application

2. **SETUP**
    ```bash
    - Build Docker 
    docker-compose build

    - Up Docker
    docker-compose up 

    - Down Docker
    docker-compose down

    - Check Docker
     docker ps

    - Enter the terminal
    docker exec -it django_app bash

    - Migrate Database
    python manage.py makemigrations

    - Apply Migration
    python manage.py migrate
