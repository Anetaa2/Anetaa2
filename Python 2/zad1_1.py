ageQuestion = "Ile masz lat \n ?"

# zapytanie uzytkownika

#pobranie danych

# age = int(input(ageQuestion))

# zadanie dla ciebie zoogluj jak w pythonie znalezc aktualy rok 

# obliczenie i wypisanie na terminal
import datetime
from datetime import datetime
 
month = datetime.now().month
year = datetime.now().year
 
print("Current month: ", month)
print("Current year: ", year)

# userBirthYear = currentYear - userAge 
userAge=int(input("ile masz lat"))
userYear=year-userAge

print("urodziles sie w ",userYear)



