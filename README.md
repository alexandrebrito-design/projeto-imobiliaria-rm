# Sistema de Orçamento de Aluguel - Imobiliária R.M.

Aplicação desenvolvida em Python com foco em automação comercial e gestão de locação imobiliária (Casas, Apartamentos e Estúdios), utilizando os conceitos fundamentais de **Orientação a Objetos (POO)** e manipulação de arquivos relacionais.

---

## Funcionalidades da Aplicação

- **Orientação a Objetos (POO):** Classes estruturadas (`Imovel` e `ContratoLocacao`) para modularização e aplicação das regras de negócio.
- **Regras de Precificação Customizadas:**
  - **Apartamentos:** Valor base com acréscimo por número de quartos e desconto opcional de 5% caso o cliente não possua crianças.
  - **Casas:** Valor base com regras específicas de acréscimo para 2 quartos.
  - **Estúdios:** Sistema progressivo de cobrança para vagas de garagem.
- **Gestão de Contratos:** Fracionamento do valor contratual em até 5 parcelas mensais com validações e tratamento de exceções (`try-except`).
- **Exportação de Dados:** Geração automatizada de um relatório detalhado de 12 meses em formato `.csv`, totalmente otimizado com codificação UTF-8 e delimitador compatível com o Microsoft Excel.

---

## Tecnologias Utilizadas

- **Python 3.x** (Linguagem principal)
- **Módulo `csv`** (Manipulação de planilhas)
- **Paradigma POO** (Classes, Métodos e Encapsulamento)

---

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `orcamento_imobiliaria.py`.
3. Abra o terminal na pasta do projeto e execute o comando:
   ```bash
   python orcamento_imobiliaria.py
