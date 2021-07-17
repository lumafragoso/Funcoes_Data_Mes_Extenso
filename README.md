# Funcoes_Data_Mes_Extenso
Assessment activity of the 1º period of IT Bachelor on Functions in Python / Atividade avaliativa do 1º periodo do Bacharelado em TI sobre Funções em Python

## Data Mês Extenso

### Goal / Objetivo

Build a function that takes a date in DD/MM/YYYY format and returns a text in the D format of mesByLength of YYYY. For each date entered, validate the date and return "Invalid date!" if the date cannot exist. Pay attention to leap years when there is February 29th. For a given year to be a leap year, it must meet the following conditions:
1. The year is divisible by 4, but not divisible by 100; or
2. If the year ends with 00 (two zeros), it is divisible by 400.

Construa uma função que receba uma data no formato DD/MM/AAAA e devolva um texto no formato D de mesPorExtenso de AAAA. Para cada data informada, valide a data e retorne "Data inválida!" caso a data não possa existir. Atenção para os anos bissextos em que há o dia 29 de fevereiro. Para que um determinado ano seja bissexto, ele precisa atender às seguintes condições:
1. O ano é divisível por 4, mas não é divisível por 100; ou
2. Caso o ano termine com 00 (dois zeros), ele é divisivel por 400.

1. Exemple / Exemplo
```py
Data no formato DD/MM/AAAA? 29/02/2020
Retorno da função: 
29 de fevereiro de 2020
```
2. Exemple / Exemplo
```py

Data no formato DD/MM/AAAA? 31/11/2020
Retorno da função: 
Data inválida!
```
