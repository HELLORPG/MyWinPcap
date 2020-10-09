import os
import UI
from WinPcap import WinPcap
from winpcapy import WinPcapUtils


if __name__ == '__main__':
    # Device.ShowAllDevice()
    input_cmd = ""
    my_winpcap = WinPcap()
    while True:
        UI.MainMenu()

        print("Please Input a Command: ", end="")

        input_cmd = input()     # 输入当前的指令
        input_cmd = input_cmd.lower()   # 切换成为小写Q
        # UI.CLISegmentation()
        print("Current Command:", "\033[1;34m%s\033[0m" % input_cmd)

        if input_cmd == "q" or input_cmd == "quit":
            UI.SystemOut("System Exit.")
            break
        elif input_cmd == "device":
            my_winpcap.show_devices()
        else:
            UI.SystemOut("\033[1;31mCommand Not Exist!\033[0m")

        UI.CLISegmentation()
