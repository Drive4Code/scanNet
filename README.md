<h1>ScanNetr</h1>
The program's objective: Scan and return all items in a network stack. (Optionals: Return OS type) , then write a python script to automate the process & Highlight changes
Ultimately the program will be used on a database of all ips, in order to list all of their possible vulnerabilities
<h2>Nmap</h2>
<code>"sudo nmap -sP 84.3.251.0/24"</code>
<h3>Current Plan:</h3>
<ul>
    <li>Get all hosts from nmap scan</li>
    <li>Iterate trough each one to get the OS, including every single port</li>