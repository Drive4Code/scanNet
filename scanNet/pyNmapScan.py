import nmap3, json, sys
import pprint

# Ideas
# Make the program check if there's a scan.json, and if there is run a different scan, highlight the differences, and output them to a diff.json (which doesn't have to be scanned each time)

class scanNet():
    # Scans the network, filters through every IP address, and attempts to identify OS model
    def __init__(self):
        self.nm = nmap3.Nmap()
        self.nmHD = nmap3.NmapHostDiscovery()
        self.ipAddr = '84.3.251.0/30' # 84.3.251.0/24
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
                newScan[host] = self.nm.nmap_os_detection(host, args=f'-F -sV')
            elif ports != 'null':
                newScan[host] = self.nm.nmap_os_detection(host, args=f'-p {ports}')
            else:
                newScan[host] = self.nm.nmap_os_detection(host, args='---max-os-tries 1 ')
        # Clean the newScan
        for host in newScan:
            newScan[host] = newScan[host][host]
        return newScan

if __name__ == '__main__':
    pp = pprint.PrettyPrinter()
    argList = sys.argv
    if argList.__contains__("-p"):
        # print(argList)
        port = argList[argList.index("-p") + 1]
        print(port)
    else:
        port = 'fast'
    sc = scanNet()
    listScan = sc.getHostsUp()
    pp.pprint(listScan)
    osScan = sc.osDetection(listScan, port)
    pp.pprint(osScan)
    for host in osScan:
        hostVals = osScan[host]
        osMatch = hostVals['osmatch'][0]
        print(f'Ip Address: {host}')
        print(osMatch['name'])