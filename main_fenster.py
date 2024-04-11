import tkinter as tk
from tkinter import ttk, END
import sqlite3
from neuer_kunde_fenster import *

# mit "state="readonly"" kann ich nutzereingaben bei entry feldern blockieren

root = tk.Tk()
root.title("Order Flow")
# root.geometry("600x310")

# Erstellen des Notebook Widgets
notebook_widget = ttk.Notebook(root)

# Erstellen der einzelnen Tabs als Frame
kunden_tab = ttk.Frame(notebook_widget)
auftraege_tab = ttk.Frame(notebook_widget)
tab3 = ttk.Frame(notebook_widget)
# Erstellen und hinzufügen der Registerkarten

notebook_widget.add(kunden_tab, text="Kunden")
notebook_widget.add(auftraege_tab, text="Aufträge")
notebook_widget.add(tab3, text="Placeholder")  # Ggf. für Artikel?

# "Expand" & "Fill" sorgen gemeinsam dafür, dass das Notebook Widget die gesamte verfügbare Fläche ausfüllt
notebook_widget.pack(expand=True, fill="both", padx=12, pady=12)

# Hinzufügen des Abschnitts "Kundennummer"
kundennummer_label_frame = ttk.LabelFrame(kunden_tab, text="Kundennummer:")
kundennummer_label_frame.grid(row=0, column=0, pady=5, padx=5, sticky="w")

kundennummer_entry = ttk.Entry(kundennummer_label_frame, width=43)
kundennummer_entry.grid(row=0, column=0, pady=5, padx=5, sticky="w")

# Füge den Default-Text in das Entry-Widget ein
kundennummer_entry.insert(0, "Die Kundennummer wird automatisch generiert!")

# Hinzufügen des Abschnitts "Anschrift"
anschrift_label_frame = ttk.LabelFrame(kunden_tab, text="Anschrift:")
anschrift_label_frame.grid(row=1, column=0, padx=5, pady=5)

# Mit der Option "width" habe ich die "Breite in Zeichen" der Combobox festgelegt
anrede_label = ttk.Label(anschrift_label_frame, text="Anrede:")
anrede_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")
anrede_combobox = ttk.Combobox(
    anschrift_label_frame,
    cursor="hand2",
    state="readonly",
    values=["Herr", "Frau", "Divers"],
    width=17
)
anrede_combobox.grid(row=3, column=0)

vorname_label = ttk.Label(anschrift_label_frame, text="Vorname:")
vorname_label.grid(row=5, column=0, sticky="w", padx=5)
vorname_entry = ttk.Entry(anschrift_label_frame)
vorname_entry.grid(row=6, column=0)

nachname_label = ttk.Label(anschrift_label_frame, text="Nachname:")
nachname_label.grid(row=5, column=1, sticky="w", padx=5)
nachname_entry = ttk.Entry(anschrift_label_frame)
nachname_entry.grid(row=6, column=1)

strasse_label = ttk.Label(anschrift_label_frame, text="Straße:")
strasse_label.grid(row=9, column=0, sticky="w", padx=5)
strasse_entry = ttk.Entry(anschrift_label_frame)
strasse_entry.grid(row=10, column=0)

hausnummer_label = ttk.Label(anschrift_label_frame, text="Hausnummer:")
hausnummer_label.grid(row=9, column=1, sticky="w", padx=5)
hausnummer_entry = ttk.Entry(anschrift_label_frame)
hausnummer_entry.grid(row=10, column=1)

# Die verwendeten Tupel mit "pady" besagen in diesem Fall einen Abstand von "0px" nach oben und von "5px" nach unten
plz_label = ttk.Label(anschrift_label_frame, text="PLZ:")
plz_label.grid(row=13, column=0, sticky="w", padx=5)
plz_entry = ttk.Entry(anschrift_label_frame)
plz_entry.grid(row=14, column=0, pady=(0, 5))

# Die verwendeten Tupel mit "pady" besagen in diesem Fall einen Abstand von "0px" nach oben und von "5px" nach unten
# Die verwendeten Tupel mit "padx" besagen in diesem Fall einen Abstand von "0px" nach links und von "5px" nach rechts
stadt_label = ttk.Label(anschrift_label_frame, text="Stadt:")
stadt_label.grid(row=13, column=1, sticky="w", padx=2)
stadt_entry = ttk.Entry(anschrift_label_frame)
stadt_entry.grid(row=14, column=1, pady=(0, 5), padx=(0, 5))

# Hinzufügen des Abschnitts "kontakt"
kontakt_label_frame = ttk.LabelFrame(kunden_tab, text="Kontaktdaten:")
kontakt_label_frame.grid(row=1, column=1, padx=5, pady=5, sticky="n")

telefon_label = ttk.Label(kontakt_label_frame, text="Telefonnummer:")
telefon_label.grid(row=0, column=0, sticky="w", padx=10)
telefon_entry = ttk.Entry(kontakt_label_frame)
telefon_entry.grid(row=1, column=0)

mobil_label = ttk.Label(kontakt_label_frame, text="Mobilnummer:")
mobil_label.grid(row=2, column=0)
mobil_entry = ttk.Entry(kontakt_label_frame)
mobil_entry.grid(row=3, column=0)

mail_label = ttk.Label(kontakt_label_frame, text="E-Mail")
mail_label.grid(row=4, column=0)
mail_entry = ttk.Entry(kontakt_label_frame)
mail_entry.grid(row=5, column=0)

# Mit "tkinter.BooleanVar()" erstellt amn ein "Variable" die den Status von z.B. Checkboxen (True/False) speichert
checkbox_status = tkinter.BooleanVar()
newsletter_checkbox = ttk.Checkbutton(kunden_tab, text="Newsletter", variable=checkbox_status)
newsletter_checkbox.grid(row=6, column=0, pady=(10, 5))


# Funktionen
def on_click_neuer_kunde():
    neuer_kunde_popup(root)

# def on_click_kunden_suchen():

# def on_click_kunde_ändern():


# Test Buttons
btn1 = ttk.Button(kunden_tab, text="Suchen")
btn1.grid(row=0, column=2)

btn2 = ttk.Button(kunden_tab, text="Ändern")
btn2.grid(row=0, column=3)

btn3 = ttk.Button(kunden_tab, text="Neuer Kunde", command=on_click_neuer_kunde)
btn3.grid(row=0, column=4)

# Sizegrip-Widget hinzufügen
# "relx" bedeutet: Die relative horizontale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil der
# Breite des Elternwidgets (0.0 bedeutet links, 1.0 bedeutet rechts)
# "rely" bedeutet: Die relative vertikale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil der
# Höhe des Elternwidgets (0.0 bedeutet oben, 1.0 bedeutet unten)
sizegrip = ttk.Sizegrip(root)
sizegrip.place(relx=1.0, rely=1.0, anchor="se")

root.mainloop()