from PIL import Image
import statistics


def apply_median_filter(image, filtered_image, window_size):
    width, height = image.size
    for x in range(width):
        for y in range(height):
            if x > 0 and y > 0 and x < image.width - 1 and y < image.height - 1:
                window_pixels = []
                for i in range(-window_size // 2, window_size // 2 + 1):
                    for j in range(-window_size // 2, window_size // 2 + 1):
                        window_pixels.append(image.getpixel((x + i, y + j)))
                window_pixels.sort()
                median_pixel = statistics.median(window_pixels)
                filtered_image.putpixel((x, y), median_pixel)


# Chamadas de funções e parâmetros
image = Image.open("images/elephant.jpg")
filtered_image = Image.new(image.mode, image.size)
window_size = 3
apply_median_filter(image, filtered_image, window_size)
filtered_image.save("images/elephant_median.jpg")
