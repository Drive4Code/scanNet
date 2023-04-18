import subprocess, sys

class scanNet():
    def __init__(self):
        # Initializes the scan, storing it in instance variable self.scan
        self.address = "84.3.251.0/24"
        self.scan = subprocess.check_output(f'sudo nmap -sP {self.address}', shell=True)
        # print(self.scan)
    
    def parseOutput(self):
        # Takes the output of nmap, splitting it into a List storing information of each device
        scan = str(self.scan).split("\\n")
        # print(scan)
        addressId = self.address[:int(len(self.address)/2)] # int(len(self.address)/2)
        print(addressId)
        addrList = []
        tmpList = []
        for device in scan: 
            print(device)
            if device.__contains__(addressId):
                tmpList.append('Ip Address')
                tmpList.append(device[(device.rindex(" ") + 1):(len(device))])
            if device.__contains__("MAC"):
                tmpList.append('Make')
                try:
                    tmpList.append(device[(device.index("(") + 1):(device.rindex(")"))])
                except:
                    continue
                tmpList = []

            if tmpList:
                addrList.append(tmpList)
        
        return addrList


        
    def removeDuplicates(self, addressList):
        # Removes all duplicate Ip Addresses in the list
        count = 0
        for item in addressList:
            for element in addressList:
                if element == item:
                    addressList.remove(item)

        for item in addressList:
            if item[1].startswith("("):
                item[1] = item[1][1:(len(item[1])-1)]
        
        return addressList
               
        
    def parseDetailedScan(self, scan):
        # Parses the individual scan done signularly for every device, 
        print(scan.split("\\n"))

    def detailedScan(self, ipAddr, arg, port):
        # Runs a detailed scan on all devices. This scan may take up to 10 seconds per device, as such it is not reccommended on big networks
        for device in ipAddr:
            address = device[1]
            print(address)
            scan = str(subprocess.check_output(f'sudo nmap -p 1-256 -O {address}', shell=True))
            device.append(self.parseDetailedScan(scan))

            


if __name__ == "__main__":
    argList = str(sys.argv)
    if argList.__contains__("-M"):
        print(argList)
        port = argList[2]
        print(port)
        # argument = 
    ipList = scanNet().removeDuplicates(scanNet().parseOutput())
    scanNet().detailedScan(ipList, arg, port)


