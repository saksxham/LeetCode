import pandas as pd

#My first Panda code ever

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # Use a left join to include all persons
    result = person.merge(address, on='personId', how='left')
    
    # Select only the required columns
    return result[['firstName', 'lastName', 'city', 'state']]