def howManyMedalsByCountry(df, country):
    """
    Returns a dictionary of dictionaries giving the number and type of medal
    for each competition where the country delegation earned medals. 
    The keys of the main dictionary are the Olympic games' years. 
    In each year's dictionary, the key are 'G', 'S', 'B' .
    Duplicated medals per team games should be handled and not counted twice.
    """
    # Garder uniquement le pays choisi
    data = df[df['Team'] == country]
    
    
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
    