import os
import UI
import re
from MyWinPcap import MyWinPcap
from winpcapy import WinPcapUtils


if __name__ == '__main__':
    # Device.ShowAllDevice()
    input_cmd = ""
    my_winpcap = MyWinPcap()
    while True:
        UI.MainMenu()

        print("Please Input a Command: ", end="")

        input_cmd = input()     # 输入当前的指令
        input_cmd = input_cmd.lower()   # 切换成为小写Q
        # UI.CLISegmentation()
        # print("Current Command:", "\033[1;34m%s\033[0m" % input_cmd)

        if input_cmd == "q" or input_cmd == "quit":
            UI.SystemOut("System Exit.")
            break
        elif input_cmd == "device" or input_cmd == "1" or input_cmd == "1.":
            print("Current Command:", "\033[1;34mdevice\033[0m")
            my_winpcap.show_devices()
        elif input_cmd == "device choose" or input_cmd == "2" or input_cmd == "2.":
            print("Current Command:", "\033[1;34mdevice choose\033[0m")
            my_winpcap.choose_device()
        elif input_cmd == "current device" or input_cmd == "3" or input_cmd == "3.":
            print("Current Command:", "\033[1;34mcurrent device\033[0m")
            my_winpcap.show_current_device()
        elif input_cmd == "print" or input_cmd == "4" or input_cmd == "4.":
            print("Current Command:", "\033[1;34mprint\033[0m")
            my_winpcap.print()
        else:
            UI.SystemOut("\033[1;31mCommand Not Exist!\033[0m")
            cmd_guess = ""
            for i in range(0, len(input_cmd)):
                cmd_guess += ".*"
                cmd_guess += input_cmd[i]
            cmd_guess += ".*"
            for cmd in UI.ALL_COMMAND:
                if re.match(cmd_guess, cmd, flags=re.I):
                    print("是否希望输入: %s" % cmd)
                    break


        UI.CLISegmentation()
