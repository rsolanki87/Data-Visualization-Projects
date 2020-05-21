import csv
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from country_codes import get_country_code

# Load CO2 emissions data.
filename = 'co-emissions-per-capita.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    cc_emissions = {}
    country_names, years, co2_emiss = [], [], []
    for row in reader:
        country_name = row[0]
        year = row[2]
        co2_emis = float(row[3])
        country_names.append(country_name)
        years.append(year)
        co2_emiss.append(co2_emis)
        code = get_country_code(country_name)
        if code:
            cc_emissions[code] = co2_emis

# Group the countries into 3 emissions levels.
cc_emi_1, cc_emi_2, cc_emi_3 = {}, {}, {}
for cc, emis in cc_emissions.items():
    if emis < 5:
        cc_emi_1[cc] = emis
    elif emis < 10:
        cc_emi_2[cc] = emis
    else:
        cc_emi_3[cc] = emis

# See how many countries are in each level.
print(len(cc_emi_1), len(cc_emi_2), len(cc_emi_3))

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'World CO2 Emissions in 2017, by Country (in metric tons)'
wm.add('0-5t', cc_emi_1)
wm.add('5t-10t', cc_emi_2)
wm.add('>10t', cc_emi_3)

wm.render_to_file('world_co2_emissions.svg')