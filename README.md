# local-network-port-scanner
A Python-based network security tool designed to identify reachable hosts and open TCP ports within an authorized lab environment.  The scanner runs from PC1 on VLAN 30 (Security VLAN) and performs TCP scans against explicitly authorized hosts and ports.

scanner1.py
The first version of the project implemented a basic TCP port scanner using Python's socket library. The scanner accepted an authorized IP address as input and tested a predefined list of commonly used TCP ports. It identified which ports were open and displayed the results in the terminal. 

scanner2.py
The second version improved the scanner by allowing the user to specify a starting and ending port. Instead of being limited to a fixed list of common ports, the scanner could test any TCP port range within the authorized lab environment
