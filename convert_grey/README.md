# Conversão para Tons de Cinza

Este é um exemplo de código Python que demonstra a conversão de uma imagem colorida para tons de cinza usando a biblioteca PIL (Python Imaging Library).

## Pré-requisitos

Certifique-se de ter os seguintes requisitos atendidos antes de executar o código:

* Python 3.x instalado
* Biblioteca PIL instalada (`pip install pillow`)

## Como executar o código

1. Faça o download do código-fonte para o seu computador.
2. Certifique-se de ter uma imagem para converter para tons de cinza e salve-a no mesmo diretório do código.
3. No código-fonte, localize a linha onde é feita a abertura da imagem e ajuste o caminho do arquivo para corresponder ao nome e localização da sua imagem.
4. Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o código.
5. Execute o código com o comando `python nome_do_arquivo.py`, substituindo "nome_do_arquivo.py" pelo nome do arquivo do código.
6. Aguarde até que o processamento seja concluído. O resultado será salvo como uma nova imagem com o nome "elephant_grey.jpg" no mesmo diretório.

## Explicação do código

### Conversão para Tons de Cinza

O objetivo deste código é converter uma imagem colorida para tons de cinza usando a biblioteca PIL.

Primeiro, a biblioteca PIL é importada para permitir a manipulação de imagens. Em seguida, a imagem original é aberta usando a função `Image.open()` e armazenada na variável `img`.

A função `convert_to_greyscale()` é definida para converter a imagem para tons de cinza. Ela recebe a imagem original como parâmetro e cria uma cópia da imagem. Em seguida, utiliza o método `convert()` da biblioteca PIL, passando o argumento `"L"` para realizar a conversão para tons de cinza. A imagem convertida em tons de cinza é retornada pela função.

No corpo do código principal, a função `convert_to_greyscale()` é chamada, passando a imagem original como argumento. A imagem convertida é armazenada na variável `img_grey`.

Por fim, a imagem convertida é salva usando o método `save()` com o nome "elephant_grey.jpg".
