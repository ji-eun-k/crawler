from openpyxl import Workbook

wb = Workbook()
sheet_1 = wb.active
sheet_2 = wb.create_sheet('매출현황')
sheet_1.title = '총매출현황'

sheet_1 = wb['총매출현황']
sheet_1['A1'] = '첫번째 cell'
sheet_1['A2'] = '두번째 cell'

wb.save("C:\\Users\\s_jeun097\\Desktop\\crawler\\1.xls")