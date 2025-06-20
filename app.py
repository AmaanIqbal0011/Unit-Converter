import streamlit as st

def unit_converter(value , unit_from , unit_to):
    
    conversions = {
    # Identity conversions
        "meter_meter": 1,
        "kilometer_kilometer": 1,
        "centimeter_centimeter": 1,
        "millimeter_millimeter": 1,
        "gram_gram": 1,
        "kilogram_kilogram": 1,
        "milligram_milligram": 1,
        "liter_liter": 1,
        "milliliter_milliliter": 1,
        "mile_mile": 1,
        "yard_yard": 1,
        "foot_foot": 1,
        "inch_inch": 1,

        # Length & distance
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "meter_centimeter": 100,
        "centimeter_meter": 0.01,
        "centimeter_millimeter": 10,
        "millimeter_centimeter": 0.1,
        "kilometer_mile": 0.621371,
        "mile_kilometer": 1.60934,
        "mile_yard": 1760,
        "yard_mile": 1 / 1760,
        "yard_foot": 3,
        "foot_yard": 1 / 3,
        "foot_inch": 12,
        "inch_foot": 1 / 12,
        "inch_centimeter": 2.54,
        "centimeter_inch": 1 / 2.54,
        "meter_inch": 39.3701,
        "inch_meter": 1 / 39.3701,
        "meter_foot": 3.28084,
        "foot_meter": 1 / 3.28084,
        "yard_centimeter": 91.44,
        "centimeter_yard": 1 / 91.44,
        "yard_meter": 0.9144,
        "meter_yard": 1 / 0.9144,
        "foot_centimeter": 30.48,
        "centimeter_foot": 1 / 30.48,

        # Weight
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        "gram_milligram": 1000,
        "milligram_gram": 0.001,

        # Volume
        "liter_milliliter": 1000,
        "milliliter_liter": 0.001
}

    key = f"{unit_from}_{unit_to}"   
    
    if key in conversions:
        conversion = conversions[key] 
        return value * conversion
    else:
        "Conversion Not Supported"

units = [
    "meter", "kilometer", "centimeter", "millimeter",
    "gram", "kilogram", "milligram",
    "liter", "milliliter",
    "mile", "yard", "foot", "inch"
]


st.title("Unit Converter")
st.markdown("### Convert length,weight and Time Instantly")  
st.markdown("Select a Category, enter a Value, and get result instantly.")
value = st.number_input("Enter the value: ",min_value=1.0,step=1.0)

unit_from = st.selectbox("convert From: ",units)
unit_to = st.selectbox("Convert to: ",units)

if st.button("Convert"):
    result = unit_converter(value,unit_from,unit_to)
    st.markdown(f"{value} {unit_from} to {unit_to} = {result}")
    
