class SpatioTemporalData:
    def __init__(self, df):
        self.df = df
        
    def when(self, location):
        """
        Takes a location as an argument and returns a list containing the
        years where games were held in the given location,
        """
        data = self.df[self.df['City'] == location].drop_duplicates(subset=['Year'])
        return list(data['Year'].values)
        
        
    def where(self, date):
        """
        takes a date as an argument and returns the location where the
        Olympics took place in the given year.
        """
        data = self.df[self.df['Year'] == date]
        if len(data) == 0:
            return None
        
        index = data[data['Event'].str.contains("Olympic")]
        if len(index) == 0:
            index = data[data['Team'].str.contains("Olympic")]
        if len(index) == 0:
            index = data[data['Games'].str.contains("Olympic")]
        if len(index) == 0:
            return None

        index = index.drop_duplicates(subset=['City'])
        return(index['City'].values)

        