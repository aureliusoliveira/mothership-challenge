#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 19:12:46 2022

@author: aurelius
"""
import json
import sys
import getopt
import pandas as pd


# Tentativas frustradas de baixar o json 'data.json' programaticamente. :-(
# url = "https://drive.google.com/file/d/1IDCjpDZh5St97jw4K_bAewJ8hf-rax9C/view"

# Tentativa 1
# =============================================================================
# import urllib.request
# 
# fp = urllib.request.urlopen(url)
# mybytes = fp.read()
# 
# mystr = mybytes.decode("utf8")
# fp.close()
# 
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(mystr)
# print(soup.prettify())
# =============================================================================


# Tentativa 2
# =============================================================================
# import requests
# r = requests.get(url)
# mystr = r.text
# 
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(mystr)
# print(soup.prettify())
# =============================================================================

# TODO: Criar um módulo ou uma classe que centralize estas funções de uso geral, 
# por ora vamos apenas em frente. :P

def coletar_transacoes(path_json_transacoes):
    "Pega o caminho do arquivo json de transações e retorna as transações disponíveis."
	
    json_transacoes = open(path_json_transacoes)
    
    transacoes = json.load(json_transacoes)
    
    json_transacoes.close()
    
    return transacoes

def converter_2nf(transacoes):
    """Converte uma coleção transações de um objeto json complexo (https://acervolima.com/serializar-e-desserializar-json-complexo-em-python/)
    em dataframes normalizados tipo 2NF: dim_product e fact_sale."""
    
    df = pd.json_normalize(transacoes,
                           "ItemList", 
                           ["CreateDate", "EmissionDate", "Discount", "NFeNumber", "NFeID"])

    df["ProductName"] = df["ProductName"].astype('category')

    df["ProductID"] = df["ProductName"].cat.codes

    dim_product = df.loc[df["ProductID"].unique(), ["ProductID", "ProductName"]]

    fact_sale = df.loc[:, ~df.columns.isin(["ProductName"])]
    
    relational_dfs = {'dim_product': dim_product, 
                      'fact_sale': fact_sale}
    
    return relational_dfs

class RelationalDataFrames:
    def __init__(self, path_json_transacoes):
        self.path_json_transacoes = path_json_transacoes
        self.transacoes = coletar_transacoes(path_json_transacoes)        
        
        relational_dfs = converter_2nf(self.transacoes)
        self.dim_product = relational_dfs['dim_product']
        self.fact_sale = relational_dfs['fact_sale']
        
    
# =============================================================================
# if __name__ == "__main__":
#     # Coletando parâmetros de entrada (caminho do json de transações)
#     opts, args = getopt.getopt(sys.argv[1:], "f:")
#     path_json_transacoes = None
#     
#     for opt, arg in opts:
#         if opt == "-f":
#             path_json_transacoes = arg
# =============================================================================
    
# =============================================================================
#     
# 	
#     
# 
# 
# data_json = open('data.json')
# 
# data = json.load(data_json)
# 
# data_json.close()
# 
# df = pd.json_normalize(data,
#                        "ItemList", 
#                        ["CreateDate", "EmissionDate", "Discount", "NFeNumber", "NFeID"])
# 
# df["ProductName"] = df1["ProductName"].astype('category')
# 
# df["ProductID"] = df["ProductName"].cat.codes
# 
# dim_product = df.loc[df["ProductID"].unique(), ["ProductID", "ProductName"]]
# 
# fact_sale = df1.loc[:, ~df1.columns.isin(["ProductName"])]
# 
# =============================================================================
