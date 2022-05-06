variabila = input("Introdu un numar: ")
#este_intreg = int(variabila)
try:
    este_intreg = int(variabila)
except ValueError as e:
    print('eroare de valoare', e)
except Exception as e:
    # print(e.__doc__)   #arata tipul de eroare
    print('A aparut o eroare', e)
finally:
    print('se ruleaza oricum')