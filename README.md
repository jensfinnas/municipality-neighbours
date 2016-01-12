# Neighbour list generator

A Python program to generate csv files with neighbour relations. Primarily to be used with municipalities.


### Install

Install `csvkit`, the only dependecy.

```
    pip install -r requirements.txt
```

### Usage

``` python
from regionlist import RegionList 

munis = RegionList("input/municipalities.csv", "name_short")

munis.as_csv("output/muni_neighbours_by_skl_code.csv", "skl_code")
munis.as_csv("output/muni_neighbours_by_long_name.csv", "name_long")
munis.as_csv("output/muni_neighbours_by_short_name.csv", "name_short")

munis.as_transposed_csv("output/transposed.csv", fields=["name_long", "name_short", "skl_code"])

```

RegionList expects the input csv to have one column namned `neighbours` with a comman separated list of neighbours. The second argument, `key`, is the name of the column to match by.