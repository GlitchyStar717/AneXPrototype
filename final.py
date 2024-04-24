# %%
#IMport necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
#import the smartphone data
df = pd.read_csv('./smartphone_cleaned_v5.csv')
df.head()

# %%
#Pre=Processing
df.sort_values(by='model',ascending=True,inplace=True)
df["SN"] = list(range(len(df.index)))
df=df.set_index('SN')

#Remove the NA values   
df =df.ffill(axis=0)
#Remove the errors where no memory slot but the NA filling method has given storage
df['extended_upto'] = np.where(df['extended_memory_available']==0,0,df['extended_upto'])
df.fillna({'fast_charging':22},inplace=True) #ffill didn't work for iphone 11 and iphone 11 pro in the 1st run of code. so it manually for 2 mobiles
df.fillna({'extended_upto':0},inplace=True) #ffill didn't work for iphone 11 and iphone 11 pro in the 1st run of code. so it manually for 2 mobiles
df.info()

# %%
# pre-processing
df2= df.copy()
#price
category = 'price'
p1 = np.percentile(df[category],1)
p2 = np.percentile(df[category],99)
df2.query(f"{category} >= {p1} and {category} <= {p2}",inplace=True)

# #refresh_rate
# category = 'refresh_rate'
# p1 = np.percentile(df2[category],10)
# p2 = np.percentile(df2[category],90)
# df2 = df2.query(f"{category} >= {p1} and {category} <= {p2}")

#resolution
#convert to number
def evaluate_resolution(expression):
    try:
        # Replace special characters and evaluate the expression
        expression = expression['resolution'].replace(" ", "").replace("x", "*")
        return eval(expression)
        
    except Exception as e:
        # Handle any errors that occur during evaluation
        print(f"Error evaluating expression '{expression}': {e}")
        return False

# Apply the function and assign the result to a new column
df2['pixels'] = df2.apply(evaluate_resolution, axis=1)

df2.info()
print(df2)

#filter resolution
# category = 'pixels'
# p1 = np.percentile(df2[category],1)
# p2 = np.percentile(df2[category],100)
# df2 = df2.query(f"{category} >= {p1} and {category} <= {p2}")

# sorted(df2['price'].unique())
# df2.query("refresh_rate < 80")


# %%
#Another method (not recommended) for finding the quartiles, doesn't take into account the volumes of mobiles having the value. only takes into account the values.

# #defining the ceiling
# max_cores = max(df2["num_cores"].unique())
# max_speed = max(df2["processor_speed"].unique())
# max_ram = max(df2["ram_capacity"].unique())
# max_price = max(df2["price"].unique())
# max_rear = max(df2["primary_camera_rear"].unique())
# max_front = max(df2["primary_camera_front"].unique())
# max_resolution = max(df2["pixels"].unique())
# max_refresh = max(df2["refresh_rate"].unique())

# max_specs = [max_cores,max_speed,max_ram,max_price,max_rear,max_front,max_front,max_resolution,max_refresh]

# #defining the ceilings
# q1_cores = np.percentile(df['num_cores'].unique(),25)
# q1_speed = np.percentile(df2["processor_speed"].unique(),25)
# q1_ram = np.percentile(df2["ram_capacity"].unique(),25)
# q1_price = np.percentile(df2["price"].unique(),25)
# q1_rear = np.percentile(df2["primary_camera_rear"].unique(),25)
# q1_front = np.percentile(df2["primary_camera_front"].unique(),25)
# q1_resolution = np.percentile(df2["pixels"].unique(),25)
# q1_refresh = np.percentile(df2["refresh_rate"],25)

# q1_specs = [q1_cores,q1_speed,q1_ram,q1_price,q1_rear,q1_front,q1_front,q1_resolution,q1_refresh]

# #defining the ceiling
# q2_cores = np.percentile(df2["num_cores"].unique(),50)
# q2_speed = np.percentile(df2["processor_speed"].unique(),50)
# q2_ram = np.percentile(df2["ram_capacity"].unique(),50)
# q2_price = np.percentile(df2["price"].unique(),50)
# q2_rear = np.percentile(df2["primary_camera_rear"].unique(),50)
# q2_front = np.percentile(df2["primary_camera_front"].unique(),50)
# q2_resolution = np.percentile(df2["pixels"].unique(),50)
# q2_refresh = np.percentile(df2["refresh_rate"],50)

