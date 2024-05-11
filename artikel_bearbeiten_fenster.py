import tkinter
from tkinter import ttk, END


def artikel_bearbeiten_popup(root):
    """Diese Funktion erstellt ein Pop-up-Fenster, in dem man Artikel/Dienstleistungen verwalten kann."""

    artikel_bearbeiten_fenster = tkinter.Toplevel(root)
    artikel_bearbeiten_fenster.title("Order Flow - Artikel/Dienstleistungen verwalten")

    # Sizegrip-Widget hinzufügen
    # "relx" bedeutet: Die relative horizontale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil
    # der Breite des Elternwidgets (0.0 bedeutet links, 1.0 bedeutet rechts)
    # "rely" bedeutet: Die relative vertikale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil
    # der Höhe des Elternwidgets (0.0 bedeutet oben, 1.0 bedeutet unten)
    sizegrip = ttk.Sizegrip(artikel_bearbeiten_fenster)
    sizegrip.place(relx=1.0, rely=1.0, anchor="se")
