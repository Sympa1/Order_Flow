# Order_Flow
Eine simple Softwarelösung um Kunden und Aufträge zu verwalten. Der Funktionsumfang soll folgende Punkte beinhalten: 1. Kunden 
anlegen, Kunden anhand des Namens/Kundennummer aufrufen, 3. Aufträge anlegen, 4. Aufträge aufrufen, 5. Aufträge als PDF 
exportieren, 6. Artikel anlegen, 7. Artikel bezüglich der Aufträge aufrufen.
Zwei Kunden sind vorangelegt (Jane Doe, Kundennummer 1 & Max Mustermann, Kundennummer 2). Die zwei vorab angelegten 
Kunden sind frei erfunden.
Die Kundendatenbank ist bewusst mit einem 1 zu 1 Verhältnisse gesplittet. Dadurch soll z.B. die Datenkonsistenz, wenn sich 
beispielsweise die Mobilfunknummer ändert sichergestellt werden. Auch soll dadurch die Effizienz gesteigert werden. Durch die 
daraus resultierende efficient Indexierung, soll sich die Abfrageleistung sich verbessern.
Ich habe mich bewusst für eine SQLite Datenbank entschiede, da ich hier eine höhere portabilität habe. Die Datenbank befindet 
sich einfach in einer locale Datei, was das Arbeiten mit GitHub/mehreren PCs deutlich vereinfacht. Sinnvoll wäre natürlich ein
SQL Server, sofern man mit mehreren gleichzeitig darauf zuge reifen möchte.
Das aktuelle GUI wird Step by Step auf- und ausgebaut. Teilweise gibt es noch Platzhalter, oder Elemente die Testweise 
eingebaut sind.
# Updates 
- 11.04.2024 → Die neuen Kunden legt man nun per Klick auf den Button "Neuer Kunde" an. Es folgt ein Pop-up-Fenster zur 
  eingabe der Kundendaten. Die "Newsletter" Checkbox ist aktuell noch ohne Funktion, bis ich einen sinnvollen weg zur 
  implementierung der funktion dahinter gefunden habe.
  Es gibt jetzt die Möglichkeit Kontaktdaten den jeweiligen Kunden zuzuordnen. Diese werden in einer separaten Tabelle 
  gespeichert und stehen in einer 1 zu 1 relation zueinander. Das "main_fenster" GUI wird schrittweise angepasst.
- 25.03.2024 → Nach dem Klicken auf den Button "Speichern" wird die Kundennummer automatisch angezeigt. Diese besteht aus dem 
  Primärschlüssel der Tabelle und dem Zusatz "KD". Außerdem gibt es jetzt den Button "Neuer Kunde" was den Inhalt aller Entry's
  und der Combobox zurücksetzt. Es ist auch möglich sich den Inhalt der Tabelle "Kunden" in der Konsole ausgeben zu lassen 
  ("Anzeigen" Button).
- 24.03.2024 → Weitere GUI Anpassungen und die Möglichkeit erste Eingaben in der SQLite Datenbank zu speichern.
- 18.03.2024 → Erstes kleinere GUI Update.
- 17.03.2024 → Erstellen der Datenbank mit der Kundentabelle.