# q2_specs = [q2_cores,q2_speed,q2_ram,q2_price,q2_rear,q2_front,q2_front,q2_resolution,q2_refresh]

# #defining the ceiling
# q3_cores = np.percentile(df2["num_cores"].unique(),75)
# q3_speed = np.percentile(df2["processor_speed"].unique(),75)
# q3_ram = np.percentile(df2["ram_capacity"].unique(),75)
# q3_price = np.percentile(df2["price"].unique(),75)
# q3_rear = np.percentile(df2["primary_camera_rear"].unique(),75)
# q3_front = np.percentile(df2["primary_camera_front"].unique(),75)
# q3_resolution = np.percentile(df2["pixels"].unique(),75)
# q3_refresh = np.percentile(df2["refresh_rate"],75)

# q3_specs = [q3_cores,q3_speed,q3_ram,q3_price,q3_rear,q3_front,q3_front,q3_resolution,q3_refresh]
# q1_specs,q2_specs,q3_specs,max_specs

# %%
#defining the ceiling
max_cores = max(df2["num_cores"].unique())
max_speed = max(df2["processor_speed"].unique())
max_ram = max(df2["ram_capacity"].unique())
max_price = max(df2["price"].unique())
max_rear = max(df2["primary_camera_rear"].unique())
max_front = max(df2["primary_camera_front"].unique())
max_resolution = max(df2["pixels"].unique())
max_refresh = max(df2["refresh_rate"].unique())
max_battery = max(df2["battery_capacity"].unique())
max_charging = max(df2["fast_charging"].unique())


max_specs = [max_cores,max_speed,max_ram,max_price,max_rear,max_front,max_resolution,max_refresh,max_battery,max_charging]

#defining the ceilings
q1_cores = np.percentile(df2['num_cores'],25)
q1_speed = np.percentile(df2["processor_speed"],25)
q1_ram = np.percentile(df2["ram_capacity"],25)
q1_price = np.percentile(df2["price"],25)
q1_rear = np.percentile(df2["primary_camera_rear"],25)
q1_front = np.percentile(df2["primary_camera_front"],25)
q1_resolution = np.percentile(df2["pixels"],25)
q1_refresh = np.percentile(df2["refresh_rate"],25)
q1_battery = np.percentile(df2["battery_capacity"],25)
q1_charging = np.percentile(df2["fast_charging"],25)

q1_specs = [q1_cores,q1_speed,q1_ram,q1_price,q1_rear,q1_front,q1_resolution,q1_refresh,q1_battery,q1_charging]

#defining the ceiling
q2_cores = np.percentile(df2["num_cores"],50)
q2_speed = np.percentile(df2["processor_speed"],50)
q2_ram = np.percentile(df2["ram_capacity"],50)
q2_price = np.percentile(df2["price"],50)
q2_rear = np.percentile(df2["primary_camera_rear"],50)
q2_front = np.percentile(df2["primary_camera_front"],50)
q2_resolution = np.percentile(df2["pixels"],50)
q2_refresh = np.percentile(df2["refresh_rate"],50)
q2_battery = np.percentile(df2["battery_capacity"],50)
q2_charging = np.percentile(df2["fast_charging"],50)

q2_specs = [q2_cores,q2_speed,q2_ram,q2_price,q2_rear,q2_front,q2_resolution,q2_refresh,q2_battery,q2_charging]

#defining the ceiling
q3_cores = np.percentile(df2["num_cores"],75)
q3_speed = np.percentile(df2["processor_speed"],75)
q3_ram = np.percentile(df2["ram_capacity"],75)
q3_price = np.percentile(df2["price"],75)
q3_rear = np.percentile(df2["primary_camera_rear"],75)
q3_front = np.percentile(df2["primary_camera_front"],75)
q3_resolution = np.percentile(df2["pixels"],75)
q3_refresh = np.percentile(df2["refresh_rate"],75)
q3_battery = np.percentile(df2["battery_capacity"],75)
q3_charging = np.percentile(df2["fast_charging"],75)

q3_specs = [q3_cores,q3_speed,q3_ram,q3_price,q3_rear,q3_front,q3_resolution,q3_refresh,q3_battery,q3_charging]
q1_specs,q2_specs,q3_specs,max_specs

