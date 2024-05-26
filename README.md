# Order_Flow
Eine simple Softwarelösung um Kunden und Aufträge zu verwalten. Der Funktionsumfang soll folgende Punkte beinhalten: 1. Kunden 
anlegen, 2. Kunden anhand des Namens/Kundennummer aufrufen, 3. Aufträge anlegen, 4. Aufträge aufrufen, 5. Aufträge als PDF 
exportieren, 6. Artikel anlegen, 7. Artikel bezüglich der Aufträge aufrufen.
Zwei Kunden sind vorangelegt (Maxime Musterfrau, Kundennummer 1 & Jane Doe, Kundennummer 2). Die zwei vorab angelegten 
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
- 26.05.2024 → Verlinkung der oberen Menüleiste zum "Neuer Kunde Pop-up-Fenster hinzugefügt". Anfänge des "Artikel bearbeiten" 
  Tabs sind hinzugefügt.
- 20.05.2024 → Das Pop-up-Fenster "Artikel hinzufügen" wurde optisch aufbereitet inkl. das Hinzufügen der Steuerbuttons.
  Die Funktion (fenster_destroy) wurde in eine eigene Datei ausgelagert. Die Funktionalität neue Artikel einzugeben und zu 
  speichern ist hinzugefügt. Den EK & VK kann mit Punkt oder mit Komma eingeben. Ein Datenbank ERM wurde hinzugefügt.
- 11.05.2024 → Im Main Fenster ist es nun möglich Kunden aufzurufen und deren Daten dauerhaft zu ändern. Das GUI für das 
  Pop-up-Fenster umd Artikel/Dienstleistungen hinzuzufügen wurde erstellt. Die Funktion dazu folgt.
- 01.05.2024 → Hinzufügen einer Menübar im Hauptfenster als vorbereitung zur Verwaltung von Artikeln/Dienstleistungen.
- 25.04.2024 → Kleinere strukturelle Anpassungen bezüglich der Funktionen, sowie hinzufüge der "Kunden suchen" Funktion.
- 19.04.2024 → Leichte strukturelle Anpassungen im Quellcode. Vorbereitende Maßnahmen für die Funktionen des "Main Fenster" 
  bezüglich des Kunden Tabs.
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