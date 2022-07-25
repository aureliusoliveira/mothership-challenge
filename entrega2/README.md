# Entrega 2
## Código com pyspark que retorne o total liquido
Resultado obtido executando o script __entrega2.py__, da seguinte maneira:
No terminal ou command prompt, digite <code>spark-submit entrega2.py -f <transacoes.json></code>.
Minha principal dificuldade nesta atividade foi o de revisar os conhecimentos de Spark e Pyspark. Primeiramente, cogitei em utilizar operações de manipulação em Dataframe, mas depois de descobrir que eu poderia [rodar consultas programaticamente utilizando views temporárias](https://datacamp-community-prod.s3.amazonaws.com/02213cb4-b391-4516-adcd-57243ced8eed "PySpark SQL Basics Cheat Sheet") segui por este caminho.

### E se eu tivesse mais tempo?
* Revisaria o requirement.txt (O que talvez nem fosse necessário já que o Pipfile está sendo rastreado pelo controle de versão)
* Construiria um Dockerfile automatizando a construção do ambiente teste.
* Talvez isso pudesse virar um serviço...
