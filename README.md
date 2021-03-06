# akdif_fridge

von 

Jäch Philipp, Maetz Maximilian & Moosbruger Jakob

## Thema 
3-stündiger Workshop zur Implementierung eines Kühlschranks mittels Python in einem Graphical User Interface. 
Hauptmerkmal: GUI-Programmierung in Python

### Dagstuhldreieck
  
  -> Wie funktioniert das? 
Aus der technologischen Perspektive erfolgt hier ein Wechsel vom Programmieren einer Ausgabe in der Konsole zum Arbeiten mit einem UI. Daher werden zentrale Fragen sein: Welche Möglichkeiten habe ich etwas anzuzeigen? Welche Parameter muss ich verstellen um ein anderes Erscheinungsbild zu bekommen? Welche Möglichkeiten habe ich um meinem Code ein "Gesicht" zu geben? 

  -> Wie wirkt das? 
Aus dieser Perspektive heraus werden sich grundlegende Fragen stellen, wie zum Beispiel das Bearbeiten meinens Codes, das Erscheinungsbild verändert. Der Code welchen wir erschaffen bildet etwas ab, welcher vom User verwendet wird. Ein wichtiger Punkt im Design des eigenen Programms ist nachher, wie wirkt das auf den oder die Benutzer_in? Zeilen die wir schreiben wirken sich sofort auf das Erscheinungsbild aus und die Funktionsweise von eben diesen. 

  -> Wie wird das genutzt? 
Die Implementierung des Kühlschrankes, stellt eine Abbildung der Relität dar. Leitende Fragen zum wirken eben dieser Abbildung stellen sich im Bezug auf Simulationen. Wo werden Simulationen angewandt? Wie werden Simulationen verwendet? Die Erkenntnisse aus der Arbeit mit der, vermeintlich einfachen abbildung eines Kühlschrank und die daraus resultierenden Probleme, können verwendet werden um nachher zu erkennen, wo die Grenzen der Abbildung von Realitäten liegen.  

### REFERENZIMPLEMENTIERUNG: 
**Kühlschrank der auf und zu gemacht wird und Objekte rein und rausgeben kann!**

#### Running

##### Create virtual Environment

```bash
$ python3 -m venv venv
$ source ./venv/bin/activate
```

##### Install requirements
```bash
$ pip install -r requirements.txt
```

##### Run Application

```bash
$ ./main.py
```

# Konzept 

### 1. Zielgruppe  
Wahlfach ab 9. Schulstufe, Lehrplan Informatik 5. Klasse AHS – gültig ab dem Schuljahr 2018/2019

### 2. Kompetenzerwerb
Den Grundkompetenzerwerb des Workshops stellt die Aneignung der Fähigkeit der Erstellung eines Graphical User Interface (GUI) mittels der Programmiersprache Python dar. Diese Kompetenz ist im Lehrplan unter dem Punkt *Praktische Informatik* zu finden. 

    Praktische Informatik
    –	Begriffe und Konzepte der Informatik verstehen und Methoden und Arbeitsweisen anwenden können
    –	Algorithmen erklären, entwerfen, darstellen und in einer Programmiersprache implementieren können
    –	Grundprinzipien von Automaten, Algorithmen, Datenstrukturen und Programmen erklären können
    –	Datenbanken benutzen und einfache Datenmodelle entwerfen können

Wichtig ist hierbei, dass die Schüler_innen die Konzepte eines GUI erkennen, bearbeiten und beschreiben können. Die *10 User Interface Design Guidelines* von Nielsen und Molich dienen als Grundlage für den Prozess. 

