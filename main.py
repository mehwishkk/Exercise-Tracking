import requests
import datetime

GENDER = YOUR GENDER
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE
x = datetime.datetime.now()
print(x.date())
date_str=str(x.date())
print(date_str)
time_str=f'{x.hour}:{x.minute}'
print(time_str)
exercise_input=input("Tell me which exercise u did:")
api_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID= 'YOUR NUTRITIONIX APP ID'
API_KEY='YOUR NUTRITIONIX API KEY'
sheet_endpoint = "https://api.sheety.co/workoutTracking/sheet1"
nutrientparams = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age": AGE
}
headers = {
'Content-Type':'application/json',
'x-app-id':APP_ID,
'x-app-key':API_KEY
}
nutri_response = requests.post(url=api_endpoint,json=nutrientparams,headers=headers)
result = nutri_response.json()

for exercise in result['exercises']:
    print(exercise)
    sheet_parameters = {
        'sheet1': {
            'date': date_str,
            'time': time_str,
            "query": exercise_input,
            "exercise": exercise['user_input'],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]}
    }

    Sheet_response = requests.post(url=sheet_endpoint,json=sheet_parameters)
    print(Sheet_response.status_code)
    print(Sheet_response.text)


