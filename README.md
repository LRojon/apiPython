# API
## Sommaire
* ## [Cardmaker](#Cardmaker)
    * [Obtenir les cartes](##Obtenir&nbsp;les&nbsp;cartes)
    * Envoyer une carte
    * Obtenir les classes
    * Obtenir les raretés
    * Obtenir les divinités

# Cardmaker

## Obtenir&nbsp;les&nbsp;cartes  
Toutes les valeurs de retour sont aux format JSON

Obtenir toutes les cartes  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/cardmaker/card/get/all  
  
Filtrer les cartes  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/cardmaker/card/filter/name=\<valeur\>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/cardmaker/card/filter/class=\<valeur\>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/cardmaker/card/filter/stat=\<valeur\>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/cardmaker/card/filter/rarity=\<valeur\>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/cardmaker/card/filter/god=\<valeur\>  

## Envoie de carte 
Tout les paramêtres sont à envoyer au format JSON

Envoyer une carte
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/cardmaker/card/set/one
```json
{
   id: integer,
   name: string,
   job: integer,
   effect: string,
   copy: integer,
   stat: "<FOR/DEX/INT>",
   cost: integer,
   requirement: "<FOR>/<DEX>/<INT>",
   rarity: integer,
   god: integer
}
```

## Obtenir les classes  

## Obtenir les raretés  

## Obtenir les divinités  
