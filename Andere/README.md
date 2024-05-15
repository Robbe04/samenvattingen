# Welkom bij de **Andere** sectie van mijn samenvattingbranche
In deze tak worden andere persoonlijke/handige dingen online gezet wat ofwel: **wel**, **niet** of **deels** te maken heeft met vakken van school.

#  [Vbs-bestanden](https://github.com/Robbe04/samenvattingen/edit/main/Andere/README.md)
Het allereerste Andere onderwerp zijn `vbs-bestanden`. Hiermee kan je allerlei handige scriptjes bouwen om zo bv. een aantal vensters open te doen op een bepaalde locatie. 
Je kan dus bv. cmd openen waarin automatisch een bepaald commando wordt gestart dat bv. een map maakt in de gebruiker die het bestand opent op een bepaalde locatie. 

Het **basisonderdeel** van deze cursus is klaar, maar er komt nog een uitbreiding aan! Wegens de examen zal dit wel wat langer duren aangezien ik minder tijd ga hebben. 
### Probeer vbs eens uit!
Probeer deze starterscode eens uit als inzicht wat vbs is: 
``` vbs
    ' Het maken van een map in de Documents-map genaamd "Test_vbs"
    Dim wshShell
    Set wshShell = WScript.CreateObject("WScript.Shell")
    wshShell.Run "cmd /c mkdir %USERPROFILE%\Documents\Test_vbs", 0, True 
```
