# Relative Dateipfade
Bei einer relativen Pfadangabe wird kommt es häufig zu Import-Fehlern. 

Das können wir verhindern, indem wir eine Funktion einbauen, die den relativen Pfad (also wie komme ich vom Skript zur Datei) in einen  absoluten Pfad (also wo genau liegt die Datei in einem spezifischen Dateisystem) umwandelt.

## Beispiel
relativer Pfad: `db/example_db.sqlite`
absoluter Pfad: `c:\repos\flaskshowcase\datenbanken\db\example_db.sqlite`