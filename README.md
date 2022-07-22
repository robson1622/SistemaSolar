# SistemaSolar
Representação do nosso sistema solar.
Utilizei python para fins de apredizado. As parte física aquí foi simplificada, para um sistemas com uma precisão científica seria necessário a utilização dos conceitos de integral e derivada, o modo como eu fiz foi incremento simples de velocidade com aceleração e posicao com velocidade.


![Animação inicial do jogo](./Arquivos/animacao.gif "Animação inicial do jogo")

## Como compilar
Baixe os arquivos, e no seu melhor terminal execute o comando:
  ```bash
  python main.py
  ```

[![Programa rodando]()](https://user-images.githubusercontent.com/57491372/180504110-cb9f38dc-7f78-4b67-8234-05c844e22f0f.mp4)

Tanto a constante gravitacional G como a acelerção foram alteradas para que os astros se movessem desta forma, caso queira, pode-se experimentar com valores reais, no entanto, deve-se alterar também a posição que os astros seram exibidos na tela.
<br/>
1 - G e a aceleração estão definidos em CampoGravitacional.py
<br/>
2 - As posições na tela estão definidas em Astro.py

## TCC em que a tese foi [sistema de imersão para simulação de n-corpos em astrofisica](https://www1.univap.br/marketing/publico/ipd/fisica-astronomia/mestrado/Luiz.pdf), que resolve as imperfeições do presente projeto.
