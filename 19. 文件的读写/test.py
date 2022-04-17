"""
文件的读写自动化测试用的比较多
我们通常读取txt, yaml, mysql, ini, excel文件
"""

# with open("./mytest.txt") as f:
#     #  readlines返回一个列表, 列表各项是一个字符串
#     for line in f.readlines():
#         #  不写的话默认删除前后的空格, 下面就是删除换行符
#         line = line.strip("\n")
#         print(line)
#         print(line.split(","))

# f = open("mytest.txt")
# print(f.readlines())
# f.close()

# import xlrd
#
#
# class ReadXlsx:
#     data_path = "test.xlsx"
#     excel = xlrd.open_workbook(data_path)
#     #  找到指定的表单
#     sheet = excel.sheet_by_index(0)
#     #  row和col的值必须要知道
#     row, col = sheet.nrows, sheet.ncols
#     print(row, col)
#
#     def read_from_xlsx(self):
#         rowValue = self.sheet.row_values(0)
#         print(rowValue)
#
#
# e = ReadXlsx()
# e.read_from_xlsx()


import yaml


path = "test.yml"
file = open(path, encoding="UTF-8")
result = file.read()
print(result)

file_dict = yaml.load(result, Loader=yaml.FullLoader)
print(file_dict)

