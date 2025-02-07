import os

qr_folder = 'C:/estagio/Qr_codes'  # Pasta onde os QR codes estão armazenados
qr_files = [f for f in os.listdir(qr_folder) if f.endswith('.png')]  # Obtém os arquivos .png

with open('index.html', 'w') as file:
    file.write('<html><body>\n')
    for qr in qr_files:
        file.write(f'<img src="{qr_folder}/{qr}" alt="{qr}" width="150" height="150" />\n')
    file.write('</body></html>\n')
