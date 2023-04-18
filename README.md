<h1>ScanNet</h1>
The program's objective: Scan and return all items in a network stack. Optimally, this should Return OS type and all possoble data that can be gathered with nmap, then a python script should automate the process & Highlight changes compared with the last scan(s)
Ultimately the program will be used in the industrial field, in order to list all of the machines and their possible vulnerabilities
<h2>Nmap</h2>
<code>"sudo nmap -sP 84.3.251.0/24"</code>
<h3>Current Plan:</h3>
<ul>
    <li>Get all hosts from nmap scan</li>
    <li>Iterate trough each one to get the OS, including every single port</li>
    <li>Dump the Scan to output.json</li>