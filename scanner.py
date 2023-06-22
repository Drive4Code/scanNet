import nmap3, json, sys, os, subprocess
import pprint

class scanNet():
    # Scans the network, filters through every IP address, and attempts to identify OS model
    def __init__(self, ip):
        self.nm = nmap3.Nmap()
        self.nmHD = nmap3.NmapHostDiscovery()
        self.ipAddr = ip # 84.3.251.0/24
        self.outDir = os.path.join('output','output.json')
        

    def getHostsUp(self):
        # Removes from the list all hosts that aren't up
        scan = self.nmHD.nmap_no_portscan(self.ipAddr)
        parsedScan = {}
        for host in scan:
            try:
                values = scan[host]
                state = values['state']
                if state['state'] != 'down':
                    parsedScan[host] = scan[host]
            except:
                None 
        return parsedScan

    def osDetection(self, scan, ports):
        # Detects the OS & Ports Up for all hosts that are up
        newScan = {}
        for host in scan:
            if ports == 'fast':
                newScan[host] = self.nm.nmap_os_detection(host, args=f'-F --max-os-tries 1 --osscan-limit --osscan-guess')
            elif ports != None:
                newScan[host] = self.nm.nmap_os_detection(host, args=f'-p {ports} -r')
            else:
                newScan[host] = self.nm.nmap_os_detection(host, args='')
        # Simplyfy the Scan, removing nested Dictionaries
        try:
            for host in newScan:
                newScan[host] = newScan[host][host]
        except KeyError():
            print("WARN scan couldn't be simplified")
        return newScan

    def filterScan(self,scan):
        # Removes the Ip of the machine the scan was executed on
        pass

    def dumpToJson(self, scan):
        # Dumps the scan to a Json file
        with open(self.outDir, 'w') as outFile:
            json.dump(scan, outFile, indent=2)
            outFile.close()

    def cleanScan(self):
        # Executes a Quick Scan to List all Hosts, and an OS Scan, Returning a Dictionary
        listScan = self.getHostsUp()
        print('List Scan: ')
        pp.pprint(listScan)
        osScan = self.osDetection(listScan, port)
        print('Os Scan: ')
        pp.pprint(osScan)
        for host in osScan:
            print(f'Ip Address: {host}')
            hostVals = osScan[host]
            try:
                osMatch = hostVals['osmatch'][0]
                print(osMatch['name'])
            except:
                print(f'Os Not Found on {host}')
        return osScan


if __name__ == '__main__':
    # First and foremost, check if the script is running as root. If not, it calls itself back and runs it as such:
    print('Running as UID %d' % os.geteuid())
    if os.geteuid() != 0:
        try:
            subprocess.check_call(['sudo', sys.executable] + sys.argv)
        except:
            raise Exception("The program must be ran as Root.")
    
    # The program immediately checks for the flags to understand how to run everything
    argList = sys.argv
    try:
        argList.index('-h')
        print('-i  Input the Ip Address(es) You want to scan. Example: 84.3.251.0/24 \n-p  Specifies the ports or port range to scan  \n-f or --fast  Uses some tricks to reduce the osScan Times. Note this disables the ability to specfy ports')
        exit()
    except ValueError:
        None
    
    try:
        ipAddr = argList[argList.index('-i')+1]
    except ValueError:
        raise Exception("Please provide an IP Address with the -i flag")
    sc = scanNet(ipAddr)
    pp = pprint.PrettyPrinter()
    port = None
    
    if argList.__contains__("-p") and (argList.__contains__("-F") or argList.__contains__("-f") or argList.__contains__("--fast")):
        # Addresses a rare instance where the User Specifies both ports and fast mode at the same time
        print("The Fast argument and the Port specification can't go together. FAST mode will be activated")
        port = 'fast'
        scan = sc.cleanScan()
        sc.dumpToJson(scan)
    elif argList.__contains__("-p"):
        # Specifies the ports to be scaned. Can be specified with a range (1-1000) or single port. Checkout the nmap docs for more info
        port = argList[argList.index("-p") + 1]
        print(f'Ports to Be Scanned: {port}')
        scan = sc.cleanScan()
        sc.dumpToJson(scan)
    elif argList.__contains__('-f') or argList.__contains__('-F') or argList.__contains__('--fast'):
        # Scans the top 100 ports, and passes some arguments to speed nmap up
        print('FAST mode Active')
        port = 'fast'
        scan = sc.cleanScan()
        sc.dumpToJson(scan)
    else:
        scan = sc.cleanScan()
        sc.dumpToJson(scan)
        
    