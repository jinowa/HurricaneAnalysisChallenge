# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
updated_damages = []
def update_damages():
    for damage in damages:
        if damage == "Damages not recorded":
            updated_damages.append("Damages not recorded")
        elif "M" in damage:
            updated_damages.append(conversion["M"]*float(damage.strip("M")))
        elif "B" in damage:
            updated_damages.append(conversion["B"]*float(damage.strip("B")))
        else:
            updated_damages.append(float(damage))
    return updated_damages

# test function by updating 
#print(updated_damages)
update_damages()

# 2 
# Create a Table
#print list length function if lists are not equal length used in construct_dict()
listlen = {"length Names": len(names),"length Month": len(months),"length Year": len(years),"length Max Sustained Wind": len(max_sustained_winds),"length Areas Affected": len(areas_affected),"length Damage": len(updated_damages),"length Deaths": len(deaths)} 
def print_listlength():
    for k,v in listlen.items():
        print("{} is {}".format(k,v))

#write your construct hurricane dictionary function here:
hurricanes = {}
hurricanes_by_year  = {}
def construct_dict():
    for i in range(0, len(names)):
        if (len(names) == len(months) == len(years) == len(max_sustained_winds) == len(areas_affected) == len(updated_damages) == len(deaths)):
            hurricanes[names[i]] = {
                "Month": months[i],
                "Year": years[i],
                "Max Sustained Wind": max_sustained_winds[i],
                "Areas Affected": areas_affected[i],
                "Damage": updated_damages[i],
                "Deaths": deaths[i]
                }           
        else:
            print("!!!!!!!ERROR!!!!!!!!!\nChecking length of lists. Lenghts have to be all the same!!!!!")
            print_listlength()
            break    
    return hurricanes

# Create and view the hurricanes dictionary
construct_dict()
print(hurricanes)

# 3
# Organizing by Year
def construct_hurricanes_by_year_dict():
    for i in range(0, len(years)):
        if hurricanes_by_year.get(years[i]) == None: #key entry not available add key
            hurricanes_by_year[years[i]] = [hurricanes[names[i]]]
        else:
            #if key available append list entry from list
            hurricanes_by_year[years[i]].append([hurricanes[names[i]]])
    return hurricanes_by_year

# create a new dictionary of hurricanes with year and key
construct_hurricanes_by_year_dict()
print(hurricanes_by_year)

# 4
# Counting Damaged Areas
print("Hurricans by year List:")
for k,v in hurricanes_by_year.items():
    print("Year: {} List {}\n".format(k,v))

# 5 
# Calculating Maximum Hurricane Count
area_stats = {}
def count_affected_areas():
    for areaslist in areas_affected:
        for area in areaslist:
            if area not in area_stats:
                area_stats[area] = 1
            else:
                area_stats[area] += 1       
    return area_stats
 
count_affected_areas()

# find most frequently affected area and the number of hurricanes involved in
top_affected_area = []
def find_most_affected_areas(area_lst,n):
    for k,v in area_lst.items():
        top_affected_area.append([k,v])
    top_affected_area.sort(key=lambda x : x[1], reverse = True)

    print("\nTop {} list of most affected areas.\n".format(n))
    for area in top_affected_area[:n]:
        print("Hit {hits} times in {area}".format(hits= area[1], area = area[0]))

find_most_affected_areas(area_stats,5) # for maximum n = len(area_stats)

# 6
# Calculating the Deadliest Hurricane
highest_death_list = []
def highest_death_toll():
  #save as list and sort
  for key, reports in hurricanes.items():
    highest_death_list.append([key, reports["Deaths"]])
  highest_death_list.sort(key = lambda x: x[1] ,reverse = True)
  
  print("\n{} was the Hurricane with the highest death toll: {}".format(highest_death_list[0][0], highest_death_list[0][1]))
  return highest_death_list[0]

# find highest mortality hurricane and the number of deaths
highest_death_toll()
# 7
# Rating Hurricanes by Mortality
m_rated_hurricanes = {0:[], 1:[], 2:[], 3:[], 4:[]}
# rated_hurricanes = {
#  mortality rating 0 : [huricanname1, huricanname2, ...], mortality rating 1 : [huricanname1, huricanname2, ...]
#}
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
def rated_hurricanes():
  for cane, reports in hurricanes.items():
    currentcane = cane
    currentdeaths = reports["Deaths"]
# categorize hurricanes in new dictionary with mortality severity as key
    if currentdeaths >= mortality_scale[4]:
      m_rated_hurricanes[4].append(currentcane)
    elif currentdeaths >= mortality_scale[3] and currentdeaths < mortality_scale[4]:      
      m_rated_hurricanes[3].append(currentcane)    
    elif currentdeaths >= mortality_scale[2] and currentdeaths < mortality_scale[3]:
      m_rated_hurricanes[2].append(currentcane)
    elif currentdeaths >= mortality_scale[1] and currentdeaths < mortality_scale[2]:
      m_rated_hurricanes[1].append(currentcane)
    elif currentdeaths >= mortality_scale[0] and currentdeaths < mortality_scale[1]:
      m_rated_hurricanes[0].append(currentcane)
  #print(m_rated_hurricanes)
rated_hurricanes()
for mortality_ratings, m_hurricanes in m_rated_hurricanes.items():
  print("\nMortality rate " + str(mortality_ratings) + "\n")
  [print(hurrican) for hurrican in m_hurricanes]
  

# 8 Calculating Hurricane Maximum Damage
def greatest_damage():
  nameofmaxdamagecane = "Cuba I"
  maxdamage = 0
  for cane, data in hurricanes.items():
    if data["Damage"] != "Damages not recorded":
      if maxdamage < data["Damage"]:
        maxdamage = data["Damage"]
        nameofmaxdamagecane = cane
  print("\nHurricane {} caused ${} of damage.".format(nameofmaxdamagecane,int(maxdamage)))

greatest_damage()
# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000,
                5: "Damages not recorded"}
d_rated_hurricanes = {0:[], 1:[], 2:[], 3:[], 4:[], "Damages not recorded":[]}
# categorize hurricanes in new dictionary with damage severity as key
def rated_damages_hurricanes():
  for cane, reports in hurricanes.items():
    currentcane = cane
    currentdamage = reports["Damage"]
# categorize hurricanes in new dictionary with mortality severity as key
    if currentdamage == "Damages not recorded":
      d_rated_hurricanes["Damages not recorded"].append(currentcane)

    if currentdamage != "Damages not recorded":
      if currentdamage >= damage_scale[4]:
        d_rated_hurricanes[4].append(currentcane)
      elif currentdamage >= damage_scale[3] and currentdamage < damage_scale[4]:      
        d_rated_hurricanes[3].append(currentcane)    
      elif currentdamage >= damage_scale[2] and currentdamage < damage_scale[3]:
        d_rated_hurricanes[2].append(currentcane)
      elif currentdamage >= damage_scale[1] and currentdamage < damage_scale[2]:
        d_rated_hurricanes[1].append(currentcane)
      elif currentdamage >= damage_scale[0] and currentdamage < damage_scale[1]:
        d_rated_hurricanes[0].append(currentcane)
rated_damages_hurricanes()
for damage_ratings, d_hurricanes in d_rated_hurricanes.items():
  print("\nDamage rate " + str(damage_ratings) + "\n")
  [print(hurrican) for hurrican in d_hurricanes]
