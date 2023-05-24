from PIL import Image


def adjust_brightness(image, factor):
    # Cria uma cópia da imagem
    adjusted_image = image.copy()

    # Obtém os pixels da imagem
    pixels = adjusted_image.load()

    # Obtém tamanho da imagem
    largura, altura = adjusted_image.size

    # Percorre cada pixel da imagem e ajusta o brilho
    for i in range(largura):
        for j in range(altura):
            # Obtém a cor do pixel (R, G, B)
            r, g, b = pixels[i, j]

            # Ajusta o valor de cada componente de cor r, g, b com o brilho
            r = int(r * factor)
            g = int(g * factor)
            b = int(b * factor)

            # Verifica se os valores estão dentro do intervalo [0, 255]
            r = max(0, min(r, 255))
            g = max(0, min(g, 255))
            b = max(0, min(b, 255))

            # Define a nova cor do pixel
            pixels[i, j] = (r, g, b)

    return adjusted_image


# Carrega a imagem desejada
imagem = Image.open("images/elephant.jpg")

# Fator de brilho
fator = 3.5

# Ajusta o brilho da imagem
imagem_ajustada = adjust_brightness(imagem, fator)

# Salva a imagem resultante
imagem_ajustada.save("images/elephant_brightness.jpg")
