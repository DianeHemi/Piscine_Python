from collections import defaultdict


def howManyMedals(df, name):
    """
    Returns a dictionary of dictionaries giving the number and type of medals
    for each year during which the participant won medals
    The keys of the main dictionary are the Olympic games years. 
    In each year's dictionary, the keys are G, S, B
    corresponding to the type of medals won (gold, silver, bronze). The innermost values
    correspond to the number of medals of a given type won for a given year
    """
    # Garder uniquement le sportif 'name'
    data = df[df['Name'] == name]
    if len(data) == 0:
        return 0
    
    # Trier par annee et avoir nb et type de medaille pour chaque
    years = data['Year'].unique()
    medals = {'G':0, 'S':0, 'B':0}
    ret = {}

    for element in years:
        med = data[data['Year'] == element]['Medal'].value_counts()
        if 'Gold' in med:
            medals['G'] = med['Gold']
            g = med['Gold']
        if 'Silver' in med:
            medals['S'] = med['Silver']
        if 'Bronze' in med:
            medals['B'] = med['Bronze']
        ret[element] = medals
        medals = {'G':0, 'S':0, 'B':0}

    return ret
    
    