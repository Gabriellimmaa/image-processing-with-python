# Filtro de Mediana em Imagem

Este código em Python demonstra como aplicar um filtro de mediana em uma imagem utilizando a biblioteca PIL (Python Imaging Library) e a biblioteca estatística padrão.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos atendidos antes de executar o código:

* Python 3.x instalado
* Biblioteca PIL instalada (`pip install pillow`)

## Como executar o código

1. Faça o download do código-fonte para o seu computador.
2. Certifique-se de ter uma imagem no formato suportado (por exemplo, JPEG) no diretório "images" com o nome "elephant.jpg".
3. No código-fonte, localize a linha onde é chamada a função `apply_median_filter()` e verifique se o caminho do arquivo de imagem está correto.
4. Ajuste o parâmetro `window_size` de acordo com o tamanho da janela do filtro de mediana desejado.
5. Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o código.
6. Execute o código com o comando `python nome_do_arquivo.py`, substituindo "nome_do_arquivo.py" pelo nome do arquivo do código.
7. Aguarde até que o processamento seja concluído. O resultado será uma nova imagem salva como "elephant_median.jpg" no diretório "images".

## Explicação do código

O código começa importando a classe `Image` da biblioteca PIL e o módulo `statistics` para calcular a mediana dos valores dos pixels.

Em seguida, é definida a função `apply_median_filter()` que recebe a imagem original, uma imagem para armazenar o resultado filtrado e o tamanho da janela do filtro de mediana como parâmetros.

Dentro da função, o tamanho da imagem é obtido usando o método `size`, e em seguida, dois loops `for` são utilizados para percorrer cada pixel da imagem.

Para cada pixel no centro da imagem (desconsiderando a borda), uma janela de tamanho especificado é criada, e os valores dos pixels dessa janela são coletados em uma lista chamada `window_pixels`. Esses valores são então ordenados usando o método `sort()`.

A mediana dos valores é calculada usando a função `statistics.median()` aplicada à lista `window_pixels`. O pixel mediano é obtido e atribuído ao pixel correspondente na imagem filtrada usando o método `putpixel()`.

No corpo principal do código, a imagem original é aberta usando a função `Image.open()` e armazenada na variável `image`. Uma nova imagem, do mesmo tamanho e modo que a imagem original, é criada usando o método `Image.new()` e armazenada na variável `filtered_image`.

O tamanho da janela do filtro de mediana é definido na variável `window_size`.

A função `apply_median_filter()` é chamada, passando a imagem original, a imagem filtrada e o tamanho da janela como argumentos.

Por fim, a imagem filtrada é salva usando o método `save()` com o nome "elephant_median.jpg" no diretório "images".

Certifique-se de ter permissão de escrita no diretório onde deseja salvar a imagem filtrada.

Espero que isso ajude a entender o que está acontecendo neste código. Sinta-se à vontade para ajustar e personalizar conforme necessário.
