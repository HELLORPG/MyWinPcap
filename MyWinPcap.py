from winpcapy import WinPcapDevices
from winpcapy import WinPcapUtils
import UI


class MyWinPcap:
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

    def choose_device(self):
        print("请输入网卡名称或编号: ", end="")
        name = input()
        if name.isdecimal():
            if 0 < int(name) <= len(self.devices):
                # print(type(self.devices.keys()))
                key = list(self.devices.keys())[int(name) - 1]
                print("是否选择: %s" % (self.devices[key] + "  :  " + key))
                print("yes/no: ", end="")
                yes_or_no = input()
                if yes_or_no == "yes":
                    self.current_device = key
                else:
                    return
            else:
                print("没有该编号的网卡.")

        else:
            devices_keys = self.devices.keys()
            devices_names = []
            for key in devices_keys:
                devices_names.append(self.devices[key])

            if name in devices_names:
                index = devices_names.index(name)
                key = list(devices_keys)[index]
                print("是否选择: %s" % (self.devices[key] + "  :  " + key))
                print("yes/no: ", end="")
                yes_or_no = input()
                if yes_or_no == "yes":
                    self.current_device = key
                else:
                    return
            else:
                print("没有该名称的网卡.")

    def show_current_device(self):
        if self.current_device == "":
            print("当前未选择网卡.")
        else:
            print("当前网卡为: %s" % (self.devices[self.current_device] + "  :  " + self.current_device))
        return

    def print(self):
        # WinPcapUtils.capture_on_device_name(self.current_device, print_data)
        WinPcapUtils.capture_on_device_name(self.current_device, analysis_data)
        return

    def test(self):
        WinPcapUtils.capture_on_and_print("Intel(R) Ethernet Connection (7) I219-V")
        return


def print_data(win_pcap, param, header, pkt_data):
    ip_frame = pkt_data[14:]
    # Parse ips
    # print(ip_frame)
    src_ip = ".".join([str(b) for b in ip_frame[0xc:0x10]])
    dst_ip = ".".join([str(b) for b in ip_frame[0x10:0x14]])
    print("%s -> %s" % (src_ip, dst_ip))

def analysis_data(win_pcap, param, header, pkt_data):
    """
    提供了一种输出方式，这种输出方式伴随着对报文的数据段进行分析，因此区别于print_data，改名为analysis_data
    :param win_pcap:
    :param param:
    :param header:
    :param pkt_data:
    :return:
    """
    UI.DataSegmentation()

    # 整理原始的报文数据
    data_seg = " ".join(["{:02x}".format(x) for x in pkt_data])
    print("原始报文数据: ")
    print(data_seg)

    # 进行Ethernet协议解析
    analysis_ethernet(pkt_data)


def analysis_ethernet(data:str):
    dst_mac = ":".join(["{:02x}".format(x) for x in data[0:6]])
    src_mac = ":".join(["{:02x}".format(x) for x in data[6:12]])
    UI.PartSegmentation()
    print("Ethernet >>>")
    print("Src Mac: %s" % src_mac)
    print("Dst Mac: %s" % dst_mac)
    print("上层协议类型: ", end="")
    type = data[12] * 0x100 + data[13]
    if type == 0x0800:
        print("IPv4")
        analysis_ipv4(data[14:])
    elif type == 0x0806:
        print("ARP")
    elif type == 0x8864:
        print("PPPoE")
    elif type == 0x86DD:
        print("IPv6")
    return


def analysis_ipv4(data:str):
    UI.PartSegmentation()
    print("IP >>>")
    version = (data[0] & 0xF0) / 0x10
    header_total_length = (data[0] & 0x0F) * 4
    tos = data[1]
    total_length = (data[2] * 0x100 + data[3]) * 4
    protocol = data[9]
    ttl = data[8]
    src_ip = ".".join([str(x) for x in data[12:16]])
    dst_ip = ".".join([str(x) for x in data[16:20]])

    # 用于输出分析的内容
    print("Version: %d" % version)
    print("Header Total Length: %d B" % header_total_length)
    print("Type of Service: %#x" % tos)
    print("Total Length: %d B" % total_length)
    print("TTL: %d" % ttl)
    if protocol == 6:
        print("上层协议: TCP (%#x)" % protocol)
    elif protocol == 17:
        print("上层协议: UDP (%#x)" % protocol)
    elif protocol == 1:
        print("上层协议: ICMP (%#x)" % protocol)
    elif protocol == 2:
        print("上层协议: IGMP (%#x)" % protocol)
    print("Src IP: %s" % src_ip)
    print("Dst IP: %s" % dst_ip)
    return


if __name__ == '__main__':
    test_pcap = MyWinPcap()
    print("begin")
    test_pcap.test()