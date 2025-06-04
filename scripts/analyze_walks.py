import json

#Loading the data
with open(r'C:\Users\Khali\sprint-to-the-goal\data') as file:
    walks = json.load(file)

# Basic Data Calculations
total_distance = sum(walk['distance_km'] for walk in walks)
total_avg_pace = sum(walk['avg_pace_min_per_km'] for walk in walks)
total_calories = sum(walk['calories'] for walk in walks)
average_pace = total_avg_pace / len(walks)
total_duration = sum(walk['duration_min'] for walk in walks)
total_entry = len(walks)

# Basic Print
print(f"\n\n\t\tTotal Statistics")
print("-" * 48)
print(f"Total Distance: {total_distance:.2f} km")
print(f"Total Calories Burned: {total_calories} kcal")
print(f"My Average Pace Maintained: {average_pace:.2f} min/km")
print(f"Total Duration: {total_duration} minutes")
print(f"Total Entry: {total_entry}")

# Divide your data into first 5 and last 5 walks
# Divide your data into two halves dynamically
half_index = len(walks) // 2
first_half = walks[:half_index] # First Half entry
last_half = walks[half_index:] # Last Half entry

# This function calculates averages for each walk metric from a list of walk dictionaries
def calculate_averages(walk_data):
    total_distance = sum(walk['distance_km'] for walk in walk_data)
    total_duration = sum(walk['duration_min'] for walk in walk_data)
    total_pace = sum(walk['avg_pace_min_per_km'] for walk in walk_data)
    total_steps = sum(walk['steps'] for walk in walk_data)
    total_calories = sum(walk['calories'] for walk in walk_data)
    count = len(walk_data)

# Return a dictionary (like a JSON object) of averages
    return {
        "avg_distance": total_distance / count,
        "avg_duration": total_duration / count,
        "avg_pace": total_pace / count,
        "avg_steps": total_steps / count,
        "avg_calories": total_calories / count
    }
first_averages = calculate_averages(first_half)
last_averages = calculate_averages(last_half)

# Calculate how each metric changed from first 5 walks to last 5 walks
improvements = {
    key: last_averages[key] - first_averages[key]
    for key in first_averages
}

# Function to display all the data in a table format
def display_comparison(first, last, change):
    print("\n\n\n📊 AVERAGES COMPARISON (First Half vs. Last Half)")
    print("-" * 50)
    print(f"{'Metric':<15}{'First Half':<15}{'Last Half':<15}{'Change':<15}")
    print("-" * 50)

    for key in first:
        metric = key.replace("avg_", "").capitalize().replace("_", " ")
        f_val = round(first[key], 2)
        l_val = round(last[key], 2)
        c_val = round(change[key], 2)
        print(f"{metric:<15}{f_val:<15}{l_val:<15}{c_val:<15}")
    print("-" * 50)

display_comparison(first_averages, last_averages, improvements)

