ajax = [
    "Heinz Stuy",
    "Ruud Krol",
    "Wim Suurbier",
    "Horst Blankenburg",
    "Barry Hulshoff",
    "Gerrie Mühren",
    "Arie Haan",
    "Johan Neeskens",
    "Sjaak Swart",
    "Johan Cruyff",
    "Dick van Dijk",
    "Johnny Rep",
]

vitesse = [
    "Dick Beukhof",
    "Willy Melchers",
    "Ben Bosma",
    "Nico Kunst",
    "Ben Gerritsen",
    "Willy Veenstra",
    "Bram van Kerkhof",
    "Herman Veenendaal",
    "Co Prins",
    "Theo Rutten",
    "Henk Vleeming",
    "Henk Hofs",
    "John Meeuwsen",
]

ajax_speler_profielen =[]
ajax_lenght = 0
while ajax_lenght < len(ajax):
    ajax_speler_profielen.append({"Full Name": ajax[ajax_lenght], "ID": 123 + ajax_lenght, "Team": "Ajax"})
    ajax_lenght += 1

print(ajax_speler_profielen)

vitesse_speler_profielen =[]
vitesse_lenght = 0
while vitesse_lenght < len(vitesse):
    vitesse_speler_profielen.append({"Full Name": vitesse[vitesse_lenght], "ID": vitesse_lenght, "Team": "Vitesse"})
    vitesse_lenght += 1

print(vitesse_speler_profielen)

doelpunten = [
    {"minuut": 10, "id_scoorende_speler": 7},
    {"minuut": 28, "id_scoorende_speler": 7},
    {"minuut": 32, "id_scoorende_speler": 9},
    {"minuut": 42, "id_scoorende_speler": 9},
    {"minuut": 47, "id_scoorende_speler": 9},
    {"minuut": 49, "id_scoorende_speler": 10},
    {"minuut": 51, "id_scoorende_speler": 10},
    {"minuut": 63, "id_scoorende_speler": 5},
    {"minuut": 70, "id_scoorende_speler": 4},
    {"minuut": 75, "id_scoorende_speler": 19},
    {"minuut": 78, "id_scoorende_speler": 9},
    {"minuut": 81, "id_scoorende_speler": 10},
    {"minuut": 88, "id_scoorende_speler": 7},
]

doelpunten_info = []
alle_spelers = [ajax_speler_profielen, vitesse_speler_profielen]
def pak_doelpunten_info(spelers, doelpunten):
    doelpunten_info.append({"minuut", "speler_naam", "team_naam"})