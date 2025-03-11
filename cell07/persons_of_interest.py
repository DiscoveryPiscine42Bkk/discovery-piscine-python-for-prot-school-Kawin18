
def famous_births(persons):

    sorted_persons = sorted(persons.values(), key=lambda x: x['date_of_birth'])
    

    for person in sorted_persons:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

# ตัวอย่างการใช้งาน
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "2007" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "2003" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "2001" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "2025" }
}

# เรียกใช้เมธอด famous_births
famous_births(women_scientists)
