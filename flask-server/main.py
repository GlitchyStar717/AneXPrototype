import numpy as np # type: ignore
import pandas as pd # type: ignore

# yes_no_option = ["Yes", "No"]
def question_list():
    
    exact_questions = [
        {
            "question": "What phone do you want?",
            "options": ["IPhone", "Android", "Open to Both"],
        },
        {
            "question": "Do you want a particular smartphone brand?",
            "options": ["No", "Yes"],
        },
        {
            "question": "What screen size would you prefer?",
            "options": [
                'below 6.1"',
                'between 6.1" & 6.6"',
                'above 6.6"',
                "Doesn't matter",
            ],
        },
        {"question": "Do you want your phone to have 5g?", "options": ["Yes", "No", "Any"]},
        {
            "question": "What is your budget range?",
            "options": ["Budget", "Midrange", "Flagship", "Any"],
        },
    ]

    performance_questions = [
        {
            "question": "Do you frequently play games on your smartphone?",
            "options": ["Yes", "No"],
        },
        {"question": "Do you use a lot of apps?", "options": ["Yes", "No"]},
        {
            "question": "Do you want to take high quality photos and videos?",
            "options": ["Yes", "No"],
        },
        {
            "question": "Do you wish to use your smartphone for over 5 years?",
            "options": ["Yes", "No"],
        },
        {
            "question": "Do you wish to have all new features in your smartphone?",
            "options": ["Yes", "No"],
        },
    ]

    camera_questions = [
        {
            "question": "Do you want a camera that shoot good in night time?",
            "options": ["Yes", "No"],
        },
        {
            "question": "Would you love to shoot zoom and portrait shots?",
            "options": ["Yes", "No"],
        },
        {"question": "Do you want to shoot many videos?", "options": ["Yes", "No"]},
        {"question": "Do you want to shoot many photos?", "options": ["Yes", "No"]},
    ]

    software_questions = [
        {
            "question": "Do you want to get new updates for 5+ years?",
            "options": ["Yes", "No"],
        },
        {
            "question": "Do you mind useless apps pre-installed in your smartphone?",
            "options": ["Yes", "No"],
        },
        {
            "question": "Do you like to have easy software support?",
            "options": ["Yes", "No"],
        },
        {
            "question": "Can you distinguish between smooth and non-smooth animation?",
            "options": ["Yes", "No"],
        },
    ]

    display_questions = [
        {"question": "Do you do a lot of scrolling?", "options": ["Yes", "No"]},
        {"question": "Do you like watching movies in mobile?", "options": ["Yes", "No"]},
        {
            "question": "Do you consume a lot of media like YouTube and more?",
            "options": ["Yes", "No"],
        },
        {
            "question": "Do you wish to use phone a lot on sunlight?",
            "options": ["Yes", "No"],
        },
    ]

    storage_questions = [
        {
            "question": "Do you store a lot of offline media like movies or other files in smartphones?",
            "options": ["Yes", "No"],
        },
        {
            "question": "Do you want your smartphone to be able to store everything you want for years to come?",
            "options": ["Yes", "No"],
        },
        {
            "question": "Do you want to transfer from and to your smartphones quickly?",
            "options": ["Yes", "No"],
        },
        {"question": "Do you download a lot of apps or games?", "options": ["Yes", "No"]},
    ]

    battery_questions = [
        {"question": "Do you like a bigger battery?", "options": ["Yes", "No"]},
        {"question": "Do you charge very rarely?", "options": ["Yes", "No"]},
        {"question": "Do you want fast charging?", "options": ["Yes", "No"]},
    ]


    all_questions = []
    all_questions.extend(exact_questions)
    all_questions.extend(performance_questions)
    all_questions.extend(camera_questions)
    all_questions.extend(software_questions)
    all_questions.extend(display_questions)
    all_questions.extend(storage_questions)
    all_questions.extend(battery_questions)

    # Combine all questions into a single array
    # { "questions": [{"question":"", "options":[]},{}] }

    final_object = {"questions": []}
    for item in all_questions:
        final_object["questions"].append(item)


    return final_object


