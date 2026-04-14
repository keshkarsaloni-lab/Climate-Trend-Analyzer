def yearly_analysis(df):
    """
    Perform yearly temperature analysis
    """

    yearly = df.groupby('year')['temperature'].mean().reset_index()
    return yearly