import numpy as np # type: ignore
import pandas as pd # type: ignore

# yes_no_option = ["Yes", "No"]

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

    

# get_ipython().system('jupyter nbconvert --to script main.ipynb')

