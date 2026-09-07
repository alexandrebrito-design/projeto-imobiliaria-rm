import csv


class Imovel:
  def __init__(self, tipo, quartos, tem_crianca, vagas_garagem):
    self.tipo = tipo.lower()
    self.quartos = int(quartos)
    self.tem_crianca = bool(tem_crianca)
    self.vagas_garagem = int(vagas_garagem)
    self.valor_base = 0.0
    self.valor_mensal = 0.0

  def calcular_aluguel(self):
    # a) Tipos de locação e valores padrões
    if self.tipo == "apartamento":
      self.valor_base = 700.00
      # c) Apartamento com 2 quartos acréscimo de R$ 200,00
      if self.quartos == 2:
        self.valor_base += 200.00
      # g) Desconto de 5% se não possuir crianças
      if not self.tem_crianca:
        desconto = self.valor_base * 0.05
        self.valor_base -= desconto

    elif self.tipo == "casa":
      self.valor_base = 900.00
      # d) Casa com 2 quartos acréscimo de R$ 250,00
      if self.quartos == 2:
        self.valor_base += 250.00

    elif self.tipo == "estudio":
      self.valor_base = 1200.00
      # f) Estúdio: R$ 250,00 pelas primeiras 2 vagas, e R$ 60,00 por vaga adicional
      if self.vagas_garagem > 0:
        if self.vagas_garagem <= 2:
          self.valor_base += 250.00
        else:
          vagas_extras = self.vagas_garagem - 2
          self.valor_base += 250.00 + (vagas_extras * 60.00)

    # e) Vaga de garagem para casas e apartamentos: R$ 300,00
    if self.tipo in ["apartamento", "casa"] and self.vagas_garagem > 0:
      self.valor_base += 300.00

    self.valor_mensal = self.valor_base
    return self.valor_mensal


class ContratoLocacao:
  def __init__(self, valor_total=2000.00, parcelas=5):
    self.valor_total = float(valor_total)
    self.parcelas = int(parcelas)

  def calcular_parcelas_contrato(self):
    if self.parcelas < 1 or self.parcelas > 5:
      raise ValueError("O contrato pode ser parcelado em no máximo 5 vezes.")
    return self.valor_total / self.parcelas


def gerar_csv_parcelas(
    nome_arquivo, valor_mensal, valor_contrato_parcela, total_meses=12
):
  try:
    # Adicionado encoding='utf-8-sig' para o Excel ler os acentos perfeitamente
    # E trocado o separador de ',' para ';' para o Excel separar nas colunas certas
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8-sig") as arquivo:
      escritor = csv.writer(arquivo, delimiter=";")
      escritor.writerow(
          ["Mes", "Aluguel Mensal (R$)", "Parcela Contrato (R$)", "Total Mes (R$)"]
      )

      for mes in range(1, total_meses + 1):
        total_mes = valor_mensal + (
            valor_contrato_parcela if mes <= 5 else 0.0
        )
        escritor.writerow(
            [
                f"Mês {mes}",
                f"{valor_mensal:.2f}",
                (
                    f"{valor_contrato_parcela:.2f}"
                    if mes <= 5
                    else "0.00"
                ),
                f"{total_mes:.2f}",
            ]
        )
    print(f"\n[Sucesso] Arquivo '{nome_arquivo}' gerado e formatado para o Excel!")
  except Exception as e:
    print(f"Erro ao gerar o arquivo CSV: {e}")


# --- Execução Principal da Aplicação ---
if __name__ == "__main__":
  print("=== SISTEMA DE ORÇAMENTO DE ALUGUEL - IMOBILIÁRIA R.M ===")
  try:
    tipo_imovel = input(
        "Digite o tipo de imóvel (Apartamento / Casa / Estudio): "
    ).strip()
    qtd_quartos = int(input("Digite a quantidade de quartos (1 ou 2): "))
    tem_crianca_input = (
        input("Possui crianças? (s/n): ").strip().lower() == "s"
    )
    qtd_vagas = int(input("Digite a quantidade de vagas de garagem desejadas: "))
    qtd_parcelas_contrato = int(
        input("Deseja parcelar o contrato de R$ 2.000,00 em quantas vezes (1 a 5)? ")
    )

    # Instanciando as classes (Conceito de POO exigido)
    imovel = Imovel(
        tipo_imovel, qtd_quartos, tem_crianca_input, qtd_vagas
    )
    aluguel = imovel.calcular_aluguel()

    contrato = ContratoLocacao(valor_total=2000.00, parcelas=qtd_parcelas_contrato)
    valor_parcela_contrato = contrato.calcular_parcelas_contrato()

    print("\n--- RESUMO DO ORÇAMENTO ---")
    print(f"Tipo de Imóvel: {tipo_imovel.capitalize()}")
    print(f"Valor do Aluguel Mensal Ajustado: R$ {aluguel:.2f}")
    print(
        f"Valor do Contrato: R$ 2.000,00 dividido em {qtd_parcelas_contrato}x de"
        f" R$ {valor_parcela_contrato:.2f}"
    )

    # h) No final a aplicação deve apresentar o valor do aluguel mensal orçado e o contrato
    # i) Geração do arquivo .csv com as 12 parcelas
    gerar_csv_parcelas(
        "orcamento_12_meses.csv", aluguel, valor_parcela_contrato
    )

  except ValueError as erro:
    print(f"\n[Erro de Validação]: {erro}. Insira dados numéricos válidos.")