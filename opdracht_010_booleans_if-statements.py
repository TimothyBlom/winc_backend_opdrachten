regen = True
zonnig = True
overdag = True
koeienBuiten = False
veelWind = False
gierputVol = True
koeienMoetenGemolken = True
herfst = True

koeienBinnen = "Haal de koeien naar binnen"
koeienMelken = "Melk de koeien"
landBemesten = "Bemest het land"
grasMaaien = "Maai het gras voor hooi"

#als de koeien gemolgen moeten worden
print(koeienMelken) if koeienMoetenGemolken and koeienBuiten == False else print(koeienBinnen, "om ze te melken") if koeienBuiten else print()

#als het regent en nacht is
print("de koeien zijn al binnen snachts in de regen") if regen and overdag == False and koeienBuiten else print("het is nacht en het regent, ", koeienBinnen) if regen and overdag == False else print()

#als er veel wind staat
print(koeienBinnen) if veelWind else print()

#gierput vol en het regent
print(koeienBinnen, "om het land te bemesten") if gierputVol and regen and koeienBuiten else print(landBemesten) if gierputVol and regen else print()

#als het herfst is en de zon schijnt moet het gras worden gemaaid
print(koeienBinnen, "om het gras te maaien") if herfst and zonnig and koeienBuiten else print(grasMaaien) if herfst and zonnig else print()

print("breng de koeien naar buiten") if herfst and zonnig else print("koeien zijn al buiten") if koeienBuiten and herfst and zonnig else print()