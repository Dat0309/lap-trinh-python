def new_string(str):
    return str if len(str) >= 2 and str[:2] == "Is" else "Is" + str
        