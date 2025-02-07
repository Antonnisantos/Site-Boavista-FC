import qrcode
from PIL import Image
import os

# Configurações
output_folder = "qr_codes"  # Pasta para salvar os QR codes
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# URLs das imagens (substitua pelos links reais das suas imagens)
image_urls = [
    "https://drive.google.com/file/d/1qdH57_QMJ2ttX4qIUhzs3k2D2a1PbjOw/view?usp=drive_link",
    "https://drive.google.com/file/d/1_F0hL3Tz3TKhz8IGN-3pGnkoied0mL-1/view?usp=drive_link",
    "https://drive.google.com/file/d/1LjL8ySLR2ZjcSC321HxinN7n6hwM0Hxf/view?usp=drive_link"
]

# Caminho da imagem central (símbolo do QR code)
center_image_path = "C:/estagio/imagemfundo/Logos.png"

# Redimensiona a imagem central (tamanho maior)
center_image = Image.open(center_image_path)
center_size = (150, 150)  # Tamanho da imagem central
center_image = center_image.resize(center_size)

# Função para gerar QR codes
def generate_qr_code(data, output_path, center_image):
    qr = qrcode.QRCode(
        version=7,  # Versão mais alta para mais módulos
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Correção de erro alta
        box_size=15,  # Aumentei o tamanho dos módulos
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Cria o QR code
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Adiciona o símbolo central
    pos = ((qr_img.size[0] - center_image.size[0]) // 2, (qr_img.size[1] - center_image.size[1]) // 2)
    qr_img.paste(center_image, pos)

    # Salva o QR code
    qr_img.save(output_path)

# Gera 500 QR codes
for i in range(1, 501):
    # Alterna entre as 3 imagens
    image_url = image_urls[(i - 1) % len(image_urls)]
    
    # Nome do arquivo
    file_name = f"artigo{i:03d}.png"
    output_path = os.path.join(output_folder, file_name)

    # Gera o QR code
    generate_qr_code(image_url, output_path, center_image)
    print(f"Gerado: {output_path}")

print("Todos os QR codes foram gerados!")

