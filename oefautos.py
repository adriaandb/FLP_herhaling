import mod_autos as ma
from datetime import datetime



log=open("logboek2.txt", "a")
log.close()

def toon_alles(lijst):
    print("Wagenpark:")
    print()
    for key, value in lijst.items():
        print("Auto : "+key)
        for x in value:
            print(x+ " : " +value[x])
        print()

    bericht="De gehele lijst is opgevraagd"
    schrijf_log(bericht)
#-------------------------------

def beschikbaar(lijst):
    print("Beschikbare wagens:")
    print()
    for key, value in lijst.items():
        if value["Verhuurd"]=="nee":
            print("Auto : " + key)
            for x in value:
                print(x + " : " + value[x])
            print()
    bericht="Er is ogevraagd welke autos beschikbaar zijn"
    schrijf_log(bericht)
#-------------------------------

def verhuurd(lijst):
    print("Verhuurde wagens:")
    print()
    for key, value in lijst.items():
        if value["Verhuurd"] == "ja":
            print("Auto : " + key)
            for x in value:
                print(x + " : " + value[x])
            print()

#-------------------------------

def verhuur(lijst):
    #om na te gaan of kenteken wel in lijst staat
    bekend=""
    while not bekend=="j":
        auto_uithuur = input("Welke wagen wil je verhuren (geef kenteken)")
        for x in lijst:
            if auto_uithuur==x:
                bekend = "j"
        else:
            if not bekend=="j":
                print("Kenteken niet bekend")

#status 'verhuurd' veranderen
    for key in lijst:
        if key==auto_uithuur:
            if lijst[auto_uithuur]["Verhuurd"]=="ja":
                print("De", lijst[auto_uithuur]["Merk"], lijst[auto_uithuur]["Model"], "met kenteken", auto_uithuur,
                      "is al verhuurd.")
            else:
                lijst[auto_uithuur]["Verhuurd"]="ja"
                print("De", lijst[auto_uithuur]["Merk"], lijst[auto_uithuur]["Model"], "met kenteken", auto_uithuur,
          "is bij deze verhuurd.")


#-------------------------------


def beschikbaar_maken(lijst):
    bekend = ""
    while not bekend == "j":
        auto_beschikbaar = input("Welke wagen is weer beschikbaar")
        for x in lijst:
            if auto_beschikbaar == x:
                bekend = "j"
        else:
            if not bekend == "j":
                print("Kenteken niet bekend")

    for key in lijst:
        if key == auto_beschikbaar:
            if lijst[auto_beschikbaar]["Verhuurd"] == "Ja":
                lijst[auto_beschikbaar]["Verhuurd"] = "Nee"
                print("De", lijst[auto_beschikbaar]["Merk"], lijst[auto_beschikbaar]["Model"], "met kenteken", auto_beschikbaar,
          "is bij deze weer beschikbaar.")
            else:
                print("De", lijst[auto_beschikbaar]["Merk"], lijst[auto_beschikbaar]["Model"], "met kenteken",
                      auto_beschikbaar,
                      "is al beschikbaar.")

#-------------------------------

def add_auto(lijst):
    nieuwe_auto={}
    addnrplaat=input("geef nummerplaat nieuwe auto in")
    addmerk=input("geef merk nieuwe auto in")
    addmodel=input("geef model nieuwe auto in")
    addbrandstof = input("geef brandstof nieuwe auto in")


    nieuwe_auto={ addnrplaat : {"Merk":addmerk, "Model" : addmodel ,"Brandstof":addbrandstof,"Verhuurd":"nee"}}
    lijst.update(nieuwe_auto)
    print("Nieuwe wagen",addmerk, addmodel, "met kenteken", addnrplaat, "is toegevoegd aan het wagenpark")


#-------------------------------

def del_auto(lijst):
    bekend = ""
    while not bekend == "j":
        nrplaat=input("Geef nummerplaat in van te verwijderen auto")
        for x in lijst:
            if nrplaat == x:
                bekend = "j"
        else:
            if not bekend == "j":
                print("Kenteken niet bekend")

    temp= lijst[nrplaat]
    lijst.pop(nrplaat)
    #print(temp[nrplaat]["Merk"]+temp[nrplaat]["Model"] , "met nummerplaat", nrplaat, "is verwijderd uit het wagenpark")
    print("Auto met nummerplaat", nrplaat , "is verwijderd uit het wagenpark")

#-------------------------------

def schrijf_log(bericht):
    log = open("logboek2.txt", "a")
    now=str(datetime.now())
    log.writelines("\n"+now+" :")
    log.writelines("\n"+"\t"+bericht)
    log.close()






def menu():

    print("1. Toon alle wagens")
    print("2. Toon beschikbare wagens")
    print("3. Verhuurde wagens")
    print("4. Verhuur een wagen")
    print("5. Zet wagen weer als beschikbaar")
    print("6. Voeg een wagen toe ")
    print("7. Verwijder een wagen")


#hoofdprogramma
lijst=ma.autos1
print("Dit is het auto verhuur programma")
while True:
    print("-------------------------------")
    menu()
    keuze=input("Maak een keuze:")
    print("-------------------------------")


    if keuze=="1":
        toon_alles(lijst)
    elif keuze=="2":
        beschikbaar(lijst)
    elif keuze=="3":
        verhuurd(lijst)
    elif keuze=="4":
        verhuur(lijst)
    elif keuze == "5":
        beschikbaar_maken(lijst)
    elif keuze == "6":
        add_auto(lijst)
    elif keuze == "7":
        del_auto(lijst)
    elif keuze=="stop":
        break