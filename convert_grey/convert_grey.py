from PIL import Image


def convert_to_greyscale(image):
    # Cria uma cópia da imagem
    greyscale_image = image.copy()

    # Converte a imagem para tons de cinza
    greyscale_image = greyscale_image.convert("L")

    return greyscale_image


# Carrega a imagem desejada
image = Image.open("images/elephant.jpg")

# Converte a imagem para tons de cinza
greyscale_image = convert_to_greyscale(image)

# Salva a imagem resultante
greyscale_image.save("images/elephant_grey.jpg")
