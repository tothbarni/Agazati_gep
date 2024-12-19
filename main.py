import minosites
import sorozat
import helyzet_tagfuggvenyek
"""
print("I/A:")
minosites.minosites()

print("\nII/A,B:")
sor = sorozat.sorozat()
sorozat_str = sorozat.sorozat2(sor)
print(sorozat_str)

print("\nII/D,E")
db = sorozat.tizzeloszthato(sor)
sorozat.konzolra_ir(db)

#II/F:
sorozat.fajl_ir(db)
"""
gepek = helyzet_tagfuggvenyek.beolvasas("gep.txt")
helyzet_tagfuggvenyek.gepek_szama(gepek)
helyzet_tagfuggvenyek.atlag(gepek)
helyzet_tagfuggvenyek.legkisebb(gepek)