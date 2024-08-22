SQUADS_DATA = [
  [
    "1",
    "GK",
    "Juan Botasso",
    "(1908-10-23)23 October 1908 (aged 21)",
    "",
    "Quilmes",
    "Argentina",
    "Argentina",
    "1930"
  ],
  [
    "9",
    "FW",
    "Roberto Cherro",
    "(1907-02-23)23 February 1907 (aged 23)",
    "",
    "Boca Juniors",
    "Argentina",
    "Argentina",
    "1930"
  ],
  [
    "-",
    "MF",
    "Pierre Braine",
    "(1900-10-26)26 October 1900 (aged 29)",
    "42",
    "Royal Beerschot AC",
    "Belgium",
    "Belgium",
    "1930"
  ],
  [
    "-",
    "MF",
    "Alexis Chantraine",
    "(1901-03-16)16 March 1901 (aged 29)",
    "0",
    "Royal FC Liegeois",
    "Belgium",
    "Belgium",
    "1930"
  ],
  [
    "-",
    "GK",
    "Jean De Bie",
    "(1892-05-09)9 May 1892 (aged 38)",
    "37",
    "Royal Racing Club de Bruxelles",
    "Belgium",
    "Belgium",
    "1930"
  ],
  [
    "-",
    "MF",
    "Oscar",
    "(1991-09-09)9 September 1991 (aged 22)",
    "29",
    "Chelsea",
    "Brazil",
    "England",
    "2010"
  ],
  [
    "-",
    "MF",
    "Paulinho",
    "(1988-07-25)25 July 1988 (aged 25)",
    "25",
    "Tottenham Hotspur",
    "Brazil",
    "England",
    "2010"
  ],
  [
    "-",
    "MF",
    "Hernanes",
    "(1985-05-29)29 May 1985 (aged 29)",
    "23",
    "Internazionale",
    "Brazil",
    "Italy",
    "2014"
  ],
  [
    "-",
    "MF",
    "Luiz Gustavo",
    "(1987-07-23)23 July 1987 (aged 26)",
    "17",
    "VfL Wolfsburg",
    "Brazil",
    "Germany",
    "2014"
  ],
  [
    "-",
    "MF",
    "Fernandinho",
    "(1985-05-04)4 May 1985 (aged 29)",
    "6",
    "Manchester City",
    "Brazil",
    "England",
    "2014"
  ],
  [
    "-",
    "MF",
    "Willian",
    "(1988-08-09)9 August 1988 (aged 25)",
    "5",
    "Chelsea",
    "Brazil",
    "England",
    "2014"
  ],
  [
    "-",
    "FW",
    "Lee Keun-Ho",
    "(1985-04-11)11 April 1985 (aged 29)",
    "62",
    "Sangju Sangmu",
    "South Korea",
    "South Korea",
    "2014"
  ],
  [
    "-",
    "FW",
    "Koo Ja-Cheol",
    "(1989-02-27)27 February 1989 (aged 25)",
    "35",
    "Mainz 05",
    "South Korea",
    "Germany",
    "2014"
  ],
  [
    "-",
    "FW",
    "Kim Shin-Wook",
    "(1988-04-14)14 April 1988 (aged 26)",
    "26",
    "Ulsan Hyundai",
    "South Korea",
    "South Korea",
    "2014"
  ]
]


# 📚 assignment (1)
def players_as_dictionaries(squads_list):
    list_p = []
    keyes_list = ["number","position","name",
                  "date_of_birth","caps","club","country","club_country","year"]
    for i in squads_list:
        dict_p = {}
        indx = 0
        for j in i:
            dict_p[keyes_list[indx]] = j
            indx += 1
        list_p.append(dict_p)
    return list_p
#------------------------------------------------------
# 📚 assignment (2)
def players_by_position(squads_list):
    list_p = players_as_dictionaries(squads_list)
    dict_by_position = {}
    for i in list_p:
        dict_by_position.setdefault(i["position"],[])
        dict_by_position[i["position"]].append(i)
    return dict_by_position
