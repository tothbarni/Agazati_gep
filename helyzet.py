class Helyzet:
    def __init__(self, id, hely, tipus, ipcim):
        self.id = int(id)
        self.hely = hely
        self.tipus = tipus
        self.ipcim = ipcim

    def __str__(self):
        return f"ID: {self.id}, Hely: {self.hely}, Típus: {self.tipus}, IP: {self.ipcim}"

def beolvasas(fajlnev):
    gepek = []
    file = open(fajlnev, "r")
    sorok = file.readlines()
    file.close()
    fejléc = sorok[0]
    for i in range(1, len(sorok)):
        id, hely, tipus, ipcim = sorok[i].strip().split("!")
        gepek.append(Helyzet(id, hely, tipus, ipcim))
    return gepek

def gepek_szama(gepek):
    print(f"III/A, B:\nA gépek száma: {len(gepek)}.")

def atlag(gepek):
    paros_taz = []
    for i in range(len(gepek)):
        gep = gepek[i]
        if int(gep.hely[1:]) % 2 == 0:
            paros_taz.append(gep.id)
    if (0 < len(paros_taz)):
        atlag = sum(paros_taz) / len(paros_taz)
        print(f"III/C:\nA páros teremszámú termek azonosító átlaga: {atlag:.2f}.")
    else:
        print("III/C:\nNincs páros teremszámú terem.")

def legkisebb(gepek):
    aszt_gep = []
    for i in range(len(gepek)):
        gep = gepek[i]
        if gep.tipus == "asztali":
            aszt_gep.append(gep)
    if (0 < len(aszt_gep)):
        legkisebb_gep = aszt_gep[0]
        for o in range(len(aszt_gep)):
            gep = aszt_gep[o]
            if (gep.id < legkisebb_gep.id):
                legkisebb_gep = gep
        print(f"III/D:\nA legkisebb asztali gép azonosítója: {legkisebb_gep.id}, helye: {legkisebb_gep.hely}.")
    else:
        print("III/D:\nNincs asztali gép.")