Der Workshop kann auch als Lehrplanübergreifend beschrieben werden, da er auch andere wichtige Aspekte abdeckt. Insbesondere Themen des Unterpunktes *Informatik, Mensch & Gesellschaft* können durch die Diskussion des entstandenen Produktes herausgearbeitet werden.

    Informatik, Mensch und Gesellschaft
    – Die Bedeutung von Informatik in der Gesellschaft beschreiben, die Auswirkungen auf die Einzelnen und die Gesellschaft einschätzen und Vor- und Nachteile an konkreten Beispielen abwägen können
    – Maßnahmen und rechtliche Grundlagen im Zusammenhang mit Datensicherheit, Datenschutz und Urheberrecht kennen und anwenden können
    – Die Entwicklung der Informatik beschreiben und bewerten können
    – Informatikberufe und Einsatzmöglichkeiten der Informatik in verschiedenen Berufsfeldern benennen und einschätzen können
    
Der Erfahrung, wie Realität durch Computerprogramme abgebildet werden kann, soll eine Bearbeitung von Fragen über die Bedeutung und Auswirkung von digitaler Simulation in unserer Gesellschaft folgen. 

Weiters werden im Workshop auch Bereiche der *Angewandten Informatik* & *Informatiksysteme* gelehrt. Die Schüler_innen benötigen nämlich diverse Software zur Erstellung des Programmes, Kommunikationstools um den Fortschritt in der Teamarbeit zu besprechen und außerdem Tools zur Bearbeitung eines gemeinsamen Projekts, beispielsweise GitHub.  

### 3. Didaktisches Design
Projektorientierter Unterricht, Plenum, Heterogenität —> Openendedness

Im Geiste des Computational Thinking Konzepts findet eine Kontextualisierung bei der Betrachtung eines Beispielskühlschranks, worauf eine De-Kontextualisierung im Ausarbeiten der allgemeinen Eigenschaften eines Kühlschranks folgt und Re-Kontextualisierung im Zuge der Erarbeitung der Kühlschranksimulation, mit den Mitteln der GUI-Programmierung.

### 4 Vorkenntnisse der Schüler_innen und Verarbeitung von Heterogenität
Programmiervorkenntnisse benötigt.
Die Schüler_innen kennen die Basis-Konzepte und Methoden zur Erstellung eines Programms in der Programmiersprache Python. Grundlegende Konzepte des Programmierens sowie Organisation des eigenen Code sind bekannt. 

Die Heterogenität kann mittels "Openendedness" verarbeitet werden. Die einzelnen Meilensteine des Projekt und die Unterpunkte sind aufbauend für den nächsten, jedoch hat jeder für sich einen breiten Rahmen an Möglichkeiten um erforscht zu werden. Dadurch können Schüler_innen welche schneller voran kommen, anfangen mit dem eigenen Code zu experimentieren währendessen, vermeintlich langsamere Schüler_innen an den Grundsteinen arbeiten. Durch dieses Setting kann die Kreativität der einzelnen gefördert werden. 

<ins>
Je nach Klasse kann das Projekt auch in Gruppen gemacht werden, in dem z.B. Leistungsstärkere SuS mit Leisungsschwächeren SuS in einer Gruppe sind, können diese voneinander lernen.
Die genaue Guppenzusammensetzung und Anzahl an SuS ist jedoch von der Klasse abhängig.
</ins>

### 5 Überprüfung des Kompetenzerwerb
Die Schüler_innen bewerten und diskutieren anhand der *Design Guidelines* die Projekte ihrer Mitschüler_innen. Weiters kann durch die Diskussion der von den Schüler_innen erstellten Projekte eine kritischer Denkprozess angeregt werden, welchen Nutzen Simulationen haben. Ziel ist es, die eigene Abbildung eines Kühlschrank kritisch zu hinterfragen und eventuelle Differenzen zur Realität zu erkennen. In der Diskussion können Themen wie zum Beispiel die Relevanz von realitätsgetreuen Simulationen anhand von realen Beispielen herausgearbeitet werden. (Siehe Simulationen der Corona-Virus-Infektionsraten)

### 6 Gewünschtes Ergebnis aus dem Workshop
Am Ende soll eine fertige Implementation des Kühlschrankmodells vorliegen. Die Schüler_innen sollen im Zuge dieser Implementation die Grundkonzepte der Erstellung und Programmierung eines Graphical User Interface verstehen und ähnliche Programme erstellen können. Auf das Verständnis sowohl der Simulationen, als auch der Richtlinien des Designs nach Nielsen und Molich legen wir wert.

