import json
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code

# Load the data into a list.
filename = 'gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Build a dictionary of GDP data.
cc_gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdps[code] = gdp

# Group the countries GDP into 3 levels.
cc_gdps_1, cc_gdps_2, cc_gdps_3 = {}, {}, {}
for cc, gdp in cc_gdps.items():
    if gdp < 5000000000:
        cc_gdps_1[cc] = round(gdp / 1000000000)
    elif gdp < 50000000000:
        cc_gdps_2[cc] = round(gdp / 1000000000)
    else:
        cc_gdps_3[cc] = round(gdp / 1000000000)

# See how many countries are in each level.
print(len(cc_gdps_1), len(cc_gdps_2), len(cc_gdps_3))

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'World GDP in 2016, by Country (in billions USD)'
wm.add('0-5bn', cc_gdps_1)
wm.add('5bn-50bn', cc_gdps_2)
wm.add('>50bn', cc_gdps_3)

wm.render_to_file('world_gdp.svg')
