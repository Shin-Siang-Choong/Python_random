df = df.loc[:, (df != df.iloc[0]).any()]
