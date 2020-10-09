CLI_WIDTH = 100
ALL_COMMAND = ["device", "device choose", "current device", "print"]


def CLISegmentation():
    """
    CLI界面中分割两段显示
    :return:
    """
    for i in range(0, CLI_WIDTH):
        print("=", end="")
    print("", end="\n")
    return


def DataSegmentation():
    for i in range(0, CLI_WIDTH):
        print("-", end="")
    print("", end="\n")
    return


def PartSegmentation():
    for i in range(0, CLI_WIDTH):
        print(".", end="")
    print("", end="\n")
    return


def SystemOut(x:str):
    print("\n>>>>> ", end="")
    print(x)
    return


def MainMenu():
    SystemOut("MainMenu:")
    print("1. device: 显示网卡")
    print("2. device choose: 选择一个网卡进行监听")
    print("3. current device: 当前选择的网卡")
    print("4. print: 打印监听内容")
    return