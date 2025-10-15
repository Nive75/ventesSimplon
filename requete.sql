-- a) Chiffre d'affaires par produit
SELECT produit, SUM(prix * qte) AS chiffre_affaires FROM ventes GROUP BY produit ORDER BY chiffre_affaires DESC;


-- b) Ventes par produit (quantité)
SELECT produit, SUM(qte) AS ventes_totales
FROM ventes
GROUP BY produit
ORDER BY ventes_totales DESC;


-- c) Ventes par région (quantité)
SELECT region, SUM(qte) AS ventes_par_region
FROM ventes
GROUP BY region
ORDER BY ventes_par_region DESC;