# view.py - Hier wird angezeigt, was passiert

def show_task(aufgaben: list[str]) -> None:  # list[str]: Eine Liste mit Aufgaben als Strings
    if not aufgaben:  # Falls keine Aufgaben vorhanden sind
        print("Es gibt keine Aufgaben in der Liste.")  # Zeigt eine Meldung an
        return
    for i, aufgabe in enumerate(aufgaben):  # Durchläuft die Liste der Aufgaben
        print(f"{i + 1}. {aufgabe}")  # Zeigt die Aufgabe mit ihrer Nummer an

# Hier zeigen wir das Hauptmenü an
def anzeigenMenue() -> None:  # None: Gibt nichts zurück, zeigt nur das Menü an
    print("\nWas möchtest du tun?")
    print("1. Eine neue Aufgabe hinzufügen")
    print("2. Alle Aufgaben anzeigen")
    print("3. Eine Aufgabe als erledigt markieren")
    print("4. Eine Aufgabe löschen")
    print("5. Das Programm beenden")
