import sqlite3


# Funktionen für das "Neuer Kunde" Pop-up-Fenster

def neuer_kunden_fenster_destroy(neuer_kunde_fenster):
    """Diese Funktion schließ das "Neuer Kunde" Pop-up-Fenster und übergabe daten aus?"""
    neuer_kunde_fenster.destroy()


def neuer_kunde_speichern(anrede_combobox, vorname_entry, nachname_entry, strasse_entry, hausnummer_entry, plz_entry, stadt_entry, telefon_entry, mobil_entry, mail_entry):
    """Die Nutzereingaben werden an diese Funktion übergeben, als "str" zwischengespeichert und per SQL Script in der Datenbank gespeichert. Sollte
    Datenbank noch nicht bestehen, wird sie erstellt. Im Anschluss wird das Pop-up-Fenster "Neuer Kunde" mit der Funktion
    "neuer_kunde_fenster_destroy" geschlossen"""

    anrede = anrede_combobox.get()
    vorname = vorname_entry.get()
    nachname = nachname_entry.get()
    strasse = strasse_entry.get()
    hausnummer = hausnummer_entry.get()
    plz = plz_entry.get()
    stadt = stadt_entry.get()
    telefon = telefon_entry.get()
    mobil = mobil_entry.get()
    mail = mail_entry.get()

    print(anrede, vorname, nachname, strasse, hausnummer, plz, stadt, telefon, mobil, mail)

    # SQL Code
    # Die Verbindung mit der Datenbank herstellen
    verbindung = sqlite3.connect("data.db")

    # Mit dieser Anweisung werden die Tabellen erstellt, sofern diese noch nicht existieren
    tabelle_kontaktdaten_erstellen = '''
    CREATE TABLE IF NOT EXISTS Kontaktdaten (
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        Telefonnummer TEXT, 
        Mobil TEXT, 
        Mail TEXT
    )'''

    tabelle_kunden_erstellen = '''
    CREATE TABLE IF NOT EXISTS Kunden (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        KontaktID INTEGER,
        Anrede TEXT,
        Vorname TEXT,
        Nachname TEXT,
        Strasse TEXT,
        Hausnummer TEXT,
        PLZ TEXT,
        Stadt TEXT,
        FOREIGN KEY(KontaktID) REFERENCES Kontaktdaten(ID)
    )'''

    verbindung.execute(tabelle_kontaktdaten_erstellen)
    verbindung.execute(tabelle_kunden_erstellen)

    # Der SQL Befehl um die Daten in die Tabelle "Kontaktdaten" einzufügen
    einfuege_abfrage_kontakttabelle = '''INSERT INTO Kontaktdaten (Telefonnummer, Mobil, Mail) VALUES (?, ?, ?)'''

    # Dieser Tupel ersetzt die Platzhalter "?" in der einfüge Abfrage"
    kontaktdaten_tupel = (telefon, mobil, mail)

    # "der_curser" führt z.B. SQL Abfragen aus
    der_curser = verbindung.cursor()
    der_curser.execute(einfuege_abfrage_kontakttabelle, kontaktdaten_tupel)

    # KontaktID des gerade eingefügten Kontakts abrufen
    kontakt_id = der_curser.lastrowid

    # Der SQL Befehl um die Daten in die Tabelle "Kunden" einzufügen
    einfuege_abfrage_kundentabelle = '''INSERT INTO Kunden (KontaktID, Anrede, Vorname, Nachname, Strasse, Hausnummer, PLZ, 
    Stadt) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''

    # Dieser Tupel ersetzt die Platzhalter "?" in der einfüge Abfrage"
    kundendaten_tupel = (kontakt_id, anrede, vorname, nachname, strasse, hausnummer, plz, stadt)

    # Mit dem "cursor" die SQL Abfrage ausführen.
    der_curser.execute(einfuege_abfrage_kundentabelle, kundendaten_tupel)

    # Durch den "commit" werden die änderungen dauerhaft gespeichert
    verbindung.commit()

    # Niemals vergessen die Verbindung nach gebrauch zu schließen
    verbindung.close()

    # Fenster schließen
    neuer_kunden_fenster_destroy(neuer_kunde_fenster)
