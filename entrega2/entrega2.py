#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 15:36:22 2022

@author: aurelius
"""

# Uso Geral
import sys
import getopt
import json

# Bibliotecas Spark
import findspark
findspark.init()

from pyspark.sql import SparkSession

def coletar_transacoes(path_json_transacoes):
    "Pega o caminho do arquivo json de transações e retorna as transações disponíveis."
	
    json_transacoes = open(path_json_transacoes)
    
    data_transacoes = json.load(json_transacoes)
    
    json_transacoes.close()
    
    return data_transacoes['transacoes']

def calcular_total_liquido(transacoes):
    """Calcula o total liquido em uma coleção de transações.
		Args:
			path_json_transacoes (list): Coleção de transações.
	"""
    
    spark = SparkSession.builder.appName("Entrega2").getOrCreate()	
    df = spark.createDataFrame(transacoes)
	
    df.createOrReplaceTempView("transacoes")

    query = """
		WITH transacoes_liquidas AS (
		        SELECT (total_bruto * (1 - (ROUND((IFNULL(desconto_percentual, 0)/100), 4)))) AS total_liquido 
		          FROM transacoes)        
		
		SELECT ROUND(SUM(total_liquido), 2) AS total_liquido 
		  FROM transacoes_liquidas
		""" 
    result = spark.sql(query)
	
    return result.show()
	
if __name__ == "__main__":
    # Coletando parâmetros de entrada (caminho do json de transações)
    opts, args = getopt.getopt(sys.argv[1:], "f:")
    path_json_transacoes = ""

    
    for opt, arg in opts:
        if opt == "-f":
            path_json_transacoes = arg
	
    transacoes = coletar_transacoes(path_json_transacoes)
    
    calcular_total_liquido(transacoes)
