def check(sample=[]):
    if empty_data(sample):
        return False
    elif not all_numerics(sample):
        return False
    elif int(sample[0]) < 35 or int(sample[0]) > 75:
        return False
    elif int(sample[1]) != 0 and int(sample[1]) !=1:
        return False
    elif int(sample[2]) != 0 and int(sample[2]) !=1 and int(sample[2]) !=2 and int(sample[2]) !=3:
        return False
    elif int(sample[3]) <= 0:
        return False
    elif int(sample[4]) <= 0:
        return False
    elif int(sample[5]) != 0 and int(sample[5]) !=1:
        return False
    elif int(sample[6]) != 0 and int(sample[6]) !=1 and int(sample[6]) !=2:
        return False
    elif int(sample[7]) <= 0:
        return False
    elif int(sample[8]) != 0 and int(sample[8]) !=1:
        return False
    elif int(sample[9]) < 0:
        return False
    elif int(sample[10]) != 1 and int(sample[10]) !=2 and int(sample[10]) !=3:
        return False
    elif int(sample[11]) < 0:
        return False
    elif int(sample[12]) != 1 and int(sample[12]) !=2 and int(sample[12]) !=3:
        return False
    else:
        return True

def empty_data(sample=[]):
    for i in range(len(sample)):
        if sample[i] == "":
            return True
    return False

def all_numerics(sample=[]):
    for i in range(len(sample)):
        if not sample[i].isnumeric():
            return False
    return True

def error_msg(sample=[]):
    if empty_data(sample):
        return "Faltan datos por introducir."
    elif not all_numerics(sample):
        return "Todas las entradas deben de ser numeros enteros"
    elif int(sample[0]) < 35 or int(sample[0]) > 75:
        return "La edad debe de estar comprendida entre 35 y 75"
    elif int(sample[1]) != 0 and int(sample[1]) !=1:
        return "Sexo debe de ser 0 o 1."
    elif int(sample[2]) != 0 and int(sample[2]) !=1 and int(sample[2]) !=2 and int(sample[2]) !=3:
        return "Tipo de dolor pectoral debe de ser 0, 1, 2 o 3."
    elif int(sample[3]) <= 0:
        return "La tension en reposo debe de ser mayor que 0."
    elif int(sample[4]) <= 0:
        return "El colesterol debe de ser mayor que 0."
    elif int(sample[5]) != 0 and int(sample[5]) !=1:
        return "La glucemia en ayunas debe de ser 0 o 1."
    elif int(sample[6]) != 0 and int(sample[6]) !=1 and int(sample[6]) !=2:
        return "Tipo de dolor pectoral debe de ser 0, 1 o 2."
    elif int(sample[7]) <= 0:
        return "La PPM maximas deben de ser mayores que 0."
    elif int(sample[8]) != 0 and int(sample[8]) !=1:
        return "La angina inducida debe de ser 0 o 1."
    elif int(sample[9]) < 0:
        return "La depresion ST debe de ser mayor o igual que 0."
    elif int(sample[10]) != 1 and int(sample[10]) !=2 and int(sample[10]) !=3:
        return "La pendiente debe de ser 1, 2 o 3."
    elif int(sample[11]) < 0:
        return "El no de vasos mayores debe de ser mayor o igual que 0."
    elif int(sample[12]) != 1 and int(sample[12]) !=2 and int(sample[12]) !=3:
        return "La pendiente debe de ser 1, 2 o 3."
    
    return ""

#print(error_msg(["40","0","0","0","0","0","0","0","0","0","0","0","0"]))