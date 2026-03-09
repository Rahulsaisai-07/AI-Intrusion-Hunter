#  AI Intrusion Hunter

An **anime-style cybersecurity project** built with Python that monitors network traffic in real time and detects suspicious activity.

This project demonstrates **packet sniffing, intrusion monitoring, and basic network analysis** using the Scapy library.

---

##  Features

* Real-time packet monitoring
* Displays source IP addresses
* Detects suspicious repeated connections
* Simple intrusion detection logic
* Lightweight Python script

---

##  Technologies Used

* Python
* Scapy
* Network Packet Analysis

---

##  Project Structure

```
AI-Intrusion-Hunter
│
├── intrusion_hunter.py
├── requirements.txt
└── README.md
```

---

##  Installation

Clone the repository:

```
git clone https://github.com/yourusername/AI-Intrusion-Hunter.git
cd AI-Intrusion-Hunter
```

Install dependencies:

```
pip install scapy
```

---

## ▶ Run the Program

```
python intrusion_hunter.py
```

The script will start capturing packets and display the **source IP addresses** of incoming traffic.

Example output:

```
Packet from: 192.168.1.4
Packet from: 192.168.1.7
Packet from: 192.168.1.4
```

---

##  How It Works

1. The program captures live network packets.
2. It checks whether the packet contains an **IP layer**.
3. If found, it prints the **source IP address**.
4. Repeated IP activity can indicate potential suspicious behavior.

---

##  Educational Purpose

This project is created for **educational and cybersecurity learning purposes only**.
It helps students understand **network traffic analysis and intrusion detection concepts**.

---

##  Author

**Bairi Rahul Sai**

Cybersecurity Enthusiast
Ethical Hacking | Network Security | Python Automation
