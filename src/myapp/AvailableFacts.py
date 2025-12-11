from enum import Enum

class InitialFacts(str, Enum):

    #-----------------------Tax Classification----------------------#
    UTILIZA_CREDITO = "utiliza-credito"
    NAO_PAGOU_TOTAL_DA_FATURA = "nao-pagou-total-da-fatura"
    REALIZA_COMPRAS_INTERNACIONAIS = "realiza-compras-internacionais"
    USA_CHEQUE_ESPECIAL = "usa-cheque-especial"
    CONTRATOU_EMPRESTIMO = "contratou-emprestimo"
    CONTRATOU_FINANCIAMENTO = "contratou-financiamento"
    COMPRA_MOEDA_ESTRANGEIRA = "compra-moeda-estrangeira"
    VENDE_MOEDA_ESTRANGEIRA = "vende-moeda-estrangeira"
    CONTRATOU_SEGURO = "contratou-seguro"
    RESGATOU_RENDA_FIXA = "resgatou-renda-fixa"


class ResultFacts(str, Enum):
    
    #-----------------------Tax Classification----------------------#

    USA_CREDITO_ROTATIVO = "usa-credito-rotativo"
    IMPOSTO_IOF = "imposto-iof"
