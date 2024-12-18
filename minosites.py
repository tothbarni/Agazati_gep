def minosites():
    m_nev = input("Múzeum neve: ")
    l_nev = input("Látogató neve: ")
    ert = int(input("Értékelés: "))
    i = 0
    while(i < 1):
        print("\nI/B:")
        if (1 <= ert <= 20):
            print("Köszönjük az értékelést!")
            i += 1
        elif (ert <= 0):
            print("Az értékelés nem lehet negatív vagy 0!")
            ert = int(input("Értékelés: "))
        elif (ert > 20):
            print("20 pont feletti értékelés nem elfogadható!")
            ert = int(input("Értékelés: "))
