from functools import reduce
def result(df):
    composed_function = compose(filter_dataframe_by_subregion,filter_dataframe_by_region, filter_dataframe_by_letter_a)

    result_df = composed_function(df)

    print(result_df.to_markdown(index=False))

def compose(*funcs):
    return lambda initial: reduce(lambda acc, f: f(acc), reversed(funcs), initial)

def filter_dataframe_by_region(dframe):
    print("wybieranie tylko regionu EUROPE")
    filtered_df = dframe[(dframe['Region'] == 'Europe') |(dframe['Region'] == 'Americas') ]
    '''print(dframe.to_markdown(index=False))'''
    return filtered_df

def filter_dataframe_by_letter_a(dframe):
    print("wybieranie tylko państw które zawierają literę a")
    filtered_df = dframe[dframe['Country'].str.lower().str.contains('a')]
    '''print(dframe.to_markdown(index=False))'''
    return filtered_df
def filter_dataframe_by_subregion(dframe):
    print("wybieranie tylko państw które leżą w wschodniej lub środkowej europie lub połudiowej Ameryce")
    filtered_df = dframe[(dframe['Subregion'] == 'Western Europe') | (dframe['Subregion'] == 'Central Europe') | (dframe['Subregion'] == 'South America') ]
    '''print(dframe.to_markdown(index=False))'''
    return filtered_df