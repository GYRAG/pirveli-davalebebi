a = float(input("პირველი გვერდის სიგრძე: "))
b = float(input("მეორე გვერდის სიგრძე: "))
c = float(input("მესამე გვერდის სიგრძე: "))

if a + b > c and b + c > a and c + a > b:
    print("სამკუთხედს აწყობა შესაძლებელია(:")
else:
    print("ეჰ, ვერ ავაწყობთ სამკუთხედს):")
