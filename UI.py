CLI_WIDTH = 100


def CLISegmentation():
    """
    CLI界面中分割两段显示
    :return:
    """
    for i in range(0, CLI_WIDTH):
        print("=", end="")
    print("", end="\n")
    return


def SystemOut(x:str):
    print("\n>>>>> ", end="")
    print(x)
    return


def MainMenu():
    SystemOut("MainMenu:")
    print("device: 显示网卡")

    return