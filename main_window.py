import tkinter as tk
from tkinter import ttk

mainWindow = tk.Tk()
mainWindow.title("Order Flow")
mainWindow.geometry("600x300")


# Erstellen des Notebook Widget
notebookWidget = ttk.Notebook(mainWindow)
# Erstellen der einzelen Tabs als Frame
tab1 = ttk.Frame(notebookWidget)
tab2 = ttk.Frame(notebookWidget)
tab3 = ttk.Frame(notebookWidget)

# Erstellen und Hinzufügen der Registerkarten 
notebookWidget.add(tab1, text="Kunden")
notebookWidget.add(tab2, text="Placeholder")
notebookWidget.add(tab3, text="Placeholder")

# Expand und Fill sorgen gemeinsam dafür, dass das Notebook Widget die gesamte verfügabre Fläche ausfüllt
notebookWidget.pack(expand=True, fill="both", pady=5, padx=5)


# Hinzufügen des Abschnitts "Anschrift", Kotaktdaten und Bankverbindung
anschriftLabelFrame = ttk.LabelFrame(tab1, text="Anschrift")
anschriftLabelFrame.pack(padx=5, pady=5)

konaktLabelFrame = ttk.LabelFrame(tab1, text="Kontaktdaten")
konaktLabelFrame.pack(padx=5, pady=5)

bvLabelFrame = ttk.LabelFrame(tab1, text="Bankverbindung")
bvLabelFrame.pack(padx=5, pady=5)


# Inhalt des Abschnitts "Anschrift"
kdNrLabel = ttk.Label(anschriftLabelFrame, text="Kundennummer:")
kdNrLabel.grid(row=0, column=0, pady=5, padx=5, sticky="w")
kdNrLabelAusgabe = ttk.Label(anschriftLabelFrame, text="Wird automatisch generiert", background="light gray")
kdNrLabelAusgabe.grid(row=1, column=0, pady=5, padx=5, sticky="w")

# Der sticky="ew"-Parameter sorgt dafür, dass der Separator horizontal erweitert wird und sich an den Seiten des Label-Frames ausrichtet.
# "grid_rowconfigure" defniert eine fixe höhe einer "row". der erste Wert bezieht auf die ausgebwählte Reihe und der zweite Wert auf die Höhe.
separator1 = ttk.Separator(anschriftLabelFrame, orient="horizontal")
separator1.grid(row=2, column=0, columnspan=2, sticky="ew")
anschriftLabelFrame.grid_rowconfigure(2, weight=1)

anredeLabel = ttk.Label(anschriftLabelFrame, text="Anrede:")
anredeLabel.grid(row=3, column=0, pady=5, padx=5)
anredeCombobox = ttk.Combobox(
    anschriftLabelFrame,
    cursor="hand2",
    state="readonly",
    values=["Herr", "Frau", "Divers"]
    )
anredeCombobox.grid(row=4, column=0)

vornameLabel = ttk.Label(anschriftLabelFrame, text="Vorname:")
vornameLabel.grid(row=5, column=0)

vornameEntry = ttk.Entry(anschriftLabelFrame)
vornameEntry.grid(row=6, column=0)


# Sizegrip-Widget hinzufügen
# "relx" bedeutet: Die relative horizontale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil der Breite des Elternwidgets (0.0 bedeutet links, 1.0 bedeutet rechts)
# "rely" bedeutet:  Die relative vertikale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil der Höhe des Elternwidgets (0.0 bedeutet oben, 1.0 bedeutet unten)
sizegrip = ttk.Sizegrip(mainWindow)
sizegrip.place(relx=1.0, rely=1.0, anchor="se")


mainWindow.mainloop()