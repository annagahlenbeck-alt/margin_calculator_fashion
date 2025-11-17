# Margin Calculator for Fashion (DTC + Wholesale)

# A simple pricing tool that:
# - Calculates production cost
# - Computes wholesale and DTC prices using standard fashion margins
# - Compares against competitor prices


def calculate_production_cost(material_cost, labour_cost, other_costs):
    return material_cost + labour_cost + other_costs


def parse_competitor_prices(prices_input):
    prices = [int(p.strip()) for p in prices_input.split(",")]
    return round(sum(prices) / len(prices))


def calculate_wholesale_price(production_cost, margin=2.35):
    return round(production_cost * margin)


def calculate_dtc_price(production_cost, competitor_avg, margin=4.75):
    base_price = production_cost * margin
    return round((base_price + competitor_avg) / 2)


def main():
    print("Fashion Margin Calculator (DTC + Wholesale)")

    material_cost = int(input("Cost of materials: "))
    labour_cost = int(input("Labour cost: "))
    other_costs = int(input("Other costs (packaging, trims, etc.): "))

    competitor_prices_input = input("Enter 3 competitor prices, separated by commas: ")

    production_cost = calculate_production_cost(material_cost, labour_cost, other_costs)
    competitor_avg = parse_competitor_prices(competitor_prices_input)

    wholesale = calculate_wholesale_price(production_cost)
    dtc = calculate_dtc_price(production_cost, competitor_avg)

    print(f"\nWholesale price: {wholesale}")
    print(f"DTC price: {dtc}")
    print("\nPrices are based on standard industry margins and competitor benchmarks.")


if __name__ == "__main__":
    main()
