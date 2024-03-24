# Order_Flow
Eine simple Softwarelösung um Kunden und Auftrage zu managen. Zwei Kunden sind vorangelegt (Maxi Musterfrau, Kundennummer 1 & Max Mustermann, Kundennnummer 2). Die zwei vorab angelegten Kunden sind frei erfunden.
Die Kundendatenbank ist bewusst mit einem 1 zu 1 verhältniss gesplittet. Hier besteht dann die Möglichkeit, den Zugriff für die Kontaktdaten zu beschränken.
Ich habe mich bewusst für eine SQLite Datenbank entschiede, da ich hier eine höhere portabilität habe. Die Datenbank befindet sich einfach in einer localen Datei, was das Arbeiten mit GitHub/meheren PCs deutlich vereinfacht. Sinnvoll wäre natürlich ein SQL Server, sofern man mit meheren gleichzeitig darauf zugereifen möchte.
# Updates 
- 24.03.2024 → Weitere GUI Anpassungen und die Möglichkeit erste Eingaben in der SQLite Datenbank zu speichern. 
- 18.03.2024 → Erstes kleinere GUI Update.
- 17.03.2024 → Erstellen der Datenbank mit der Kundentabelle.