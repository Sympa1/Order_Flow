import tkinter
from tkinter import ttk, END
from artikel_hinzufügen_fenster_funktion import *
from fenster_destroy import *

# Deklaration der MwSt Liste mit Wertzuweisungen als String
mwst_liste = ["7%", "19%"]


def artikel_hinzufuegen_popup(root):
    """Diese Funktion erstellt ein Pop-up-Fenster, in dem man Artikel verwalten kann."""

    artikel_hinzufügen_fenster = tkinter.Toplevel(root)
    artikel_hinzufügen_fenster.title("Order Flow - Artikel hinzufügen")

    # Hinzufügen des Abschnitts Artikel- oder Dienstleistungsdaten
    artikel_label_frame = ttk.LabelFrame(artikel_hinzufügen_fenster, text="Artikel:")
    artikel_label_frame.grid(row=0, column=0, pady=5, padx=5, sticky="w")

    bezeichnung_label = ttk.Label(artikel_label_frame, text="Artikel Bezeichnung:")
    bezeichnung_label.grid(row=0, column=0, padx=5, sticky="w")
    bezeichnung_entry = ttk.Entry(artikel_label_frame)
    bezeichnung_entry.grid(row=1, column=0, padx=5)

    beschreibung_label = ttk.Label(artikel_label_frame, text="Artikel Beschreibung:")
    beschreibung_label.grid(row=2, column=0, padx=5, sticky="w")
    beschreibung_entry = ttk.Entry(artikel_label_frame)
    beschreibung_entry.grid(row=3, column=0, padx=5)

    ek_label = ttk.Label(artikel_label_frame, text="Einkaufspreis:")
    ek_label.grid(row=0, column=1, padx=5, sticky="w")
    ek_entry = ttk.Entry(artikel_label_frame)
    ek_entry.grid(row=1, column=1, padx=5)

    vk_label = ttk.Label(artikel_label_frame, text="Verkaufspreis:")
    vk_label.grid(row=2, column=1, padx=5, sticky="w")
    vk_entry = ttk.Entry(artikel_label_frame)
    vk_entry.grid(row=3, column=1, padx=5)

    lieferant_label = ttk.Label(artikel_label_frame, text="Lieferant:")
    lieferant_label.grid(row=4, column=0, padx=5, sticky="w")
    lieferant_entry = ttk.Entry(artikel_label_frame)
    lieferant_entry.grid(row=5, column=0, padx=5, pady=(0, 5))

    mwst_label = ttk.Label(artikel_label_frame, text="MwSt:")
    mwst_label.grid(row=4, column=1, padx=5, sticky="w")
    mwst_combobox = ttk.Combobox(
        artikel_label_frame,
        cursor="hand2",
        values=mwst_liste,
        width=17
    )
    mwst_combobox.grid(row=5, column=1, padx=5, pady=(0, 5))

    # Hinzufügen der Steuerbuttons "Speichern & Abbrechen"
    btn_frame = ttk.Frame(artikel_hinzufügen_fenster)
    btn_frame.grid(row=1, column=0, padx=5, pady=(0, 5))

    btn_speichern = ttk.Button(btn_frame, text="Speichern",
                               command=lambda: artikel_hinzufuegen(artikel_hinzufügen_fenster, bezeichnung_entry,
                                                                   beschreibung_entry, ek_entry, vk_entry, lieferant_entry,
                                                                   mwst_combobox))
    btn_speichern.grid(row=0, column=0)

    btn_abbrechen = ttk.Button(btn_frame, text="Abbrechen", command=lambda: fenster_destroy(artikel_hinzufügen_fenster))
    btn_abbrechen.grid(row=0, column=1)

    # Sizegrip-Widget hinzufügen
    # "relx" bedeutet: Die relative horizontale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil
    # der Breite des Elternwidgets (0.0 bedeutet links, 1.0 bedeutet rechts)
    # "rely" bedeutet: Die relative vertikale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil
    # der Höhe des Elternwidgets (0.0 bedeutet oben, 1.0 bedeutet unten)
    sizegrip = ttk.Sizegrip(artikel_hinzufügen_fenster)
    sizegrip.place(relx=1.0, rely=1.0, anchor="se")
