# controller.py - Das ist das Steuerzentrum, das alles koordiniert
import model  # Importiert das Modul, das Aufgaben speichert und verwaltet
import view  # Importiert das Modul, das die Anzeige steuert

# Diese Funktion steuert das gesamte Programm
def hauptprogramm() -> None:  # None: Gibt nichts zurück, führt nur das Menü aus
    while True:  # Eine Endlosschleife, damit das Menü immer wieder angezeigt wird
        view.anzeigenMenue()  # Zeigt das Menü an
        auswahl: str = input("Gib eine Zahl ein: ")  # Holt die Eingabe vom Benutzer
        
        # Hier fügen wir eine neue Aufgabe hinzu
        if auswahl == "1":
            aufgabe: str = input("Was möchtest du erledigen?: ")  # Fragt nach der Aufgabe
            prioritaet: str = input("Wie wichtig ist diese Aufgabe? (hoch/mittel/niedrig): ")  # Fragt nach Priorität
            model.aufgabeHinzufuegen(aufgabe, prioritaet)  # Fügt die Aufgabe zur Datei hinzu
            return
        
        # Hier zeigen wir alle Aufgaben an
        if auswahl == "2":
            aufgaben: list[str] = model.holeAufgaben()  # Holt die Liste der Aufgaben
            view.show_task(aufgaben)  # Zeigt die Liste auf dem Bildschirm
            return
        
        # Hier wird eine Aufgabe als erledigt markiert
        if auswahl == "3":
            aufgaben: list[str] = model.holeAufgaben()  # Holt die Liste der Aufgaben
            view.show_task(aufgaben)  # Zeigt die Liste an
            try:
                index: int = int(input("Welche Aufgabe hast du erledigt? Nummer eingeben: ")) - 1  # Fragt nach der Aufgabe-Nummer
                model.mark_task_done(index)  # Markiert die Aufgabe als erledigt
            except (ValueError, IndexError):
                print("Das hat nicht funktioniert. Bitte eine gültige Zahl eingeben.")  # Falls eine ungültige Nummer eingegeben wird
            return

if __name__ == "__main__":
    hauptprogramm()  # Startet das Hauptprogramm


