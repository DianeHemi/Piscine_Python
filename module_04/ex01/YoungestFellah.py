def youngestfellah(df, year):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
    df: pandas.DataFrame object containing the dataset.
    year: integer corresponding to a year.
    Returns:
    dct: dictionary with 2 keys for female and male athlete.
    """
    # Garder seulement la bonne annee
    data = df[df['Year'] == year]
    if len(data) == 0:
        return {'f':'nan', 'm': 'nan'}

    M = data.loc[data['Sex'] == 'M']['Age'].min()
    F = data.loc[data['Sex'] == 'F']['Age'].min()
    return {'f':F, 'm': M}