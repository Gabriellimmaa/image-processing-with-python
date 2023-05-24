# Rotação de Imagem

Este código em Python demonstra como rotacionar uma imagem utilizando a biblioteca PIL (Python Imaging Library).

## Pré-requisitos

Certifique-se de ter os seguintes requisitos atendidos antes de executar o código:

* Python 3.x instalado
* Biblioteca PIL instalada (`pip install pillow`)

## Como executar o código

1. Faça o download do código-fonte para o seu computador.
2. Certifique-se de ter uma imagem no formato suportado (por exemplo, JPEG) no diretório "images" com o nome "elephant.jpg".
3. No código-fonte, localize a linha onde é feita a chamada da função `rotate_image()` e ajuste o caminho do arquivo para corresponder ao nome e localização da sua imagem.
4. Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o código.
5. Execute o código com o comando `python nome_do_arquivo.py`, substituindo "nome_do_arquivo.py" pelo nome do arquivo do código.
6. Aguarde até que o processamento seja concluído. O resultado será salvo como uma nova imagem com o nome "elephant_rotate.jpg" no mesmo diretório.

## Explicação do código

O código começa importando a classe `Image` da biblioteca PIL.

Em seguida, é definida a função `rotate_image()` que recebe o caminho da imagem e o ângulo de rotação como parâmetros.

Dentro da função, a imagem é aberta usando o caminho especificado com `Image.open(image_path)` e armazenada na variável `image`.

A imagem é então girada utilizando o método `rotate()` com o ângulo de rotação desejado. O parâmetro `expand=True` garante que a imagem seja ajustada para conter a rotação completa.

Uma nova imagem é criada utilizando o método `Image.new()` com o modo "RGBA" e o tamanho necessário para conter a imagem girada. O valor (255, 255, 255, 0) representa a cor transparente.

A posição para colar a imagem girada no centro da nova imagem é calculada com base nas diferenças de tamanho entre as duas imagens.

A imagem girada é colada na nova imagem utilizando o método `paste()`, passando a imagem girada e a posição calculada como argumentos.

Por fim, a imagem girada é salva utilizando o método `save()` com o nome "elephant_rotate.jpg".

No corpo principal do código, a função `rotate_image()` é chamada, passando o caminho da imagem original e o ângulo de rotação como argumentos.

Certifique-se de ajustar o caminho correto da imagem em `rotate_image("images/elephant.jpg", 90)` para corresponder ao local onde a imagem original está localizada.

Lembre-se também de ter permissão de escrita no diretório onde deseja salvar a imagem girada.

Espero que isso ajude a entender o que está acontecendo neste código. Sinta-se à vontade para ajustar e personalizar conforme necessário.
