import minosites
import sorozat
from helyzet import Helyzet

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

gepek = Helyzet.beolvasas("gep.txt")
Helyzet.gepek_szama(gepek)
Helyzet.atlag(gepek)
Helyzet.legkisebb(gepek)