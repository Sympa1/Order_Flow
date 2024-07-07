import sqlite3
from tkinter import END


def kunde_suchen(kundennummer_entry, anrede_combobox, vorname_entry, nachname_entry, strasse_entry, hausnummer_entry, plz_entry,
                 stadt_entry, telefon_entry, mobil_entry, mail_entry):
    """Diese Funktion sucht anhand der Kundennummer den jeweiligen Kunden und ggf. später die dem Kunden zugeordneten Aufträge
	raus."""
    kundennummer = int(kundennummer_entry.get())
    # Die Verbindung mit der Datenbank herstellen
    verbindung = sqlite3.connect("data.db")

    # "der_curser" führt z.B. SQL Abfragen aus
    der_cursor = verbindung.cursor()

    # SQL Abfrage
    kunden_abfrage = "SELECT Kunden.Anrede, Kunden.Vorname, Kunden.Nachname, Kunden.Strasse, Kunden.Hausnummer, Kunden.PLZ, " \
                     "Kunden.Stadt, Kontaktdaten.Telefonnummer, Kontaktdaten.Mobil, Kontaktdaten.Mail FROM Kunden INNER JOIN " \
                     "Kontaktdaten ON Kunden.KontaktID = Kontaktdaten.ID WHERE Kunden.ID = ?"

    kundennummer_tupel = (kundennummer,)

    # SQL-Abfrage ausführen
    der_cursor.execute(kunden_abfrage, kundennummer_tupel)

    # Kundendaten abrufen und als Tupel in der Variable "kundendaten" speichern
    kundendaten = der_cursor.fetchone()

    # Verbindung schließen
    verbindung.close()

    # Überprüfung, ob "kundendaten" leer ist
    if kundendaten is not None:
        # Jeder Wert des Tupels wird in einer separaten Variable gespeichert und an das passende Entry übergeben. Wichtig ist
        # die Reihenfolge.
        anrede, vorname, nachname, strasse, hausnummer, plz, stadt, telefon, mobil, mail = kundendaten
        print(anrede, vorname, nachname, strasse, hausnummer, plz, stadt, telefon, mobil, mail)
        anrede_combobox.set(anrede)
        vorname_entry.delete(0, END)
        vorname_entry.insert(0, vorname)
        nachname_entry.delete(0, END)
        nachname_entry.insert(0, nachname)
        strasse_entry.delete(0, END)
        strasse_entry.insert(0, strasse)
        hausnummer_entry.delete(0, END)
        hausnummer_entry.insert(0, hausnummer)
        plz_entry.delete(0, END)
        plz_entry.insert(0, plz)
        stadt_entry.delete(0, END)
        stadt_entry.insert(0, stadt)
        telefon_entry.delete(0, END)
        telefon_entry.insert(0, telefon)
        mobil_entry.delete(0, END)
        mobil_entry.insert(0, mobil)
        mail_entry.delete(0, END)
        mail_entry.insert(0, mail)
    else:
        kundennummer_entry.delete(0, END)
        kundennummer_entry.insert(0, str(kundennummer) + " ist keine bekannte Kundennummer!")
        anrede_combobox.set("")
        vorname_entry.delete(0, END)
        nachname_entry.delete(0, END)
        strasse_entry.delete(0, END)
        hausnummer_entry.delete(0, END)
        plz_entry.delete(0, END)
        stadt_entry.delete(0, END)
        telefon_entry.delete(0, END)
        mobil_entry.delete(0, END)
        mail_entry.delete(0, END)


