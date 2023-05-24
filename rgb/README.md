# Separação dos Canais RGB de uma Imagem

Este código em Python demonstra como separar os canais de cores RGB (vermelho, verde e azul) de uma imagem utilizando a biblioteca PIL (Python Imaging Library).

## Pré-requisitos

Certifique-se de ter os seguintes requisitos atendidos antes de executar o código:

* Python 3.x instalado
* Biblioteca PIL instalada (`pip install pillow`)

## Como executar o código

1. Faça o download do código-fonte para o seu computador.
2. Certifique-se de ter uma imagem no formato suportado (por exemplo, JPEG) no diretório "images" com o nome "elephant.jpg".
3. Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o código.
4. Execute o código com o comando `python nome_do_arquivo.py`, substituindo "nome_do_arquivo.py" pelo nome do arquivo do código.
5. Aguarde até que o processamento seja concluído. Os canais separados serão salvos como "elephant_r.jpg" (canal vermelho), "elephant_g.jpg" (canal verde) e "elephant_b.jpg" (canal azul) no diretório "images".

## Explicação do código

O código começa importando a classe `Image` da biblioteca PIL.

Em seguida, é definida a função `separate_channels()` que recebe o caminho da imagem como parâmetro.

Dentro da função, a imagem é aberta usando o caminho especificado com `Image.open(image_path)` e armazenada na variável `image`.

Os canais de cores RGB são separados usando o método `split()`, que retorna três imagens separadas para cada canal: vermelho (R), verde (G) e azul (B), armazenadas nas variáveis `r`, `g` e `b`, respectivamente.

Cada canal é então salvo individualmente usando o método `save()` com os nomes "elephant_r.jpg", "elephant_g.jpg" e "elephant_b.jpg", correspondendo aos canais vermelho, verde e azul, respectivamente.

No corpo principal do código, a função `separate_channels()` é chamada, passando o caminho da imagem original como argumento.

Certifique-se de ajustar o caminho correto da imagem em `separate_channels("images/elephant.jpg")` para corresponder ao local onde a imagem original está localizada.

Lembre-se também de ter permissão de escrita no diretório onde deseja salvar os canais separados da imagem.

Espero que isso ajude a entender o que está acontecendo neste código. Sinta-se à vontade para ajustar e personalizar conforme necessário.