# get_ipython().system('jupyter nbconvert --to script main.ipynb')




#THE full recommendation process
def recommend(responses):
#THE full recommendation process
    print("\n\nResponses : ",responses)
    #Defining the default case incase user forgets to input any button. Max camera, max performance and doesn't mind the screen size, the 5g and brands
    lst = [3, 1, 4, 3, '5000-170000', True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    #Convert to list as the person who made the engine used list for analyzing.
    # for i in range(len(lst2)):
    user_inputs = responses.keys()
    print("User Inputs : ", user_inputs)
    if '0' in user_inputs:
        if responses['0'] == 'IPhone':
            lst[0]=1
        elif responses['0'] == 'Android':
            lst[0]=2
    if '1' in user_inputs:
        if responses['1'] == 'No':
            lst[1]=1
        else:
            lst[1]=2
    if '2' in user_inputs:
        if responses['2'] == 'below 6.1"':
            lst[2]=1
        elif responses['2'] == 'between 6.1" & 6.6"':
            lst[2]=2
        elif responses['2'] == 'above 6.6"':
            lst[2]=3
        else:
            lst[2]=4
    if '3' in user_inputs:
        if responses['3'] == 'Yes':
            lst[3]=1
        elif responses['3'] == 'No':
            lst[3]=2
    if '4' in user_inputs:
        if responses['4'] == 'Budget':
            lst[4]="5000-20000"
        elif responses['4'] == 'Midrange':
            lst[4]="20000-50000"
        elif responses['4'] == 'Flagship':
            lst[4]="50000-170000"
    for i in range(5,len(lst)+5):
        if f'{i}' in user_inputs:
            lst[i]= True if responses[f'{i}'] == 'Yes' else False

        
    print("List : ",lst)



    #Read the dataset
    df = pd.read_csv('./smartphone_cleaned_v5.csv')
    # df.head()  #Displaying the dataset if necessary



    #Pre process the dataset
    df.sort_values(by='model',ascending=True,inplace=True)
    df["SN"] = list(range(len(df.index)))
    df=df.set_index('SN')
    df =df.ffill(axis=0)
    df.fillna({'fast_charging':22},inplace=True) #ffill didn't work for iphone 11 and iphone 11 pro in the 1st run of code. so it manually for 2 mobiles
    df.fillna({'extended_upto':0},inplace=True) #ffill didn't work for iphone 11 and iphone 11 pro in the 1st run of code. so it manually for 2 mobiles
    df.info()




    #Make a copy of the dataset to start the modification
    df2= df.copy()
    # Filter out the outliers in the price category
    category = 'price'
    p1 = np.percentile(df[category],1)
    p2 = np.percentile(df[category],99)
    df2.query(f"{category} >= {p1} and {category} <= {p2}",inplace=True)
    # Evaluate the resolution as a mathematical quantity (pixels count)
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




    # Calculate standard quantities of the dataset for analysis and comparison
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




    #adding new columns for representing the performance and camera quality numerically
    #For categorizing the phones into "Flagship", "Midrange", and "Average"
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
    #For rating the phones in the camera aspect
    def categorize_camera(row):
        if row["phone_category"] == "flagship":
            c1 = 10
        elif row["phone_category"] == "midrange":
            c1 = 8
        else:
            c1 = 5
        c2 = (9 + (row["primary_camera_rear"]-12)/(max_rear-12)) if row["primary_camera_rear"] > 12 else 9*row["primary_camera_rear"]/12
        c3 = (9 + (row["primary_camera_front"]-10)/(max_front-10)) if row["primary_camera_front"] > 10 else 9*row["primary_camera_front"]/10
        brand_quality = {'apple':2.5, 'google':2.5, 'samsung':1.5,'huawei':1.5}
        c4 = brand_quality[row['brand_name']] if row["brand_name"] in brand_quality else 0
        total = 10 + 10 + 10 + 2.5 # sum of maximum of c1 + c2 + c3 + c4
        rating = (c1+c2+c3+c4)*10.0/total
        return rating  
    #For rating the phone's performance
    def categorize_performance(row):
        c1 = row["processor_speed"]*10/max_speed
        c2 = row["num_cores"]*10/max_cores
        c3 = (7 + 3*(row['ram_capacity']-q3_ram)/(max_ram-q3_ram)) if row['ram_capacity']>=q3_ram else 7*row['ram_capacity']/q3_ram  
        c4 = 5 if row["brand_name"] == 'apple' else 0 #Apple's bionic processors usually outperform android's chips with far more memory
        
        total = 10 + 10 + 10 + 5
        rating = (c1+c2+c3+c4)*10.0/total
        return rating
    # Adding these columns on the dataset
    df2['phone_category'] = df2.apply(categorize_phone, axis=1)
    df2['camera_ratings'] = df2.apply(categorize_camera, axis=1)
    df2['performance_ratings'] = df2.apply(categorize_performance, axis=1)




    #Adding more standard parameters based on the new added columns
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





    #Recommendation based on filtering and manipulation of the data in the columns
    #Creating a column for the final recommendation dataset
    df3 = df2.copy()
    #Using the Exact Question (0-4)
    if(lst[0]==1):
        df3.query("brand_name == 'apple'",inplace=True)
    elif(lst[0]==2):
        df3.query("brand_name != 'apple'",inplace=True)
    if(lst[1]==2):
        user_brand = input("Enter the brand you want  :  ")
        df3.query(f"brand_name == '{user_brand}'",inplace=True)
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
    #Using the Performance Questions (5-9)
    if lst[5:10].count(True)==0:
        user_performance=q1_performance
    elif any(lst[5:8]):
        user_performance = q3_performance
    else:
        user_performance=q2_performance
    if lst[5:10].count(True)>=3:
        user_performance=max_performance
    #Using the Camera Questions (10-13)
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
    #Using the Software_Questions(14-17)
    lst[15]=not lst[15] #Because it's asking a negative question. So we invert the truth value
    def bad_software(row):
        if row['brand_name'] not in ['apple','google','samsung','motorola','asus','oneplus']:
            row['rating'] = row['rating']*0.95
    if any(lst[15:17]):
        df3.apply(bad_software,axis=1)
    if lst[14]:
        df3.query("brand_name == 'google' or brand_name == 'apple' or brand_name == 'samsung'",inplace=True)
    #Using the Display Questions (18-21)
    def bad_display(row):
        if row['refresh_rate'] < q3_refresh:
            row['rating'] = row['rating']*(0.8+0.2*row['refresh_rate']/q3_refresh)
        
    if any( ([lst[5]] + lst[17:19])):
        df3.apply(bad_display,axis=1)
    if lst[19]:
        print("Choose a model with oled display. Our dataset, unfortunately, doesn't contain the information about the type of the panel.")
    if lst[20]:
        print("Choose a whose display has high NITs count. Our dataset, unfortunately, doesn't contain the information about the type of the panel.")
    #Using the Display Questions (22-25)
    def less_storage(row):
        if row['extended_memory_available'] == 0:
            row['rating'] = row['rating']*0.98
        
    if any( (lst[12:14] + lst[22:24])):
        df3.apply(less_storage,axis=1)
    if lst[24]:
        print("Choose a model with storage having UFS 3 or greater. Our dataset, unfortunately, doesn't contain the information about the type of the Flash used in storage.")
    if lst[25]:
        print("Choose a model bigger storage. Our dataset, unfortunately, doesn't contain the information about the storage and pricing of each model.")
    #Using the Battery Questions (26-28)
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



    #Returning the final recommendation
    df3.sort_values(by='rating',ascending=False,inplace=True)
    top5 = df3.head()
    print(top5)
    phoneNames = top5['model'].tolist() 
    return phoneNames