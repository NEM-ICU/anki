import requests
import os
import sys
import json

# Forces Windows terminal output to handle Japanese characters safely without crashing
sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')

# ==== Config ====
ANKI_CONNECT_URL = "http://127.0.0.1:8765"
DECK_NAME = "Japanese::Words"
NOTE_TYPE_NAME = "Word Card" 

FIELD_MAPPING = {
    "Text": "cloze_sentence", 
    "Reading": "reading",
    "Meaning": "meaning",
    "Sentence Translation": "translation",
    "Mnemonic / Notes": "formatted_notes",  
    "Image": "downloaded_image_filename"
}
# =================

word_list = [
    {
        "kanji_or_vocab": "飲む",
        "reading": "のむ",
        "meaning": "to drink",
        "cloze_sentence": "毎日、水を{{c1::飲む::to drink}}。",
        "translation": "I drink water every day.",
        "image_url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c",
        # Type notes naturally here. The code will inject the <br> tags automatically.
        "notes": """Kanji: 飲 = drink 
            Components: 口 = mouth; 欠 = opening the mouth / yawning 
            Mnemonic: Imagine opening your mouth (欠) to drink with your mouth (口).

            Verb Forms: 
            Dictionary form: 飲む (のむ) = to drink 
            Polite form: 飲みます (のみます) = polite present/future form

            Common Phrases: 
            水を飲みます = drink water 
            お茶を飲みます = drink tea 
            コーヒーを飲みます = drink coffee""",
                }
]

def invoke(action, **params):
    """Helper function to talk to AnkiConnect API"""
    payload = {"action": action, "version": 6, "params": params}
    try:
        response = requests.post(ANKI_CONNECT_URL, json=payload).json()
        if response.get("error"):
            print(f"AnkiConnect Error: {response['error']}")
            return None
        return response.get("result")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Anki. Is your Anki desktop app running?")
        return None

def download_and_store_image(vocab, url):
    """Downloads an image via URL and saves it directly inside Anki's media collection folder"""
    if not url:
        return ""
    
    file_extension = os.path.splitext(url.split("?")[0])[1]
    if not file_extension or len(file_extension) > 5:
        file_extension = ".jpg"
        
    filename = f"jlpt_n5_{vocab}{file_extension}"
    
    print(f"  -> Downloading image for '{vocab}'...")
    result = invoke("storeMediaFile", filename=filename, url=url)
    
    if result:
        return f'<img src="{filename}">'
    return ""

def create_anki_cards():
    print(f"Checking/Creating deck: '{DECK_NAME}'...")
    invoke("createDeck", deck=DECK_NAME)
    
    for item in word_list:
        # 1. Handle images safely
        image_html_tag = ""
        if "image_url" in item and item["image_url"]:
            image_html_tag = download_and_store_image(item["kanji_or_vocab"], item["image_url"])
        
        # 2. Turn normal newlines into HTML breaks automatically
        raw_notes = item.get("notes", "")
        formatted_notes = raw_notes.replace("\n", "<br>")
        
        # 3. Assemble data values
        item_data = item.copy()
        item_data["downloaded_image_filename"] = image_html_tag
        item_data["formatted_notes"] = formatted_notes
        
        # 4. Map everything to your real Anki fields
        anki_fields = {}
        for anki_field, source_key in FIELD_MAPPING.items():
            anki_fields[anki_field] = item_data.get(source_key, "")
            
        note = {
            "deckName": DECK_NAME,
            "modelName": NOTE_TYPE_NAME,
            "fields": anki_fields,
            "tags": ["jlpt_n5", "vocab_automation"]
        }
        
        result = invoke("addNote", note=note)
        if result:
            print(f"Successfully added card: {item['kanji_or_vocab']} ({item['reading']})")
        else:
            print(f"Failed to add card: {item['kanji_or_vocab']}.")

if __name__ == "__main__":
    create_anki_cards()