# %%
 
def categorize_phone(row):
    condition_apple = 7 if row["brand_name"] == 'apple' else 0 #Apple's smooth and more fluid for same theoritical specs. So, adjusting
    condition_fast_processor = (7 + 3*(row['processor_speed']-q2_speed)/(max_speed-q2_speed)) if row['processor_speed']>=q2_speed else 7*row['processor_speed']/q2_speed
    condition_ram = (9 + 1*(row['ram_capacity']-q3_ram)/(max_ram-q3_ram)) if row['ram_capacity']>=q3_ram else 9*row['ram_capacity']/q3_ram  
    condition_fluid_display = (7 + 3*(row['refresh_rate']-q3_refresh)/(max_refresh-q3_refresh)) if row['refresh_rate']>=q3_refresh else 7*row['refresh_rate']/q3_refresh
    condition_many_cores = row["num_cores"]*10/max_cores
    condition_nfc = 5 if row["has_nfc"]==True  else 0
    condition_5g=5 if row["has_5g"]==True else 0
    condition_resolution = (7 + 4*(row['pixels']-q3_resolution)/(max_resolution-q3_resolution)) if row['pixels']>=q3_resolution else 7*row['pixels']/q3_resolution
    total = condition_5g+condition_fluid_display +  condition_fast_processor + condition_ram + condition_nfc + condition_many_cores +condition_resolution+condition_apple
    if total > 50: return "flagship"
    elif total >40: return "midrange"
    else: return "average"
    # no_of_conditions_satisfied = condition_5g.astype(int)+condition_fluid_display.astype(int) +  condition_fast_processor.astype(int) + condition_nfc.astype(int) + condition_many_cores.astype(int) +condition_resolution.astype(int)
    
def categorize_camera(row):
    if row["phone_category"] == "flagship":
        c1 = 10
    elif row["phone_category"] == "midrange":
        c1 = 8
    else:
        c1 = 5

    c2 = (9 + (row["primary_camera_rear"]-12)/(max_rear-12)) if row["primary_camera_rear"] > 12 else 9*row["primary_camera_rear"]/12
    c3 = (9 + (row["primary_camera_front"]-12)/(max_front-12)) if row["primary_camera_front"] > 10 else 9*row["primary_camera_front"]/10
    
    brand_quality = {'apple':2.5, 'google':2.5, 'samsung':1.5,'huawei':1.5}
    c4 = brand_quality[row['brand_name']] if row["brand_name"] in brand_quality else 0

    total = 10 + 10 + 10 + 2 # sum of maximum of c1 + c2 + c3 + c4
    rating = (c1+c2+c3+c4)*10.0/total
    return rating
    
def categorize_performance(row):
    c1 = row["processor_speed"]*10/max_speed
    c2 = row["num_cores"]*10/max_cores
    c3 = (7 + 3*(row['ram_capacity']-q3_ram)/(max_ram-q3_ram)) if row['ram_capacity']>=q3_ram else 7*row['ram_capacity']/q3_ram  
    c4 = 5 if row["brand_name"] == 'apple' else 0 #Apple's bionic processors usually outperform android's chips with far more memory
    
    total = 10 + 10 + 10 + 5
    rating = (c1+c2+c3+c4)*10.0/total
    return rating

# %%
df2['phone_category'] = df2.apply(categorize_phone, axis=1)
df2['camera_ratings'] = df2.apply(categorize_camera, axis=1)
df2['performance_ratings'] = df2.apply(categorize_performance, axis=1)

df2


# %%
#Defining more parameters
#defining the ceiling
max_camera = max(df2["camera_ratings"].unique())
max_performance = max(df2["performance_ratings"].unique())


max_specs.append(max_camera)
max_specs.append(max_performance)

#defining the ceilings
q1_camera = np.percentile(df2['camera_ratings'],25)
q1_performance = np.percentile(df2['performance_ratings'],25)


q1_specs.append(q1_camera)
q1_specs.append(q1_performance)

#defining the ceiling
q2_camera = np.percentile(df2["camera_ratings"],50)
q2_performance = np.percentile(df2["performance_ratings"],50)


q2_specs.append(q2_camera)
q2_specs.append(q2_performance)

#defining the ceiling
q3_camera = np.percentile(df2["camera_ratings"],75)
q3_performance = np.percentile(df2["performance_ratings"],75)


