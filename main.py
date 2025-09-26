from pyscript import display, HTML, document
from datetime import datetime, timedelta, date, time
import pandas as pd

restaurant_name = 'Mr Choy'
owner_name = 'Stephen Choy'
year_established = 2017
popular_item = 'Mixed Vegetable Fried Rice'
has_delivery = True
food_names = ['Mushroom Fried Rice', 'Mixed Vegetable Fried Rice', 'Chicken Fried Rice', 'Roast Duck with Plum Sauce', 'Ribs in Hoi Sin Sauce']
food_prices = [433.50, 461.50, 461.50, 536.50, 498.99]
drink_names = ['Coke', 'Coke Zero', 'Sprite', 'Iced Tea', 'Water']
drink_prices = [37.50, 37.50, 36.50, 35.50, 15.50]
business_hours = {"from": time(hour=7, minute=30), "to": time(hour=17, minute=30)}
common_allergens = {'peanut', 'shellfish', 'egg'}
tax_rate = 0.072

df = pd.DataFrame({
    "Meals": food_names, 
    "": [""] * len(food_names),  # Spacer column
    "Price (₱)": food_prices
})

df2 = pd.DataFrame({
    "Drinks": drink_names, 
    "": [""] * len(drink_names),  # Spacer column
    "Price (₱)": drink_prices
})

df.index += 1
df2.index += 1

display(df, target="pandas-output-inner", append=False)
display(df2, target="pandas-output-inner-2", append=False)

# Inject CSS to set the spacer column width to 20px and align table headers/cells left
display(HTML("""
<style>
    #pandas-output-inner table {
        width: 40vw;        /* Set table width */
        font-size: 1.6em;    /* Adjust font size */
    }
    #pandas-output-inner th, #pandas-output-inner td {
        text-align: left !important;
        padding: 4px 4px;   /* Adjust cell padding */
    }
    #pandas-output-inner td:nth-child(3), #pandas-output-inner th:nth-child(3) {
        padding-left: 20px;
    }
    #pandas-output-inner td:nth-child(2), #pandas-output-inner th:nth-child(2) {
        background: transparent;
        border: none;
    }
</style>
"""), target="pandas-output-inner", append=True)

# Drinks Menu

display(HTML("""
<style>
    #pandas-output-inner-2 table {
        width: 40vw;
        font-size: 1.6em;
    }
    #pandas-output-inner-2 th, #pandas-output-inner-2 td {
        text-align: left !important;
        padding: 4px 4px;
    }
    #pandas-output-inner-2 td:nth-child(3), #pandas-output-inner-2 th:nth-child(3) {
        padding-left: 20px;
    }
    #pandas-output-inner-2 td:nth-child(2), #pandas-output-inner-2 th:nth-child(2) {
        background: transparent;
        border: none;
    }
</style>
"""), target="pandas-output-inner-2", append=True)