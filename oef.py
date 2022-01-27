import mod_progtalen as mp

#toon programmeurs

def toon_namen():
    for x in mp.talen:
        print(x)

toon_namen()



#naam=input("geef naam in")

#print(mp.progtalen.get(naam)["Programmeertalen"])


'''
#filter op taal

filter_dic ={}
filter_rec ={}
teller = 0
zoekterm = input("welke taal")
for key in mp.progtalen.values():
   # print(x)
    if zoekterm is  x["programmeertalen"]:
        teller = teller + 1
        filter_rec.update({teller:{"Naam":x["Naam"],"taal":x["taal"]}})
        filter_dic.update(filter_rec)
    #else:
       #print("taal niet gevonden")
print(filter_dic.values())

for x in mp.progtalen.keys():
    if mp.progtalen[x]["programmeertalen"]==taal:
        print(x)
    else:
        print("taal niet gevonden")
'''

def zoek_taal():

    taal=input("zoek op taal:")
    for key, value in mp.talen.items():

        for x in value:
            if x==taal:
                print("\nProgrammeur:", key)
                print("kan programmeren in " +x)

zoek_taal()


    #if taal in pt.items():
        #print(taal+ " machtig")


    #for key in pt:
        #print(pt.get(key)[taal])
        #if pt.items()==taal:
            #print(taal+ " machtig")
        #print(key + ':', pt[key])
       # else:
           # print(taal+ " niet machtig")