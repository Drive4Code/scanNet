import nmap3, json, sys, os
import pprint

# Ideas
# Make the program check if there's a scan.json, and if there is run a different scan, highlight the differences, and output them to a diff.json (which doesn't have to be scanned each time)

class scanNet():
    # Scans the network, filters through every IP address, and attempts to identify OS model
    def __init__(self):
        self.nm = nmap3.Nmap()
        self.nmHD = nmap3.NmapHostDiscovery()
        self.ipAddr = '84.3.251.0/24' # 84.3.251.0/24
        self.outDir = os.path.join('output','output.json')
        self.scan = self.nmHD.nmap_no_portscan(self.ipAddr)

    def getHostsUp(self):
        # Removes from the list all hosts that aren't up
        # print(self.scan)
        parsedScan = {}
        for host in self.scan:
            try:
                values = self.scan[host]
                state = values['state']
                if state['state'] != 'down':
                    parsedScan[host] = self.scan[host]
                # print("EOF")
            except:
                None 
        # print(parsedScan)
        return parsedScan

    def osDetection(self, scan, ports):
        # Detects the os for all hosts that are up
        # print(scan)
        newScan = {}
        for host in scan:
            if ports == 'fast':
                newScan[host] = self.nm.nmap_os_detection(host, args=f'-F --max-os-tries 1 --osscan-limit --osscan-guess')
            elif ports != 'Null':
                newScan[host] = self.nm.nmap_os_detection(host, args=f'-p {ports}')
            else:
                newScan[host] = self.nm.nmap_os_detection(host, args='')
        # Clean the newScan
        for host in newScan:
            newScan[host] = newScan[host][host]
        return newScan

    def dumpToJson(self, scan):
        # Dumps the scan to a Json file
        with open(self.outDir, 'w') as outFile:
            json.dump(scan, outFile, indent=2)

    def cleanScan(self):
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
                print(f'Os not Found on {host}')
        return osScan


if __name__ == '__main__':
    sc = scanNet()
    pp = pprint.PrettyPrinter()
    port = 'Null'
    argList = sys.argv
    if argList.__contains__("-p") and (argList.__contains__("-F") or argList.__contains__("-f") or argList.__contains__("--fast")):
        # Addresses a rare instance where the User Specifies both ports and fast mode at the same time
        print("The Fast argument and the Port specification can't go together. FAST mode will be activated")
        port = 'fast'
        scan = sc.cleanScan()
        sc.dumpToJson(scan)
    elif argList.__contains__("-p"):
        # Specifies the ports to be scan. Can be specified with a range (1-1000) or single port. Checkout the nmap docs for more info
        port = argList[argList.index("-p") + 1]
        print(f'Ports to Be Scanned: {port}')
        scan = sc.cleanScan()
        sc.dumpToJson(scan)
    elif argList.__contains__('-f') or argList.__contains__('-F') or argList.__contains__('--fast'):
        print('FAST mode Active')
        port = 'fast'
        scan = sc.cleanScan()
        sc.dumpToJson(scan)
    if argList.__contains__('-i'):
        # Reads a JSON as an input. Requires a path to the JSON. It then compares and highlights the difference between the current status and the provided JSON
        filePath = argList[argList.index("-i") + 1]
        
    