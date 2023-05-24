# Conversão de Imagem para Preto e Branco

Este código em Python demonstra como converter uma imagem em tons de cinza para uma imagem em preto e branco usando a biblioteca PIL (Python Imaging Library).

## Pré-requisitos

Certifique-se de ter os seguintes requisitos atendidos antes de executar o código:

* Python 3.x instalado
* Biblioteca PIL instalada (`pip install pillow`)

## Como executar o código

1. Faça o download do código-fonte para o seu computador.
2. Certifique-se de ter uma imagem em tons de cinza no formato JPEG no diretório "images" com o nome "elephant_grey.jpg".
3. No código-fonte, localize a linha onde é chamada a função `convert_to_black_white()` e verifique se o caminho do arquivo de imagem está correto.
4. Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o código.
5. Execute o código com o comando `python nome_do_arquivo.py`, substituindo "nome_do_arquivo.py" pelo nome do arquivo do código.
6. Aguarde até que o processamento seja concluído. O resultado será uma nova imagem salva como "elephant_wb.jpg" no diretório "images".

## Explicação do código

O código começa importando a classe `Image` da biblioteca PIL. Em seguida, é definida a função `convert_to_black_white()` que recebe o caminho da imagem e um limite de intensidade dos pixels como parâmetros.

Dentro da função, a imagem é aberta usando o caminho fornecido e convertida para tons de cinza usando o método `convert("L")`.

Os pixels da imagem são obtidos usando o método `load()` e armazenados na variável `pixels`.

Em seguida, são utilizados dois loops `for` para percorrer cada pixel da imagem. Para cada pixel, é verificado se o valor é menor que o limite especificado. Se for, o pixel é definido como 0 (preto); caso contrário, o pixel é definido como 255 (branco).

Após a conversão, a imagem em preto e branco é salva no caminho "images/elephant_wb.jpg" usando o método `save()`.

No final do código, a função `convert_to_black_white()` é chamada, passando o caminho da imagem "images/elephant_grey.jpg" e o limite 80 como argumentos.

Certifique-se de ter permissão de escrita no diretório onde deseja salvar a imagem em preto e branco.

Espero que isso ajude a entender o que está acontecendo neste código. Sinta-se à vontade para ajustar e personalizar conforme necessário.
