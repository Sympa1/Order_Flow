import tkinter
from tkinter import ttk, END
from neuer_kunde_funktion import *


def neuer_kunde_popup(root):
    """Diese Funktion erstellt ein Pop-up-Fenster, in dem man einen neuen Kunden Anlegen kann."""
    neuer_kunde_fenster = tkinter.Toplevel(root)
    neuer_kunde_fenster.title("Order Flow - Neuer Kunde")

    # Die Kundendateneingabefelder
    # Hinzufügen des Abschnitts "Kundennummer"
    kundennummer_label_frame = ttk.LabelFrame(neuer_kunde_fenster, text="Kundennummer:")
    kundennummer_label_frame.grid(row=0, column=0, pady=5, padx=5, sticky="w")

    kundennummer_entry = ttk.Entry(kundennummer_label_frame, width=43)
    kundennummer_entry.grid(row=1, column=0, pady=5, padx=5, sticky="w")

    # Füge den Default-Text in das Entry-Widget ein
    kundennummer_entry.insert(0, "Die Kundennummer wird automatisch generiert!")

    # Hinzufügen des Abschnitts "Anschrift"
    anschrift_label_frame = ttk.LabelFrame(neuer_kunde_fenster, text="Anschrift:")
    anschrift_label_frame.grid(row=1, column=0, padx=5, pady=5)

    # Mit der Option "width" habe ich die "Breite in Zeichen" der Combobox festgelegt
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
    kontakt_label_frame = ttk.LabelFrame(neuer_kunde_fenster, text="Kontaktdaten:")
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
    newsletter_checkbox = ttk.Checkbutton(kontakt_label_frame, text="Newsletter", variable=checkbox_status)
    newsletter_checkbox.grid(row=6, column=0, pady=(10, 5))

    # Funktionen zur Übergabe der Werte an "neuer_kunde_funktion.py"
    def on_click_speichern():
        """Speichert die Nutzereingaben als "str" und übergibt diese an die Funktion "neuer_kunde_speichern"."""
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
        neuer_kunde_speichern(anrede, vorname, nachname, strasse, hausnummer, plz, stadt, telefon, mobil, mail, neuer_kunde_fenster)

    def on_click_abbrechen():
        """Übergibt die Variable "neuer_kunde_fenster"."""
        neuer_kunden_fenster_destroy(neuer_kunde_fenster)

    # Hinzufügen der Steuer Buttons
    btn_frame = ttk.Frame(neuer_kunde_fenster)
    btn_frame.grid(row=2, column=1, pady=15, padx=15, sticky="n")

    btn_speichern = ttk.Button(btn_frame, text="Speichern", command=on_click_speichern)
    btn_speichern.grid(row=0, column=0, sticky="n")

    btn_speichern = ttk.Button(btn_frame, text="Abbrechen", command=on_click_abbrechen)
    btn_speichern.grid(row=0, column=1, sticky="n")

    # Sizegrip-Widget hinzufügen
    # "relx" bedeutet: Die relative horizontale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil
    # der Breite des Elternwidgets (0.0 bedeutet links, 1.0 bedeutet rechts)
    # "rely" bedeutet: Die relative vertikale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil
    # der Höhe des Elternwidgets (0.0 bedeutet oben, 1.0 bedeutet unten)
    sizegrip = ttk.Sizegrip(neuer_kunde_fenster)
    sizegrip.place(relx=1.0, rely=1.0, anchor="se")
