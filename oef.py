import mod_progtalen as mp

#toon programmeurs

def toon_namen():
    for x in mp.talenlijst:
        print("naam="+x)
        print(mp.talenlijst.values())


def zoek_taal():

    taal=input("geef programmeertaal in:")
    for key, value in mp.talenlijst.items():
        for x in value:
            if x==taal:
                print("\nProgrammeur:", key)
                print("kan programmeren in " +x)


def del_programmeur():
    naam=input("Welke programmeur wil je verwijderen?")
    if naam in mp.talenlijst:
        mp.talenlijst.pop(naam)
    else:
        print(naam+ "staat niet in de lijst")



def add_taal():
    talen=[]
    addtalen=[]
    taal=""
    janee="j"
    naam=input("bij wie wil je een prog taal toevoegen?")
    if naam in mp.talenlijst:
        talen=mp.talenlijst[naam]
        talen_uitlees=str(talen)
        print(naam+ " kan de talen: "+talen_uitlees)
    else:
        print(naam+" staat niet in de lijst")
        naam = input("bij wie wil je een prog taal toevoegen?")
    while not janee == "n":
        taal=input("welke taal wil je toevoegen (of typ 'stop'):")
        talen.append(taal)
        janee=input("nog een taal invoeren?")
    mp.talenlijst.update({naam : talen })
    talen_uitlees=str(mp.talenlijst[naam])
    print(naam + " kan de talen: " + talen_uitlees)

def add_programmeur():
    talen=[]
    naam = str(input("Naam van toe te voegen programmeur:"))
    naamlengte = len(naam)
    asciilijst = []
    for i in range(naamlengte):
        asciilijst.append(ord(naam[i]))
        for x in asciilijst:
            if x < 65 or x > 90:
                naamkanniet="j"
    if naamkanniet=="j":
        print("de naam bevat tekens, gelieve enkel karakters te gebruiken")
        naam = str(input("Naam van toe te voegen programmeur:"))


    #addtaal = input("Programmeertalen die hij/zij beheerst:")
    janee="j"
    while not janee=="n":
        taal=input("Welke taal beheerst de persoon:")
        talen.append(taal)
        janee=input("wil je nog een taal toevoegen?")
    mp.talenlijst.update({naam : talen})










#menu main programma
def menu():
    print("Maak je keuze:")
    print("1. Toon programmeurs")
    print("2. Toon Programmeurs die bepaalde taal spreken")
    print("3. Verwijder programmeur uit lijst")
    print("4. Voeg taal toe bij programmeur")
    print("5. Voeg programmeur toe aan lijst")

#Main programma
while (True):
    menu()
    keuze = input("Geef uw keuze in of typ 'stop': ")
    if keuze == "1":
        toon_namen()
    elif keuze == "2":
        zoek_taal()
    elif keuze == "3":
        del_programmeur()
    elif keuze == "4":
        add_taal()
    elif keuze == "5":
        add_programmeur()
    elif keuze == 'stop':
        break





