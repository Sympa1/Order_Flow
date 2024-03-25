import tkinter as tk
from tkinter import ttk, END
import sqlite3


root = tk.Tk()
root.title("Order Flow")
root.geometry("600x300")


# Erstellen des Notebook Widget
notebook_widget = ttk.Notebook(root)
# Erstellen der einzelen Tabs als Frame
tab1 = ttk.Frame(notebook_widget)
tab2 = ttk.Frame(notebook_widget)
tab3 = ttk.Frame(notebook_widget)

# Erstellen und Hinzufügen der Registerkarten 
notebook_widget.add(tab1, text="Kunden")
notebook_widget.add(tab2, text="Placeholder")
notebook_widget.add(tab3, text="Placeholder")

# Expand und Fill sorgen gemeinsam dafür, dass das Notebook Widget die gesamte verfügabre Fläche ausfüllt
notebook_widget.pack(expand=True, fill="both", pady=5, padx=5)

# Hinzufügen des Abschnitts "Kundennummer"
kundennummer_label_frame = ttk.LabelFrame(tab1, text="Kundennummer:")
kundennummer_label_frame.grid(row=0, column=0, pady=5, padx=5, sticky="w")

# Hinzufügen des Abschnitts "Anschrift", Kotaktdaten und Bankverbindung
anschrift_label_frame = ttk.LabelFrame(tab1, text="Anschrift:")
anschrift_label_frame.grid(row=1, column=0, padx=5, pady=5)


konakt_label_frame = ttk.LabelFrame(tab1, text="Kontaktdaten")
konakt_label_frame.grid(row=1, column=1, padx=5, pady=5)


bv_label_frame = ttk.LabelFrame(tab1, text="Bankverbindung")
bv_label_frame.grid(row=1,column=2, padx=5, pady=5)


# Inhalt des Abschnitts "Kundennummer"
kundennummer_label_ausgabe = ttk.Label(kundennummer_label_frame, text="Wird automatisch generiert", background="light gray")
kundennummer_label_ausgabe.grid(row=1, column=0, pady=5, padx=5, sticky="w")

# Inhalt des Abschnitts "Anschrift"
# Mit der Option "width" habe ich die "Breite in Zeichen" der Combobo0x festegelgt
anrede_label = ttk.Label(anschrift_label_frame, text="Anrede:")
anrede_label.grid(row=3, column=0, pady=5, padx=10, sticky="w")
anrede_combobox = ttk.Combobox(
    anschrift_label_frame,
    cursor="hand2",
    state="readonly",
    values=["Herr", "Frau", "Divers"],
    width=17
    )
anrede_combobox.grid(row=4, column=0, padx=5)

vorname_label = ttk.Label(anschrift_label_frame, text="Vorname:")
vorname_label.grid(row=5, column=0, sticky="w", padx=10)
vorname_entry = ttk.Entry(anschrift_label_frame)
vorname_entry.grid(row=6, column=0)

nachname_label = ttk.Label(anschrift_label_frame, text="Nachname:")
nachname_label.grid(row=5, column=1, sticky="w", padx=2)
nachname_entry = ttk.Entry(anschrift_label_frame)
nachname_entry.grid(row=6, column=1)

strasse_label = ttk.Label(anschrift_label_frame, text="Straße:")
strasse_label.grid(row=9, column=0, sticky="w", padx=10)
strasse_entry = ttk.Entry(anschrift_label_frame)
strasse_entry.grid(row=10, column=0)

hausnummer_label = ttk.Label(anschrift_label_frame, text="Hausnummer:")
hausnummer_label.grid(row=9, column=1, sticky="w", padx=2)
hausnummer_entry = ttk.Entry(anschrift_label_frame)
hausnummer_entry.grid(row=10, column=1)

# Die verwendeten Tupel mit "pady" besagen in diesem Fall einen Abstand von "0px" nach oben und von "5px" nach unten
plz_label = ttk.Label(anschrift_label_frame, text="PLZ:")
plz_label.grid(row=13, column=0, sticky="w",padx=10)
plz_entry = ttk.Entry(anschrift_label_frame)
plz_entry.grid(row=14, column=0, pady=(0, 5))

# Die verwendeten Tupel mit "pady" besagen in diesem Fall einen Abstand von "0px" nach oben und von "5px" nach unten
# Die verwendeten Tupel mit "padx" besagen in diesem Fall einen Abstand von "0px" nach links und von "5px" nach rechts
stadt_label = ttk.Label(anschrift_label_frame, text="Stadt:")
stadt_label.grid(row=13, column=1, sticky="w", padx=2)
stadt_entry = ttk.Entry(anschrift_label_frame)
stadt_entry.grid(row=14,column=1, pady=(0, 5), padx=(0, 5))


