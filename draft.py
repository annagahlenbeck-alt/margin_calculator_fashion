"""
Margin Calculator for Fashion (DTC + Wholesale)

A simple pricing tool that:
- Calculates production cost
- Computes wholesale and DTC prices using standard fashion margins
- Compares against competitor prices
"""

material_cost = input("Please enter your cost of materials ")
labour_cost = input("Please enter your labour costs ")
other_costs = input("Please enter other costs like packaging, etc ")
competitior_prices = input("Please enter 3 prices of market competitors ")


production_cost = int(material_cost) + int(labour_cost) + int(other_costs)


first, second, last = competitior_prices.split(",")
av_competitor_prize = round((int(first) + int(second) + int(last)) / 3)


dtc_price = round(production_cost * 4.75)
dtc_final_price = round((dtc_price + av_competitor_prize) / 2)

wholesale_price = round(production_cost * 2.35)


print(
    "The calculated market price for Wholesale is", wholesale_price, "and the DTC price is", dtc_final_price, ".These calculations are based on the average win margin and in comparisson with your competitiors")
