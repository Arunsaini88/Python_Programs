travel_log = [
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits":6,
        "cities":["Berlin","Hamburg","Stuttgart"]

    },
    
]
# Create a funstion to Add new distionary in list

def  add_new_country(country_vistted,time_visited,citye_visited):
    new_counter = {}
    new_counter["country"] = country_vistted
    new_counter["visited"] = time_visited
    new_counter["cityes"] = citye_visited
    travel_log.append(new_counter)
add_new_country("Russia", 12,["Moscow","Saint Petersburg"])
print(travel_log)