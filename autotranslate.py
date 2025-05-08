import csv
import json
import requests

def download_csv_from_sheets(spreadsheet_url):
    csv_url = f"{spreadsheet_url}/export?format=csv"
    response = requests.get(csv_url)
    response.raise_for_status()
    csv_data = response.text.splitlines()
    return list(csv.reader(csv_data))

def load_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)

def translate_json(json_data, translations, target_language):
    translated_data = {}
    for key, value in json_data.items():
        translation = next((row for row in translations if row[0] == key), None)
        if translation:
            lang_column = translations[0].index(target_language)
            translated_data[key] = translation[lang_column]
        else:
            translated_data[key] = value
    return translated_data

def save_translated_json(translated_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(translated_data, file, ensure_ascii=False, indent=4)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1qCbU-ais-talO3sKCPwp0Qu7848WV_0lX6x-hbSugNs'
json_file = 'ui_labels.json'
output_json_file = 'ui_labels_translated.json'

csv_data = download_csv_from_sheets(spreadsheet_url)
json_data = load_json(json_file)
translated_data = translate_json(json_data, csv_data, 'French')
save_translated_json(translated_data, output_json_file)

print(f"Traduction terminée et sauvegardée dans {output_json_file}")
