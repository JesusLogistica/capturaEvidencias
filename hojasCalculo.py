import gspread

#Usa las credenciales de la api de google sheet
gc = gspread.service_account(filename='logistica5-tableros-cbcc5f8d90e6.json')

# Abrir por titulo
sh = gc.open("prueba")

# Seleccionar primera hoja
worksheet = sh.get_worksheet(0)

# Introducir datos
worksheet.update('A1', 'dominio')
worksheet.update('A2', 'scraping.link')
worksheet.update('B1', 'fecha')
worksheet.update('B2', '22/04/2021')
worksheet.update('C1', 'num URLs indexadas')
worksheet.update('C2', '10')