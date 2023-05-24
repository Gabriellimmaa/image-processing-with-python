# Processamento de Imagens com Python

Este repositório contém exemplos de código em Python para processamento de imagens utilizando a biblioteca PIL (Python Imaging Library).

## Visão Geral

O objetivo deste repositório é fornecer exemplos práticos de como realizar diferentes operações de processamento de imagens usando Python e a biblioteca PIL. Cada exemplo é apresentado em um arquivo separado e é acompanhado por uma breve explicação do que o código faz e como executá-lo.

* [ ] Pré-requisitos

Antes de executar os exemplos de código neste repositório, certifique-se de ter os seguintes requisitos atendidos:

* [ ] Python 3.x instalado
* [ ] Biblioteca PIL instalada (`pip install pillow`) versão `pillow 8.3.1`

## Explicação Geral

* `average_filter/average_filter.py`: Aplica o filtro de média para suavizar uma imagem, calculando o valor médio dos pixels na vizinhança.
* `brightness/brightness.py`: Ajusta o brilho de uma imagem, aumentando ou diminuindo a intensidade de cada pixel.
* `contrast/contrast.py`: Realça o contraste de uma imagem, esticando a faixa de valores dos pixels.
* `convert_grey/convert_grey.py`: Converte uma imagem colorida para escala de cinza, calculando a média dos valores RGB de cada pixel.
* `flip/flip.py`: Inverte uma imagem horizontalmente ou verticalmente.
* `gaussian_filter/gaussian_filter.py`: Aplica um desfoque gaussiano a uma imagem, reduzindo ruídos e suavizando a imagem.
* `grey_to_wb/grey_to_wb.py`: Converte uma imagem em escala de cinza para preto e branco, aplicando um limite a cada pixel.
* `images/images.py`: Contém funções utilitárias para carregar e salvar imagens.
* `median_filter/median_filter.py`: Aplica o filtro de mediana para reduzir ruídos em uma imagem, substituindo cada pixel pelo valor mediano de sua vizinhança.
* `rgb/rgb.py`: Separa os canais RGB de uma imagem e salva cada canal como uma imagem separada.
* `rotate/rotate.py`: Rotaciona uma imagem em um ângulo especificado.

Para obter uma explicação mais detalhada sobre cada operação de processamento de imagens e como usar os scripts, consulte as páginas de documentação correspondentes de cada arquivo. Lá você encontrará informações adicionais, exemplos de uso e possíveis parâmetros de configuração.
