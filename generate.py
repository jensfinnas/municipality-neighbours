# encoding: utf-8

from regionlist import RegionList 

munis = RegionList("input/municipalities.csv", "name_short")

munis.as_csv("output/muni_neighbours_by_skl_code.csv", "skl_code")
munis.as_csv("output/muni_neighbours_by_long_name.csv", "name_long")
munis.as_csv("output/muni_neighbours_by_short_name.csv", "name_short")

munis.as_transposed_csv("output/transposed.csv", fields=["name_long", "name_short", "skl_code"])
