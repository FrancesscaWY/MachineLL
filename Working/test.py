# This is a sample Python script.
import matplotlib
import matplotlib.pyplot as plt
import numpy
import pandas
import tables
import jupyter_core


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}') # Press Ctrl+8 to toggle the breakpoint.
    print('matplotlib: '+matplotlib.__version__)
    print('numpy: '+numpy.__version__)
    print('pandas: '+pandas.__version__)
    print('tables: '+tables.__version__)
    print('jupyter: '+jupyter_core.__version__)

    # use matplotlib
    # 创建画布
    plt.figure(figsize=(20,8),dpi=100)
    # 绘制图像
    x = [1,2,3]
    y = [4,5,6]
    plt.plot(x,y)

    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
