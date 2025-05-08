
## Features

- **Translation Support**: The script can translate UI labels into multiple languages (French, German, Russian, etc.).
- **CSV-based Translation**: The translations are pulled from a CSV hosted on Google Sheets.
- **Flexible Input & Output**: You can specify the input JSON file, output JSON file, and desired target language.

## Requirements

- Python 3.x
- `requests` library (to download CSV from Google Sheets)
- JSON file containing UI labels
- CSV file with translations (hosted on Google Sheets)

### Install dependencies

```bash
pip install requests
```

## Usage

1. **Prepare your JSON file**: Create a JSON file (eg `sample.json`) containing your UI labels in English.

   Example format:
   ```json
   {
     "buttonAddtoCart": "Add to basket",
     "buttonCheckout": "Proceed to checkout",
     "headerTitle": "Welcome to our e-commerce platform"
   }
   ```

2. **Configure the CSV URL**: The translations are pulled from a CSV hosted on Google Sheets. The first column contains the keys (the original English labels), and the subsequent columns contain translations for each language.

   You can access the CSV file with the translations from the following link:

   [Google Sheets - UI Labels Translations](https://docs.google.com/spreadsheets/d/1qCbU-ais-talO3sKCPwp0Qu7848WV_0lX6x-hbSugNs)

   This Google Sheets file contains the necessary translations for UI labels in multiple languages (French, German, Russian, etc.). The script will read this file to perform the translations.

3. **Run the script**: Use the following Python script to translate your JSON file.

   Example command:
   ```bash
   python translate_ui_labels.py
   ```

   By default, the script translates the UI labels into French. You can change the target language by modifying the script as necessary.

4. **Output**: The script will generate a translated JSON file (`ui_labels_translated.json`), which contains the translated UI labels.
