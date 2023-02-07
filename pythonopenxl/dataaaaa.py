from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass()
class People():
    name:str
    num:int
    age:int
P=[People('sindhu',1,23),People('sri',2,25),People('lalli',2,27)]
data=[[p.name,p.num,p.age]for p in P]
for d in data:
    sheet.append(d)
wb.save("../data//dtclassdemo.xlsx")
