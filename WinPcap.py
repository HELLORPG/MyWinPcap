from winpcapy import WinPcapDevices
import UI


class WinPcap:
    devices = ""
    current_device = ""

    def __init__(self):
        self.devices = WinPcapDevices.list_devices()
        return

    def show_devices(self):
        UI.SystemOut("网卡列表: ")
        devices_keys = self.devices.keys()
        devices_names = []
        for key in devices_keys:
            devices_names.append(self.devices[key])

        i = 1
        for name in devices_names:
            print("%d. " % i, end="")
            print(name)
            i += 1
        return