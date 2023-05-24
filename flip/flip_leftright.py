from PIL import Image


def flip_image(image):
    # Cria uma cópia da imagem
    flipped_image = image.copy()

    # Obtém a largura e altura da imagem
    width, height = flipped_image.size

    # Inverte a imagem na vertical
    for y in range(height):
        for x in range(width // 2):
            left_pixel = flipped_image.getpixel((x, y))
            right_pixel = flipped_image.getpixel((width - 1 - x, y))
            flipped_image.putpixel((x, y), right_pixel)
            flipped_image.putpixel((width - 1 - x, y), left_pixel)

    return flipped_image


# Carrega a imagem desejada
image = Image.open("images/elephant.jpg")

# Inverte a imagem na vertical
flipped_image = flip_image(image)

# Salva a imagem resultante
flipped_image.save("images/elephant_flip_leftright.jpg")
