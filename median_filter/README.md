
# Aplicação do Filtro da Mediana em uma Imagem

Este é um exemplo de código Python que demonstra a aplicação do filtro da mediana em uma imagem usando a biblioteca PIL (Python Imaging Library).

## Pré-requisitos

Certifique-se de ter os seguintes requisitos atendidos antes de executar o código:

* Python 3.x instalado
* Biblioteca PIL instalada (`pip install pillow`)

## Como executar o código

1. Faça o download do código-fonte para o seu computador.
2. Certifique-se de ter uma imagem para aplicar o filtro e salve-a no mesmo diretório do código.
3. No código-fonte, localize a linha onde é feita a abertura da imagem e ajuste o caminho do arquivo para corresponder ao nome e localização da sua imagem.
4. Ajuste o tamanho da janela do filtro modificando o valor da variável `tamanho_janela`. O valor deve ser um número ímpar maior que 1.
5. Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o código.
6. Execute o código com o comando `python nome_do_arquivo.py`, substituindo "nome_do_arquivo.py" pelo nome do arquivo do código.
7. Aguarde até que o processamento seja concluído. O resultado será salvo como uma nova imagem com o nome "elephant_median.jpg" no mesmo diretório.

## Explicação do código

Este código tem como objetivo aplicar o filtro da mediana em uma imagem usando a biblioteca PIL.

A função `aplicar_filtro_mediana()` é definida para percorrer cada pixel da imagem e aplicar o filtro da mediana. Ela recebe a imagem original, uma imagem vazia para armazenar o resultado e o tamanho da janela do filtro como parâmetros. A função itera sobre cada pixel da imagem, exceto nas bordas, e constrói uma janela de tamanho especificado. Em seguida, os valores dos pixels contidos na janela são coletados em uma lista, ordenados e o valor mediano é selecionado. Esse valor mediano é então atribuído ao pixel correspondente na imagem filtrada.

No corpo principal do código, a imagem original é aberta usando a função `Image.open()` e armazenada na variável `imagem`. Em seguida, uma nova imagem vazia é criada usando a função `Image.new()`, com o mesmo modo e tamanho da imagem original, e é armazenada na variável `imagem_filtrada`. O tamanho da janela do filtro é definido na variável `tamanho_janela`. A função `aplicar_filtro_mediana()` é chamada, passando a imagem original, a imagem filtrada e o tamanho da janela como argumentos. O resultado filtrado é salvo usando o método `save()` com o nome "elephant_median.jpg".

Certifique-se de ter permissão de escrita no diretório onde a nova imagem será salva.

**Nota:** Você pode ajustar o código conforme necessário para trabalhar com diferentes imagens e parâmetros, além de personalizar as operações de salvamento e processamento adicionais, se desejar.
