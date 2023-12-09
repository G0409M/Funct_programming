from functools import reduce
def result(df):
    compose(filter_dataframe_by_letter_a(df),filter_dataframe_by_region(df))


def compose(*funcs):
    return lambda initial: reduce(lambda acc, f: f(acc), reversed(funcs), initial)

def filter_dataframe_by_region(dframe):
    print("wybieranie tylko regionu EUROPE")
    filtered_df = dframe[dframe['Region'] == 'Europe']
    dframe= filtered_df
    print(dframe.to_markdown(index=False))

def filter_dataframe_by_letter_a(dframe):
    print("wybieranie tylko państw które zawierają literę a")
    filtered_df = dframe[dframe['Country'].str.lower().str.contains('a')]
    dframe= filtered_df
    print(dframe.to_markdown(index=False))