def kunde_aendern(kundennummer_entry, anrede_combobox, vorname_entry, nachname_entry, strasse_entry, hausnummer_entry, plz_entry,
                  stadt_entry, telefon_entry, mobil_entry, mail_entry):
    """Diese Funktion speichert die eingetragenen Änderungen der Kunden Stammdaten."""
    # Ggf. macht ein "Alert Pop-Up-Fenster" sinn? Ich weiß, dass ich jedes mal alle Kundendaten neu speicher, auch wenn diese
    # sich nicht geändert haben. Wie kann ich das mit einer ("if" Abfrage) lösen?
    kundennummer = kundennummer_entry.get()
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

    # SQL Code
    # Die Verbindung mit der Datenbank herstellen
    verbindung = sqlite3.connect("data.db")

    # Der SQL Befehl um die KontaktID aus der Tabelle "Kunden" zu erhalten
    abfrage_kontaktID = '''SELECT KontaktID FROM Kunden WHERE ID = ?'''

    # Dieser Tupel ersetzt die Platzhalter "?" in der Abfrage
    kundendaten_tupel = (kundennummer)

    # "der_curser" führt z.B. SQL Abfragen aus
    der_curser = verbindung.cursor()
    der_curser.execute(abfrage_kontaktID, kundendaten_tupel)

    # Die KontaktID aus dem Ergebnis der Abfrage extrahieren 
    # "fetchone()" speichert das Ergebnis als Tupel
    # "ergebnis[0] if ergebnis else None" extrahiert dann die "kontaktID" und speichert diese zuer weiteren verwendung
    ergebnis = der_curser.fetchone()
    kontaktID = ergebnis[0] if ergebnis else None

    # Prüfen ob "kontakID" einen Wert hat.
    if kontaktID is not None:
        # Der SQL Befehl um die Daten in die Tabelle "Kontaktdaten" & "Kundentabelle" zu aktualisieren
        update_abfrage_kontakttabelle = '''UPDATE Kontaktdaten SET Telefonnummer = ?, Mobil = ?, Mail = ? WHERE ID = ?'''
        update_abfrage_kundentabelle = '''UPDATE Kunden SET Anrede = ?, Vorname = ?, Nachname = ?, Strasse = ?, Hausnummer = ?, PLZ = ?, 
        Stadt = ? WHERE ID = ?'''

        # Dieser Tupel ersetzt die Platzhalter "?" in der update Abfrage"
        kontaktdaten_tupel = (telefon, mobil, mail, kontaktID)
        kundendaten_tupel = (anrede, vorname, nachname, strasse, hausnummer, plz, stadt, kundennummer)

        # "der_curser" führt z.B. SQL Abfragen aus
        der_curser.execute(update_abfrage_kontakttabelle, kontaktdaten_tupel)
        der_curser.execute(update_abfrage_kundentabelle, kundendaten_tupel)

        # Durch den "commit" werden die änderungen dauerhaft gespeichert
        verbindung.commit()


def sum_mwst(art_mwst_combobox, art_nvk_entry, sum_mwst_entry, art_bvk_entry):
    """
    Diese Funktion berechnet den Bruttoverkaufspreis und die Höhe der MwSt.
    Parameters
    ----------
    art_mwst_combobox
    art_nvk_entry
    sum_mwst_entry
    art_bvk_entry

    Returns
    -------
    -/-
    """
    mwst_satz = float(art_mwst_combobox.get().replace("%", ""))
    netto_vk = float(art_nvk_entry.get().replace(",", "."))

    if mwst_satz == 7.0:
        brutto_vk = round(netto_vk * 1.07, 2)
        sum_mwst = round(brutto_vk - netto_vk, 2)
        art_bvk_entry.insert(0, str(brutto_vk).replace(".", ","))
        sum_mwst_entry.insert(0, str(sum_mwst).replace(".", ","))
    else:
        brutto_vk = round(netto_vk * 1.19, 2)
        sum_mwst = round(brutto_vk - netto_vk, 2)
        art_bvk_entry.insert(0, str(brutto_vk).replace(".", ","))
        sum_mwst_entry.insert(0, str(sum_mwst).replace(".", ","))


def gewinn(art_nvk_entry, art_gewinn_entry, art_ek_entry):  # ICh muss den EK anstelle des Brutto VK nehmen!!!
    ek = float(art_ek_entry.get().replace(",", "."))
    netto_vk = float(art_nvk_entry.get().replace(".", ","))

    gewinn = netto_vk - ek

    art_gewinn_entry.insert(0, str(gewinn).replace(".", ","))


def wrapper_mwst_gewinn(art_mwst_combobox, art_nvk_entry, sum_mwst_entry, art_bvk_entry, art_gewinn_entry, art_ek_entry):
    sum_mwst(art_mwst_combobox, art_nvk_entry, sum_mwst_entry, art_bvk_entry)
    gewinn(art_nvk_entry, art_gewinn_entry, art_ek_entry)


def artikel_suchen():
    pass


def artikel_aendern():
    pass
