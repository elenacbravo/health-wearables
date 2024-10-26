# Health Wearables Ecosystem

## Overview
The Health Wearables ecosystem is a centralized platform designed to monitor and manage health-related IoT wearables. 
The system enables real-time communication between wearables and a monitoring system, allowing devices to react based on certain health conditions. 
(For example, if a heart rate monitor detects an abnormal rate, the system can trigger a blood pressure monitor to take an additional reading).

### Key features of the project: 
- **Event Bus**: Provides a publish-subscribe mechanism for communication between wearables and the central monitoring system.
- **Database**: Stores data for registered wearables.
- **Frontend Interface**: Intuitive UI for device management and health data visualization.
- **Health Monitoring**: Automated abnormal health metric detection, triggering events and notifying the appropriate devices.
- **Logging and Testing**: Comprehensive logging for debugging, with automated tests to verify functionality.
- **Containerization and Orchestration**: Deployable via Docker and Kubernetes (via the Helm charts).

---

## System architecture

### Components
1. **Backend**: Built with Flask, it provides the REST API for managing wearables and health events.
2. **Event Bus**: A custom in-memory publish-subscribe service that allows seamless communication between devices.
3. **Database**: SQLite, managed by SQLAlchemy, for storing wearable data and historical records.
4. **Frontend**: HTML, CSS, and JavaScript-based UI for device registration, management, and health data display.
5. **Kubernetes Deployment**: Helm charts enable easy deployment and scaling in a Kubernetes environment.

### Technologies used
- **Backend**: Python, Flask, Flask-SQLAlchemy
- **Event Bus**: Custom Python implementation (could be expanded to MQTT)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite for local development
- **Containerization**: Docker
- **Orchestration**: Kubernetes, Helm

---

## Prerequisites

Please ensure the following are installed before setup:

- **Docker**: [Get Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Get Docker Compose](https://docs.docker.com/compose/install/)
- **Helm**: [Get Helm](https://helm.sh/docs/intro/install/)
- **Python 3.10**: [Download Python](https://www.python.org/downloads/) (for local testing)



## Setup Instructions

### 1. Clone the repository

git clone https://github.com/elenacbravo/health-wearables.git

cd health-wearables  



## Setup and usage guide
### 2. Build and run locally with Docker Compose
Use Docker Compose to build and run the containers for both the backend and frontend.


docker-compose up --build

### 3. Access the application

After running the above command, you can access:

- **Frontend**: [http://localhost:8080](http://localhost:8080)
- **Backend API**: [http://localhost:5001](http://localhost:5001)
### Registering a wearable

1. Go to the frontend at [http://localhost:8080](http://localhost:8080).
2. Fill out the device type and status form to register a new wearable.
3. The system will monitor health metrics and trigger notifications based on the events received.

## Usage

### Event bus

The event bus is a central component that facilitates device-to-device communication. Devices can publish events (such as an abnormal heart rate) which can be consumed by other devices in real-time.

### Health monitoring

The backend periodically checks for abnormal health metrics and publishes events. Devices subscribed to these events can take specific actions, such as sending notifications or taking additional measurements.

### Frontend interface

The frontend provides basic device management, where you can:

- Register new wearables.
- View device status.
- Monitor live updates on heart rate and other health metrics.

## Running tests

To run backend tests, including those for the Event Bus, database operations, and health monitoring:

- Navigate to the backend directory.
- Install the required Python packages and run the tests with pytest.


cd backend
pip install -r requirements.txt
pytest tests/

## Deployment on Kubernetes

To deploy the application on Kubernetes using Helm, package and install the chart as follows:

### Package the Helm chart

helm package helm/health-monitoring

### Install the Helm chart

helm install health-monitoring ./health-monitoring

### Accessing the application on kubernetes

Depending on your setup, use port-forwarding or a LoadBalancer to access the frontend and backend services.

### Logs

All backend logs are stored in the `backend/logs` directory. You can check these for debugging or audit purposes.

## Examples of further improvements

- **Real-Time data visualization**: Integrate charts for live monitoring of health metrics on the frontend.
- **Expanded notification system**: Add email or SMS notifications for critical events.