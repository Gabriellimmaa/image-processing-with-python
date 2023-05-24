# Ajuste de Contraste em uma Imagem

Este é um exemplo de código Python que demonstra o ajuste de contraste em uma imagem usando a biblioteca PIL (Python Imaging Library).

## Pré-requisitos

Certifique-se de ter os seguintes requisitos atendidos antes de executar o código:

* Python 3.x instalado
* Biblioteca PIL instalada (`pip install pillow`)

## Como executar o código

1. Faça o download do código-fonte para o seu computador.
2. Certifique-se de ter uma imagem para ajustar o contraste e salve-a no mesmo diretório do código.
3. No código-fonte, localize a linha onde é feita a abertura da imagem e ajuste o caminho do arquivo para corresponder ao nome e localização da sua imagem.
4. No código-fonte, defina o fator de contraste na variável `fator`.
5. Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o código.
6. Execute o código com o comando `python nome_do_arquivo.py`, substituindo "nome_do_arquivo.py" pelo nome do arquivo do código.
7. Aguarde até que o processamento seja concluído. O resultado será salvo como uma nova imagem com o nome "elephant_contrast.jpg" no mesmo diretório.

## Explicação do código

### Ajuste de Contraste

O objetivo deste código é ajustar o contraste de uma imagem usando a biblioteca PIL.

Primeiro, a biblioteca PIL é importada para permitir a manipulação de imagens. Em seguida, a imagem original é aberta usando a função `Image.open()` e armazenada na variável `imagem`.

A função `adjust_contrast()` é definida para ajustar o contraste da imagem. Ela recebe a imagem original e o fator de contraste como parâmetros. A função cria uma cópia da imagem original e, em seguida, percorre cada pixel da imagem usando dois loops `for`. Para cada pixel, o valor de cada componente de cor (R, G, B) é ajustado utilizando a fórmula `nova_cor = int((c - 128) * fator + 128)`. Essa fórmula subtrai 128 de cada componente de cor para normalizar os valores entre -128 e 127, multiplica pelo fator de contraste e, em seguida, adiciona 128 para restaurar os valores originais no intervalo [0, 255]. Os valores resultantes são verificados para garantir que estejam dentro do intervalo válido [0, 255]. A nova cor é definida para o pixel correspondente na imagem ajustada.

No corpo do código principal, o fator de contraste é definido na variável `fator`. A função `adjust_contrast()` é chamada, passando a imagem original e o fator de contraste como argumentos. A imagem ajustada é armazenada na variável `imagem_ajustada`.

Por fim, a imagem ajustada é salva usando o método `save()` com o nome "elephant_contrast.jpg".
