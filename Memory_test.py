import tkinter as tk
import random

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory")

        # Kartenpaare definieren und mischen - 18 Paare für ein 6x6-Feld
        pairs = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:18] * 2 
        random.shuffle(pairs)
        self.cards = pairs

        # Spielfeld und Statusvariablen initialisieren
        self.buttons = []
        self.first_choice = None
        self.revealed_cards = [False] * len(self.cards)

        # Punkteanzeige
        self.score = 0
        self.score_label = tk.Label(master, text=f"Punkte: {self.score}")
        self.score_label.grid(row=6, column=0, columnspan=6)

        # Layout erstellen
        for i in range(20):  # Für ein 6x6 Gitter (36 Elemente)
            btn = tk.Button(master, text='*', width=5, height=2,
                            command=lambda i=i: self.reveal_card(i))
            btn.grid(row=i // 5, column=i % 5) #Durchbrochenes Design
            self.buttons.append(btn)

    def reveal_card(self, index):
        if not self.revealed_cards[index]:
            if self.first_choice is None:
                # Erste Karte aufdecken
                self.first_choice = index
                self.buttons[index].config(text=self.cards[index])
            else:
                # Zweite Karte aufdecken und überprüfen
                second_choice = index
                self.buttons[index].config(text=self.cards[index])

                if self.cards[self.first_choice] == self.cards[second_choice]:
                    # Übereinstimmung gefunden - Punkte erhöhen
                    print("Gefunden: ", self.cards[self.first_choice])
                    self.revealed_cards[self.first_choice] = True
                    self.revealed_cards[second_choice] = True
                    self.score += 1
                    self.update_score()
                    # Reset für den nächsten Zug
                    self.first_choice = None
                else:
                    # Keine Übereinstimmung - verdecken nach kurzer Zeit
                    print("Keine Übereinstimmung.")
                    # Nach der Verzögerung die Karten verdecken und den ersten Wahl zurücksetzen.
                    self.master.after(1000, lambda first=self.first_choice, second=second_choice: self.hide_cards(first, second))

    def hide_cards(self, first_index, second_index):
        # Karten wieder verdecken (kein Match)
        if not self.revealed_cards[first_index]:
            self.buttons[first_index].config(text='*')
        if not self.revealed_cards[second_index]:
            self.buttons[second_index].config(text='*')

        # Nach dem Verstecken den ersten Wahl zurücksetzen.
        self.first_choice = None

    def update_score(self):
        # Aktualisiere die Punkteanzeige im Fenster.
        self.score_label.config(text=f"Punkte: {self.score}")

# Hauptprogramm starten
root = tk.Tk()
game = MemoryGame(root)
root.mainloop()