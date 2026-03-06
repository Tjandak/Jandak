soubor = "polednice.txt"
soubor = "alice.txt"

with open(soubor, "r", encoding="utf-8") as f:
    text = f.read()

slova = text.split()
print("Počet slov v textu:", len(slova))

pocty_slov = {}

for slovo in slova:
    if slovo in pocty_slov:
        pocty_slov[slovo] += 1
    else:
        pocty_slov[slovo] = 1

serazena_slova = sorted(pocty_slov.items(), key=lambda x: x[1], reverse=True)

print("\nNejčastější slova:")
for slovo, pocet in serazena_slova[:10]:
    print(slovo, pocet)

print("\n16-té nejčastější slovo:", serazena_slova[15][0], "s počtem", serazena_slova[15][1])

text_bez_mezer = text.replace(" ", "").replace("\n", "")

pocty_pismen = {}

for pismeno in text_bez_mezer:
    if pismeno in pocty_pismen:
        pocty_pismen[pismeno] += 1
    else:
        pocty_pismen[pismeno] = 1

serazena_pismena = sorted(pocty_pismen.items(), key=lambda x: x[1], reverse=True)

print("\nNejčastější písmena:")
for pismeno, pocet in serazena_pismena[:10]:
    print(pismeno, pocet)

osmipismenna = set()

for slovo in slova:
    if len(slovo) == 8:
        osmipismenna.add(slovo)

print("\nPočet různých osmipísmenných slov:")
print(len(osmipismenna))
