import datetime
def check_cnp(cnp: str) -> bool:
    if len(cnp) != 13 or not cnp.isnumeric():
        return False
    if int(cnp[0]) not in range(1, 10):
        return False
    date_string = cnp[1:3] + '-' + cnp[3:5] + '-' + cnp[5:7]
    try:
        datetime.datetime.strptime(date_string, "%y-%m-%d")
    except ValueError:
        return False
    if int(cnp[7:9]) not in range(1, 47) and int(cnp[7:9]) not in range(51, 53):
        return False
    if int(cnp[9:12]) not in range(1, 1000):
        return False
    cnp2 = '279146358279'
    suma = 0
    for i in range(len(cnp) - 1):
        suma += int(cnp[i]) * int(cnp2[i])
    c = 1 if suma % 11 == 10 else suma % 11
    if int(cnp[-1]) != c:
        return False
    return True
def date_print(cnp: str) -> None:
    if int(cnp[0]) == 9:
        print("Sexul: Unknown")
    elif int(cnp[0]) % 2 != 0:
        print("Sexul: M")
    else:
        print("Sexul: F")
    date_string = cnp[1:3] + cnp[3:5] + cnp[5:7]
    print("Data de nastere: ", datetime.datetime.strptime(date_string, "%y%m%d").date())
    return
def main():
    cnp = input("Introduceti cnp-ul: ")
    # cnp = '5010201191480'
    msg = "cnp-ul: " + cnp + " nu este valid"
    if check_cnp(cnp):
        msg = "cnp-ul " + cnp + " este valid"
    print(msg)
    if check_cnp(cnp):
        date_print(cnp)
if __name__ == "__main__":
    main()