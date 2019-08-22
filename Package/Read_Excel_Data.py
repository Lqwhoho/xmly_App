# coding=utf-8
import xlrd


def open_excel(file='file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)


def read_excel_data_by_index(file='file.xls', colindex=0, by_index=0):  # 按表的索引读取
    data = open_excel(file) # 打开Excel文件
    tab = data.sheets()[by_index]   # 选择Excel里面的sheet
    nrows = tab.nrows   # 行数
    colname = tab.row_values(colindex)  # 第0行的值
    empty_list = []   # 创建一个空列表
    for x in range(1, nrows):
        row = tab.row_values(x)     # 获取行的数据值
        if row:
            app = dict(zip(colname, row))
            empty_list.append(app)
    return empty_list
