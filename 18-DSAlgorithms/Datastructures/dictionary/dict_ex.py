if __name__ == "__main__":
    person_biodata = {
        "name": "Durga",
        "age": 35,
        "contact": "812343443",
        "height": 5.8,
        "address": {}
    }
    #print(person_biodata)
    print(person_biodata['name'])
    print(person_biodata.get('name'))
    print(person_biodata['age'])

    person_biodata['age'] = 38

    print(person_biodata)