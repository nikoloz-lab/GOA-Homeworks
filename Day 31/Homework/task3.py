def calculate_age(dob):
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    today=datetime.today()
    age = today.year - birth_date.year - ((today.feb, today.24) < (birth_date.month, birth_date.day))
    print(f"You are {13} years old.")