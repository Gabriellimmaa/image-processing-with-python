from PIL import Image


def convert_to_black_white(image_path, threshold):
    # Abrir a imagem em tons de cinza
    img = Image.open(image_path).convert("L")

    # Obter os pixels da imagem
    pixels = img.load()

    # Percorrer cada pixel da imagem e converter para preto ou branco
    for i in range(img.width):
        for j in range(img.height):
            # Verificar se o valor do pixel é menor que o limite
            if pixels[i, j] < threshold:
                pixels[i, j] = 0  # Preto
            else:
                pixels[i, j] = 255  # Branco

    # Salvar a imagem em preto e branco
    img.save("images/elephant_wb.jpg")


# Utilizar a função para converter a imagem
convert_to_black_white("images/elephant_grey.jpg", 80)
