#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd


def person_a():
    """Reads the data in data/school_performance.csv
    and returns a dataframe with the first 5,000 rows.

    Returns:
    dataframe: containing first 5,000 rows of school_performace.csv
    """
    # Code goes over here.

    df = pd.read_csv("/home/mlbd-2025_fork/data/school_performance.csv")
    
    # Return the first 5,000 rows
    return df.head(5000)

    
    raise NotImplementedError()

def person_b(df):
    """Keeps only the data from the female students. 
    Where the column "gender" equals "female". 

    Parameters:
    df (dataframe): First 5,000 rows of school_performace.csv

    Returns:
    dataframe: Data from the female students
    """
    # Code goes over here.
<<<<<<< HEAD
    return df[df["gender"] == "female"]
=======
    raise NotImplementedError()
>>>>>>> upstream/main


def person_c(df):
    """Calculates the mean from the column "grade"

    Parameters:
    df (dataframe): Data from female students

    Returns:
    float: Mean grade
    """
    return df["grade"].mean()

    raise NotImplementedError()

def main():
    """ Main program """
    # Code goes over here.
    df = person_a()
    df = person_b(df)
    res = person_c(df)

    print(f"Mean grade of female students is {res}")

if __name__ == "__main__":
    main()
