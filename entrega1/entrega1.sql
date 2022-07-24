WITH taxas_contratos_ativos AS (
		SELECT contrato_id, cliente_id, percentual/100 percentual  
		  FROM contrato
		  WHERE ativo = 1),
	 
	 totais_liquidos AS (
	 	SELECT tca.contrato_id,
	 		   tca.cliente_id,
	 		   t.valor_total * (1 - (ISNULL(t.percentual_desconto, 0))/100) AS valor_descontado,
	 		   tca.percentual
	 	  FROM taxas_contratos_ativos tca
	 	  JOIN transacao t ON t.contrato_id = tca.contrato_id
		  )

SELECT c.nome,
	   ROUND(SUM(tl.valor_descontado * tl.percentual), 2) ganho_total
  FROM cliente c
  JOIN totais_liquidos tl ON tl.cliente_id = c.cliente_id
  GROUP BY c.nome;

-- Ideia inicial:
/*
SELECT c.nome, ROUND(SUM((t.valor_total * (1 - ISNULL(t.percentual_desconto, 0) / 100)) * co.percentual/100), 2) ganho_total 
	FROM cliente c 
	JOIN contrato co ON co.cliente_id  = c.cliente_id
	JOIN transacao t ON t.contrato_id = co.contrato_id
WHERE co.ativo = 1
GROUP BY nome;*/









