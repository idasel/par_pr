# import json
# import math

# with open('parallelepipeds.json', 'r') as file:
#   data = json.load(file)

# print(f"Total number of figures {len(data)}")

# sum_diag = sum_volume = sum_surface_area = sum_alpha = sum_beta = sum_gamma = sum_radius_described_sphere = sum_volume_described_sphere = 0

# result = {}

# for key, values in data.items():
#     a = float(values['a'])
#     b = float(values['b'])
#     c = float(values['c'])

#     diag = math.sqrt(a**2 + b**2 + c**2)
#     volume = a * b * c
#     surface_area = 2 * (a*b + a*c + b*c)
#     alpha = math.degrees(math.acos(a/diag))
#     beta = math.degrees(math.acos(b/diag))
#     gamma = math.degrees(math.acos(c/diag))
#     radius_described_sphere = diag / 2
#     volume_described_sphere = (4/3) * math.pi * (radius_described_sphere ** 3)
    
#     sum_diag += diag
#     sum_volume += volume
#     sum_surface_area += surface_area
#     sum_alpha += alpha
#     sum_beta += beta
#     sum_gamma += gamma
#     sum_radius_described_sphere += radius_described_sphere
#     sum_volume_described_sphere += volume_described_sphere

#     result[key] = {
#         "diag": str(diag),
#         "volume": str(volume),
#         "surface_area": str(surface_area),
#         "alpha": str(alpha),
#         "beta": str(beta),
#         "gamma": str(gamma),
#         "radius_described_sphere": str(radius_described_sphere),
#         "volume_described_sphere": str(volume_described_sphere)
#     }
#     with open('result.json', 'w') as file:
#       json.dump(result, file, indent=4)


# total_figures = len(data)
# avg_diag = sum_diag / total_figures
# avg_volume = sum_volume / total_figures
# avg_surface_area = sum_surface_area / total_figures
# avg_alpha = sum_alpha / total_figures
# avg_beta = sum_beta / total_figures
# avg_gamma = sum_gamma / total_figures
# avg_radius_described_sphere = sum_radius_described_sphere / total_figures
# avg_volume_described_sphere = sum_volume_described_sphere / total_figures

# averages = {
#     "avg_diag": str(avg_diag),
#     "avg_volume": str(avg_volume),
#     "avg_surface_area": str(avg_surface_area),
#     "avg_alpha": str(avg_alpha),
#     "avg_beta": str(avg_beta),
#     "avg_gamma": str(avg_gamma),
#     "avg_radius_described_sphere": str(avg_radius_described_sphere),
#     "avg_volume_described_sphere": str(avg_volume_described_sphere)
# }
# for key, value in averages.items():
#     print(f"Среднее значение {key.replace('_', ' ')}: {value}")
import json
import math

pict = """
MY FIRST SKRIPT

    /------/
   /      /|
  /      / |
 /------/  |
 |      |  /
 |      | /
 |______|/

I LOVE PYTHON
"""
print(pict)

def read_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def calculate_parameters(data):
    result = {}
    for key, values in data.items():
        a = float(values['a'])
        b = float(values['b'])
        c = float(values['c'])

        diag = math.sqrt(a**2 + b**2 + c**2)
        volume = a * b * c
        surface_area = 2 * (a*b + a*c + b*c)
        alpha = math.degrees(math.acos(a/diag))
        beta = math.degrees(math.acos(b/diag))
        gamma = math.degrees(math.acos(c/diag))
        radius_described_sphere = diag / 2
        volume_described_sphere = (4/3) * math.pi * (radius_described_sphere ** 3)
        
        result[key] = {
            "diag": str(diag),
            "volume": str(volume),
            "surface_area": str(surface_area),
            "alpha": str(alpha),
            "beta": str(beta),
            "gamma": str(gamma),
            "radius_described_sphere": str(radius_described_sphere),
            "volume_described_sphere": str(volume_described_sphere)
        }
    return result

def calculate_average(data):
    total_figures = len(data)
    sum_diag = sum_volume = sum_surface_area = sum_alpha = sum_beta = sum_gamma = sum_radius_described_sphere = sum_volume_described_sphere = 0
    
    for values in data.values():
        sum_diag += float(values['diag'])
        sum_volume += float(values['volume'])
        sum_surface_area += float(values['surface_area'])
        sum_alpha += float(values['alpha'])
        sum_beta += float(values['beta'])
        sum_gamma += float(values['gamma'])
        sum_radius_described_sphere += float(values['radius_described_sphere'])
        sum_volume_described_sphere += float(values['volume_described_sphere'])
    
    avg_diag = sum_diag / total_figures
    avg_volume = sum_volume / total_figures
    avg_surface_area = sum_surface_area / total_figures
    avg_alpha = sum_alpha / total_figures
    avg_beta = sum_beta / total_figures
    avg_gamma = sum_gamma / total_figures
    avg_radius_described_sphere = sum_radius_described_sphere / total_figures
    avg_volume_described_sphere = sum_volume_described_sphere / total_figures
    
    return {
        "avg_diag": str(avg_diag),
        "avg_volume": str(avg_volume),
        "avg_surface_area": str(avg_surface_area),
        "avg_alpha": str(avg_alpha),
        "avg_beta": str(avg_beta),
        "avg_gamma": str(avg_gamma),
        "avg_radius_described_sphere": str(avg_radius_described_sphere),
        "avg_volume_described_sphere": str(avg_volume_described_sphere)
    }

def write_result(result, filename):
    with open(filename, 'w') as file:
        json.dump(result, file, indent=4)

def main():
    data = read_data('parallelepipeds.json')
    result = calculate_parameters(data)
    print(f"Total number of figures {len(result)}.")
    avg = calculate_average(result)
    write_result(avg, 'statistics.json')
    for key, value in avg.items():
        print(f"Average {key.replace('_', ' ')}: {value}")
    
    write_result(result, 'result.json')

main()
