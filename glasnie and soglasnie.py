glasnie = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
soglasnie = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]


while True:
    print("\n \nВведите слово")
    slovo = input()
    c = tuple(slovo)

    for i in c:
        print (i)
    

    list = []
    d = list.append(i)
    print(list)

    if i in list[0] in glasnie:
        print("Слово начинается с гласной буквы ")

    if i in list[0] in soglasnie:
        print("Слово начинается с согласной буквы")




