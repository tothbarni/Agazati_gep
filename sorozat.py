import random

def sorozat():
    sorozat = []
    for i in range(0, 15):
        szam = random.randint(-90, 501)
        sorozat.append(szam)
    return sorozat

def sorozat2(sorozat):
    sorozat_str:str = ""
    for i in range(0, len(sorozat)-1):
        sorozat_str += str(sorozat[i]) + "*"
    sorozat_str += str(sorozat[len(sorozat)-1])
    return sorozat_str

def tizzeloszthato(sorozat):
    db:int = 0
    for i in range(0, len(sorozat)):
        if (sorozat[i] % 10 == 0):
            db += 1
    return db

def konzolra_ir(db:int):
    print(f"Tízzel osztható számok száma: {db}")

def fajl_ir(db):
    f = open("kimutatas.txt","a")
    f.write(f"II/F:\nTízzel osztható számok száma: {db}.")