#------------------------------------------------------
# 📚 assignment (3)
def players_by_country_and_position(squads_list):
    list_p = players_as_dictionaries(squads_list)
    dict_by_country = {}
    for i in list_p:
        dict_by_country.setdefault(i["country"],{})
        dict_by_country[i["country"]].setdefault(i["position"], [])
        dict_by_country[i["country"]][i["position"]].append(i)
    return dict_by_country



# Assignment 1
def test_assignment_1():
    result = players_as_dictionaries(SQUADS_DATA)
    assert len(result) == 14

    assert result[0] == {
        'caps': '',
        'club': 'Quilmes',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1908-10-23)23 October 1908 (aged 21)',
        'name': 'Juan Botasso',
        'number': '1',
        'position': 'GK',
        'year': '1930'
    }

    assert result[1] == {
        'caps': '',
        'club': 'Boca Juniors',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1907-02-23)23 February 1907 (aged 23)',
        'name': 'Roberto Cherro',
        'number': '9',
        'position': 'FW',
        'year': '1930'
    }

    assert result[-1] == {
        'caps': '26',
        'club': 'Ulsan Hyundai',
        'club_country': 'South Korea',
        'country': 'South Korea',
        'date_of_birth': '(1988-04-14)14 April 1988 (aged 26)',
        'name': 'Kim Shin-Wook',
        'number': '-',
        'position': 'FW',
        'year': '2014'
    }


# Assignment 2
def test_assignment_2():
    result = players_by_position(SQUADS_DATA)
    assert len(result) == 3  # 3 positions

    goalkeepers = result['GK']
    assert len(goalkeepers) == 2

    assert goalkeepers[0] == {
        'caps': '',
        'club': 'Quilmes',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1908-10-23)23 October 1908 (aged 21)',
        'name': 'Juan Botasso',
        'number': '1',
        'position': 'GK',
        'year': '1930'
    }

    midfielders = result['MF']
    assert len(midfielders) == 8
    assert midfielders[0] == {
        'caps': '42',
        'club': 'Royal Beerschot AC',
        'club_country': 'Belgium',
        'country': 'Belgium',
        'date_of_birth': '(1900-10-26)26 October 1900 (aged 29)',
        'name': 'Pierre Braine',
        'number': '-',
        'position': 'MF',
        'year': '1930'
    }

    forwards = result['FW']
    assert len(forwards) == 4

    assert forwards[0] == {
        'caps': '',
        'club': 'Boca Juniors',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1907-02-23)23 February 1907 (aged 23)',
        'name': 'Roberto Cherro',
        'number': '9',
        'position': 'FW',
        'year': '1930'
    }


# Assignment 3
def test_assignment_3():
    result = players_by_country_and_position(SQUADS_DATA)
    assert len(result) == 4

    expected_countries = {'Argentina', 'Belgium', 'Brazil', 'South Korea'}
    assert set(result.keys()) == expected_countries

    # Argentina
    argentina = result['Argentina']
    assert len(argentina) == 2

    ar_goalkeepers = argentina['GK']
    ar_forwards = argentina['FW']
    assert len(ar_goalkeepers) == 1
    assert len(ar_forwards) == 1

    # Brazil

    brazil = result['Brazil']
    assert len(brazil) == 1  # Only midfielders

    br_midfielders = brazil['MF']
    assert len(br_midfielders) == 6

    assert br_midfielders[0] == {
        'caps': '29',
        'club': 'Chelsea',
        'club_country': 'England',
        'country': 'Brazil',
        'date_of_birth': '(1991-09-09)9 September 1991 (aged 22)',
        'name': 'Oscar',
        'number': '-',
        'position': 'MF',
        'year': '2010'
    }

    assert br_midfielders[-1] == {
        'caps': '5',
        'club': 'Chelsea',
        'club_country': 'England',
        'country': 'Brazil',
        'date_of_birth': '(1988-08-09)9 August 1988 (aged 25)',
        'name': 'Willian',
        'number': '-',
        'position': 'MF',
        'year': '2014'
    }

test_assignment_1()
test_assignment_2()
test_assignment_3()

print("all tests passed!!!")
