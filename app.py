import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')




# Graphique 2 : Ventes par produit (quantité) 
px.bar(données.groupby('produit', as_index=False)['qte'].sum(), x='produit', y='qte', title='Ventes par produit (quantité)').write_html('ventes-par-produit.html') 
print('ventes-par-produit.html généré avec succès !')

# Graphique 3 : Chiffre d'affaires par produit 
px.bar((données.assign(ca=données['qte']*données['prix']).groupby('produit', as_index=False)['ca'].sum()), x='produit', y='ca', title="Chiffre d'affaires par produit").write_html('chiffre-affaires-par-produit.html') 
print('chiffre-affaires-par-produit.html généré avec succès !')