# SmartFactory Monitor  
### Personal Project – Industrial Machine Monitoring & Anomaly Detection MVP

SmartFactory Monitor is a modular industrial machine monitoring system built as a personal learning project.  

It simulates multi-machine sensor data, performs statistical anomaly detection, detects trends, provides root-cause hints, logs data persistently, and visualizes both live and historical performance.

This project focuses on understanding how real industrial monitoring platforms are structured — not on building a production system.

---

## 🚀 Project Goal

To design a simplified but structured monitoring system that demonstrates:

- Real-time telemetry simulation
- Explainable anomaly detection
- Modular architecture
- Historical analytics
- Manager-level risk overview

The purpose of this project is learning system design + applied ML fundamentals as a fresher.

---

## 🏗 Architecture Overview

The project is modular and divided into logical layers:

```
machine_monitor/
│
├── app.py                # Main Streamlit dashboard
│
├── sensors/
│   └── temperature.py    # Sensor simulation logic
│
├── brain/
│   ├── trend.py          # Trend detection
│   ├── root_cause.py     # Root cause reasoning
│   └── analyzer.py       # Anomaly scoring logic
│
├── utils/
│   └── logger.py         # CSV logging system
│
└── data/
    └── logs.csv          # Historical log storage
```

This separation makes the system scalable and easier to extend.

---

## 🔴 Core Features Implemented

### 1️⃣ Live Machine Monitoring

- Multi-machine support
- Area grouping
- Real-time temperature simulation
- Status classification (NORMAL / WARNING / DANGER)
- Clean dashboard interface using Streamlit

---

### 2️⃣ Simulation Control (Demo Mode)

Allows switching between:

- Normal Operation
- Rising Temperature
- Overload Scenario

This helps demonstrate how anomaly behavior changes under different operating conditions.

---

### 3️⃣ Trend Detection

Detects whether temperature is:

- Stable
- Increasing
- Rapidly increasing

Based on recent historical values.

---

### 4️⃣ Root Cause Hint System (Rule-Based)

Provides possible causes such as:

- Overload condition
- Cooling system issue
- Continuous rising trend
- High sustained temperature

This is explainable logic (not black-box ML).

---

### 5️⃣ Statistical Anomaly Scoring

Implements a simplified anomaly score:

Anomaly Score = |Current - Average| / Average

This normalizes deviation relative to machine behavior.

Outputs:

- NORMAL (low deviation)
- WARNING (moderate deviation)
- DANGER (high deviation)

This is the foundation of Z-score based anomaly detection.

---

### 6️⃣ Persistent Logging System

- Logs timestamp
- Machine ID
- Area
- Temperature
- Status

Stored in CSV for historical analysis.

---

### 7️⃣ Analytics Page (Historical View)

- Load historical logs
- Filter by machine
- Display temperature trends
- Show last 20 records

Separates:

Live Monitoring vs Historical Analysis

---

### 8️⃣ Factory Summary (Manager View)

Displays:

- Number of machines in WARNING
- Number of machines in DANGER

Provides executive-level overview.

---

## 📊 Concepts Demonstrated

- Modular software design
- Separation of concerns
- Real-time simulation logic
- Statistical anomaly detection (baseline deviation)
- Explainable AI reasoning
- Logging & persistence
- Dashboard data visualization

---

## 🧠 Learning Focus

This project was built to understand:

- How industrial monitoring systems are structured
- How anomaly detection works conceptually
- How statistical reasoning improves rule-based systems
- How to separate monitoring, analytics, and intelligence layers

It is not intended as a production-ready platform.

---

## 🔮 Future Improvements (Planned)

- Proper Z-score implementation using standard deviation
- Multi-sensor support (vibration, load)
- Database integration (PostgreSQL)
- Isolation Forest using scikit-learn
- Deployment with Docker
- REST API version of analytics engine

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- CSV Logging
- Modular architecture design

---

## ▶ How To Run

1. Clone the repository
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run app.py
```

---

## 🎯 Author Note

This is a personal learning project developed to strengthen understanding of system design, applied ML fundamentals, and industrial monitoring concepts as a fresher software engineer.
