# model.py - Hier speichern wir unsere Aufgaben und verwalten sie
from typing import Iterable  # Importiert eine Möglichkeit, Listen von Texten zu verwenden
import os  # Importiert das Betriebssystemmodul, um mit Dateien zu arbeiten

# Das ist die Datei, in der wir unsere Aufgaben speichern
TodoListe: str = "todo.txt"  # str: Eine Zeichenkette (Text), speichert den Dateinamen

# Diese Funktion schreibt einen Text in eine Datei und überschreibt alles darin
def speichernDateiInhalt(pfad: str, daten: str) -> None:  # str: Datei-Pfad, str: Inhalt, None: Gibt nichts zurück
    with open(pfad, "w+") as datei:  # Öffnet die Datei im Schreibmodus
        datei.write(daten)  # Schreibt den gegebenen Text in die Datei

# Diese Funktion speichert eine Liste von Textzeilen in einer Datei
def speichernZeilenListe(pfad: str, daten: Iterable[str]) -> None:  # Iterable[str]: Eine Sammlung von Zeichenketten
    with open(pfad, "w+") as datei:  # Öffnet die Datei im Schreibmodus
        datei.writelines(daten)  # Schreibt jede Zeile aus der Liste in die Datei

# Diese Funktion liest den gesamten Inhalt einer Datei und gibt ihn als Zeichenkette zurück
def ladenDateiInhalt(pfad: str) -> str:  # str: Gibt den gesamten Dateiinhalt als Zeichenkette zurück
    with open(pfad, "r") as datei:  # Öffnet die Datei im Lesemodus
        return datei.read()  # Liest den gesamten Inhalt der Datei und gibt ihn zurück

# Diese Funktion liest alle Zeilen einer Datei und gibt sie als Liste von Zeichenketten zurück
def ladenZeilenListe(pfad: str) -> list[str]:  # list[str]: Eine Liste von Zeichenketten
    with open(pfad, "r") as datei:  # Öffnet die Datei im Lesemodus
        return datei.readlines()  # Liest alle Zeilen der Datei und gibt sie als Liste zurück

# Hier holen wir uns die Liste der Aufgaben aus der Datei
def holeAufgaben() -> list[str]:  # list[str]: Gibt eine Liste von Aufgaben (als Strings) zurück
    if not os.path.exists(TodoListe):  # Prüft, ob die Datei existiert
        return []  # Falls nicht, wird eine leere Liste zurückgegeben
    return ladenZeilenListe(TodoListe)  # Liest die Datei und gibt die Aufgaben zurück

# Diese Funktion speichert die aktuelle Aufgabenliste
def aktualisierenAufgaben(aufgaben: Iterable[str]) -> None:  # Iterable[str]: Eine Sammlung von Zeichenketten
    speichernZeilenListe(TodoListe, aufgaben)  # Speichert die aktualisierte Liste in die Datei

# Hier fügen wir eine neue Aufgabe zur Liste hinzu
def aufgabeHinzufuegen(aufgabe: str, prioritaet: str = "mittel") -> None:  # str: Die Aufgabe, str: Die Priorität
    with open(TodoListe, "a", encoding="utf-8") as datei:  # Öffnet die Datei im Anhangmodus
        datei.write(f"[ ] {aufgabe} ({prioritaet})\n")  # Fügt eine neue Aufgabe mit Priorität hinzu

# Diese Funktion markiert eine Aufgabe als erledigt
def mark_task_done(index: int) -> None:  # int: Die Position der Aufgabe in der Liste
    aufgaben: list[str] = holeAufgaben()  # Holt die aktuelle Liste der Aufgaben
    if 0 <= index < len(aufgaben):  # Prüft, ob die eingegebene Nummer gültig ist
        aufgaben[index] = aufgaben[index].replace("[ ]", "[X]", 1)  # Ersetzt das Kästchen mit "[X]"
        aktualisierenAufgaben(aufgaben)  # Speichert die geänderte Liste

# Hier wird eine Aufgabe aus der Liste gelöscht
def aufgabeLoeschen(index: int) -> None:  # int: Die Position der zu löschenden Aufgabe
    aufgaben: list[str] = holeAufgaben()  # Holt die aktuelle Liste der Aufgaben
    if 0 <= index < len(aufgaben):  # Prüft, ob die eingegebene Nummer gültig ist
        del aufgaben[index]  # Löscht die gewählte Aufgabe
        aktualisierenAufgaben(aufgaben)  # Speichert die neue Liste
