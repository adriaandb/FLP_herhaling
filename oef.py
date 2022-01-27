import mod_progtalen as mp

#toon programmeurs
for x in mp.progtalen:
    print(x)




#naam=input("geef naam in")

#print(mp.progtalen.get(naam)["Programmeertalen"])


#filter op taal

filter_dic ={}
filter_rec ={}
teller = 0
zoekterm = input("welke taal")
for x in mp.progtalen.values():
   # print(x)
    if zoekterm is  x["programmeertalen"]:
        teller = teller + 1
        filter_rec.update({teller:{"Naam":x["Naam"],"taal":x["taal"]}})
        filter_dic.update(filter_rec)
    #else:
       #print("taal niet gevonden")
print(filter_dic.values())

'''
for x in mp.progtalen.keys():
    if mp.progtalen[x]["programmeertalen"]==taal:
        print(x)
    else:
        print("taal niet gevonden")
'''
taal=input("zoek op taal:")
for n, pt in mp.progtalen.items():
    print("\nProgrammeur:", n)
    for x in pt:
        print(pt["programmeertalen"])


    #if taal in pt.items():
        #print(taal+ " machtig")


    #for key in pt:
        #print(pt.get(key)[taal])
        #if pt.items()==taal:
            #print(taal+ " machtig")
        #print(key + ':', pt[key])
       # else:
           # print(taal+ " niet machtig")