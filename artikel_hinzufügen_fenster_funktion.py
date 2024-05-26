from fenster_destroy import *
import sqlite3


def artikel_hinzufuegen(artikel_hinzufuegen_fenster, bezeichnung_entry, beschreibung_entry, ek_entry, vk_entry,
                        lieferant_entry, mwst_combobox):
    """Diese Funktion fügt neu eingetragene Artikel der Datenbank hinzu. Die Artikelnummer wird dann die ID."""

    # Erfassen & speichern der Nutzereingaben
    bezeichnung = bezeichnung_entry.get()
    beschreibung = beschreibung_entry.get()
    einkaufspreis = ek_entry.get()
    verkaufspreis = vk_entry.get()
    mwst = int(mwst_combobox.get().replace("%", "").replace(",", ""))
    lieferant = lieferant_entry.get()

    # Kontrolle
    print(bezeichnung, beschreibung, einkaufspreis, verkaufspreis, lieferant)

    # SQL Code
    # Die Verbindung mit der Datenbank herstellen
    verbindung = sqlite3.connect("data.db")

    # Erstellen der Tabelle, sofern diese noch nicht existiert
    tabelle_artikel_erstellen = '''
    CREATE TABLE IF NOT EXISTS Artikel (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Bezeichnung TEXT,
    Beschreibung TEXT,
    Einkaufspreis NUMERIC(10, 5),
    Verkaufspreis NUMERIC(10, 5),
    MwSt INTEGER,
    Lieferant TEXT
    )'''

    verbindung.execute(tabelle_artikel_erstellen)

    # Einfügen der Artikeldaten in die Tabelle
    einfuegen_artikeldaten = '''INSERT INTO Artikel (
    Bezeichnung, Beschreibung, Einkaufspreis, Verkaufspreis, MwSt, Lieferant
    )
    VALUES (
        ?, ?, ?, ?, ?, ?
        )'''

    artikeldaten_tupel = (bezeichnung, beschreibung, einkaufspreis, verkaufspreis, mwst, lieferant)

    der_curser = verbindung.cursor()
    der_curser.execute(einfuegen_artikeldaten, artikeldaten_tupel)

    # Änderungen dauerhaft speichern und die Verbindung trennen
    verbindung.commit()
    verbindung.close()

    fenster_destroy(artikel_hinzufuegen_fenster)
