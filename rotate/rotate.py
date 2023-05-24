from PIL import Image


def rotate_image(image_path, angle):
    # Abrir a imagem
    image = Image.open(image_path)

    # Girar a imagem com o ângulo desejado
    rotated_image = image.rotate(angle, expand=True)

    # Criar uma nova imagem com o tamanho necessário para conter a imagem girada
    new_image = Image.new('RGBA', rotated_image.size, (255, 255, 255, 0))

    # Colar a imagem girada no centro da nova imagem
    position = (
        (new_image.size[0] - rotated_image.size[0]) // 2,
        (new_image.size[1] - rotated_image.size[1]) // 2
    )
    new_image.paste(rotated_image, position)

    # Salvar a imagem girada
    rotated_image.save("images/elephant_rotate.jpg")


# Chamada da função com o caminho da imagem e o ângulo de rotação
rotate_image("images/elephant.jpg", 90)