q3_specs.append(q3_camera)
q3_specs.append(q3_performance)


q1_specs,q2_specs,q3_specs,max_specs


# %%
#Input Questions for recommendation

stage1 = [
    'How do you want to get recommendation?  :  ',
    'Entering your own phrase  :  ',
    'Get your questions asked  :  '
]

exact_questions = [
    '1.) IPhone 2.) Android 3.)Open to both  :  ',
    "Do you want a particular smartphone brand? \n1.) No 2.) Yes (We will ask your to input your brand later)  :  ",
    'What screen size would you prefer? \n1.) below 6.1" 2.) between 6.1" & 6.6" 3.) above 6.6" 4.) Doesn\'t matter  :  ',
    'Do you want your phone to have 5g? \n1.) Yes 2.) No 3.) Any  :  ',
    'What is your budget range Example (inside the "") "45000-50000"?  :  '
]
performance_questions = [
    'Do you frequently play games on your smartphone? (y/n)  :  ',
    'Do you use a lot of apps? (y/n)  :  ',
    'Do you want to take high quality photos and videos (y/n)  :  ',
    'Do you wish to use your smartphone for over 5 years? (y/n)  :  ',
    'Do you wish to have all new features in your smartphone? (y/n)  :  '
]
camera_questions = [
    # 'Do you want to take high quality photos and videos? (y/n)  :  ', #Qn 8
    'Do you want a camera that shoot good in night time? (y/n)  :  ',
    'Would you love to shoot zoom and potrait shots? (y/n)  :  ',
    'Do you want to shoot many videos? (y/n)  :  ',
    'Do you want to shoot many photos? (y/n)  :  '
]
software_questions = [
    'Do you want to get new updates for 5+ years? (y/n)  :  ',
    "Do you mind useless apps pre-installed in your smartphone? (y/n)  :  ",
    'Do you like to have easy software support? (y/n)',
    'Can you distinguish between smooth and non smooth animation? (y/n)  :  '
]
display_questions = [
    #'Do you frequently play games on your smartphone? (y/n)  :  ', #Qn 6
    'Do you do a lot of scrolling? (y/n)  :  ',
    "Do you like watching movies in mobile? (y/n)  :  ",
    'Do you consume a lot of media like youtube and more? (y/n)  :  ',
    'Do you wish to use phone a lot on sunlight? (y/n)  :  '
]
storage_questions = [
    # "Do you take a lot of photos and videos? (y/n)  :  ", # Qn 13 and 14
    'Do you store a lot of offline medias like movies or other files in smartphones? (y/n)  :  ',
    "Do you want your smartphone to be able to store everything you want for years to come? (y/n)  :  ",
    'Do you want to transfer from and to your smartphones quickly? (y/n)  :  ',
    'Do you download a lot of apps or games? (y/n)  :  ' 
]

# #Haven't yet implemented the rating system for each sub-category so useless since no specs can deliever the speaker quality. 
# speaker_questions = [
#     # "Would you like a good speaker? \n1.) yes (y) 2.) don't mind (n)  :  " 
# ]

battery_questions = [
    "Do you like a bigger battery? (y/n)  :  ",
    'Do you charge very rarely? (y/n)  :  ',
    "Do you want fast charging? (y/n)  :  "
    # 'Do you want wireless charging? (y/n)  :  '
]

all_categories = [exact_questions,performance_questions, camera_questions,software_questions,display_questions,storage_questions,battery_questions]

# %%
#Asking the questions
print("\n\nWELCOME TO THE RECOMMENDATION SYSTEM. JUST ANSWER FEW QUESTIONS AND YOU WILL GET YOUR PERSONALIZED REOMMENDATION.\n\n")
lst = []
for category in all_categories:
    for questions in category:
        lst.append(input(questions))

#Processing y into True and n into False for easier manipulation
mapping_dict = {'y':True,'n':False}
lst = list(map(lambda x: mapping_dict[x] if x in mapping_dict else x,lst))

# %%
lst

# %%
df3 = df2.copy()

#Exact Question (0-4)
if(lst[0]==1):
    df3.query("brand_name == 'apple'",inplace=True)
elif(lst[0]==2):
    df3.query("brand_name != 'apple'",inplace=True)
