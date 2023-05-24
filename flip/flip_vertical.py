from PIL import Image


def flip_image(image):
    # Cria uma cópia da imagem
    flipped_image = image.copy()

    # Obtém a largura e altura da imagem
    width, height = flipped_image.size

    # Inverte a imagem na vertical
    for y in range(height // 2):
        for x in range(width):
            upper_pixel = flipped_image.getpixel((x, y))
            lower_pixel = flipped_image.getpixel((x, height - 1 - y))
            flipped_image.putpixel((x, y), lower_pixel)
            flipped_image.putpixel((x, height - 1 - y), upper_pixel)

    return flipped_image


# Carrega a imagem desejada
image = Image.open("images/elephant.jpg")

# Inverte a imagem na vertical
flipped_image = flip_image(image)

# Salva a imagem resultante
flipped_image.save("images/elephant_flip_topbottom.jpg")
