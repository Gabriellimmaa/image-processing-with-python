# Filtro Gaussiano para Desfoque de Imagem

Este é um exemplo de código Python que demonstra como aplicar um filtro gaussiano para desfocar uma imagem usando a biblioteca PIL (Python Imaging Library) e a biblioteca NumPy.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos atendidos antes de executar o código:

* Python 3.x instalado
* Bibliotecas PIL e NumPy instaladas (`pip install pillow numpy`)

## Como executar o código

1. Faça o download do código-fonte para o seu computador.
2. Certifique-se de ter uma imagem para aplicar o filtro e salve-a no mesmo diretório do código.
3. No código-fonte, localize a linha onde é feita a abertura da imagem e ajuste o caminho do arquivo para corresponder ao nome e localização da sua imagem.
4. Ajuste o valor do parâmetro `radius` na linha `imagem_desfocada = gaussian_blur(imagem, 10)` para controlar o nível de desfoque desejado (maior valor de `radius` resulta em um desfoque mais intenso).
5. Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o código.
6. Execute o código com o comando `python nome_do_arquivo.py`, substituindo "nome_do_arquivo.py" pelo nome do arquivo do código.
7. Aguarde até que o processamento seja concluído. O resultado será salvo como uma nova imagem com o nome "elephant_gaussian.jpg" no mesmo diretório.

## Explicação do código

O objetivo desse código é aplicar um filtro gaussiano para desfocar uma imagem usando a biblioteca PIL e a biblioteca NumPy.

A função `gaussian_blur()` é definida para realizar o desfoque gaussiano na imagem. Ela recebe a imagem original e o raio do kernel como parâmetros. A função realiza as seguintes etapas:

1. Converte a imagem em uma matriz NumPy.
2. Cria um kernel gaussiano usando a função `_create_gaussian_kernel()`.
3. Aplica o filtro gaussiano à matriz da imagem usando a função `_apply_gaussian_filter()`.
4. Converte a matriz resultante de volta para uma imagem PIL.
5. Retorna a imagem desfocada.

A função `_create_gaussian_kernel()` é responsável por criar o kernel gaussiano. Ela recebe o raio do kernel como parâmetro e realiza as seguintes etapas:

1. Calcula o tamanho do kernel com base no raio.
2. Cria uma matriz de zeros para armazenar o kernel.
3. Calcula os pesos do kernel usando a fórmula gaussiana.
4. Normaliza o kernel dividindo-o pela soma de seus valores.
5. Retorna o kernel.

A função `_apply_gaussian_filter()` aplica o filtro gaussiano à matriz da imagem. Ela recebe a matriz da imagem e o kernel como parâmetros e realiza as seguintes etapas:

1. Extrai as dimensões da imagem e do kernel.
2. Cria uma cópia da matriz da imagem para armazenar o resultado filtrado.
3. Percorre cada pixel da imagem, exceto as bordas.
4. Obtém a vizinhança do pixel usando o tamanho do kernel.
5. Aplica o filtro ponderado pela vizinhança e pelo kernel.
6. Atribui o valor filtrado ao pixel correspondente na imagem filtrada.

No corpo do código principal, a imagem original é aberta usando a função `Image.open()` e armazenada na variável `imagem`. Em seguida, a função `gaussian_blur()` é chamada, passando a imagem e o valor do raio como argumentos. A imagem desfocada é armazenada na variável `imagem_desfocada`.

Por fim, a imagem desfocada é salva usando o método `save()` com o nome "elephant_gaussian.jpg".
