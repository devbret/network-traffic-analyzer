# Network Traffic Analyzer

A traffic analyzer built with Python which uses Scapy to capture network packets and matplotlib to visualize the distribution of protocols.

## Features

- **Packet Capture:** Uses Scapy to sniff network packets on the active network interface.
- **Protocol Analysis:** Counts and categorizes packets by protocol type.
- **Data Visualization:** Generates a pie chart to visually represent the captured protocol distribution.

## Prerequisites

- **Python 3.6+**
- **Administrative Privileges:** Running the script usually requires elevated privileges to capture packets.
- **Tkinter:** Required for matplotlib's interactive backend. On Debian/Ubuntu-based systems, install Tkinter using:
  ```
  sudo apt-get install python3-tk
  ```

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/devbret/network-traffic-analyzer.git
   cd network-traffic-analyzer
   ```

2. Create a virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application using the virtual environment’s Python interpreter. Since capturing packets typically requires administrative privileges, start the script with sudo:

```
sudo ./venv/bin/python3 app.py
```

The script will capture fifty packets by default. Once captured, the program displays packet counts per protocol and either opens an interactive window or saves a visualization.

## Troubleshooting

Below you will find two common errors and how to resolve each.

1. **ModuleNotFoundError: No module named 'scapy':**

   Ensure you are using the virtual environment's Python interpreter.

2. **Tkinter Not Found:**

   Install Tkinter using your system's package manager:

   ```
   sudo apt-get install python3-tk
   ```

## Requirements

The project depends on the following Python libraries:

- Scapy
- matplotlib

All required dependencies are listed in the requirements.txt file.