if(lst[1]==2):
    user_brand = input("Enter the brand you want")
    df3.query(f"brand_name == {user_brand}",inplace=True)
if(lst[2]==1):
    df3.query("screen_size <= 6.1",inplace=True)
elif(lst[2]==2):
    df3.query("screen_size > 6.1 and screen_size <=6.6",inplace=True)
elif(lst[2]==3):
    df3.query("screen_size > 6.6",inplace=True)
if(lst[3]==1):
    df3.query("has_5g == True",inplace=True)
elif(lst[3]==2):
    df3.query("has_5g != False",inplace=True)
budget_min, budget_max = map(int,lst[4].split('-'))
df3.query(f"price >= {budget_min} and price <= {budget_max}",inplace=True)


#Performance Questions (5-9)

if lst[5:10].count(True)==0:
    user_performance=q1_performance
elif any(lst[5:8]):
    user_performance = q3_performance
else:
    user_performance=q2_performance
if lst[5:10].count(True)>=3:
    user_performance=max_performance


#Camera Questions (10-13)
def user_performance_camera(row):
    row['rating'] = row['rating']*(1 - 0.1*abs(user_performance-row['performance_ratings'])/row['performance_ratings'])
    row['rating'] = row['rating']*(1 - 0.1*abs(user_camera-row['camera_ratings'])/row['camera_ratings'])
if not lst[7] and lst[10:14].count(True)==0:
    user_camera=q1_camera
elif ([lst[7]]+lst[11:14]).count(True)==1:
    user_camera = q2_camera
else:
    user_performance=q3_camera
if lst[10]:
    user_camera=max_camera

df3.apply(user_performance_camera,axis=1)

#Software_Questions(14-17)
lst[15]=not lst[15] #Because it's asking a negative question. So we invert the truth value
def bad_software(row):
    if row['brand_name'] not in ['apple','google','samsung','motorola','samsung']:
        row['rating'] = row['rating']*0.95
if any(lst[15:17]):
    df3.apply(bad_software,axis=1)
if lst[14]:
    df3.query("brand_name == 'google' or brand_name == 'apple' or brand_name == 'samsung'",inplace=True)

#Display Questions (18-21)
def bad_display(row):
    if row['refresh_rate'] < q3_refresh:
        row['rating'] = row['rating']*(0.8+0.2*row['refresh_rate']/q3_refresh)
    
if any( ([lst[5]] + lst[17:19])):
    df3.apply(bad_display,axis=1)
if lst[19]:
    print("Choose a model with oled display. Our dataset, unfortunately, doesn't contain the information about the type of the panel.")
if lst[20]:
    print("Choose a whose display has high NITs count. Our dataset, unfortunately, doesn't contain the information about the type of the panel.")

#Display Questions (22-25)
def less_storage(row):
    if row['extended_memory_available'] == 0:
        row['rating'] = row['rating']*0.98
    
if any( (lst[12:14] + lst[22:24])):
    df3.apply(less_storage,axis=1)
if lst[24]:
    print("Choose a model with storage having UFS 3 or greater. Our dataset, unfortunately, doesn't contain the information about the type of the Flash used in storage.")
if lst[25]:
    print("Choose a model bigger storage. Our dataset, unfortunately, doesn't contain the information about the storage and pricing of each model.")

#Battery Questions (26-28)
def battery_low(row):
    if row['brand_name'] != 'apple':
        if row['battery_capacity'] <q1_battery:
            row['rating'] = row['rating']*(0.98 + 0.02*row['battery_capacity']/q3_battery)
        
    else:
        if row['battery_capacity'] < 2*q1_battery/3: #My independent study shows that the 2/3rd of theoritical capacity of battery gives same backup in iphones.
            row['rating'] = row['rating']*(0.98 + 0.02*row['battery_capacity']/q3_battery)
        

def charging_slow(row):
    if row['fast_charging'] < q1_charging: 
        row['rating'] = row['rating']*(0.985 + 0.015*row['fast_charging']/q3_charging)
    
    
if (lst[5:8]+lst[12:14]+lst[26:28]).count(True)>=2:
    df3.apply(battery_low,axis=1)
if lst[26]:
    df3.apply(charging_slow,axis=1)

df3.sort_values(by='rating',ascending=False,inplace=True)


# %%
df3.to_csv("Recommendation.csv")
df3

# %%



