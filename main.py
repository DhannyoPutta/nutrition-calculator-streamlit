import streamlit as st
import pandas as pd
import random

st.title("Dietary Planner")
st.sidebar.header("Chat with Nutritionist")

with st.sidebar:
    messages = st.container(height=720)
    if prompt := st.chat_input("Chat with Personal Nutritionist"):
        messages.chat_message("user").write(prompt)
        response = random.choice(
        [
            "Sate Padang",
            "Rendang Sapi",
            "Nasi Goreng",
        ]
    )
        messages.chat_message("nutritionist").write(response)


col1, col2 = st.columns(2)
    
height = col1.number_input("Height in cm")
weight = col1.number_input("Mass in kg")
age = col1.number_input("Age")

df = pd.DataFrame({'Activity Level': ["Sedentary - Less than 5,000 steps daily", 
                                      "Lightly active - About 5,000 to 7,499 steps daily", 
                                      "Moderately active - About 7,500 to 9,999 steps daily", 
                                      "Very active - More than 10,000 steps daily", 
                                      "Super active - More than 12,500 steps daily"]})
df1 = pd.DataFrame({'Gender': ["Male", "Female"]})

activityLevel = col2.selectbox(
    "Activity Level",
    df['Activity Level']
)

gender = col2.selectbox(
    "Gender",
    df1['Gender']
)

c1 = st.container()
col1, col2 = c1.columns(2)

BMR = 0.0
if (gender == "Male"):
    BMR = 88.362 + (13.397 * float(weight)) + (4.799 * float(height)) - (5.677 * float(age))
else:
    BMR = 447.593 + (9.247 * float(weight)) + (3.098 * float(height)) - (4.330 * float(age))
BMR = round(BMR, 1)
col1.metric(label="Basal Metabolic Rate", value=BMR)

#If statement to determine normal or not

TDEE = 0.0
match (activityLevel):
    case "Sedentary - Less than 5,000 steps daily":
        TDEE = BMR*1.2
    case "Lightly active - About 5,000 to 7,499 steps daily":
        TDEE = BMR*1.375
    case "Moderately active - About 7,500 to 9,999 steps daily":
        TDEE = BMR*1.55
    case "Very active - More than 10,000 steps daily":
        TDEE = BMR*1.725
    case "Super active - More than 12,500 steps daily":
        TDEE = BMR*1.9   
    case _:
        TDEE = 0
TDEE = round(TDEE, 2)
col1.metric(label="Total Daily Energy Expenditure (kcals)", value=TDEE)

recommendedIntake = TDEE

BMI = 0.0
if (weight > 0 and height  > 0):
    BMI = float(weight)/(height*height)*10000
BMI = round(BMI, 1)
BMIStatus = ""

if (BMI < 18.5):
    BMIStatus = "Underweight"
    recommendedIntake += 500
elif(BMI>18.5 and BMI<25):
    BMIStatus = "Normal"
elif(BMI>25 and BMI<30):
    BMIStatus = "Overweight"
    recommendedIntake -= 500
else:
    BMIStatus = "Obese"
    recommendedIntake -= 1000

recommendedIntake = round(recommendedIntake, 2)
col1.metric(label="Recommmended Daily Intake (kcals)", value=recommendedIntake)
col1.metric(label="Body Mass Index", value=str(BMI)+" (" + BMIStatus + ")")

carbohydrates0 = round(45/100 * TDEE, 2)
carbohydrates1 = round(65/100 * TDEE, 2)
proteins0 = round(10/100 * TDEE, 2)
proteins1 = round(35/100 * TDEE, 2)
fats0 = round(20/100 * TDEE, 2)
fats1 = round(35/100 * TDEE, 2)

col2.metric(label="Recommended Daily Carbohydrate Intake (kcals)", value=str(carbohydrates0) + " - " + str (carbohydrates1))
col2.metric(label="Recommended Daily Protein Intake (kcals)", value=str(proteins0) + " - " + str (proteins1))
col2.metric(label="Recommended Daily Fat Intake (kcals)", value=str(fats0) + " - " + str (fats1))

st.markdown("# Swiss Food Database")
foodf = pd.read_csv("Swiss_food_composition_database.csv", encoding='unicode_escape')
st.dataframe(foodf, use_container_width=True)
