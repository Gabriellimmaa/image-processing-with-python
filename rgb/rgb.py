from PIL import Image


def separate_channels(image_path):
    image = Image.open(image_path)

    # Separar os canais RGB
    r, g, b = image.split()

    # Salvar cada canal separadamente
    r.save("images/elephant_r.jpg")
    g.save("images/elephant_g.jpg")
    b.save("images/elephant_b.jpg")


# Chamada da função com o caminho da imagem
separate_channels("images/elephant.jpg")