### 7 Meilensteine
    1. Bringe ein grafisches Programm zum Laufen
    2. Der leere Kühlschrank 
    3. Befüllen und entleeren 
    4. Öffnen und Schließen
    5. Ablaufdatum (Datenstruktur erweitern) 
    6. Timer und verderben
    7. Open End
    
### 8 Korrelationen
Jeder Meilenstein für sich bildet ein Modul des End-Programmes. Die einzelnen Meilensteine setzen jedoch den jeweils vorherigen heraus. 
In jeder Phase des Projektes gilt es am Ende ein fertiges Programm zu haben, mit verschiedenen Funktionalitäten, durch diesen Umstand können Meilensteine flexibel an die Bedürfnisse der Schüler_innen angepasst werden und falls benötigt verlängert, oder verkürzt behandelt werden. 

### 9 Welche Materialien, Voraussetzungen werden gebraucht:
     Basic-Wissen über Python
     Rechner 
     Python (https://www.python.org) 
     VS Codium (https://vscodium.com) 
     QT for Python (https://build-system.fman.io/pyqt5-tutorial)
     QT Designer (https://build-system.fman.io/qt-designer-download)
     Installationsguide 


#  Stundenplanung  


| Inhalt | Methode/Material | Zeit | Produkt |
| ------------- | ------------- | ------ | ------------- |
| Begrüßung | | 5 min  | |
| Einführung in Python GUI/Unterschiede zu sequenzbasierten Arbeiten| Vortrag/PPT | 10 min | |
| Installieren der benötigten Software | Guide/Vorzeigen | 30 min | |
| Beispiel Kühlschrank erklären und diskutieren. Was kann ein Kühlschrank? | Diskussion | 15 min | |
| <ins>Grundanforderungen des Programm es erarbeiten. Evtl. mit der Refernzimplementierung arbeiten, falls wenig Input von den SuS kommt.</ins> | Diskussion/Show & Tell/Beamer | 10 min | Anforderungen |
| Erstellung vom "Kühlschrank". Vorzeigen des Codes zur Grundstruktur und Arbeit im QT Designer. | Show & Tell/Beamer | 20 min | Grundgerüst | 
| Die Erarbeitung vom eigenen "Kühlschrank". Struktur erstellen und grafisch implementieren | Gruppen-/ Einzelarbeit. Computer pro Gruppe od. SuS/ Cheatsheet | 40 min | Eigener "Kühlschrank" |
| Pause | | 10 min | Energie | 
| Befüllen des Kühlschranks. Vorzeigen des Codes für Befüllung | Show & Tell/Beamer | 20 min | Methode zum Befüllen | 
| Erstellen einer eigenen Befüllmethode und Entleerung | Gruppen-/ Einzelarbeit. Computer pro Gruppe od. SuS/Cheatsheet | 30 min | "Kühlschrank" mit Grundfunktionalität |
|Vorzeigen der Button-Erstellung und wie man die Datenstruktur erweitert | Show & Tell/Beamer | 10 min | Buttons zum Öffnen und Schließen |
| Selbständiges Erarbeiten einer Datenstruktur und Buttons mit verschiedenen Funktionalitäten | Gruppen-/ Einzelarbeit. Computer pro Gruppe od. SuS/Cheatsheet | Aufgabe zu Hause | "Kühlschrank" mit erweiterter Grundfunkionalität |
| Vorstellen der eigenen Projekte und Diskussion der Ergebnisse | Präsentation/Diskussion | 60 min | |



# Quellen
Lehrplan Informatik 5. Klasse AHS. Abgerufen von https://www.ahs-informatik.com/informatik-5-klasse/
User Interface Design Guidelines: 10 Rules of Thumb. Abgerufen von https://www.interaction-design.org/literature/article/user-interface-design-guidelines-10-rules-of-thumb 
