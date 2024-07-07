import tkinter as tk
from tkinter import ttk, END
from tkinter import *
from neuer_kunde_fenster import *
from main_fenster_funktionen import *
from artikel_hinzufügen_fenster import *
from PIL import Image, ImageTk
from fenster_destroy import fenster_destroy

# "PIL" steht für das Modul "Pillow" - mit "pip install Pillow" zu installieren.

mwst_liste = ["7%", "19%"]

root = tk.Tk()
root.title("Order Flow")

img_path = r"Icons\lupe_icon.png"
img = ImageTk.PhotoImage(Image.open(img_path).resize((15, 15)))

# Erstellen des Optionen-Menüs
menue_leiste = Menu(root)
# Zuweisen des Optionen-Menüs zum Root Fenster
root.config(menu=menue_leiste)

# Erstellen Optionen Menü "Gruppen"
# tearoff=0 verhindert das Abtrennen des Menüs
datei_menue = Menu(menue_leiste, tearoff=0)
bearbeiten_menue = Menu(menue_leiste, tearoff=0)
# Mit der Cascade ersten wir eine Art "Gruppe" zur auswahl mehere Optionen z.B. speichern oder öffnen
menue_leiste.add_cascade(label="Datei - Placeholder", menu=datei_menue)
menue_leiste.add_cascade(label="Bearbeiten", menu=bearbeiten_menue)

# Hinzufügen der möglichen Optionen zu der Gruppe, nebst command Befehl
datei_menue.add_command(label="Öffnen - Placeholder")
bearbeiten_menue.add_command(label="Artikel hinzufügen", command=lambda: artikel_hinzufuegen_popup(root, mwst_liste))
bearbeiten_menue.add_command(label="Kunden hinzufügen", command=lambda: neuer_kunde_popup(root))

# Erstellen des Notebook Widgets
notebook_widget = ttk.Notebook(root)

# Erstellen der einzelnen Tabs als Frame
kunden_tab = ttk.Frame(notebook_widget)
auftraege_tab = ttk.Frame(notebook_widget)
artikel_tab = ttk.Frame(notebook_widget)
# Erstellen und hinzufügen der Registerkarten

notebook_widget.add(kunden_tab, text="Kunden")
notebook_widget.add(auftraege_tab, text="Aufträge")
notebook_widget.add(artikel_tab, text="Artikel")  # Ggf. für Artikel?

# "Expand" & "Fill" sorgen gemeinsam dafür, dass das Notebook Widget die gesamte verfügbare Fläche ausfüllt
notebook_widget.pack(expand=True, fill="both", padx=12, pady=12)

"""Kunden Tab"""
# Hinzufügen des Abschnitts "Kundennummer"
kundennummer_label_frame = ttk.LabelFrame(kunden_tab, text="Kundennummer")
kundennummer_label_frame.grid(row=0, column=0, pady=5, padx=5, sticky="w")

kundennummer_entry = ttk.Entry(kundennummer_label_frame, width=36)
kundennummer_entry.grid(row=0, column=0, pady=5, padx=5)

# Hinzufügen des Abschnitts "Anschrift"
anschrift_label_frame = ttk.LabelFrame(kunden_tab, text="Anschrift")
anschrift_label_frame.grid(row=1, column=0, padx=5, pady=5, sticky="w")

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
plz_entry.grid(row=14, column=0, pady=(0, 5), padx=(3, 5))

# Die verwendeten Tupel mit "pady" besagen in diesem Fall einen Abstand von "0px" nach oben und von "5px" nach unten
# Die verwendeten Tupel mit "padx" besagen in diesem Fall einen Abstand von "0px" nach links und von "5px" nach rechts
stadt_label = ttk.Label(anschrift_label_frame, text="Stadt:")
stadt_label.grid(row=13, column=1, sticky="w", padx=2)
stadt_entry = ttk.Entry(anschrift_label_frame)
stadt_entry.grid(row=14, column=1, pady=(0, 5), padx=(0, 5))

# Hinzufügen des Abschnitts "Kontakt"
kontakt_label_frame = ttk.LabelFrame(kunden_tab, text="Kontaktdaten")
kontakt_label_frame.grid(row=1, column=1, padx=5, pady=5, sticky="n")

telefon_label = ttk.Label(kontakt_label_frame, text="Telefonnummer:")
telefon_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
telefon_entry = ttk.Entry(kontakt_label_frame)
telefon_entry.grid(row=1, column=0)

