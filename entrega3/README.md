# Entrega 3
## Resolução de problema de transformação de dados (NF-e)
Resultado é obtido instanciando a classe _RelationalDataFrames_ no script __entrega3.py__, da seguinte maneira:
```python
from entrega3 import RelationalDataFrames
rdfs = RelationalDataFrames(<json_transacoes>)
dim_product = rdfs.dim_product.
fact_sale = rdfs.fact_sale
```
__Obs.__: Testes deverão ser realizados criando-se um <code><script_teste>.py</code> no diretório-pai que contenha o diretório __entrega3__.

Sou viciado em Python _one-liners_. Sei que nem sempre é possível obter código enxuto e limpo, mas após algumas horas de pesquisa cheguei neste [artigo](https://stackoverflow.com/questions/38231591/split-explode-a-column-of-dictionaries-into-separate-columns-with-pandas "Split / Explode a column of dictionaries into separate columns with pandas") no [StackOverflow](https://stackoverflow.com/). Porém, a solução de fato veio após um entendimento mais apurado do método [<code>pandas.json_normalize</code>](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.json_normalize.html). 

### E se eu tivesse mais tempo?
* Disponibilizaria o pacote __entrega3__ como um bibliotenca utilizando setuptools, egg ou wheel. Algo que pudesse ser feito com <code>pip install -e .</code>, ou seja, uma biblioteca que pudesse ser instalada num ambiente virtual ou no ambiente de desenvolvimento.
* Implementação da leitura do JSON a partir da URL.
* Desenvolveria um pacote centralizador de funções de uso geral. Dessa forma, eu poderia reaproveitar código e funções em outras aplicações.
