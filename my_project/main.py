# import for_import
#
# run_distance = float(input(f"Ile km?"))
# run_time = float(input(f"Ile czasu?"))
#
# avg_speed2 = for_import.avg_speed(run_distance, run_time)
# print(f"będzie ile {avg_speed2}")

import calculations.investment

def asc_for_int_value(massage):
    input_value = input(massage)
    return int(input_value)

print("Kalkulator")

initial_value = asc_for_int_value("Jaka kvota?")
percentage = asc_for_int_value("Jaki procent?")
years = asc_for_int_value("Ile lat?")

final_value = calculations.investment.calculate_investment_value(initial_value, percentage, years)
print(f"nu wot = {final_value:.2f}")
