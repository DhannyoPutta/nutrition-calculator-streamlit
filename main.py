import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)
    
height = col1.number_input("Height in cm")
weight = col1.number_input("Mass in kg")
age = col1.number_input("Age")

df = pd.DataFrame({'Activity Level': ["Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"]})
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

BMR = 0
if (gender == "Male"):
    BMR = 88.362 + (13.397 * float(weight)) + (4.799 * float(height)) - (5.677 * float(age))
else:
    BMR = 447.593 + (9.247 * float(weight)) + (3.098 * float(height)) - (4.330 * float(age))
BMR = round(BMR, 1)
col1.metric(label="Basal Metabolic Rate", value=BMR)

#If statement to determine normal or not

TDEE = 0
match (activityLevel):
    case "Sedentary":
        TDEE = BMR*1.2
    case "Lightly active":
        TDEE = BMR*1.375
    case "Moderately active":
        TDEE = BMR*1.55
    case "Very active":
        TDEE = BMR*1.725
    case "Super active":
        TDEE = BMR*1.9   
    case _:
        TDEE = 0
TDEE = round(TDEE, 1)
col1.metric(label="Total Daily Energy Expenditure", value=TDEE)

carbohydrates0 = round(45/100 * TDEE, 2)
carbohydrates1 = round(65/100 * TDEE, 2)
proteins0 = round(10/100 * TDEE, 2)
proteins1 = round(35/100 * TDEE, 2)
fats0 = round(20/100 * TDEE, 2)
fats1 = round(35/100 * TDEE, 2)

col2.metric(label="Recommended Daily Carbohydrate Intake (kcals)", value=str(carbohydrates0) + " - " + str (carbohydrates1))
col2.metric(label="Recommended Daily Protein Intake (kcals)", value=str(proteins0) + " - " + str (proteins1))
col2.metric(label="Recommended Daily Fat Intake (kcals)", value=str(fats0) + " - " + str (fats1))

#Calculating Macronutrient Needs

#Basal Metabolic Rate (BMR): This is the number of calories your body needs at rest to maintain vital functions.
#Harris-Benedict Equation: Done
#For men: BMR = 88.362 + (13.397 * weight in kg) + (4.799 * height in cm) - (5.677 * age in years)
#For women: BMR = 447.593 + (9.247 * weight in kg) + (3.098 * height in cm) - (4.330 * age in years)

#Total Daily Energy Expenditure (TDEE): This is the number of calories you need per day based on activity level. Done
#TDEE = BMR * Activity Factor
#Activity Factors:
#Sedentary (little or no exercise): BMR * 1.2
#Lightly active (light exercise/sports 1-3 days/week): BMR * 1.375
#Moderately active (moderate exercise/sports 3-5 days/week): BMR * 1.55
#Very active (hard exercise/sports 6-7 days a week): BMR * 1.725
#Super active (very hard exercise/physical job): BMR * 1.9

#Macronutrient Distribution: Done
#Carbohydrates: 45-65% of total daily calories
#Proteins: 10-35% of total daily calories
#Fats: 20-35% of total daily calories

#Information needed from users: Done
#Height in cm
#Weight in kg
#Age in years
#Activity Level