mobil_label = ttk.Label(kontakt_label_frame, text="Mobilnummer:")
mobil_label.grid(row=2, column=0, padx=5, sticky="w")
mobil_entry = ttk.Entry(kontakt_label_frame)
mobil_entry.grid(row=3, column=0)

mail_label = ttk.Label(kontakt_label_frame, text="E-Mail:")
mail_label.grid(row=4, column=0, sticky="w", padx="5")
mail_entry = ttk.Entry(kontakt_label_frame)
mail_entry.grid(row=5, column=0, padx=3)

# Mit "tkinter. BooleanVar()" erstellt amn eine "Variable" die den Status von z.B. Checkboxen (True/False) speichert
checkbox_status = tkinter.BooleanVar()
newsletter_checkbox = ttk.Checkbutton(kontakt_label_frame, text="Newsletter", variable=checkbox_status)
newsletter_checkbox.grid(row=6, column=0, padx=5, pady=(20, 4))

# Steuer Buttons
btn_frame_kunde = ttk.Frame(kunden_tab)
btn_frame_kunde.grid(row=1, column=2)

# Die "lambda" Funktion wird verwendet, um die Parameterübergabe zu ermöglichen.
btn1_kunde = ttk.Button(kundennummer_label_frame, image=img, command=lambda: kunde_suchen(kundennummer_entry, anrede_combobox,
                                                                                          vorname_entry,
                                                                                          nachname_entry, strasse_entry,
                                                                                          hausnummer_entry,
                                                                                          plz_entry, stadt_entry, telefon_entry,
                                                                                          mobil_entry,
                                                                                          mail_entry))
btn1_kunde.grid(row=0, column=1, padx=5)

btn2_kunde = ttk.Button(btn_frame_kunde, text="Ändern", width=15, command=lambda: kunde_aendern(kundennummer_entry,
                                                                                                anrede_combobox,
                                                                                                vorname_entry,
                                                                                                nachname_entry, strasse_entry,
                                                                                                hausnummer_entry,
                                                                                                plz_entry, stadt_entry,
                                                                                                telefon_entry, mobil_entry,
                                                                                                mail_entry))
btn2_kunde.grid(row=6, column=0)

btn3_kunde = ttk.Button(btn_frame_kunde, text="Neuer Kunde", width=15, command=lambda: neuer_kunde_popup(root))
btn3_kunde.grid(row=7, column=0)

btn4_kunde = ttk.Button(btn_frame_kunde, text="Beenden", width=15, command=lambda: fenster_destroy(root))
btn4_kunde.grid(row=8, column=0)

# Platzhalter
plc1_kunde = ttk.Label(btn_frame_kunde, text="")
plc1_kunde.grid(row=0, column=0)

plc2_kunde = ttk.Label(btn_frame_kunde, text="")
plc2_kunde.grid(row=1, column=0)

plc3_kunde = ttk.Label(btn_frame_kunde, text="")
plc3_kunde.grid(row=2, column=0)

plc4_kunde = ttk.Label(btn_frame_kunde, text="")
plc4_kunde.grid(row=3, column=0)

plc5_kunde = ttk.Label(btn_frame_kunde, text="")
plc5_kunde.grid(row=4, column=0)

plc6_kunde = ttk.Label(btn_frame_kunde, text="")
plc6_kunde.grid(row=5, column=0)

"""Aufträge Tab"""

"""Artikel Tab"""
art_nummer_frame = ttk.LabelFrame(artikel_tab, text="Artikelnummer")
art_nummer_frame.grid(row=0, column=0, pady=5, padx=5, sticky="w")
art_nummer_entry = ttk.Entry(art_nummer_frame, width=36)
art_nummer_entry.grid(row=0, column=0, pady=5, padx=5, sticky="w")

art_daten_frame = ttk.LabelFrame(artikel_tab, text="Artikeldaten")
art_daten_frame.grid(row=1, column=0, pady=5, padx=5, sticky="w")

art_bezeichnung = ttk.Label(art_daten_frame, text="Artikel Bezeichnung:")
art_bezeichnung.grid(row=0, column=0, padx=5, sticky="w")
art_bezeichnung_entry = ttk.Entry(art_daten_frame, width=43)
art_bezeichnung_entry.grid(row=1, column=0, padx=5)

art_beschreibung = ttk.Label(art_daten_frame, text="Artikel Beschreibung:")
art_beschreibung.grid(row=2, column=0, padx=5, sticky="w")
art_beschreibung_entry = ttk.Entry(art_daten_frame, width=43)
art_beschreibung_entry.grid(row=3, column=0)

