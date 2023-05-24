# Inversão de Imagem na Vertical e Horizontal

Este é um exemplo de código Python que demonstra como inverter uma imagem na vertical e horizontal usando a biblioteca PIL (Python Imaging Library).

## Pré-requisitos

Certifique-se de ter os seguintes requisitos atendidos antes de executar o código:

* Python 3.x instalado
* Biblioteca PIL instalada (`pip install pillow`)

## Como executar o código

1. Faça o download do código-fonte para o seu computador.
2. Certifique-se de ter uma imagem para inverter e salve-a no mesmo diretório do código.
3. No código-fonte, localize a linha onde é feita a abertura da imagem e ajuste o caminho do arquivo para corresponder ao nome e localização da sua imagem.
4. Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o código.
5. Execute o código com o comando `python nome_do_arquivo.py`, substituindo "nome_do_arquivo.py" pelo nome do arquivo do código.
6. Aguarde até que o processamento seja concluído. O resultado será salvo como uma nova imagem com o nome "elephant_flip_leftright.jpg" (inversão horizontal) ou "elephant_flip_topbottom.jpg" (inversão vertical) no mesmo diretório.

## Explicação do código

### Inversão de Imagem na Vertical

O objetivo desse código é inverter uma imagem na vertical usando a biblioteca PIL.

A função `flip_image()` é definida para realizar a inversão vertical da imagem. Ela recebe a imagem original como parâmetro, cria uma cópia da imagem e percorre metade das linhas da imagem. Em cada iteração, os pixels das linhas superiores são trocados pelos pixels das linhas inferiores usando o método `putpixel()` da biblioteca PIL.

No corpo do código principal, a imagem original é aberta usando a função `Image.open()` e armazenada na variável `image`. Em seguida, a função `flip_image()` é chamada, passando a imagem original como argumento. A imagem invertida é armazenada na variável `flipped_image`.

Por fim, a imagem invertida é salva usando o método `save()` com o nome "elephant_flip_topbottom.jpg".

### Inversão de Imagem na Horizontal

O objetivo desse código é inverter uma imagem na horizontal usando a biblioteca PIL.

A função `flip_image()` é definida para realizar a inversão horizontal da imagem. Ela recebe a imagem original como parâmetro, cria uma cópia da imagem e percorre metade das colunas da imagem. Em cada iteração, os pixels das colunas à esquerda são trocados pelos pixels das colunas à direita usando o método `putpixel()` da biblioteca PIL.

No corpo do código principal, a imagem original é aberta usando a função `Image.open()` e armazenada na variável `image`. Em seguida, a função `flip_image()` é chamada, passando a imagem original como argumento. A imagem invertida é armazenada na variável `flipped_image`.

* [ ] Por fim, a imagem invertida é salva usando o método `save()` com o nome "elephant_flip_leftright.jpg".
