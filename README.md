# Cijferlijst

## Inleiding

Je werkt op een school en je krijgt een bestandje met allemaal cijfers, jij moet deze cijfers eigenlijk met de hand invullen maar zoals een echte programmeur betaamt, ga je dit natuurlijk automatiseren.
Je gaat dus een script schrijven die een bestand inleest en de cijfers in een dictionary zet. en daar het gemiddelde van berekent.

### Stappenplan

#### 1. Maak een nieuwe python file aan en noem deze `cijferlijst.py`.
#### 2. Maak een functie die cijfers genereert

<details>
  <summary>Stappenplan voor stap 2</summary>

  * Open het bestand `cijferlijst.txt` en genereer een cijferlijst.
        <details><summary>Kom je hier niet uit hoe je data in een bestand zet?</summary>
            
        with open("cijferlijst.txt", "w") as file: 
    (De "w" staat voor write)
  

  * Maak een for loop die 10 cijfers genereert tussen de 1 en 10 en voeg deze toe aan het bestand.
  * Sluit het bestand. (`file.close()`)
</details>

#### 3. Functie voor het inlezen van de cijfers

   <details> 
     <summary>Stappenplan voor stap 3</summary>
   
   * Deze functie moet het bestand openen en de cijfers inlezen.
   * Maak een dictionary aan waarin je de cijfers in zet.
   * Loop door het bestand en voeg de cijfers toe aan de dictionary.
   * Return de dictionary.

   </details>


#### 4. Functie voor het berekenen van het gemiddelde

   <details>
    <summary>Stappenplan voor stap 4</summary>

   * Deze functie krijgt de dictionary met cijfers als argument.
   * Bereken het gemiddelde van de cijfers.
   * Return het gemiddelde.
    </details>


#### 5. Functie voor het printen van de cijfers en het gemiddelde

   <details>
    <summary>Stappenplan voor stap 5</summary>

   * Deze functie krijgt de dictionary met cijfers en het gemiddelde als argument.
   * Print de cijfers en het gemiddelde.
    
    Statistieken per vak:
    Vak: wiskunde, Gemiddelde score: 6.3, Hoogste score: 10.0, Laagste score: 1.0
    Vak: nederlands, Gemiddelde score: 5.6, Hoogste score: 10.0, Laagste score: 2.0
    Vak: engels, Gemiddelde score: 4.6, Hoogste score: 10.0, Laagste score: 1.0

</details>


### Bonus

We genereren nu cijfers tussen de 1 en 10, maar probeer eens een float te genereren tussen de 1 en 10. (bv. 7.5) en zorg dat je het gemiddelde ook met 1 decimaal print.