art_lieferant = ttk.Label(art_daten_frame, text="Lieferant:")
art_lieferant.grid(row=4, column=0, padx=5, sticky="w")
art_lieferant_entry = ttk.Entry(art_daten_frame, width=43)
art_lieferant_entry.grid(row=5, column=0, pady=(0, 5))

art_kalkulation_frame = ttk.LabelFrame(artikel_tab, text="Artikelkalkulation")
art_kalkulation_frame.grid(row=1, column=1, pady=5, padx=5, sticky="w")

art_ek = ttk.Label(art_kalkulation_frame, text="Einkaufspreis:")
art_ek.grid(row=0, column=0, padx=5, sticky="w")
art_ek_entry = ttk.Entry(art_kalkulation_frame)
art_ek_entry.grid(row=1, column=0, padx=5)

art_nvk = ttk.Label(art_kalkulation_frame, text="Netto Verkaufspreis:")
art_nvk.grid(row=2, column=0, padx=5, sticky="w")
art_nvk_entry = ttk.Entry(art_kalkulation_frame)
art_nvk_entry.grid(row=3, column=0, padx=5)

art_mwst = ttk.Label(art_kalkulation_frame, text="MwSt. Satz:")
art_mwst.grid(row=4, column=0, padx=5, sticky="w")
art_mwst_combobox = ttk.Combobox(
    art_kalkulation_frame,
    cursor="hand2",
    values=mwst_liste,
    width=17
)
art_mwst_combobox.grid(row=5, column=0, padx=5, pady=(0, 5))

art_gewinn = ttk.Label(art_kalkulation_frame, text="Artikel Gewinn:")
art_gewinn.grid(row=0, column=1, padx=5, sticky="w")
art_gewinn_entry = ttk.Entry(art_kalkulation_frame)
art_gewinn_entry.grid(row=1, column=1)

sum_mwst = ttk.Label(art_kalkulation_frame, text="Summe der MwSt.:")
sum_mwst.grid(row=2, column=1, padx=5, sticky="w")
sum_mwst_entry = ttk.Entry(art_kalkulation_frame)
sum_mwst_entry.grid(row=3, column=1)

art_bvk = ttk.Label(art_kalkulation_frame, text="Brutto Verkaufspreis:")
art_bvk.grid(row=4, column=1, padx=5, sticky="w")
art_bvk_entry = ttk.Entry(art_kalkulation_frame)
art_bvk_entry.grid(row=5, column=1, padx=5, pady=(0, 5))

# Steuer Buttons
btn_frame_artikel = ttk.Frame(artikel_tab)
btn_frame_artikel.grid(row=1, column=2)

btn1_artikel = ttk.Button(art_nummer_frame, image=img)
btn1_artikel.grid(row=0, column=1, padx=5)

btn2_artikel = ttk.Button(btn_frame_artikel, text="Berechnen", width=15, command=lambda: wrapper_mwst_gewinn(art_mwst_combobox,
                                                                                                             art_nvk_entry,
                                                                                                             sum_mwst_entry,
                                                                                                             art_bvk_entry,
                                                                                                             art_gewinn_entry,
                                                                                                             art_ek_entry))
btn2_artikel.grid(row=2, column=0)

btn3_artikel = ttk.Button(btn_frame_artikel, text="Ändern", width=15)
btn3_artikel.grid(row=3, column=0)

btn4_artikel = ttk.Button(btn_frame_artikel, text="Neuer Artikel", width=15, command=lambda: artikel_hinzufuegen_popup(root,
                                                                                                                       mwst_liste))
btn4_artikel.grid(row=4, column=0)

btn5_artikel = ttk.Button(btn_frame_artikel, text="Beenden", width=15, command=lambda: fenster_destroy(root))
btn5_artikel.grid(row=5, column=0)

# Platzhalter
plc1_artikel = ttk.Label(btn_frame_artikel, text="")
plc1_artikel.grid(row=0, column=0)

plc2_artikel = ttk.Label(btn_frame_artikel, text="")
plc2_artikel.grid(row=1, column=0)

# Sizegrip-Widget hinzufügen
# "relx" bedeutet: Die relative horizontale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil der
# Breite des Elternwidgets (0.0 bedeutet links, 1.0 bedeutet rechts)
# "rely" bedeutet: Die relative vertikale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil der
# Höhe des Elternwidgets (0.0 bedeutet oben, 1.0 bedeutet unten)
sizegrip = ttk.Sizegrip(root)
sizegrip.place(relx=1.0, rely=1.0, anchor="se")

root.mainloop()
