import pandas as pd
import datetime

# Wczytanie plików z ograniczeniem do 2 milionów rekordów
file_paths = {
    "item_properties_part1": "item_properties_part1.csv",
    "item_properties_part2": "item_properties_part2.csv",
    "events": "events.csv",
    "category_tree": "category_tree.csv",
}

# Wczytanie danych
item_properties_part1 = pd.read_csv(file_paths["item_properties_part1"], nrows=2000000)
item_properties_part2 = pd.read_csv(file_paths["item_properties_part2"], nrows=2000000)
events = pd.read_csv(file_paths["events"], nrows=2000000)
category_tree = pd.read_csv(file_paths["category_tree"])  # Ten plik jest mały, dlatego wczytujemy cały

# Konwersja timestampów do formatu datetime dla czytelności
events['timestamp'] = pd.to_datetime(events['timestamp'], unit='ms', origin='unix')
item_properties_part1['timestamp'] = pd.to_datetime(item_properties_part1['timestamp'], unit='ms', origin='unix')
item_properties_part2['timestamp'] = pd.to_datetime(item_properties_part2['timestamp'], unit='ms', origin='unix')

# Łączenie item_properties
item_properties = pd.concat([item_properties_part1, item_properties_part2], ignore_index=True)

# Usunięcie duplikatów
item_properties = item_properties.drop_duplicates()

# Usuwanie prefiksu 'n' w kolumnie 'value'
item_properties["value"] = item_properties["value"].astype(str)
item_properties["value"] = item_properties["value"].str.replace('n', '', regex=False)

# Sprawdzenie unikalnych wartości w kluczowych kolumnach
print("Unikalne itemid w events:", events["itemid"].nunique())
print("Unikalne itemid w item_properties:", item_properties["itemid"].nunique())

# Łączenie danych z eventami na bazie itemid
merged_data = pd.merge(events, item_properties, on="itemid", how="left")

# Sprawdzenie brakujących wartości po pierwszym merge
print("Braki po pierwszym merge:")
print(merged_data.isnull().sum())

# Konwersja categoryid w category_tree na string
category_tree["categoryid"] = category_tree["categoryid"].astype(str)

# Łączenie z hierarchią kategorii na bazie kolumny 'value'
merged_data = pd.merge(
    merged_data,
    category_tree,
    left_on="value",
    right_on="categoryid",
    how="left"
)

# Sprawdzenie brakujących wartości po drugim merge
print("Braki po drugim merge:")
print(merged_data.isnull().sum())

# Uzupełnianie braków metodą mediany dla kolumn numerycznych
merged_data.fillna(merged_data.median(numeric_only=True), inplace=True)

# Usuwanie rekordów, które nadal mają braki
merged_data.dropna(inplace=True)

# Sprawdzenie brakujących wartości po dropna
print("Braki po dropna:")
print(merged_data.isnull().sum())

# Eksport połączonych danych do pliku CSV
merged_data.head(2000000).to_csv("merged_data2mln.csv", index=False)
