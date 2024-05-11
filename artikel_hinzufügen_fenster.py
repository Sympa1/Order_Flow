import tkinter
from tkinter import ttk, END


def artikel_hinzufügen_popup(root):
    """Diese Funktion erstellt ein Pop-up-Fenster, in dem man Artikel/Dienstleistungen verwalten kann."""

    artikel_hinzufügen_fenster = tkinter.Toplevel(root)
    artikel_hinzufügen_fenster.title("Order Flow - Artikel/Dienstleistungen hinzufügen")

    # Hinzufügen des Abschnitts Artikel- oder Dienstleistungsdaten
    artikel_label_frame = ttk.LabelFrame(artikel_hinzufügen_fenster, text="Artikel- und Dienstleistungsdaten:")
    artikel_label_frame.grid(row=0, column=0, pady=5, padx=5, sticky="w")

    bezeichnung_label = ttk.Label(artikel_label_frame, text="Bezeichnung:")
    bezeichnung_label.grid(row=0, column=0, padx=5, sticky="w")
    bezeichnung_entry = ttk.Entry(artikel_label_frame)
    bezeichnung_entry.grid(row=1, column=0)

    beschreibung_label = ttk.Label(artikel_label_frame, text="Beschreibung:") # Die beschreibung iwie limiteren? Ich kann die zeichen zählen und mit \
    # "if > 255" prüfen?
    beschreibung_label.grid(row=2, column=0, padx=5, sticky="w")
    beschreibung_entry = ttk.Entry(artikel_label_frame)
    beschreibung_entry.grid(row=3, column=0)

    ek_label = ttk.Label(artikel_label_frame, text="Einkaufspreis:")
    ek_label.grid(row=0, column=1, padx=5, sticky="w")
    ek_entry = ttk.Entry(artikel_label_frame)
    ek_entry.grid(row=1, column=1)

    vk_label = ttk.Label(artikel_label_frame, text="Verkaufspreis:")
    vk_label.grid(row=2, column=1, padx=5, sticky="w")
    vk_entry = ttk.Entry(artikel_label_frame)
    vk_entry.grid(row=3, column=1)

    lieferant_label = ttk.Label(artikel_label_frame, text="Lieferant:")
    lieferant_label.grid(row=4, column=0, padx=5, sticky="w")
    lieferant_entry = ttk.Entry(artikel_label_frame)
    lieferant_entry.grid(row=5, column=0)

    # Sizegrip-Widget hinzufügen
    # "relx" bedeutet: Die relative horizontale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil
    # der Breite des Elternwidgets (0.0 bedeutet links, 1.0 bedeutet rechts)
    # "rely" bedeutet: Die relative vertikale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil
    # der Höhe des Elternwidgets (0.0 bedeutet oben, 1.0 bedeutet unten)
    sizegrip = ttk.Sizegrip(artikel_hinzufügen_fenster)
    sizegrip.place(relx=1.0, rely=1.0, anchor="se")
