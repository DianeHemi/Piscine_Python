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
    
    # Retirer les competitions sans podium
    data = data.dropna(axis=0, how='any', subset=['Medal'])
    
    
    # Trier par annee et avoir nb et typ de medaille pour chaque
    medals = data['Year']
    print(medals)