# Order_Flow
Eine simple Softwarelösung um Kunden und Aufträge zu managen. Der Funktionsumfang soll folgende Punkte beinhalten: 1. Kunden anlegen, Kunden anhand des Namens/Kundennummer aufrufen, 3. Aufträge anlegen, 4. Aufträge aufrufen, 5. Aufträge als PDF exportieren, 6. Artikel anlegen, 7. Artikel bezüglich der Aufträge aufrufen.
Zwei Kunden sind vorangelegt (Maxi Musterfrau, Kundennummer 1 & Max Mustermann, Kundennnummer 2). Die zwei vorab angelegten Kunden sind frei erfunden.
Die Kundendatenbank ist bewusst mit einem 1 zu 1 verhältniss gesplittet. Hier besteht dann die Möglichkeit, den Zugriff für die Kontaktdaten zu beschränken.
Ich habe mich bewusst für eine SQLite Datenbank entschiede, da ich hier eine höhere portabilität habe. Die Datenbank befindet sich einfach in einer localen Datei, was das Arbeiten mit GitHub/meheren PCs deutlich vereinfacht. Sinnvoll wäre natürlich ein SQL Server, sofern man mit meheren gleichzeitig darauf zugereifen möchte.
Das aktuelle GUI entspricht nicht meinen Vorstellungen und dient dem Testzweck.
# Updates 
- 25.03.2024 → Nach dem Klicken auf den Button "Speichern" wird die Kundennummer automatisch angezeigt. Diese besteht aus dem Primärschlüssel der Tabelle und dem Zusatz "KD". Außerdem gibt es jetzt den Button "Neuer Kunde" was den Inhalt aller Entrys und der Combobox zurücksetzt. Es ist auch möglich sich den Inhalt der Tabelle "Kunden" in der Konsole ausgeben zu lassen ("Anzeigen" Button).
- 24.03.2024 → Weitere GUI Anpassungen und die Möglichkeit erste Eingaben in der SQLite Datenbank zu speichern.
- 18.03.2024 → Erstes kleinere GUI Update.
- 17.03.2024 → Erstellen der Datenbank mit der Kundentabelle.