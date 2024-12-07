# This is a sample Python script.
import random

import matplotlib
import matplotlib.pyplot as plt
import numpy
import pandas
import tables
import jupyter_core
import matplotlib.font_manager as fm
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

# 打印所有已加载的字体
# for font in fm.fontManager.ttflist:
#     print(font.name)
import matplotlib.font_manager as fm

# 查找系统中所有可用的字体
font_paths = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# 查找包含 Noto Sans CJK 的字体文件
found_fonts = [font for font in font_paths if 'NotoSansCJK' in font]
# 打印找到的字体路径
print(found_fonts)

from matplotlib import rcParams
rcParams['font.sans-serif'] = ['Noto Sans CJK']

# 设置字体为 Noto Sans CJK
# rcParams['font.family'] = 'sans-serif'
# rcParams['font.sans-serif'] = ['Noto Sans CJK Regular', 'DejaVu Sans', 'Bitstream Vera Sans']

# 生成一个简单的图形，查看是否能显示中文
# plt.text(0.5, 0.5, '你好，世界', fontsize=20, ha='center')
# plt.show()


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}') # Press Ctrl+8 to toggle the breakpoint.
    # print('matplotlib: '+matplotlib.__version__)
    # print('numpy: '+numpy.__version__)
    # print('pandas: '+pandas.__version__)
    # print('tables: '+tables.__version__)
    # print('jupyter: '+jupyter_core.__version__)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # use matplotlib
    # 创建画布
    plt.figure(figsize=(20,8),dpi=100)
    # 绘制图像
    x = [1,2,3]
    y = [4,5,6]
    plt.plot(x,y)
    plt.show()
    x = range(60)
    y_shanghai = [random.uniform(15, 18) for i in x]
    plt.figure(figsize=(20, 8), dpi=100)
    plt.plot(x, y_shanghai)
    plt.title("上海")
    plt.show()
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