# Die "speichern" Funktion
def speichern():
   # Hier speichern wir die aktuellen Eingaben der Nutzer in Variablen
   anrede = anrede_combobox.get()
   vorname = vorname_entry.get()
   nachname = nachname_entry.get()
   strasse = strasse_entry.get()
   hausnummer = hausnummer_entry.get()
   plz = plz_entry.get()
   stadt = stadt_entry.get()

   print(anrede, vorname, nachname, strasse, hausnummer, plz, stadt)
   
   # SQL Code
   # Die Verbindung mit der Datenbank herstellen
   verbindung = sqlite3.connect("Order_Flow/data.db")
   # Mit dieser Anweisung wird die Tabelle erstellt, sofern diese noch nicht existiert
   tabelle_erstellen ='''CREATE TABLE IF NOT EXISTS Kunden (Kundennummer INTEGER PRIMARY KEY AUTOINCREMENT, Vorname TEXT, Nachname TEXT, Strasse TEXT, Hausnummer TEXT, PLZ TEXT, Stadt TEXT)'''
   verbindung.execute(tabelle_erstellen)

   # Der SQL Befehl um die Daten in die Tabelle einzufügen
   einfügeabfrage = '''INSERT INTO Kunden (Anrede, Vorname, Nachname, Strasse, Hausnummer, PLZ, Stadt) VALUES (?, ?, ?, ?, ?, ?, ?)'''
   # Dieser Tupel ersetzt die Platzhalter "?" in der "einfügeabfrage"
   daten_tupel = (anrede, vorname, nachname, strasse, hausnummer, plz, stadt)

   # Der Curser führt z.B. SQL Abfragen aus
   der_curser = verbindung.cursor()
   der_curser.execute(einfügeabfrage, daten_tupel)

   # Durch den "commit" werden die änderungen dauerhaft gespeichert
   verbindung.commit()

   # Die Kundennummer abrufen und im ENtry anzeigen
   # Den Primärschlüssel abrufen & in einer Variable speichern. Dazu nutzt man "lastrowid". Lastrowid gibt den Wert des zuletzt eingefügten Primärschlüssels zurück (integer).
   primärschlüssel = der_curser.lastrowid
   # Jetzt wird der Zusatz "KD" hinzugefügt, was dann die Kundennumer ergibt
   kundennummer = str(primärschlüssel) + "KD"
   # Löscht den aktuellen Inhalt
   kundennummer_label_ausgabe.config(text=" ")
   # Fügt die Kundennummer ein
   kundennummer_label_ausgabe.config(text=kundennummer)

   # Durch den "commit" werden die änderungen dauerhaft gespeichert
   verbindung.commit()

   # Niemals vergessen die Verbidnung nach gebrauch zu schließen
   verbindung.close()

def neuer_kunde():
   # Setzt den Text wieder auf Stadart zurück
   kundennummer_label_ausgabe.config(text="Wird automatisch generiert")
   # Mit "set" setzten wir den Inhalt der Combobox auf einen lehren String
   anrede_combobox.set(" ")
   # "0" und "END" beziehen sich auf den Index der Zeichen in dem Entry Widget. END Ziehlt auf ein undifiniertes Ende. 
   vorname_entry.delete(0, END)
   nachname_entry.delete(0, END)
   strasse_entry.delete(0, END)
   hausnummer_entry.delete(0, END)
   plz_entry.delete(0, END)
   stadt_entry.delete(0, END)

def tabelleninhalt_anzeigen():
   # Verbindung zur Datenbank aufbauen
   verbindung = sqlite3.connect("Order_Flow/data.db")
   # Der Curser führt z.B. SQL Abfragen aus
   der_curser = verbindung.cursor()
    # Ausführen einer Abfrage, um alle Inhalte der Tabelle anzuzeigen
   der_curser.execute("SELECT * FROM Kunden")
   # "fetchall" Zieht sich alle Infos einer Tabelle und speichert die einzelenen Zeilen als Tupel
   daten = der_curser.fetchall()
   # Schließen der Verbindung zur Datenbank
   verbindung.close()
   print(daten)


# Test Buttons
btn1 = ttk.Button(tab1, text="Speichern", command=speichern)
btn1.grid(row=0, column=1)

btn2 = ttk.Button(tab1, text="Anzeigen", command=tabelleninhalt_anzeigen)
btn2.grid(row=0, column=2)

btn3 = ttk.Button(tab1, text="Neuer Kunde", command=neuer_kunde)
btn3.grid(row=1, column=1, sticky="n")


# Sizegrip-Widget hinzufügen
# "relx" bedeutet: Die relative horizontale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil der Breite des Elternwidgets (0.0 bedeutet links, 1.0 bedeutet rechts)
# "rely" bedeutet:  Die relative vertikale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil der Höhe des Elternwidgets (0.0 bedeutet oben, 1.0 bedeutet unten)
sizegrip = ttk.Sizegrip(root)
sizegrip.place(relx=1.0, rely=1.0, anchor="se")


root.mainloop()