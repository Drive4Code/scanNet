<h1>ScanNet</h1>
The program's objective: Scan and return all items in a network stack. Optimally, this should Return OS type and all possible data that can be gathered with nmap, then a python script should automate the process & Highlight changes compared with the last scan(s)
Ultimately the program will be used in the industrial field, in order to list all of the machines and their possible vulnerabilities
<h2>Instructions</h2>
<ol>
    <li>Install the requirements through <code>pip3 install -r requirements.txt</code></li>
    <li>Run the program though <code>python3 scanner.py -i IP_ADDR_RANGE</code></li>
</ol>
<p>The program will run on the specified ip range. It will generate a JSON called <code>output.json</code> under the output directory.</p>
<p>For more information, you can use the -h flag which will generate the following:</p>
<p>
-i  Input the Ip Address(es) You want to scan. Example: 84.3.251.0/24\
-p  Specifies the ports or port range to scan\
-f or --fast  Uses some tricks to reduce the osScan Times. Note this disables the ability to specfy ports\
-i  Input the Ip Address(es) You want to scan. Example: 84.3.251.0/24\
-p  Specifies the ports or port range to scan\
-f or --fast  Uses some tricks to reduce the osScan Times. Note this disables the ability to specfy ports. <a href="https://nmap.org/book/man-port-specification.html">Documentation</a>
</p>