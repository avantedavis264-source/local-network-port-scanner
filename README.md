## Local Network Security Port Scanner

A Python-based network security tool designed to identify reachable hosts and open TCP ports within an authorized lab environment. The scanner runs from **PC1 on VLAN 30 (Security VLAN)** and performs TCP scans against explicitly authorized hosts and ports.

### Project Objectives
* Develop a Python-based security tool using socket programming.
* Improve understanding of network segmentation and VLAN-based environments.

### scanner1.py — Version 1

The first version of the project implemented a basic TCP port scanner using Python's `socket` library. The scanner accepted an authorized IP address as input and tested a predefined list of commonly used TCP ports. It identified which ports were open and displayed the results in the terminal.

[![Scanner1.py](img width="850" height="479" alt="image" src="https://github.com/user-attachments/assets/5b782df4-e9c2-42fa-b070-dc2c6a681ac9" />
)](https://youtu.be/Cix6meoelvE)

### scanner2.py — Version 2

The second version improved the scanner by allowing the user to specify a starting and ending port. Instead of being limited to a fixed list of common ports, the scanner could test any TCP port range within the authorized lab environment.

### Skills Demonstrated
* Python programming
* TCP/IP networking
* TCP port scanning
* Linux/Bash command-line usage
* Git and GitHub
