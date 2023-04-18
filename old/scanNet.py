import subprocess

class scanNet():
    def __init__(self):
        # Initializes the scan, storing it in instance variable scan
        self.address = "84.3.251.0/24" # 84.3.251.40
        self.scan = subprocess.check_output(f'sudo nmap -sP {self.address}', shell=True)
        # print(self.scan)
    
    def parseOutput(self):
        # Taks the output of nmap, splitting it into a 2D List storing information of each device
        scan = str(self.scan).split("\\n")
        # print(scan)
        addressId = self.address[:int(len(self.address) / 2)]
        print(addressId)
        addrList = {}
        count = 0
        for device in scan:
            if count % 2 == 0:
                tmpList = []
            print(device)
            if device.__contains__(addressId):
                ipAddr = device[(device.rindex(" ") + 1):]
                addrList[ipAddr] = ""
                lstIndx = ipAddr
            
            if device.__contains__("Host"):
                addrList[lstIndx] = device[(device.index("(") + 1):device.rindex("s")] + 's'
                lstIndx = ""
                # tmpList.append(device[(device.index("(") + 1):device.rindex("s")] + 's')

            # if tmpList:
            #     addrList.append(tmpList)
        print(addrList)
        self.addrList = addrList

    # def detailedScan(self):
    #     # Runs a detailed scan on all devices. This scan may take up to 10 seconds per device, as such it is NOT RECCOMMENDED ON BIG NETWORKS
    #     for device in self.addrList:
    #         # ipAddr = device[]


scanNet().parseOutput()
# scanNet().detailedScan()