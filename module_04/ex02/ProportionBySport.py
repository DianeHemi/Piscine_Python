def proportionBySport(df, year, sport, gender):
    """
        Returns a float corresponding to the proportion (%) of participants who played 
        the given sport among the participants of the given gender.
        The function answers questions like the following: 
            "What was the percentage of female basketball players among 
            all the female participants of the 2016 Olympics?"
        Raise no exceptions
    """
    # Return only one column : df['Col'] / df[["Col1", "Col2"]]
    
    # Garder seulement la bonne annee et le bon genre
    data = df[(df['Year'] == year) & (df['Sex'] == gender)]
    if len(data) == 0:
        return 0
    
    #Retirer doublons
    data = data.drop_duplicates(subset=['Name'])
    
    nb = data[data['Sport'] == sport]
    return (nb.shape[0] / data.shape[0])


    
    
    