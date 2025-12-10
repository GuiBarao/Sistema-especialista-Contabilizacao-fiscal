(defrule verifica-credito-rotativo
    (utiliza-credito)
    (nao-pagou-total-da-fatura)
        =>
    (assert (usa-credito-rotativo)))


(defrule classifica-imposto-IOF
    (or (realiza-compras-internacionais) (usa-cheque-especial) (usa-credito-rotativo) 
    (contratou-emprestimo) (contratou-financiamento) (compra-moeda-estrangeira) 
    (vende-moeda-estrangeira) (contratou-seguro) (and (resgatou-renda-fixa) 
    (dias-investimento ?d) (test (< ?d 30))))
        =>
    (assert (imposto-iof)))