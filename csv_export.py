import csv

words = [
    {
        "kanji_or_vocab": "高い",
        "reading": "たかい",
        "meaning": "high / expensive",
        "cloze_sentence": "このバッグはとても{{c1::高い::expensive}}です。",
        "translation": "This bag is very expensive.",
        "image_url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c",
        "notes": "Kanji: 高 = tall / high / expensive\nComponents: 高 = high tower structure\nMnemonic: A tall building that costs a lot to build.\n\nWord Type: I-Adjective\n\nGrammar Note:\nCan mean high in altitude/height OR expensive in price.\n\nCommon Phrases:\n背が高い = tall (person)\n物価が高い = cost of living is high"
    },
]

file_path = "jlpt_n5_detailed_template_words_201_300.csv"
fieldnames = ["kanji_or_vocab", "reading", "meaning", "cloze_sentence", "translation", "image_url", "notes"]

with open(file_path, mode="w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for item in words:
        writer.writerow(item)

print(f"Generated {len(words)} items in CSV successfully.")
