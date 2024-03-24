from openpyxl import workbook, load_workbook


class Uzdrowisko:

    def __init__(self):
        self.name = ''
        self.link = ''
        self.file = load_workbook('baza.xlsx')
        self.sheet = self.file.active

    def read_from_xlsx(self,index):
        self.name = self.sheet['B' + str(index + 1)].value
        self.link = self.sheet['C' + str(index + 1)].value

    def search_in_xlsx(self,key):
        tmp = [[],[]]
        x = 2
        while(self.sheet['B' + str(x)].value):
            if(key == self.sheet['B' + str(x)].value[0:len(key)]):
                tmp[0].append(self.sheet['B' + str(x)].value)
                tmp[1].append(self.sheet['C' + str(x)].value)
            x+=1
        return tmp

    