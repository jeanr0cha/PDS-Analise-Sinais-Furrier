(Proposto pela Professora Leticia Araújo Silva)

Objetivo explorar o efeito da frequência de amostragem de sinais continuos e discretos.
Observando a influência da redução e aumento da taxa de amostragem e o fenomeno do aliasing.

* 1 Gerar um sinal senoidal continuo de 5hz
* 2 Amostragem do sinal com diferentes frequências
* 3 Mostrar o que acontece quando a taxa de amostragem é inferior a frequencia minima de nyquist

📝 Descrição
Este projeto, desenvolvido em Python, serve como uma ferramenta visual para o estudo de conceitos fundamentais em Processamento Digital de Sinais. O script gera um sinal senoidal e demonstra o impacto de diferentes taxas de amostragem, ilustrando graficamente.

✨ Funcionalidades
O programa demonstra visualmente os seguintes conceitos:

Geração de Sinal Contínuo: Cria um sinal senoidal de 5 Hz como referência.

Amostragem de Sinais: Amostra o sinal contínuo utilizando diferentes frequências (taxas).

Visualização do Teorema de Nyquist: Mostra graficamente por que a taxa de amostragem deve ser o dobro da frequência do sinal.

Demonstração de Aliasing: Permite ao usuário modificar facilmente as taxas para visualizar o que acontece quando o Teorema de Nyquist não é respeitado.

Linguagem: Python 

📊 Resultados Visuais
Abaixo estão os gráficos gerados pelo script, que ilustram o processo de amostragem.

![Sinal Contínuo Original](exemplo_furrier\Figure_1.png) 
Este é o sinal senoidal de 5 Hz que serve como base para o estudo.

![Amostragem com Taxa de 100 amostras/s](exemplo_furrier\Figure_2.png)  
Com uma taxa alta, a representação do sinal é bastante fiel ao original.

![Amostragem com Taxa de 50 amostras/s](exemplo_furrier\Figure_3.png)   
Reduzindo a taxa pela metade, ainda conseguimos reconstruir o sinal, pois 50 Hz > 10 Hz

![Amostragem com Taxa de 25 amostras/s](exemplo_furrier\Figure_4.png)    
Com 25 amostras por segundo, a forma do sinal começa a ficar menos definida, mas a frequência fundamental ainda é preservada.

📂 Clone do Repositório
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)


Desenvolvido em Setembro de 2024.