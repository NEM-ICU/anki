import requests
import sys
import textwrap

# Forces Windows terminal output to handle Japanese characters safely without crashing
sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')

# ==== Config ====
ANKI_CONNECT_URL = "http://127.0.0.1:8765"
DECK_NAME = "Japanese::Jukugo(N5)"
NOTE_TYPE_NAME = "Jukugo"

# Left side = Exact field names in your Anki Note Type
# Right side = Keys from the word_list dictionary below
FIELD_MAPPING = {
    "Word": "word",
    "Reading": "reading",
    "Meaning": "meaning",
    "Breakdown": "formatted_breakdown"
}
# =================

# -*- coding: utf-8 -*-
# Jukugo (compound word) list covering all readings of the listed kanji.

word_list = [
    {
        "word": "一",
        "reading": "いち (ichi)",
        "meaning": "one",
        "breakdown": """\
            一 = いち (one)"""
    },
    {
        "word": "一つ",
        "reading": "ひとつ (hitotsu)",
        "meaning": "one (thing)",
        "breakdown": """\
            一 = ひと (one)
            つ = okurigana"""
    },
    {
        "word": "一人",
        "reading": "ひとり (hitori)",
        "meaning": "one person",
        "breakdown": """\
            一人 = ひとり (irregular reading)"""
    },
    {
        "word": "一月",
        "reading": "いちがつ (ichigatsu)",
        "meaning": "January",
        "breakdown": """\
            一 = いち (one)
            月 = がつ (month / moon)"""
    },
    {
        "word": "一日",
        "reading": "いちにち (ichinichi)",
        "meaning": "one day",
        "breakdown": """\
            一 = いち (one)
            日 = にち (day / sun)"""
    },
    {
        "word": "一日",
        "reading": "ついたち (tsuitachi)",
        "meaning": "first day of the month",
        "breakdown": """\
            一日 = ついたち (irregular reading)"""
    },
    {
        "word": "一年",
        "reading": "いちねん (ichinen)",
        "meaning": "one year",
        "breakdown": """\
            一 = いち (one)
            年 = ねん (year)"""
    },
    {
        "word": "一万",
        "reading": "いちまん (ichiman)",
        "meaning": "ten thousand",
        "breakdown": """\
            一 = いち (one)
            万 = まん (ten thousand)"""
    },
    {
        "word": "一円",
        "reading": "いちえん (ichien)",
        "meaning": "one yen",
        "breakdown": """\
            一 = いち (one)
            円 = えん (yen / circle)"""
    },
    {
        "word": "一万円",
        "reading": "いちまんえん (ichiman'en)",
        "meaning": "ten thousand yen",
        "breakdown": """\
            一 = いち (one)
            万 = まん (ten thousand)
            円 = えん (yen / circle)"""
    },
    {
        "word": "一分",
        "reading": "いっぷん (ippun)",
        "meaning": "one minute",
        "breakdown": """\
            一 = いっ (one)
            分 = ぷん (minute / part)"""
    },
    {
        "word": "一本",
        "reading": "いっぽん (ippon)",
        "meaning": "one (long object)",
        "breakdown": """\
            一 = いっ (one)
            本 = ぽん (book / origin)"""
    },
    {
        "word": "一時",
        "reading": "いちじ (ichiji)",
        "meaning": "one o'clock",
        "breakdown": """\
            一 = いち (one)
            時 = じ (time / hour)"""
    },
    {
        "word": "一足",
        "reading": "いっそく (issoku)",
        "meaning": "one pair (of footwear)",
        "breakdown": """\
            一 = いっ (one)
            足 = そく (foot / leg)"""
    },
    {
        "word": "一生",
        "reading": "いっしょう (isshou)",
        "meaning": "whole life",
        "breakdown": """\
            一 = いっ (one)
            生 = しょう (life / birth)"""
    },
    {
        "word": "一行",
        "reading": "いちぎょう (ichigyou)",
        "meaning": "one line",
        "breakdown": """\
            一 = いち (one)
            行 = ぎょう (go)"""
    },
    {
        "word": "一字",
        "reading": "いちじ (ichiji)",
        "meaning": "one character",
        "breakdown": """\
            一 = いち (one)
            字 = じ (character)"""
    },
    {
        "word": "一言",
        "reading": "ひとこと (hitokoto)",
        "meaning": "a single word",
        "breakdown": """\
            一 = ひと (one)
            言 = こと (say)"""
    },
    {
        "word": "一間",
        "reading": "ひとま (hitoma)",
        "meaning": "one room",
        "breakdown": """\
            一 = ひと (one)
            間 = ま (between / interval)"""
    },
    {
        "word": "一週間",
        "reading": "いっしゅうかん (isshuukan)",
        "meaning": "one week",
        "breakdown": """\
            一 = いっ (one)
            週 = しゅう (week)
            間 = かん (between / interval)"""
    },
    {
        "word": "万一",
        "reading": "まんいち (man'ichi)",
        "meaning": "by any chance",
        "breakdown": """\
            万 = まん (ten thousand)
            一 = いち (one)"""
    },
    {
        "word": "二",
        "reading": "に (ni)",
        "meaning": "two",
        "breakdown": """\
            二 = に (two)"""
    },
    {
        "word": "二つ",
        "reading": "ふたつ (futatsu)",
        "meaning": "two (things)",
        "breakdown": """\
            二 = ふた (two)
            つ = okurigana"""
    },
    {
        "word": "二人",
        "reading": "ふたり (futari)",
        "meaning": "two people",
        "breakdown": """\
            二人 = ふたり (irregular reading)"""
    },
    {
        "word": "二月",
        "reading": "にがつ (nigatsu)",
        "meaning": "February",
        "breakdown": """\
            二 = に (two)
            月 = がつ (month / moon)"""
    },
    {
        "word": "二日",
        "reading": "ふつか (futsuka)",
        "meaning": "second day / two days",
        "breakdown": """\
            二日 = ふつか (irregular reading)"""
    },
    {
        "word": "二十日",
        "reading": "はつか (hatsuka)",
        "meaning": "twentieth day",
        "breakdown": """\
            二十日 = はつか (irregular reading)"""
    },
    {
        "word": "二年",
        "reading": "にねん (ninen)",
        "meaning": "two years",
        "breakdown": """\
            二 = に (two)
            年 = ねん (year)"""
    },
    {
        "word": "二百",
        "reading": "にひゃく (nihyaku)",
        "meaning": "two hundred",
        "breakdown": """\
            二 = に (two)
            百 = ひゃく (hundred)"""
    },
    {
        "word": "二足",
        "reading": "にそく (nisoku)",
        "meaning": "two pairs (of footwear)",
        "breakdown": """\
            二 = に (two)
            足 = そく (foot / leg)"""
    },
    {
        "word": "三",
        "reading": "さん (san)",
        "meaning": "three",
        "breakdown": """\
            三 = さん (three)"""
    },
    {
        "word": "三つ",
        "reading": "みっつ (mittsu)",
        "meaning": "three (things)",
        "breakdown": """\
            三 = みっ (three)
            つ = okurigana"""
    },
    {
        "word": "三月",
        "reading": "さんがつ (sangatsu)",
        "meaning": "March",
        "breakdown": """\
            三 = さん (three)
            月 = がつ (month / moon)"""
    },
    {
        "word": "三日",
        "reading": "みっか (mikka)",
        "meaning": "third day / three days",
        "breakdown": """\
            三日 = みっか (irregular reading)"""
    },
    {
        "word": "三人",
        "reading": "さんにん (sannin)",
        "meaning": "three people",
        "breakdown": """\
            三 = さん (three)
            人 = にん (person)"""
    },
    {
        "word": "三百",
        "reading": "さんびゃく (sanbyaku)",
        "meaning": "three hundred",
        "breakdown": """\
            三 = さん (three)
            百 = びゃく (hundred)"""
    },
    {
        "word": "三千",
        "reading": "さんぜん (sanzen)",
        "meaning": "three thousand",
        "breakdown": """\
            三 = さん (three)
            千 = ぜん (thousand)"""
    },
    {
        "word": "三分",
        "reading": "さんぷん (sanpun)",
        "meaning": "three minutes",
        "breakdown": """\
            三 = さん (three)
            分 = ぷん (minute / part)"""
    },
    {
        "word": "三本",
        "reading": "さんぼん (sanbon)",
        "meaning": "three (long objects)",
        "breakdown": """\
            三 = さん (three)
            本 = ぼん (book / origin)"""
    },
    {
        "word": "三日月",
        "reading": "みかづき (mikazuki)",
        "meaning": "crescent moon",
        "breakdown": """\
            三 = み (three)
            日 = か (day / sun)
            月 = づき (month / moon)"""
    },
    {
        "word": "三時半",
        "reading": "さんじはん (sanjihan)",
        "meaning": "half past three",
        "breakdown": """\
            三 = さん (three)
            時 = じ (time / hour)
            半 = はん (half)"""
    },
    {
        "word": "四",
        "reading": "し (shi)",
        "meaning": "four",
        "breakdown": """\
            四 = し (four)"""
    },
    {
        "word": "四",
        "reading": "よん (yon)",
        "meaning": "four",
        "breakdown": """\
            四 = よん (four)"""
    },
    {
        "word": "四つ",
        "reading": "よっつ (yottsu)",
        "meaning": "four (things)",
        "breakdown": """\
            四 = よっ (four)
            つ = okurigana"""
    },
    {
        "word": "四月",
        "reading": "しがつ (shigatsu)",
        "meaning": "April",
        "breakdown": """\
            四 = し (four)
            月 = がつ (month / moon)"""
    },
    {
        "word": "四日",
        "reading": "よっか (yokka)",
        "meaning": "fourth day / four days",
        "breakdown": """\
            四日 = よっか (irregular reading)"""
    },
    {
        "word": "四人",
        "reading": "よにん (yonin)",
        "meaning": "four people",
        "breakdown": """\
            四人 = よにん (irregular reading)"""
    },
    {
        "word": "四時",
        "reading": "よじ (yoji)",
        "meaning": "four o'clock",
        "breakdown": """\
            四 = よ (four)
            時 = じ (time / hour)"""
    },
    {
        "word": "四百",
        "reading": "よんひゃく (yonhyaku)",
        "meaning": "four hundred",
        "breakdown": """\
            四 = よん (four)
            百 = ひゃく (hundred)"""
    },
    {
        "word": "四千",
        "reading": "よんせん (yonsen)",
        "meaning": "four thousand",
        "breakdown": """\
            四 = よん (four)
            千 = せん (thousand)"""
    },
    {
        "word": "五",
        "reading": "ご (go)",
        "meaning": "five",
        "breakdown": """\
            五 = ご (five)"""
    },
    {
        "word": "五つ",
        "reading": "いつつ (itsutsu)",
        "meaning": "five (things)",
        "breakdown": """\
            五 = いつ (five)
            つ = okurigana"""
    },
    {
        "word": "五月",
        "reading": "ごがつ (gogatsu)",
        "meaning": "May",
        "breakdown": """\
            五 = ご (five)
            月 = がつ (month / moon)"""
    },
    {
        "word": "五日",
        "reading": "いつか (itsuka)",
        "meaning": "fifth day / five days",
        "breakdown": """\
            五日 = いつか (irregular reading)"""
    },
    {
        "word": "五人",
        "reading": "ごにん (gonin)",
        "meaning": "five people",
        "breakdown": """\
            五 = ご (five)
            人 = にん (person)"""
    },
    {
        "word": "五円",
        "reading": "ごえん (goen)",
        "meaning": "five yen",
        "breakdown": """\
            五 = ご (five)
            円 = えん (yen / circle)"""
    },
    {
        "word": "五百",
        "reading": "ごひゃく (gohyaku)",
        "meaning": "five hundred",
        "breakdown": """\
            五 = ご (five)
            百 = ひゃく (hundred)"""
    },
    {
        "word": "五分",
        "reading": "ごふん (gofun)",
        "meaning": "five minutes",
        "breakdown": """\
            五 = ご (five)
            分 = ふん (minute / part)"""
    },
    {
        "word": "六",
        "reading": "ろく (roku)",
        "meaning": "six",
        "breakdown": """\
            六 = ろく (six)"""
    },
    {
        "word": "六つ",
        "reading": "むっつ (muttsu)",
        "meaning": "six (things)",
        "breakdown": """\
            六 = むっ (six)
            つ = okurigana"""
    },
    {
        "word": "六月",
        "reading": "ろくがつ (rokugatsu)",
        "meaning": "June",
        "breakdown": """\
            六 = ろく (six)
            月 = がつ (month / moon)"""
    },
    {
        "word": "六日",
        "reading": "むいか (muika)",
        "meaning": "sixth day / six days",
        "breakdown": """\
            六日 = むいか (irregular reading)"""
    },
    {
        "word": "六人",
        "reading": "ろくにん (rokunin)",
        "meaning": "six people",
        "breakdown": """\
            六 = ろく (six)
            人 = にん (person)"""
    },
    {
        "word": "六百",
        "reading": "ろっぴゃく (roppyaku)",
        "meaning": "six hundred",
        "breakdown": """\
            六 = ろっ (six)
            百 = ぴゃく (hundred)"""
    },
    {
        "word": "六本",
        "reading": "ろっぽん (roppon)",
        "meaning": "six (long objects)",
        "breakdown": """\
            六 = ろっ (six)
            本 = ぽん (book / origin)"""
    },
    {
        "word": "七",
        "reading": "しち (shichi)",
        "meaning": "seven",
        "breakdown": """\
            七 = しち (seven)"""
    },
    {
        "word": "七",
        "reading": "なな (nana)",
        "meaning": "seven",
        "breakdown": """\
            七 = なな (seven)"""
    },
    {
        "word": "七つ",
        "reading": "ななつ (nanatsu)",
        "meaning": "seven (things)",
        "breakdown": """\
            七 = なな (seven)
            つ = okurigana"""
    },
    {
        "word": "七月",
        "reading": "しちがつ (shichigatsu)",
        "meaning": "July",
        "breakdown": """\
            七 = しち (seven)
            月 = がつ (month / moon)"""
    },
    {
        "word": "七日",
        "reading": "なのか (nanoka)",
        "meaning": "seventh day / seven days",
        "breakdown": """\
            七日 = なのか (irregular reading)"""
    },
    {
        "word": "七人",
        "reading": "しちにん (shichinin)",
        "meaning": "seven people",
        "breakdown": """\
            七 = しち (seven)
            人 = にん (person)"""
    },
    {
        "word": "七時",
        "reading": "しちじ (shichiji)",
        "meaning": "seven o'clock",
        "breakdown": """\
            七 = しち (seven)
            時 = じ (time / hour)"""
    },
    {
        "word": "八",
        "reading": "はち (hachi)",
        "meaning": "eight",
        "breakdown": """\
            八 = はち (eight)"""
    },
    {
        "word": "八つ",
        "reading": "やっつ (yattsu)",
        "meaning": "eight (things)",
        "breakdown": """\
            八 = やっ (eight)
            つ = okurigana"""
    },
    {
        "word": "八月",
        "reading": "はちがつ (hachigatsu)",
        "meaning": "August",
        "breakdown": """\
            八 = はち (eight)
            月 = がつ (month / moon)"""
    },
    {
        "word": "八日",
        "reading": "ようか (youka)",
        "meaning": "eighth day / eight days",
        "breakdown": """\
            八日 = ようか (irregular reading)"""
    },
    {
        "word": "八人",
        "reading": "はちにん (hachinin)",
        "meaning": "eight people",
        "breakdown": """\
            八 = はち (eight)
            人 = にん (person)"""
    },
    {
        "word": "八百",
        "reading": "はっぴゃく (happyaku)",
        "meaning": "eight hundred",
        "breakdown": """\
            八 = はっ (eight)
            百 = ぴゃく (hundred)"""
    },
    {
        "word": "九",
        "reading": "きゅう (kyuu)",
        "meaning": "nine",
        "breakdown": """\
            九 = きゅう (nine)"""
    },
    {
        "word": "九",
        "reading": "く (ku)",
        "meaning": "nine",
        "breakdown": """\
            九 = く (nine)"""
    },
    {
        "word": "九つ",
        "reading": "ここのつ (kokonotsu)",
        "meaning": "nine (things)",
        "breakdown": """\
            九 = ここの (nine)
            つ = okurigana"""
    },
    {
        "word": "九月",
        "reading": "くがつ (kugatsu)",
        "meaning": "September",
        "breakdown": """\
            九 = く (nine)
            月 = がつ (month / moon)"""
    },
    {
        "word": "九日",
        "reading": "ここのか (kokonoka)",
        "meaning": "ninth day / nine days",
        "breakdown": """\
            九日 = ここのか (irregular reading)"""
    },
    {
        "word": "九時",
        "reading": "くじ (kuji)",
        "meaning": "nine o'clock",
        "breakdown": """\
            九 = く (nine)
            時 = じ (time / hour)"""
    },
    {
        "word": "九人",
        "reading": "きゅうにん (kyuunin)",
        "meaning": "nine people",
        "breakdown": """\
            九 = きゅう (nine)
            人 = にん (person)"""
    },
    {
        "word": "十",
        "reading": "じゅう (juu)",
        "meaning": "ten",
        "breakdown": """\
            十 = じゅう (ten)"""
    },
    {
        "word": "十",
        "reading": "とお (too)",
        "meaning": "ten (things)",
        "breakdown": """\
            十 = とお (ten)"""
    },
    {
        "word": "十月",
        "reading": "じゅうがつ (juugatsu)",
        "meaning": "October",
        "breakdown": """\
            十 = じゅう (ten)
            月 = がつ (month / moon)"""
    },
    {
        "word": "十日",
        "reading": "とおか (tooka)",
        "meaning": "tenth day / ten days",
        "breakdown": """\
            十日 = とおか (irregular reading)"""
    },
    {
        "word": "十人",
        "reading": "じゅうにん (juunin)",
        "meaning": "ten people",
        "breakdown": """\
            十 = じゅう (ten)
            人 = にん (person)"""
    },
    {
        "word": "十円",
        "reading": "じゅうえん (juuen)",
        "meaning": "ten yen",
        "breakdown": """\
            十 = じゅう (ten)
            円 = えん (yen / circle)"""
    },
    {
        "word": "十分",
        "reading": "じゅっぷん (juppun)",
        "meaning": "ten minutes",
        "breakdown": """\
            十 = じゅっ (ten)
            分 = ぷん (minute / part)"""
    },
    {
        "word": "十分",
        "reading": "じゅうぶん (juubun)",
        "meaning": "enough",
        "breakdown": """\
            十 = じゅう (ten)
            分 = ぶん (minute / part)"""
    },
    {
        "word": "十本",
        "reading": "じゅっぽん (juppon)",
        "meaning": "ten (long objects)",
        "breakdown": """\
            十 = じゅっ (ten)
            本 = ぽん (book / origin)"""
    },
    {
        "word": "十字",
        "reading": "じゅうじ (juuji)",
        "meaning": "cross",
        "breakdown": """\
            十 = じゅう (ten)
            字 = じ (character)"""
    },
    {
        "word": "百",
        "reading": "ひゃく (hyaku)",
        "meaning": "hundred",
        "breakdown": """\
            百 = ひゃく (hundred)"""
    },
    {
        "word": "百円",
        "reading": "ひゃくえん (hyakuen)",
        "meaning": "one hundred yen",
        "breakdown": """\
            百 = ひゃく (hundred)
            円 = えん (yen / circle)"""
    },
    {
        "word": "百人",
        "reading": "ひゃくにん (hyakunin)",
        "meaning": "one hundred people",
        "breakdown": """\
            百 = ひゃく (hundred)
            人 = にん (person)"""
    },
    {
        "word": "百万",
        "reading": "ひゃくまん (hyakuman)",
        "meaning": "one million",
        "breakdown": """\
            百 = ひゃく (hundred)
            万 = まん (ten thousand)"""
    },
    {
        "word": "千",
        "reading": "せん (sen)",
        "meaning": "thousand",
        "breakdown": """\
            千 = せん (thousand)"""
    },
    {
        "word": "千円",
        "reading": "せんえん (sen'en)",
        "meaning": "one thousand yen",
        "breakdown": """\
            千 = せん (thousand)
            円 = えん (yen / circle)"""
    },
    {
        "word": "千年",
        "reading": "せんねん (sennen)",
        "meaning": "one thousand years",
        "breakdown": """\
            千 = せん (thousand)
            年 = ねん (year)"""
    },
    {
        "word": "千人",
        "reading": "せんにん (sennin)",
        "meaning": "one thousand people",
        "breakdown": """\
            千 = せん (thousand)
            人 = にん (person)"""
    },
    {
        "word": "万",
        "reading": "まん (man)",
        "meaning": "ten thousand",
        "breakdown": """\
            万 = まん (ten thousand)"""
    },
    {
        "word": "万年",
        "reading": "まんねん (mannen)",
        "meaning": "ten thousand years / eternity",
        "breakdown": """\
            万 = まん (ten thousand)
            年 = ねん (year)"""
    },
    {
        "word": "万円",
        "reading": "まんえん (man'en)",
        "meaning": "ten thousand yen",
        "breakdown": """\
            万 = まん (ten thousand)
            円 = えん (yen / circle)"""
    },
    {
        "word": "円",
        "reading": "えん (en)",
        "meaning": "yen",
        "breakdown": """\
            円 = えん (yen / circle)"""
    },
    {
        "word": "円高",
        "reading": "えんだか (endaka)",
        "meaning": "strong yen",
        "breakdown": """\
            円 = えん (yen / circle)
            高 = だか (tall / expensive)"""
    },
    {
        "word": "円安",
        "reading": "えんやす (en'yasu)",
        "meaning": "weak yen",
        "breakdown": """\
            円 = えん (yen / circle)
            安 = やす (cheap / safe)"""
    },
    {
        "word": "日",
        "reading": "ひ (hi)",
        "meaning": "day / sun",
        "breakdown": """\
            日 = ひ (day / sun)"""
    },
    {
        "word": "日",
        "reading": "にち (nichi)",
        "meaning": "day",
        "breakdown": """\
            日 = にち (day / sun)"""
    },
    {
        "word": "毎日",
        "reading": "まいにち (mainichi)",
        "meaning": "every day",
        "breakdown": """\
            毎 = まい (every)
            日 = にち (day / sun)"""
    },
    {
        "word": "今日",
        "reading": "きょう (kyou)",
        "meaning": "today",
        "breakdown": """\
            今日 = きょう (irregular reading)"""
    },
    {
        "word": "明日",
        "reading": "あした (ashita)",
        "meaning": "tomorrow",
        "breakdown": """\
            明日 = あした (irregular reading)"""
    },
    {
        "word": "明日",
        "reading": "みょうにち (myounichi)",
        "meaning": "tomorrow (formal)",
        "breakdown": """\
            明 = みょう (bright)
            日 = にち (day / sun)"""
    },
    {
        "word": "日本",
        "reading": "にほん (nihon)",
        "meaning": "Japan",
        "breakdown": """\
            日 = に (day / sun)
            本 = ほん (book / origin)"""
    },
    {
        "word": "日本",
        "reading": "にっぽん (nippon)",
        "meaning": "Japan (formal)",
        "breakdown": """\
            日 = にっ (day / sun)
            本 = ぽん (book / origin)"""
    },
    {
        "word": "日曜日",
        "reading": "にちようび (nichiyoubi)",
        "meaning": "Sunday",
        "breakdown": """\
            日 = にち (day / sun)
            曜 = よう (weekday)
            日 = び (day / sun)"""
    },
    {
        "word": "日中",
        "reading": "にっちゅう (nitchuu)",
        "meaning": "daytime",
        "breakdown": """\
            日 = にっ (day / sun)
            中 = ちゅう (inside / middle)"""
    },
    {
        "word": "一日中",
        "reading": "いちにちじゅう (ichinichijuu)",
        "meaning": "all day long",
        "breakdown": """\
            一 = いち (one)
            日 = にち (day / sun)
            中 = じゅう (inside / middle)"""
    },
    {
        "word": "休日",
        "reading": "きゅうじつ (kyuujitsu)",
        "meaning": "day off / holiday",
        "breakdown": """\
            休 = きゅう (rest)
            日 = じつ (day / sun)"""
    },
    {
        "word": "来日",
        "reading": "らいにち (rainichi)",
        "meaning": "coming to Japan",
        "breakdown": """\
            来 = らい (come)
            日 = にち (day / sun)"""
    },
    {
        "word": "半日",
        "reading": "はんにち (hannichi)",
        "meaning": "half a day",
        "breakdown": """\
            半 = はん (half)
            日 = にち (day / sun)"""
    },
    {
        "word": "前日",
        "reading": "ぜんじつ (zenjitsu)",
        "meaning": "the previous day",
        "breakdown": """\
            前 = ぜん (before / front)
            日 = じつ (day / sun)"""
    },
    {
        "word": "後日",
        "reading": "ごじつ (gojitsu)",
        "meaning": "at a later date",
        "breakdown": """\
            後 = ご (after / behind)
            日 = じつ (day / sun)"""
    },
    {
        "word": "先日",
        "reading": "せんじつ (senjitsu)",
        "meaning": "the other day",
        "breakdown": """\
            先 = せん (previous / ahead)
            日 = じつ (day / sun)"""
    },
    {
        "word": "本日",
        "reading": "ほんじつ (honjitsu)",
        "meaning": "today (formal)",
        "breakdown": """\
            本 = ほん (book / origin)
            日 = じつ (day / sun)"""
    },
    {
        "word": "西日",
        "reading": "にしび (nishibi)",
        "meaning": "western sun",
        "breakdown": """\
            西 = にし (west)
            日 = び (day / sun)"""
    },
    {
        "word": "土日",
        "reading": "どにち (donichi)",
        "meaning": "Saturday and Sunday",
        "breakdown": """\
            土 = ど (earth)
            日 = にち (day / sun)"""
    },
    {
        "word": "火",
        "reading": "ひ (hi)",
        "meaning": "fire",
        "breakdown": """\
            火 = ひ (fire)"""
    },
    {
        "word": "火曜日",
        "reading": "かようび (kayoubi)",
        "meaning": "Tuesday",
        "breakdown": """\
            火 = か (fire)
            曜 = よう (weekday)
            日 = び (day / sun)"""
    },
    {
        "word": "火山",
        "reading": "かざん (kazan)",
        "meaning": "volcano",
        "breakdown": """\
            火 = か (fire)
            山 = ざん (mountain)"""
    },
    {
        "word": "火花",
        "reading": "ひばな (hibana)",
        "meaning": "spark",
        "breakdown": """\
            火 = ひ (fire)
            花 = ばな (flower)"""
    },
    {
        "word": "花火",
        "reading": "はなび (hanabi)",
        "meaning": "fireworks",
        "breakdown": """\
            花 = はな (flower)
            火 = び (fire)"""
    },
    {
        "word": "休火山",
        "reading": "きゅうかざん (kyuukazan)",
        "meaning": "dormant volcano",
        "breakdown": """\
            休 = きゅう (rest)
            火 = か (fire)
            山 = ざん (mountain)"""
    },
    {
        "word": "水",
        "reading": "みず (mizu)",
        "meaning": "water",
        "breakdown": """\
            水 = みず (water)"""
    },
    {
        "word": "水曜日",
        "reading": "すいようび (suiyoubi)",
        "meaning": "Wednesday",
        "breakdown": """\
            水 = すい (water)
            曜 = よう (weekday)
            日 = び (day / sun)"""
    },
    {
        "word": "水道",
        "reading": "すいどう (suidou)",
        "meaning": "water supply",
        "breakdown": """\
            水 = すい (water)
            道 = どう (road / way)"""
    },
    {
        "word": "水田",
        "reading": "すいでん (suiden)",
        "meaning": "paddy field",
        "breakdown": """\
            水 = すい (water)
            田 = でん (rice field)"""
    },
    {
        "word": "水中",
        "reading": "すいちゅう (suichuu)",
        "meaning": "underwater",
        "breakdown": """\
            水 = すい (water)
            中 = ちゅう (inside / middle)"""
    },
    {
        "word": "雨水",
        "reading": "あまみず (amamizu)",
        "meaning": "rainwater",
        "breakdown": """\
            雨 = あま (rain)
            水 = みず (water)"""
    },
    {
        "word": "山水",
        "reading": "さんすい (sansui)",
        "meaning": "landscape",
        "breakdown": """\
            山 = さん (mountain)
            水 = すい (water)"""
    },
    {
        "word": "生水",
        "reading": "なまみず (namamizu)",
        "meaning": "unboiled water",
        "breakdown": """\
            生 = なま (life / birth)
            水 = みず (water)"""
    },
    {
        "word": "下水",
        "reading": "げすい (gesui)",
        "meaning": "sewage",
        "breakdown": """\
            下 = げ (below)
            水 = すい (water)"""
    },
    {
        "word": "入水",
        "reading": "にゅうすい (nyuusui)",
        "meaning": "entering water",
        "breakdown": """\
            入 = にゅう (enter)
            水 = すい (water)"""
    },
    {
        "word": "飲み水",
        "reading": "のみみず (nomimizu)",
        "meaning": "drinking water",
        "breakdown": """\
            飲 = の (drink)
            み = okurigana
            水 = みず (water)"""
    },
    {
        "word": "木",
        "reading": "き (ki)",
        "meaning": "tree",
        "breakdown": """\
            木 = き (tree)"""
    },
    {
        "word": "木曜日",
        "reading": "もくようび (mokuyoubi)",
        "meaning": "Thursday",
        "breakdown": """\
            木 = もく (tree)
            曜 = よう (weekday)
            日 = び (day / sun)"""
    },
    {
        "word": "大木",
        "reading": "たいぼく (taiboku)",
        "meaning": "large tree",
        "breakdown": """\
            大 = たい (big)
            木 = ぼく (tree)"""
    },
    {
        "word": "木立",
        "reading": "こだち (kodachi)",
        "meaning": "grove",
        "breakdown": """\
            木 = こ (tree)
            立 = だち (stand)"""
    },
    {
        "word": "土木",
        "reading": "どぼく (doboku)",
        "meaning": "civil engineering",
        "breakdown": """\
            土 = ど (earth)
            木 = ぼく (tree)"""
    },
    {
        "word": "金",
        "reading": "かね (kane)",
        "meaning": "money",
        "breakdown": """\
            金 = かね (gold / money)"""
    },
    {
        "word": "金",
        "reading": "きん (kin)",
        "meaning": "gold",
        "breakdown": """\
            金 = きん (gold / money)"""
    },
    {
        "word": "金曜日",
        "reading": "きんようび (kin'youbi)",
        "meaning": "Friday",
        "breakdown": """\
            金 = きん (gold / money)
            曜 = よう (weekday)
            日 = び (day / sun)"""
    },
    {
        "word": "金魚",
        "reading": "きんぎょ (kingyo)",
        "meaning": "goldfish",
        "breakdown": """\
            金 = きん (gold / money)
            魚 = ぎょ (fish)"""
    },
    {
        "word": "金山",
        "reading": "きんざん (kinzan)",
        "meaning": "gold mine",
        "breakdown": """\
            金 = きん (gold / money)
            山 = ざん (mountain)"""
    },
    {
        "word": "大金",
        "reading": "たいきん (taikin)",
        "meaning": "large sum of money",
        "breakdown": """\
            大 = たい (big)
            金 = きん (gold / money)"""
    },
    {
        "word": "小金",
        "reading": "こがね (kogane)",
        "meaning": "small savings",
        "breakdown": """\
            小 = こ (small)
            金 = がね (gold / money)"""
    },
    {
        "word": "入金",
        "reading": "にゅうきん (nyuukin)",
        "meaning": "deposit",
        "breakdown": """\
            入 = にゅう (enter)
            金 = きん (gold / money)"""
    },
    {
        "word": "出金",
        "reading": "しゅっきん (shukkin)",
        "meaning": "withdrawal",
        "breakdown": """\
            出 = しゅっ (exit / take out)
            金 = きん (gold / money)"""
    },
    {
        "word": "白金",
        "reading": "はっきん (hakkin)",
        "meaning": "platinum",
        "breakdown": """\
            白 = はっ (white)
            金 = きん (gold / money)"""
    },
    {
        "word": "口金",
        "reading": "くちがね (kuchigane)",
        "meaning": "clasp / cap",
        "breakdown": """\
            口 = くち (mouth)
            金 = がね (gold / money)"""
    },
    {
        "word": "土",
        "reading": "つち (tsuchi)",
        "meaning": "earth / soil",
        "breakdown": """\
            土 = つち (earth)"""
    },
    {
        "word": "土曜日",
        "reading": "どようび (doyoubi)",
        "meaning": "Saturday",
        "breakdown": """\
            土 = ど (earth)
            曜 = よう (weekday)
            日 = び (day / sun)"""
    },
    {
        "word": "土手",
        "reading": "どて (dote)",
        "meaning": "embankment",
        "breakdown": """\
            土 = ど (earth)
            手 = て (hand)"""
    },
    {
        "word": "土足",
        "reading": "どそく (dosoku)",
        "meaning": "shoes on (indoors)",
        "breakdown": """\
            土 = ど (earth)
            足 = そく (foot / leg)"""
    },
    {
        "word": "土中",
        "reading": "どちゅう (dochuu)",
        "meaning": "underground",
        "breakdown": """\
            土 = ど (earth)
            中 = ちゅう (inside / middle)"""
    },
    {
        "word": "赤土",
        "reading": "あかつち (akatsuchi)",
        "meaning": "red soil",
        "breakdown": """\
            赤 = あか (red)
            土 = つち (earth)"""
    },
    {
        "word": "国土",
        "reading": "こくど (kokudo)",
        "meaning": "national territory",
        "breakdown": """\
            国 = こく (country)
            土 = ど (earth)"""
    },
    {
        "word": "年",
        "reading": "とし (toshi)",
        "meaning": "year",
        "breakdown": """\
            年 = とし (year)"""
    },
    {
        "word": "今年",
        "reading": "ことし (kotoshi)",
        "meaning": "this year",
        "breakdown": """\
            今年 = ことし (irregular reading)"""
    },
    {
        "word": "毎年",
        "reading": "まいとし (maitoshi)",
        "meaning": "every year",
        "breakdown": """\
            毎 = まい (every)
            年 = とし (year)"""
    },
    {
        "word": "毎年",
        "reading": "まいねん (mainen)",
        "meaning": "every year",
        "breakdown": """\
            毎 = まい (every)
            年 = ねん (year)"""
    },
    {
        "word": "来年",
        "reading": "らいねん (rainen)",
        "meaning": "next year",
        "breakdown": """\
            来 = らい (come)
            年 = ねん (year)"""
    },
    {
        "word": "年上",
        "reading": "としうえ (toshiue)",
        "meaning": "older",
        "breakdown": """\
            年 = とし (year)
            上 = うえ (above)"""
    },
    {
        "word": "年下",
        "reading": "としした (toshishita)",
        "meaning": "younger",
        "breakdown": """\
            年 = とし (year)
            下 = した (below)"""
    },
    {
        "word": "少年",
        "reading": "しょうねん (shounen)",
        "meaning": "boy / youth",
        "breakdown": """\
            少 = しょう (few)
            年 = ねん (year)"""
    },
    {
        "word": "新年",
        "reading": "しんねん (shinnen)",
        "meaning": "new year",
        "breakdown": """\
            新 = しん (new)
            年 = ねん (year)"""
    },
    {
        "word": "年中",
        "reading": "ねんじゅう (nenjuu)",
        "meaning": "all year round",
        "breakdown": """\
            年 = ねん (year)
            中 = じゅう (inside / middle)"""
    },
    {
        "word": "年月",
        "reading": "としつき (toshitsuki)",
        "meaning": "years and months",
        "breakdown": """\
            年 = とし (year)
            月 = つき (month / moon)"""
    },
    {
        "word": "年月",
        "reading": "ねんげつ (nengetsu)",
        "meaning": "years and months",
        "breakdown": """\
            年 = ねん (year)
            月 = げつ (month / moon)"""
    },
    {
        "word": "学年",
        "reading": "がくねん (gakunen)",
        "meaning": "school year",
        "breakdown": """\
            学 = がく (study)
            年 = ねん (year)"""
    },
    {
        "word": "生年",
        "reading": "せいねん (seinen)",
        "meaning": "year of birth",
        "breakdown": """\
            生 = せい (life / birth)
            年 = ねん (year)"""
    },
    {
        "word": "長年",
        "reading": "ながねん (naganen)",
        "meaning": "many years",
        "breakdown": """\
            長 = なが (long)
            年 = ねん (year)"""
    },
    {
        "word": "半年",
        "reading": "はんとし (hantoshi)",
        "meaning": "half a year",
        "breakdown": """\
            半 = はん (half)
            年 = とし (year)"""
    },
    {
        "word": "前年",
        "reading": "ぜんねん (zennen)",
        "meaning": "previous year",
        "breakdown": """\
            前 = ぜん (before / front)
            年 = ねん (year)"""
    },
    {
        "word": "本年",
        "reading": "ほんねん (honnen)",
        "meaning": "this year",
        "breakdown": """\
            本 = ほん (book / origin)
            年 = ねん (year)"""
    },
    {
        "word": "多年",
        "reading": "たねん (tanen)",
        "meaning": "many years",
        "breakdown": """\
            多 = た (many)
            年 = ねん (year)"""
    },
    {
        "word": "青年",
        "reading": "せいねん (seinen)",
        "meaning": "young man",
        "breakdown": """\
            青 = せい (blue)
            年 = ねん (year)"""
    },
    {
        "word": "後年",
        "reading": "こうねん (kounen)",
        "meaning": "later years",
        "breakdown": """\
            後 = こう (after / behind)
            年 = ねん (year)"""
    },
    {
        "word": "高年",
        "reading": "こうねん (kounen)",
        "meaning": "old age",
        "breakdown": """\
            高 = こう (tall / expensive)
            年 = ねん (year)"""
    },
    {
        "word": "時",
        "reading": "とき (toki)",
        "meaning": "time",
        "breakdown": """\
            時 = とき (time / hour)"""
    },
    {
        "word": "時",
        "reading": "じ (ji)",
        "meaning": "o'clock",
        "breakdown": """\
            時 = じ (time / hour)"""
    },
    {
        "word": "何時",
        "reading": "なんじ (nanji)",
        "meaning": "what time",
        "breakdown": """\
            何 = なん (what)
            時 = じ (time / hour)"""
    },
    {
        "word": "時間",
        "reading": "じかん (jikan)",
        "meaning": "time / hours",
        "breakdown": """\
            時 = じ (time / hour)
            間 = かん (between / interval)"""
    },
    {
        "word": "分",
        "reading": "ふん (fun)",
        "meaning": "minute",
        "breakdown": """\
            分 = ふん (minute / part)"""
    },
    {
        "word": "分",
        "reading": "ぷん (pun)",
        "meaning": "minute",
        "breakdown": """\
            分 = ぷん (minute / part)"""
    },
    {
        "word": "分かる",
        "reading": "わかる (wakaru)",
        "meaning": "to understand",
        "breakdown": """\
            分 = わ (minute / part)
            かる = okurigana"""
    },
    {
        "word": "半分",
        "reading": "はんぶん (hanbun)",
        "meaning": "half",
        "breakdown": """\
            半 = はん (half)
            分 = ぶん (minute / part)"""
    },
    {
        "word": "大分",
        "reading": "だいぶ (daibu)",
        "meaning": "considerably",
        "breakdown": """\
            大 = だい (big)
            分 = ぶ (minute / part)"""
    },
    {
        "word": "多分",
        "reading": "たぶん (tabun)",
        "meaning": "probably",
        "breakdown": """\
            多 = た (many)
            分 = ぶん (minute / part)"""
    },
    {
        "word": "何分",
        "reading": "なんぷん (nanpun)",
        "meaning": "how many minutes",
        "breakdown": """\
            何 = なん (what)
            分 = ぷん (minute / part)"""
    },
    {
        "word": "半",
        "reading": "はん (han)",
        "meaning": "half",
        "breakdown": """\
            半 = はん (half)"""
    },
    {
        "word": "半月",
        "reading": "はんつき (hantsuki)",
        "meaning": "half moon",
        "breakdown": """\
            半 = はん (half)
            月 = つき (month / moon)"""
    },
    {
        "word": "午前",
        "reading": "ごぜん (gozen)",
        "meaning": "morning / a.m.",
        "breakdown": """\
            午 = ご (noon)
            前 = ぜん (before / front)"""
    },
    {
        "word": "午後",
        "reading": "ごご (gogo)",
        "meaning": "afternoon / p.m.",
        "breakdown": """\
            午 = ご (noon)
            後 = ご (after / behind)"""
    },
    {
        "word": "午前中",
        "reading": "ごぜんちゅう (gozenchuu)",
        "meaning": "during the morning",
        "breakdown": """\
            午 = ご (noon)
            前 = ぜん (before / front)
            中 = ちゅう (inside / middle)"""
    },
    {
        "word": "前",
        "reading": "まえ (mae)",
        "meaning": "before / front",
        "breakdown": """\
            前 = まえ (before / front)"""
    },
    {
        "word": "名前",
        "reading": "なまえ (namae)",
        "meaning": "name",
        "breakdown": """\
            名 = な (name)
            前 = まえ (before / front)"""
    },
    {
        "word": "前後",
        "reading": "ぜんご (zengo)",
        "meaning": "before and after",
        "breakdown": """\
            前 = ぜん (before / front)
            後 = ご (after / behind)"""
    },
    {
        "word": "前半",
        "reading": "ぜんはん (zenhan)",
        "meaning": "first half",
        "breakdown": """\
            前 = ぜん (before / front)
            半 = はん (half)"""
    },
    {
        "word": "一年前",
        "reading": "いちねんまえ (ichinenmae)",
        "meaning": "one year ago",
        "breakdown": """\
            一 = いち (one)
            年 = ねん (year)
            前 = まえ (before / front)"""
    },
    {
        "word": "気前",
        "reading": "きまえ (kimae)",
        "meaning": "generosity",
        "breakdown": """\
            気 = き (spirit / energy)
            前 = まえ (before / front)"""
    },
    {
        "word": "人前",
        "reading": "ひとまえ (hitomae)",
        "meaning": "in public",
        "breakdown": """\
            人 = ひと (person)
            前 = まえ (before / front)"""
    },
    {
        "word": "出前",
        "reading": "でまえ (demae)",
        "meaning": "delivery",
        "breakdown": """\
            出 = で (exit / take out)
            前 = まえ (before / front)"""
    },
    {
        "word": "手前",
        "reading": "てまえ (temae)",
        "meaning": "this side / in front",
        "breakdown": """\
            手 = て (hand)
            前 = まえ (before / front)"""
    },
    {
        "word": "食前",
        "reading": "しょくぜん (shokuzen)",
        "meaning": "before meals",
        "breakdown": """\
            食 = しょく (eat)
            前 = ぜん (before / front)"""
    },
    {
        "word": "目前",
        "reading": "もくぜん (mokuzen)",
        "meaning": "before one's eyes",
        "breakdown": """\
            目 = もく (eye)
            前 = ぜん (before / front)"""
    },
    {
        "word": "後",
        "reading": "あと (ato)",
        "meaning": "after",
        "breakdown": """\
            後 = あと (after / behind)"""
    },
    {
        "word": "後ろ",
        "reading": "うしろ (ushiro)",
        "meaning": "behind",
        "breakdown": """\
            後 = うし (after / behind)
            ろ = okurigana"""
    },
    {
        "word": "後半",
        "reading": "こうはん (kouhan)",
        "meaning": "second half",
        "breakdown": """\
            後 = こう (after / behind)
            半 = はん (half)"""
    },
    {
        "word": "今後",
        "reading": "こんご (kongo)",
        "meaning": "from now on",
        "breakdown": """\
            今 = こん (now)
            後 = ご (after / behind)"""
    },
    {
        "word": "食後",
        "reading": "しょくご (shokugo)",
        "meaning": "after meals",
        "breakdown": """\
            食 = しょく (eat)
            後 = ご (after / behind)"""
    },
    {
        "word": "読後",
        "reading": "どくご (dokugo)",
        "meaning": "after reading",
        "breakdown": """\
            読 = どく (read)
            後 = ご (after / behind)"""
    },
    {
        "word": "毎",
        "reading": "まい (mai)",
        "meaning": "every",
        "breakdown": """\
            毎 = まい (every)"""
    },
    {
        "word": "毎月",
        "reading": "まいつき (maitsuki)",
        "meaning": "every month",
        "breakdown": """\
            毎 = まい (every)
            月 = つき (month / moon)"""
    },
    {
        "word": "毎月",
        "reading": "まいげつ (maigetsu)",
        "meaning": "every month",
        "breakdown": """\
            毎 = まい (every)
            月 = げつ (month / moon)"""
    },
    {
        "word": "毎週",
        "reading": "まいしゅう (maishuu)",
        "meaning": "every week",
        "breakdown": """\
            毎 = まい (every)
            週 = しゅう (week)"""
    },
    {
        "word": "毎時",
        "reading": "まいじ (maiji)",
        "meaning": "every hour",
        "breakdown": """\
            毎 = まい (every)
            時 = じ (time / hour)"""
    },
    {
        "word": "週",
        "reading": "しゅう (shuu)",
        "meaning": "week",
        "breakdown": """\
            週 = しゅう (week)"""
    },
    {
        "word": "今週",
        "reading": "こんしゅう (konshuu)",
        "meaning": "this week",
        "breakdown": """\
            今 = こん (now)
            週 = しゅう (week)"""
    },
    {
        "word": "来週",
        "reading": "らいしゅう (raishuu)",
        "meaning": "next week",
        "breakdown": """\
            来 = らい (come)
            週 = しゅう (week)"""
    },
    {
        "word": "先週",
        "reading": "せんしゅう (senshuu)",
        "meaning": "last week",
        "breakdown": """\
            先 = せん (previous / ahead)
            週 = しゅう (week)"""
    },
    {
        "word": "週間",
        "reading": "しゅうかん (shuukan)",
        "meaning": "week (duration)",
        "breakdown": """\
            週 = しゅう (week)
            間 = かん (between / interval)"""
    },
    {
        "word": "週休",
        "reading": "しゅうきゅう (shuukyuu)",
        "meaning": "weekly day off",
        "breakdown": """\
            週 = しゅう (week)
            休 = きゅう (rest)"""
    },
    {
        "word": "今",
        "reading": "いま (ima)",
        "meaning": "now",
        "breakdown": """\
            今 = いま (now)"""
    },
    {
        "word": "今月",
        "reading": "こんげつ (kongetsu)",
        "meaning": "this month",
        "breakdown": """\
            今 = こん (now)
            月 = げつ (month / moon)"""
    },
    {
        "word": "今時",
        "reading": "いまどき (imadoki)",
        "meaning": "nowadays",
        "breakdown": """\
            今 = いま (now)
            時 = どき (time / hour)"""
    },
    {
        "word": "古今",
        "reading": "ここん (kokon)",
        "meaning": "past and present",
        "breakdown": """\
            古 = こ (old)
            今 = こん (now)"""
    },
    {
        "word": "先月",
        "reading": "せんげつ (sengetsu)",
        "meaning": "last month",
        "breakdown": """\
            先 = せん (previous / ahead)
            月 = げつ (month / moon)"""
    },
    {
        "word": "来月",
        "reading": "らいげつ (raigetsu)",
        "meaning": "next month",
        "breakdown": """\
            来 = らい (come)
            月 = げつ (month / moon)"""
    },
    {
        "word": "新月",
        "reading": "しんげつ (shingetsu)",
        "meaning": "new moon",
        "breakdown": """\
            新 = しん (new)
            月 = げつ (month / moon)"""
    },
    {
        "word": "名月",
        "reading": "めいげつ (meigetsu)",
        "meaning": "harvest moon",
        "breakdown": """\
            名 = めい (name)
            月 = げつ (month / moon)"""
    },
    {
        "word": "文月",
        "reading": "ふみづき (fumizuki)",
        "meaning": "July (old calendar)",
        "breakdown": """\
            文 = ふみ (sentence)
            月 = づき (month / moon)"""
    },
    {
        "word": "月",
        "reading": "つき (tsuki)",
        "meaning": "moon",
        "breakdown": """\
            月 = つき (month / moon)"""
    },
    {
        "word": "月",
        "reading": "げつ (getsu)",
        "meaning": "Monday",
        "breakdown": """\
            月 = げつ (month / moon)"""
    },
    {
        "word": "月曜日",
        "reading": "げつようび (getsuyoubi)",
        "meaning": "Monday",
        "breakdown": """\
            月 = げつ (month / moon)
            曜 = よう (weekday)
            日 = び (day / sun)"""
    },
    {
        "word": "人",
        "reading": "ひと (hito)",
        "meaning": "person",
        "breakdown": """\
            人 = ひと (person)"""
    },
    {
        "word": "人",
        "reading": "にん (nin)",
        "meaning": "person (counter)",
        "breakdown": """\
            人 = にん (person)"""
    },
    {
        "word": "日本人",
        "reading": "にほんじん (nihonjin)",
        "meaning": "Japanese person",
        "breakdown": """\
            日 = に (day / sun)
            本 = ほん (book / origin)
            人 = じん (person)"""
    },
    {
        "word": "大人",
        "reading": "おとな (otona)",
        "meaning": "adult",
        "breakdown": """\
            大人 = おとな (irregular reading)"""
    },
    {
        "word": "人口",
        "reading": "じんこう (jinkou)",
        "meaning": "population",
        "breakdown": """\
            人 = じん (person)
            口 = こう (mouth)"""
    },
    {
        "word": "人気",
        "reading": "にんき (ninki)",
        "meaning": "popularity",
        "breakdown": """\
            人 = にん (person)
            気 = き (spirit / energy)"""
    },
    {
        "word": "人気",
        "reading": "ひとけ (hitoke)",
        "meaning": "signs of people",
        "breakdown": """\
            人 = ひと (person)
            気 = け (spirit / energy)"""
    },
    {
        "word": "人間",
        "reading": "にんげん (ningen)",
        "meaning": "human being",
        "breakdown": """\
            人 = にん (person)
            間 = げん (between / interval)"""
    },
    {
        "word": "外人",
        "reading": "がいじん (gaijin)",
        "meaning": "foreigner",
        "breakdown": """\
            外 = がい (outside)
            人 = じん (person)"""
    },
    {
        "word": "外国人",
        "reading": "がいこくじん (gaikokujin)",
        "meaning": "foreigner",
        "breakdown": """\
            外 = がい (outside)
            国 = こく (country)
            人 = じん (person)"""
    },
    {
        "word": "人名",
        "reading": "じんめい (jinmei)",
        "meaning": "person's name",
        "breakdown": """\
            人 = じん (person)
            名 = めい (name)"""
    },
    {
        "word": "友人",
        "reading": "ゆうじん (yuujin)",
        "meaning": "friend",
        "breakdown": """\
            友 = ゆう (friend)
            人 = じん (person)"""
    },
    {
        "word": "本人",
        "reading": "ほんにん (honnin)",
        "meaning": "the person himself",
        "breakdown": """\
            本 = ほん (book / origin)
            人 = にん (person)"""
    },
    {
        "word": "人生",
        "reading": "じんせい (jinsei)",
        "meaning": "human life",
        "breakdown": """\
            人 = じん (person)
            生 = せい (life / birth)"""
    },
    {
        "word": "人目",
        "reading": "ひとめ (hitome)",
        "meaning": "public eye",
        "breakdown": """\
            人 = ひと (person)
            目 = め (eye)"""
    },
    {
        "word": "人手",
        "reading": "ひとで (hitode)",
        "meaning": "manpower",
        "breakdown": """\
            人 = ひと (person)
            手 = で (hand)"""
    },
    {
        "word": "名人",
        "reading": "めいじん (meijin)",
        "meaning": "master / expert",
        "breakdown": """\
            名 = めい (name)
            人 = じん (person)"""
    },
    {
        "word": "先人",
        "reading": "せんじん (senjin)",
        "meaning": "predecessor",
        "breakdown": """\
            先 = せん (previous / ahead)
            人 = じん (person)"""
    },
    {
        "word": "新人",
        "reading": "しんじん (shinjin)",
        "meaning": "newcomer",
        "breakdown": """\
            新 = しん (new)
            人 = じん (person)"""
    },
    {
        "word": "古人",
        "reading": "こじん (kojin)",
        "meaning": "people of old",
        "breakdown": """\
            古 = こ (old)
            人 = じん (person)"""
    },
    {
        "word": "白人",
        "reading": "はくじん (hakujin)",
        "meaning": "white person",
        "breakdown": """\
            白 = はく (white)
            人 = じん (person)"""
    },
    {
        "word": "黒人",
        "reading": "こくじん (kokujin)",
        "meaning": "Black person",
        "breakdown": """\
            黒 = こく (black)
            人 = じん (person)"""
    },
    {
        "word": "文人",
        "reading": "ぶんじん (bunjin)",
        "meaning": "man of letters",
        "breakdown": """\
            文 = ぶん (sentence)
            人 = じん (person)"""
    },
    {
        "word": "人魚",
        "reading": "にんぎょ (ningyo)",
        "meaning": "mermaid",
        "breakdown": """\
            人 = にん (person)
            魚 = ぎょ (fish)"""
    },
    {
        "word": "待ち人",
        "reading": "まちびと (machibito)",
        "meaning": "person being waited for",
        "breakdown": """\
            待 = ま (wait)
            ち = okurigana
            人 = びと (person)"""
    },
    {
        "word": "男",
        "reading": "おとこ (otoko)",
        "meaning": "man",
        "breakdown": """\
            男 = おとこ (man)"""
    },
    {
        "word": "男子",
        "reading": "だんし (danshi)",
        "meaning": "boy / male",
        "breakdown": """\
            男 = だん (man)
            子 = し (child)"""
    },
    {
        "word": "男女",
        "reading": "だんじょ (danjo)",
        "meaning": "men and women",
        "breakdown": """\
            男 = だん (man)
            女 = じょ (woman)"""
    },
    {
        "word": "長男",
        "reading": "ちょうなん (chounan)",
        "meaning": "eldest son",
        "breakdown": """\
            長 = ちょう (long)
            男 = なん (man)"""
    },
    {
        "word": "男の子",
        "reading": "おとこのこ (otokonoko)",
        "meaning": "boy",
        "breakdown": """\
            男 = おとこ (man)
            の = okurigana
            子 = こ (child)"""
    },
    {
        "word": "男手",
        "reading": "おとこで (otokode)",
        "meaning": "male labor",
        "breakdown": """\
            男 = おとこ (man)
            手 = で (hand)"""
    },
    {
        "word": "女",
        "reading": "おんな (onna)",
        "meaning": "woman",
        "breakdown": """\
            女 = おんな (woman)"""
    },
    {
        "word": "女子",
        "reading": "じょし (joshi)",
        "meaning": "girl / female",
        "breakdown": """\
            女 = じょ (woman)
            子 = し (child)"""
    },
    {
        "word": "女の子",
        "reading": "おんなのこ (onnanoko)",
        "meaning": "girl",
        "breakdown": """\
            女 = おんな (woman)
            の = okurigana
            子 = こ (child)"""
    },
    {
        "word": "長女",
        "reading": "ちょうじょ (choujo)",
        "meaning": "eldest daughter",
        "breakdown": """\
            長 = ちょう (long)
            女 = じょ (woman)"""
    },
    {
        "word": "女手",
        "reading": "おんなで (onnade)",
        "meaning": "female labor",
        "breakdown": """\
            女 = おんな (woman)
            手 = で (hand)"""
    },
    {
        "word": "天女",
        "reading": "てんにょ (tennyo)",
        "meaning": "celestial maiden",
        "breakdown": """\
            天 = てん (heaven / sky)
            女 = にょ (woman)"""
    },
    {
        "word": "少女",
        "reading": "しょうじょ (shoujo)",
        "meaning": "girl",
        "breakdown": """\
            少 = しょう (few)
            女 = じょ (woman)"""
    },
    {
        "word": "子",
        "reading": "こ (ko)",
        "meaning": "child",
        "breakdown": """\
            子 = こ (child)"""
    },
    {
        "word": "子女",
        "reading": "しじょ (shijo)",
        "meaning": "sons and daughters",
        "breakdown": """\
            子 = し (child)
            女 = じょ (woman)"""
    },
    {
        "word": "母子",
        "reading": "ぼし (boshi)",
        "meaning": "mother and child",
        "breakdown": """\
            母 = ぼ (mother)
            子 = し (child)"""
    },
    {
        "word": "父子",
        "reading": "ふし (fushi)",
        "meaning": "father and child",
        "breakdown": """\
            父 = ふ (father)
            子 = し (child)"""
    },
    {
        "word": "赤子",
        "reading": "あかご (akago)",
        "meaning": "baby",
        "breakdown": """\
            赤 = あか (red)
            子 = ご (child)"""
    },
    {
        "word": "父",
        "reading": "ちち (chichi)",
        "meaning": "father",
        "breakdown": """\
            父 = ちち (father)"""
    },
    {
        "word": "父さん",
        "reading": "とうさん (tousan)",
        "meaning": "father (casual)",
        "breakdown": """\
            父 = とう (father)
            さん = okurigana"""
    },
    {
        "word": "父母",
        "reading": "ふぼ (fubo)",
        "meaning": "father and mother",
        "breakdown": """\
            父 = ふ (father)
            母 = ぼ (mother)"""
    },
    {
        "word": "父上",
        "reading": "ちちうえ (chichiue)",
        "meaning": "father (honorific)",
        "breakdown": """\
            父 = ちち (father)
            上 = うえ (above)"""
    },
    {
        "word": "母",
        "reading": "はは (haha)",
        "meaning": "mother",
        "breakdown": """\
            母 = はは (mother)"""
    },
    {
        "word": "母さん",
        "reading": "かあさん (kaasan)",
        "meaning": "mother (casual)",
        "breakdown": """\
            母 = かあ (mother)
            さん = okurigana"""
    },
    {
        "word": "母国",
        "reading": "ぼこく (bokoku)",
        "meaning": "home country",
        "breakdown": """\
            母 = ぼ (mother)
            国 = こく (country)"""
    },
    {
        "word": "母上",
        "reading": "ははうえ (hahaue)",
        "meaning": "mother (honorific)",
        "breakdown": """\
            母 = はは (mother)
            上 = うえ (above)"""
    },
    {
        "word": "母語",
        "reading": "ぼご (bogo)",
        "meaning": "mother tongue",
        "breakdown": """\
            母 = ぼ (mother)
            語 = ご (language / word)"""
    },
    {
        "word": "母校",
        "reading": "ぼこう (bokou)",
        "meaning": "alma mater",
        "breakdown": """\
            母 = ぼ (mother)
            校 = こう (school)"""
    },
    {
        "word": "友",
        "reading": "とも (tomo)",
        "meaning": "friend",
        "breakdown": """\
            友 = とも (friend)"""
    },
    {
        "word": "学友",
        "reading": "がくゆう (gakuyuu)",
        "meaning": "schoolmate",
        "breakdown": """\
            学 = がく (study)
            友 = ゆう (friend)"""
    },
    {
        "word": "校友",
        "reading": "こうゆう (kouyuu)",
        "meaning": "school friend",
        "breakdown": """\
            校 = こう (school)
            友 = ゆう (friend)"""
    },
    {
        "word": "名",
        "reading": "な (na)",
        "meaning": "name",
        "breakdown": """\
            名 = な (name)"""
    },
    {
        "word": "名字",
        "reading": "みょうじ (myouji)",
        "meaning": "family name",
        "breakdown": """\
            名 = みょう (name)
            字 = じ (character)"""
    },
    {
        "word": "大名",
        "reading": "だいみょう (daimyou)",
        "meaning": "feudal lord",
        "breakdown": """\
            大 = だい (big)
            名 = みょう (name)"""
    },
    {
        "word": "学名",
        "reading": "がくめい (gakumei)",
        "meaning": "scientific name",
        "breakdown": """\
            学 = がく (study)
            名 = めい (name)"""
    },
    {
        "word": "校名",
        "reading": "こうめい (koumei)",
        "meaning": "school name",
        "breakdown": """\
            校 = こう (school)
            名 = めい (name)"""
    },
    {
        "word": "国名",
        "reading": "こくめい (kokumei)",
        "meaning": "country name",
        "breakdown": """\
            国 = こく (country)
            名 = めい (name)"""
    },
    {
        "word": "本名",
        "reading": "ほんみょう (honmyou)",
        "meaning": "real name",
        "breakdown": """\
            本 = ほん (book / origin)
            名 = みょう (name)"""
    },
    {
        "word": "本名",
        "reading": "ほんめい (honmei)",
        "meaning": "real name",
        "breakdown": """\
            本 = ほん (book / origin)
            名 = めい (name)"""
    },
    {
        "word": "書名",
        "reading": "しょめい (shomei)",
        "meaning": "book title",
        "breakdown": """\
            書 = しょ (write)
            名 = めい (name)"""
    },
    {
        "word": "先",
        "reading": "さき (saki)",
        "meaning": "ahead / tip",
        "breakdown": """\
            先 = さき (previous / ahead)"""
    },
    {
        "word": "先生",
        "reading": "せんせい (sensei)",
        "meaning": "teacher",
        "breakdown": """\
            先 = せん (previous / ahead)
            生 = せい (life / birth)"""
    },
    {
        "word": "行き先",
        "reading": "いきさき (ikisaki)",
        "meaning": "destination",
        "breakdown": """\
            行 = い (go)
            き = okurigana
            先 = さき (previous / ahead)"""
    },
    {
        "word": "出先",
        "reading": "でさき (desaki)",
        "meaning": "place one is visiting",
        "breakdown": """\
            出 = で (exit / take out)
            先 = さき (previous / ahead)"""
    },
    {
        "word": "先立つ",
        "reading": "さきだつ (sakidatsu)",
        "meaning": "to precede",
        "breakdown": """\
            先 = さき (previous / ahead)
            立 = だ (stand)
            つ = okurigana"""
    },
    {
        "word": "生",
        "reading": "せい (sei)",
        "meaning": "life",
        "breakdown": """\
            生 = せい (life / birth)"""
    },
    {
        "word": "生",
        "reading": "なま (nama)",
        "meaning": "raw",
        "breakdown": """\
            生 = なま (life / birth)"""
    },
    {
        "word": "生きる",
        "reading": "いきる (ikiru)",
        "meaning": "to live",
        "breakdown": """\
            生 = い (life / birth)
            きる = okurigana"""
    },
    {
        "word": "生まれる",
        "reading": "うまれる (umareru)",
        "meaning": "to be born",
        "breakdown": """\
            生 = う (life / birth)
            まれる = okurigana"""
    },
    {
        "word": "生える",
        "reading": "はえる (haeru)",
        "meaning": "to grow",
        "breakdown": """\
            生 = は (life / birth)
            える = okurigana"""
    },
    {
        "word": "学生",
        "reading": "がくせい (gakusei)",
        "meaning": "student",
        "breakdown": """\
            学 = がく (study)
            生 = せい (life / birth)"""
    },
    {
        "word": "小学生",
        "reading": "しょうがくせい (shougakusei)",
        "meaning": "elementary school student",
        "breakdown": """\
            小 = しょう (small)
            学 = がく (study)
            生 = せい (life / birth)"""
    },
    {
        "word": "新入生",
        "reading": "しんにゅうせい (shinnyuusei)",
        "meaning": "new student",
        "breakdown": """\
            新 = しん (new)
            入 = にゅう (enter)
            生 = せい (life / birth)"""
    },
    {
        "word": "書生",
        "reading": "しょせい (shosei)",
        "meaning": "student (old)",
        "breakdown": """\
            書 = しょ (write)
            生 = せい (life / birth)"""
    },
    {
        "word": "生魚",
        "reading": "なまざかな (namazakana)",
        "meaning": "raw fish",
        "breakdown": """\
            生 = なま (life / birth)
            魚 = ざかな (fish)"""
    },
    {
        "word": "長生き",
        "reading": "ながいき (nagaiki)",
        "meaning": "long life",
        "breakdown": """\
            長 = なが (long)
            生 = い (life / birth)
            き = okurigana"""
    },
    {
        "word": "出生",
        "reading": "しゅっせい (shussei)",
        "meaning": "birth",
        "breakdown": """\
            出 = しゅっ (exit / take out)
            生 = せい (life / birth)"""
    },
    {
        "word": "山",
        "reading": "やま (yama)",
        "meaning": "mountain",
        "breakdown": """\
            山 = やま (mountain)"""
    },
    {
        "word": "山田",
        "reading": "やまだ (yamada)",
        "meaning": "Yamada",
        "breakdown": """\
            山 = やま (mountain)
            田 = だ (rice field)"""
    },
    {
        "word": "山川",
        "reading": "やまかわ (yamakawa)",
        "meaning": "mountains and rivers",
        "breakdown": """\
            山 = やま (mountain)
            川 = かわ (river)"""
    },
    {
        "word": "山道",
        "reading": "やまみち (yamamichi)",
        "meaning": "mountain path",
        "breakdown": """\
            山 = やま (mountain)
            道 = みち (road / way)"""
    },
    {
        "word": "山口",
        "reading": "やまぐち (yamaguchi)",
        "meaning": "Yamaguchi",
        "breakdown": """\
            山 = やま (mountain)
            口 = ぐち (mouth)"""
    },
    {
        "word": "山中",
        "reading": "やまなか (yamanaka)",
        "meaning": "in the mountains",
        "breakdown": """\
            山 = やま (mountain)
            中 = なか (inside / middle)"""
    },
    {
        "word": "山上",
        "reading": "さんじょう (sanjou)",
        "meaning": "mountaintop",
        "breakdown": """\
            山 = さん (mountain)
            上 = じょう (above)"""
    },
    {
        "word": "山川",
        "reading": "さんせん (sansen)",
        "meaning": "mountains and rivers",
        "breakdown": """\
            山 = さん (mountain)
            川 = せん (river)"""
    },
    {
        "word": "大山",
        "reading": "おおやま (ooyama)",
        "meaning": "large mountain",
        "breakdown": """\
            大 = おお (big)
            山 = やま (mountain)"""
    },
    {
        "word": "小山",
        "reading": "こやま (koyama)",
        "meaning": "small hill",
        "breakdown": """\
            小 = こ (small)
            山 = やま (mountain)"""
    },
    {
        "word": "高山",
        "reading": "こうざん (kouzan)",
        "meaning": "high mountain",
        "breakdown": """\
            高 = こう (tall / expensive)
            山 = ざん (mountain)"""
    },
    {
        "word": "青山",
        "reading": "あおやま (aoyama)",
        "meaning": "Aoyama",
        "breakdown": """\
            青 = あお (blue)
            山 = やま (mountain)"""
    },
    {
        "word": "中山",
        "reading": "なかやま (nakayama)",
        "meaning": "Nakayama",
        "breakdown": """\
            中 = なか (inside / middle)
            山 = やま (mountain)"""
    },
    {
        "word": "東山",
        "reading": "ひがしやま (higashiyama)",
        "meaning": "Higashiyama",
        "breakdown": """\
            東 = ひがし (east)
            山 = やま (mountain)"""
    },
    {
        "word": "西山",
        "reading": "にしやま (nishiyama)",
        "meaning": "Nishiyama",
        "breakdown": """\
            西 = にし (west)
            山 = やま (mountain)"""
    },
    {
        "word": "南山",
        "reading": "みなみやま (minamiyama)",
        "meaning": "southern mountain",
        "breakdown": """\
            南 = みなみ (south)
            山 = やま (mountain)"""
    },
    {
        "word": "北山",
        "reading": "きたやま (kitayama)",
        "meaning": "Kitayama",
        "breakdown": """\
            北 = きた (north)
            山 = やま (mountain)"""
    },
    {
        "word": "黒山",
        "reading": "くろやま (kuroyama)",
        "meaning": "crowd (lit. black mountain)",
        "breakdown": """\
            黒 = くろ (black)
            山 = やま (mountain)"""
    },
    {
        "word": "下山",
        "reading": "げざん (gezan)",
        "meaning": "descending a mountain",
        "breakdown": """\
            下 = げ (below)
            山 = ざん (mountain)"""
    },
    {
        "word": "白山",
        "reading": "はくさん (hakusan)",
        "meaning": "Mt. Hakusan",
        "breakdown": """\
            白 = はく (white)
            山 = さん (mountain)"""
    },
    {
        "word": "川",
        "reading": "かわ (kawa)",
        "meaning": "river",
        "breakdown": """\
            川 = かわ (river)"""
    },
    {
        "word": "小川",
        "reading": "おがわ (ogawa)",
        "meaning": "stream",
        "breakdown": """\
            小 = お (small)
            川 = がわ (river)"""
    },
    {
        "word": "川上",
        "reading": "かわかみ (kawakami)",
        "meaning": "upstream",
        "breakdown": """\
            川 = かわ (river)
            上 = かみ (above)"""
    },
    {
        "word": "川下",
        "reading": "かわしも (kawashimo)",
        "meaning": "downstream",
        "breakdown": """\
            川 = かわ (river)
            下 = しも (below)"""
    },
    {
        "word": "川口",
        "reading": "かわぐち (kawaguchi)",
        "meaning": "river mouth",
        "breakdown": """\
            川 = かわ (river)
            口 = ぐち (mouth)"""
    },
    {
        "word": "大川",
        "reading": "おおかわ (ookawa)",
        "meaning": "large river",
        "breakdown": """\
            大 = おお (big)
            川 = かわ (river)"""
    },
    {
        "word": "田",
        "reading": "た (ta)",
        "meaning": "rice field",
        "breakdown": """\
            田 = た (rice field)"""
    },
    {
        "word": "田中",
        "reading": "たなか (tanaka)",
        "meaning": "Tanaka",
        "breakdown": """\
            田 = た (rice field)
            中 = なか (inside / middle)"""
    },
    {
        "word": "田口",
        "reading": "たぐち (taguchi)",
        "meaning": "Taguchi",
        "breakdown": """\
            田 = た (rice field)
            口 = ぐち (mouth)"""
    },
    {
        "word": "大田",
        "reading": "おおた (oota)",
        "meaning": "Ota",
        "breakdown": """\
            大 = おお (big)
            田 = た (rice field)"""
    },
    {
        "word": "高田",
        "reading": "たかだ (takada)",
        "meaning": "Takada",
        "breakdown": """\
            高 = たか (tall / expensive)
            田 = だ (rice field)"""
    },
    {
        "word": "上田",
        "reading": "うえだ (ueda)",
        "meaning": "Ueda",
        "breakdown": """\
            上 = うえ (above)
            田 = だ (rice field)"""
    },
    {
        "word": "小田",
        "reading": "おだ (oda)",
        "meaning": "Oda",
        "breakdown": """\
            小 = お (small)
            田 = だ (rice field)"""
    },
    {
        "word": "青田",
        "reading": "あおた (aota)",
        "meaning": "green rice field",
        "breakdown": """\
            青 = あお (blue)
            田 = た (rice field)"""
    },
    {
        "word": "本田",
        "reading": "ほんだ (honda)",
        "meaning": "Honda",
        "breakdown": """\
            本 = ほん (book / origin)
            田 = だ (rice field)"""
    },
    {
        "word": "下田",
        "reading": "しもだ (shimoda)",
        "meaning": "Shimoda",
        "breakdown": """\
            下 = しも (below)
            田 = だ (rice field)"""
    },
    {
        "word": "西田",
        "reading": "にしだ (nishida)",
        "meaning": "Nishida",
        "breakdown": """\
            西 = にし (west)
            田 = だ (rice field)"""
    },
    {
        "word": "北田",
        "reading": "きただ (kitada)",
        "meaning": "Kitada",
        "breakdown": """\
            北 = きた (north)
            田 = だ (rice field)"""
    },
    {
        "word": "新田",
        "reading": "にった (nitta)",
        "meaning": "newly opened field",
        "breakdown": """\
            新 = にっ (new)
            田 = た (rice field)"""
    },
    {
        "word": "天",
        "reading": "てん (ten)",
        "meaning": "heaven",
        "breakdown": """\
            天 = てん (heaven / sky)"""
    },
    {
        "word": "天気",
        "reading": "てんき (tenki)",
        "meaning": "weather",
        "breakdown": """\
            天 = てん (heaven / sky)
            気 = き (spirit / energy)"""
    },
    {
        "word": "天上",
        "reading": "てんじょう (tenjou)",
        "meaning": "heaven",
        "breakdown": """\
            天 = てん (heaven / sky)
            上 = じょう (above)"""
    },
    {
        "word": "天国",
        "reading": "てんごく (tengoku)",
        "meaning": "paradise",
        "breakdown": """\
            天 = てん (heaven / sky)
            国 = ごく (country)"""
    },
    {
        "word": "天下",
        "reading": "てんか (tenka)",
        "meaning": "the whole country",
        "breakdown": """\
            天 = てん (heaven / sky)
            下 = か (below)"""
    },
    {
        "word": "天の川",
        "reading": "あまのがわ (amanogawa)",
        "meaning": "Milky Way",
        "breakdown": """\
            天 = あま (heaven / sky)
            の = okurigana
            川 = がわ (river)"""
    },
    {
        "word": "天道",
        "reading": "てんどう (tendou)",
        "meaning": "providence",
        "breakdown": """\
            天 = てん (heaven / sky)
            道 = どう (road / way)"""
    },
    {
        "word": "天空",
        "reading": "てんくう (tenkuu)",
        "meaning": "firmament",
        "breakdown": """\
            天 = てん (heaven / sky)
            空 = くう (sky / empty)"""
    },
    {
        "word": "天文",
        "reading": "てんもん (tenmon)",
        "meaning": "astronomy",
        "breakdown": """\
            天 = てん (heaven / sky)
            文 = もん (sentence)"""
    },
    {
        "word": "雨天",
        "reading": "うてん (uten)",
        "meaning": "rainy weather",
        "breakdown": """\
            雨 = う (rain)
            天 = てん (heaven / sky)"""
    },
    {
        "word": "南天",
        "reading": "なんてん (nanten)",
        "meaning": "southern sky",
        "breakdown": """\
            南 = なん (south)
            天 = てん (heaven / sky)"""
    },
    {
        "word": "気",
        "reading": "き (ki)",
        "meaning": "spirit",
        "breakdown": """\
            気 = き (spirit / energy)"""
    },
    {
        "word": "気",
        "reading": "け (ke)",
        "meaning": "sign / feeling",
        "breakdown": """\
            気 = け (spirit / energy)"""
    },
    {
        "word": "気分",
        "reading": "きぶん (kibun)",
        "meaning": "mood",
        "breakdown": """\
            気 = き (spirit / energy)
            分 = ぶん (minute / part)"""
    },
    {
        "word": "空気",
        "reading": "くうき (kuuki)",
        "meaning": "air",
        "breakdown": """\
            空 = くう (sky / empty)
            気 = き (spirit / energy)"""
    },
    {
        "word": "電気",
        "reading": "でんき (denki)",
        "meaning": "electricity",
        "breakdown": """\
            電 = でん (electricity)
            気 = き (spirit / energy)"""
    },
    {
        "word": "気長",
        "reading": "きなが (kinaga)",
        "meaning": "patient",
        "breakdown": """\
            気 = き (spirit / energy)
            長 = なが (long)"""
    },
    {
        "word": "気道",
        "reading": "きどう (kidou)",
        "meaning": "airway",
        "breakdown": """\
            気 = き (spirit / energy)
            道 = どう (road / way)"""
    },
    {
        "word": "本気",
        "reading": "ほんき (honki)",
        "meaning": "serious",
        "breakdown": """\
            本 = ほん (book / origin)
            気 = き (spirit / energy)"""
    },
    {
        "word": "語気",
        "reading": "ごき (goki)",
        "meaning": "tone of voice",
        "breakdown": """\
            語 = ご (language / word)
            気 = き (spirit / energy)"""
    },
    {
        "word": "雨",
        "reading": "あめ (ame)",
        "meaning": "rain",
        "breakdown": """\
            雨 = あめ (rain)"""
    },
    {
        "word": "大雨",
        "reading": "おおあめ (ooame)",
        "meaning": "heavy rain",
        "breakdown": """\
            大 = おお (big)
            雨 = あめ (rain)"""
    },
    {
        "word": "大雨",
        "reading": "たいう (taiu)",
        "meaning": "heavy rain",
        "breakdown": """\
            大 = たい (big)
            雨 = う (rain)"""
    },
    {
        "word": "小雨",
        "reading": "こさめ (kosame)",
        "meaning": "light rain",
        "breakdown": """\
            小 = こ (small)
            雨 = さめ (rain)"""
    },
    {
        "word": "雨中",
        "reading": "うちゅう (uchuu)",
        "meaning": "in the rain",
        "breakdown": """\
            雨 = う (rain)
            中 = ちゅう (inside / middle)"""
    },
    {
        "word": "花",
        "reading": "はな (hana)",
        "meaning": "flower",
        "breakdown": """\
            花 = はな (flower)"""
    },
    {
        "word": "花見",
        "reading": "はなみ (hanami)",
        "meaning": "cherry blossom viewing",
        "breakdown": """\
            花 = はな (flower)
            見 = み (see)"""
    },
    {
        "word": "花道",
        "reading": "かどう (kadou)",
        "meaning": "flower arrangement / stage walkway",
        "breakdown": """\
            花 = か (flower)
            道 = どう (road / way)"""
    },
    {
        "word": "生花",
        "reading": "せいか (seika)",
        "meaning": "fresh flowers",
        "breakdown": """\
            生 = せい (life / birth)
            花 = か (flower)"""
    },
    {
        "word": "国花",
        "reading": "こっか (kokka)",
        "meaning": "national flower",
        "breakdown": """\
            国 = こっ (country)
            花 = か (flower)"""
    },
    {
        "word": "空",
        "reading": "そら (sora)",
        "meaning": "sky",
        "breakdown": """\
            空 = そら (sky / empty)"""
    },
    {
        "word": "空",
        "reading": "くう (kuu)",
        "meaning": "empty",
        "breakdown": """\
            空 = くう (sky / empty)"""
    },
    {
        "word": "空中",
        "reading": "くうちゅう (kuuchuu)",
        "meaning": "midair",
        "breakdown": """\
            空 = くう (sky / empty)
            中 = ちゅう (inside / middle)"""
    },
    {
        "word": "空手",
        "reading": "からて (karate)",
        "meaning": "karate",
        "breakdown": """\
            空 = から (sky / empty)
            手 = て (hand)"""
    },
    {
        "word": "青空",
        "reading": "あおぞら (aozora)",
        "meaning": "blue sky",
        "breakdown": """\
            青 = あお (blue)
            空 = ぞら (sky / empty)"""
    },
    {
        "word": "大空",
        "reading": "おおぞら (oozora)",
        "meaning": "big sky",
        "breakdown": """\
            大 = おお (big)
            空 = ぞら (sky / empty)"""
    },
    {
        "word": "空車",
        "reading": "くうしゃ (kuusha)",
        "meaning": "empty vehicle",
        "breakdown": """\
            空 = くう (sky / empty)
            車 = しゃ (car)"""
    },
    {
        "word": "空白",
        "reading": "くうはく (kuuhaku)",
        "meaning": "blank",
        "breakdown": """\
            空 = くう (sky / empty)
            白 = はく (white)"""
    },
    {
        "word": "空間",
        "reading": "くうかん (kuukan)",
        "meaning": "space",
        "breakdown": """\
            空 = くう (sky / empty)
            間 = かん (between / interval)"""
    },
    {
        "word": "電",
        "reading": "でん (den)",
        "meaning": "electricity",
        "breakdown": """\
            電 = でん (electricity)"""
    },
    {
        "word": "電車",
        "reading": "でんしゃ (densha)",
        "meaning": "train",
        "breakdown": """\
            電 = でん (electricity)
            車 = しゃ (car)"""
    },
    {
        "word": "電話",
        "reading": "でんわ (denwa)",
        "meaning": "telephone",
        "breakdown": """\
            電 = でん (electricity)
            話 = わ (speak / story)"""
    },
    {
        "word": "魚",
        "reading": "さかな (sakana)",
        "meaning": "fish",
        "breakdown": """\
            魚 = さかな (fish)"""
    },
    {
        "word": "大魚",
        "reading": "たいぎょ (taigyo)",
        "meaning": "big fish",
        "breakdown": """\
            大 = たい (big)
            魚 = ぎょ (fish)"""
    },
    {
        "word": "小魚",
        "reading": "こざかな (kozakana)",
        "meaning": "small fish",
        "breakdown": """\
            小 = こ (small)
            魚 = ざかな (fish)"""
    },
    {
        "word": "上",
        "reading": "うえ (ue)",
        "meaning": "above",
        "breakdown": """\
            上 = うえ (above)"""
    },
    {
        "word": "上",
        "reading": "じょう (jou)",
        "meaning": "above",
        "breakdown": """\
            上 = じょう (above)"""
    },
    {
        "word": "上手",
        "reading": "じょうず (jouzu)",
        "meaning": "skillful",
        "breakdown": """\
            上手 = じょうず (irregular reading)"""
    },
    {
        "word": "上がる",
        "reading": "あがる (agaru)",
        "meaning": "to go up",
        "breakdown": """\
            上 = あ (above)
            がる = okurigana"""
    },
    {
        "word": "上る",
        "reading": "のぼる (noboru)",
        "meaning": "to climb",
        "breakdown": """\
            上 = のぼ (above)
            る = okurigana"""
    },
    {
        "word": "上下",
        "reading": "じょうげ (jouge)",
        "meaning": "up and down",
        "breakdown": """\
            上 = じょう (above)
            下 = げ (below)"""
    },
    {
        "word": "上空",
        "reading": "じょうくう (joukuu)",
        "meaning": "high in the sky",
        "breakdown": """\
            上 = じょう (above)
            空 = くう (sky / empty)"""
    },
    {
        "word": "左上",
        "reading": "ひだりうえ (hidariue)",
        "meaning": "upper left",
        "breakdown": """\
            左 = ひだり (left)
            上 = うえ (above)"""
    },
    {
        "word": "右上",
        "reading": "みぎうえ (migiue)",
        "meaning": "upper right",
        "breakdown": """\
            右 = みぎ (right)
            上 = うえ (above)"""
    },
    {
        "word": "目上",
        "reading": "めうえ (meue)",
        "meaning": "superior",
        "breakdown": """\
            目 = め (eye)
            上 = うえ (above)"""
    },
    {
        "word": "北上",
        "reading": "ほくじょう (hokujou)",
        "meaning": "going north",
        "breakdown": """\
            北 = ほく (north)
            上 = じょう (above)"""
    },
    {
        "word": "立ち上がる",
        "reading": "たちあがる (tachiagaru)",
        "meaning": "to stand up",
        "breakdown": """\
            立 = た (stand)
            ち = okurigana
            上 = あ (above)
            がる = okurigana"""
    },
    {
        "word": "下",
        "reading": "した (shita)",
        "meaning": "below",
        "breakdown": """\
            下 = した (below)"""
    },
    {
        "word": "下手",
        "reading": "へた (heta)",
        "meaning": "unskilled",
        "breakdown": """\
            下手 = へた (irregular reading)"""
    },
    {
        "word": "下がる",
        "reading": "さがる (sagaru)",
        "meaning": "to go down",
        "breakdown": """\
            下 = さ (below)
            がる = okurigana"""
    },
    {
        "word": "下りる",
        "reading": "おりる (oriru)",
        "meaning": "to get off",
        "breakdown": """\
            下 = お (below)
            りる = okurigana"""
    },
    {
        "word": "下る",
        "reading": "くだる (kudaru)",
        "meaning": "to descend",
        "breakdown": """\
            下 = くだ (below)
            る = okurigana"""
    },
    {
        "word": "下車",
        "reading": "げしゃ (gesha)",
        "meaning": "getting off a vehicle",
        "breakdown": """\
            下 = げ (below)
            車 = しゃ (car)"""
    },
    {
        "word": "下校",
        "reading": "げこう (gekou)",
        "meaning": "leaving school",
        "breakdown": """\
            下 = げ (below)
            校 = こう (school)"""
    },
    {
        "word": "左下",
        "reading": "ひだりした (hidarishita)",
        "meaning": "lower left",
        "breakdown": """\
            左 = ひだり (left)
            下 = した (below)"""
    },
    {
        "word": "右下",
        "reading": "みぎした (migishita)",
        "meaning": "lower right",
        "breakdown": """\
            右 = みぎ (right)
            下 = した (below)"""
    },
    {
        "word": "目下",
        "reading": "めした (meshita)",
        "meaning": "inferior",
        "breakdown": """\
            目 = め (eye)
            下 = した (below)"""
    },
    {
        "word": "目下",
        "reading": "もっか (mokka)",
        "meaning": "at present",
        "breakdown": """\
            目 = もっ (eye)
            下 = か (below)"""
    },
    {
        "word": "手下",
        "reading": "てした (teshita)",
        "meaning": "subordinate",
        "breakdown": """\
            手 = て (hand)
            下 = した (below)"""
    },
    {
        "word": "南下",
        "reading": "なんか (nanka)",
        "meaning": "going south",
        "breakdown": """\
            南 = なん (south)
            下 = か (below)"""
    },
    {
        "word": "中",
        "reading": "なか (naka)",
        "meaning": "inside",
        "breakdown": """\
            中 = なか (inside / middle)"""
    },
    {
        "word": "中国",
        "reading": "ちゅうごく (chuugoku)",
        "meaning": "China",
        "breakdown": """\
            中 = ちゅう (inside / middle)
            国 = ごく (country)"""
    },
    {
        "word": "中学",
        "reading": "ちゅうがく (chuugaku)",
        "meaning": "junior high school",
        "breakdown": """\
            中 = ちゅう (inside / middle)
            学 = がく (study)"""
    },
    {
        "word": "中小",
        "reading": "ちゅうしょう (chuushou)",
        "meaning": "small and medium",
        "breakdown": """\
            中 = ちゅう (inside / middle)
            小 = しょう (small)"""
    },
    {
        "word": "中古",
        "reading": "ちゅうこ (chuuko)",
        "meaning": "second-hand",
        "breakdown": """\
            中 = ちゅう (inside / middle)
            古 = こ (old)"""
    },
    {
        "word": "中間",
        "reading": "ちゅうかん (chuukan)",
        "meaning": "middle",
        "breakdown": """\
            中 = ちゅう (inside / middle)
            間 = かん (between / interval)"""
    },
    {
        "word": "中心",
        "reading": "ちゅうしん (chuushin)",
        "meaning": "center",
        "breakdown": """\
            中 = ちゅう (inside / middle)
            心 = しん (heart)"""
    },
    {
        "word": "中立",
        "reading": "ちゅうりつ (chuuritsu)",
        "meaning": "neutrality",
        "breakdown": """\
            中 = ちゅう (inside / middle)
            立 = りつ (stand)"""
    },
    {
        "word": "中古車",
        "reading": "ちゅうこしゃ (chuukosha)",
        "meaning": "used car",
        "breakdown": """\
            中 = ちゅう (inside / middle)
            古 = こ (old)
            車 = しゃ (car)"""
    },
    {
        "word": "文中",
        "reading": "ぶんちゅう (bunchuu)",
        "meaning": "in a sentence",
        "breakdown": """\
            文 = ぶん (sentence)
            中 = ちゅう (inside / middle)"""
    },
    {
        "word": "車中",
        "reading": "しゃちゅう (shachuu)",
        "meaning": "inside a vehicle",
        "breakdown": """\
            車 = しゃ (car)
            中 = ちゅう (inside / middle)"""
    },
    {
        "word": "道中",
        "reading": "どうちゅう (douchuu)",
        "meaning": "on the road",
        "breakdown": """\
            道 = どう (road / way)
            中 = ちゅう (inside / middle)"""
    },
    {
        "word": "国中",
        "reading": "くにじゅう (kunijuu)",
        "meaning": "throughout the country",
        "breakdown": """\
            国 = くに (country)
            中 = じゅう (inside / middle)"""
    },
    {
        "word": "一年中",
        "reading": "いちねんじゅう (ichinenjuu)",
        "meaning": "all year round",
        "breakdown": """\
            一 = いち (one)
            年 = ねん (year)
            中 = じゅう (inside / middle)"""
    },
    {
        "word": "外",
        "reading": "そと (soto)",
        "meaning": "outside",
        "breakdown": """\
            外 = そと (outside)"""
    },
    {
        "word": "外国",
        "reading": "がいこく (gaikoku)",
        "meaning": "foreign country",
        "breakdown": """\
            外 = がい (outside)
            国 = こく (country)"""
    },
    {
        "word": "外出",
        "reading": "がいしゅつ (gaishutsu)",
        "meaning": "going out",
        "breakdown": """\
            外 = がい (outside)
            出 = しゅつ (exit / take out)"""
    },
    {
        "word": "外見",
        "reading": "がいけん (gaiken)",
        "meaning": "appearance",
        "breakdown": """\
            外 = がい (outside)
            見 = けん (see)"""
    },
    {
        "word": "外食",
        "reading": "がいしょく (gaishoku)",
        "meaning": "eating out",
        "breakdown": """\
            外 = がい (outside)
            食 = しょく (eat)"""
    },
    {
        "word": "外す",
        "reading": "はずす (hazusu)",
        "meaning": "to remove",
        "breakdown": """\
            外 = はず (outside)
            す = okurigana"""
    },
    {
        "word": "外れる",
        "reading": "はずれる (hazureru)",
        "meaning": "to come off",
        "breakdown": """\
            外 = はず (outside)
            れる = okurigana"""
    },
    {
        "word": "外道",
        "reading": "げどう (gedou)",
        "meaning": "heretic",
        "breakdown": """\
            外 = げ (outside)
            道 = どう (road / way)"""
    },
    {
        "word": "校外",
        "reading": "こうがい (kougai)",
        "meaning": "off campus",
        "breakdown": """\
            校 = こう (school)
            外 = がい (outside)"""
    },
    {
        "word": "口外",
        "reading": "こうがい (kougai)",
        "meaning": "disclosure",
        "breakdown": """\
            口 = こう (mouth)
            外 = がい (outside)"""
    },
    {
        "word": "外国語",
        "reading": "がいこくご (gaikokugo)",
        "meaning": "foreign language",
        "breakdown": """\
            外 = がい (outside)
            国 = こく (country)
            語 = ご (language / word)"""
    },
    {
        "word": "左",
        "reading": "ひだり (hidari)",
        "meaning": "left",
        "breakdown": """\
            左 = ひだり (left)"""
    },
    {
        "word": "左手",
        "reading": "ひだりて (hidarite)",
        "meaning": "left hand",
        "breakdown": """\
            左 = ひだり (left)
            手 = て (hand)"""
    },
    {
        "word": "左足",
        "reading": "ひだりあし (hidariashi)",
        "meaning": "left foot",
        "breakdown": """\
            左 = ひだり (left)
            足 = あし (foot / leg)"""
    },
    {
        "word": "左目",
        "reading": "ひだりめ (hidarime)",
        "meaning": "left eye",
        "breakdown": """\
            左 = ひだり (left)
            目 = め (eye)"""
    },
    {
        "word": "左右",
        "reading": "さゆう (sayuu)",
        "meaning": "left and right",
        "breakdown": """\
            左 = さ (left)
            右 = ゆう (right)"""
    },
    {
        "word": "左折",
        "reading": "させつ (sasetsu)",
        "meaning": "left turn",
        "breakdown": """\
            左 = さ (left)
            折 = せつ (fold / bend)"""
    },
    {
        "word": "右",
        "reading": "みぎ (migi)",
        "meaning": "right",
        "breakdown": """\
            右 = みぎ (right)"""
    },
    {
        "word": "右手",
        "reading": "みぎて (migite)",
        "meaning": "right hand",
        "breakdown": """\
            右 = みぎ (right)
            手 = て (hand)"""
    },
    {
        "word": "右足",
        "reading": "みぎあし (migiashi)",
        "meaning": "right foot",
        "breakdown": """\
            右 = みぎ (right)
            足 = あし (foot / leg)"""
    },
    {
        "word": "右目",
        "reading": "みぎめ (migime)",
        "meaning": "right eye",
        "breakdown": """\
            右 = みぎ (right)
            目 = め (eye)"""
    },
    {
        "word": "右折",
        "reading": "うせつ (usetsu)",
        "meaning": "right turn",
        "breakdown": """\
            右 = う (right)
            折 = せつ (fold / bend)"""
    },
    {
        "word": "東",
        "reading": "ひがし (higashi)",
        "meaning": "east",
        "breakdown": """\
            東 = ひがし (east)"""
    },
    {
        "word": "東口",
        "reading": "ひがしぐち (higashiguchi)",
        "meaning": "east exit",
        "breakdown": """\
            東 = ひがし (east)
            口 = ぐち (mouth)"""
    },
    {
        "word": "東西",
        "reading": "とうざい (touzai)",
        "meaning": "east and west",
        "breakdown": """\
            東 = とう (east)
            西 = ざい (west)"""
    },
    {
        "word": "東日本",
        "reading": "ひがしにほん (higashinihon)",
        "meaning": "eastern Japan",
        "breakdown": """\
            東 = ひがし (east)
            日 = に (day / sun)
            本 = ほん (book / origin)"""
    },
    {
        "word": "東北",
        "reading": "とうほく (touhoku)",
        "meaning": "Tohoku",
        "breakdown": """\
            東 = とう (east)
            北 = ほく (north)"""
    },
    {
        "word": "東大",
        "reading": "とうだい (toudai)",
        "meaning": "University of Tokyo",
        "breakdown": """\
            東 = とう (east)
            大 = だい (big)"""
    },
    {
        "word": "東南",
        "reading": "とうなん (tounan)",
        "meaning": "southeast",
        "breakdown": """\
            東 = とう (east)
            南 = なん (south)"""
    },
    {
        "word": "東京",
        "reading": "とうきょう (toukyou)",
        "meaning": "Tokyo",
        "breakdown": """\
            東 = とう (east)
            京 = きょう (capital)"""
    },
    {
        "word": "西",
        "reading": "にし (nishi)",
        "meaning": "west",
        "breakdown": """\
            西 = にし (west)"""
    },
    {
        "word": "西口",
        "reading": "にしぐち (nishiguchi)",
        "meaning": "west exit",
        "breakdown": """\
            西 = にし (west)
            口 = ぐち (mouth)"""
    },
    {
        "word": "西南",
        "reading": "せいなん (seinan)",
        "meaning": "southwest",
        "breakdown": """\
            西 = せい (west)
            南 = なん (south)"""
    },
    {
        "word": "西北",
        "reading": "せいほく (seihoku)",
        "meaning": "northwest",
        "breakdown": """\
            西 = せい (west)
            北 = ほく (north)"""
    },
    {
        "word": "西日本",
        "reading": "にしにほん (nishinihon)",
        "meaning": "western Japan",
        "breakdown": """\
            西 = にし (west)
            日 = に (day / sun)
            本 = ほん (book / origin)"""
    },
    {
        "word": "西国",
        "reading": "さいごく (saigoku)",
        "meaning": "western provinces",
        "breakdown": """\
            西 = さい (west)
            国 = ごく (country)"""
    },
    {
        "word": "西京",
        "reading": "さいきょう (saikyou)",
        "meaning": "Saikyo (west capital)",
        "breakdown": """\
            西 = さい (west)
            京 = きょう (capital)"""
    },
    {
        "word": "南",
        "reading": "みなみ (minami)",
        "meaning": "south",
        "breakdown": """\
            南 = みなみ (south)"""
    },
    {
        "word": "南口",
        "reading": "みなみぐち (minamiguchi)",
        "meaning": "south exit",
        "breakdown": """\
            南 = みなみ (south)
            口 = ぐち (mouth)"""
    },
    {
        "word": "南北",
        "reading": "なんぼく (nanboku)",
        "meaning": "north and south",
        "breakdown": """\
            南 = なん (south)
            北 = ぼく (north)"""
    },
    {
        "word": "南東",
        "reading": "なんとう (nantou)",
        "meaning": "southeast",
        "breakdown": """\
            南 = なん (south)
            東 = とう (east)"""
    },
    {
        "word": "南西",
        "reading": "なんせい (nansei)",
        "meaning": "southwest",
        "breakdown": """\
            南 = なん (south)
            西 = せい (west)"""
    },
    {
        "word": "南国",
        "reading": "なんごく (nangoku)",
        "meaning": "southern country",
        "breakdown": """\
            南 = なん (south)
            国 = ごく (country)"""
    },
    {
        "word": "北",
        "reading": "きた (kita)",
        "meaning": "north",
        "breakdown": """\
            北 = きた (north)"""
    },
    {
        "word": "北口",
        "reading": "きたぐち (kitaguchi)",
        "meaning": "north exit",
        "breakdown": """\
            北 = きた (north)
            口 = ぐち (mouth)"""
    },
    {
        "word": "北国",
        "reading": "きたぐに (kitaguni)",
        "meaning": "northern country",
        "breakdown": """\
            北 = きた (north)
            国 = ぐに (country)"""
    },
    {
        "word": "北東",
        "reading": "ほくとう (hokutou)",
        "meaning": "northeast",
        "breakdown": """\
            北 = ほく (north)
            東 = とう (east)"""
    },
    {
        "word": "北西",
        "reading": "ほくせい (hokusei)",
        "meaning": "northwest",
        "breakdown": """\
            北 = ほく (north)
            西 = せい (west)"""
    },
    {
        "word": "国",
        "reading": "くに (kuni)",
        "meaning": "country",
        "breakdown": """\
            国 = くに (country)"""
    },
    {
        "word": "国語",
        "reading": "こくご (kokugo)",
        "meaning": "national language",
        "breakdown": """\
            国 = こく (country)
            語 = ご (language / word)"""
    },
    {
        "word": "国道",
        "reading": "こくどう (kokudou)",
        "meaning": "national highway",
        "breakdown": """\
            国 = こく (country)
            道 = どう (road / way)"""
    },
    {
        "word": "国立",
        "reading": "こくりつ (kokuritsu)",
        "meaning": "national",
        "breakdown": """\
            国 = こく (country)
            立 = りつ (stand)"""
    },
    {
        "word": "大国",
        "reading": "たいこく (taikoku)",
        "meaning": "great power",
        "breakdown": """\
            大 = たい (big)
            国 = こく (country)"""
    },
    {
        "word": "小国",
        "reading": "しょうこく (shoukoku)",
        "meaning": "small country",
        "breakdown": """\
            小 = しょう (small)
            国 = こく (country)"""
    },
    {
        "word": "帰国",
        "reading": "きこく (kikoku)",
        "meaning": "returning to one's country",
        "breakdown": """\
            帰 = き (return)
            国 = こく (country)"""
    },
    {
        "word": "入国",
        "reading": "にゅうこく (nyuukoku)",
        "meaning": "entering a country",
        "breakdown": """\
            入 = にゅう (enter)
            国 = こく (country)"""
    },
    {
        "word": "出国",
        "reading": "しゅっこく (shukkoku)",
        "meaning": "leaving a country",
        "breakdown": """\
            出 = しゅっ (exit / take out)
            国 = こく (country)"""
    },
    {
        "word": "本国",
        "reading": "ほんごく (hongoku)",
        "meaning": "home country",
        "breakdown": """\
            本 = ほん (book / origin)
            国 = ごく (country)"""
    },
    {
        "word": "国会",
        "reading": "こっかい (kokkai)",
        "meaning": "parliament",
        "breakdown": """\
            国 = こっ (country)
            会 = かい (meet)"""
    },
    {
        "word": "道",
        "reading": "みち (michi)",
        "meaning": "road",
        "breakdown": """\
            道 = みち (road / way)"""
    },
    {
        "word": "道",
        "reading": "どう (dou)",
        "meaning": "way",
        "breakdown": """\
            道 = どう (road / way)"""
    },
    {
        "word": "小道",
        "reading": "こみち (komichi)",
        "meaning": "path",
        "breakdown": """\
            小 = こ (small)
            道 = みち (road / way)"""
    },
    {
        "word": "大道",
        "reading": "だいどう (daidou)",
        "meaning": "main street",
        "breakdown": """\
            大 = だい (big)
            道 = どう (road / way)"""
    },
    {
        "word": "書道",
        "reading": "しょどう (shodou)",
        "meaning": "calligraphy",
        "breakdown": """\
            書 = しょ (write)
            道 = どう (road / way)"""
    },
    {
        "word": "車道",
        "reading": "しゃどう (shadou)",
        "meaning": "roadway",
        "breakdown": """\
            車 = しゃ (car)
            道 = どう (road / way)"""
    },
    {
        "word": "食道",
        "reading": "しょくどう (shokudou)",
        "meaning": "esophagus",
        "breakdown": """\
            食 = しょく (eat)
            道 = どう (road / way)"""
    },
    {
        "word": "学",
        "reading": "がく (gaku)",
        "meaning": "study",
        "breakdown": """\
            学 = がく (study)"""
    },
    {
        "word": "学校",
        "reading": "がっこう (gakkou)",
        "meaning": "school",
        "breakdown": """\
            学 = がっ (study)
            校 = こう (school)"""
    },
    {
        "word": "大学",
        "reading": "だいがく (daigaku)",
        "meaning": "university",
        "breakdown": """\
            大 = だい (big)
            学 = がく (study)"""
    },
    {
        "word": "小学校",
        "reading": "しょうがっこう (shougakkou)",
        "meaning": "elementary school",
        "breakdown": """\
            小 = しょう (small)
            学 = がっ (study)
            校 = こう (school)"""
    },
    {
        "word": "学ぶ",
        "reading": "まなぶ (manabu)",
        "meaning": "to learn",
        "breakdown": """\
            学 = まな (study)
            ぶ = okurigana"""
    },
    {
        "word": "学長",
        "reading": "がくちょう (gakuchou)",
        "meaning": "university president",
        "breakdown": """\
            学 = がく (study)
            長 = ちょう (long)"""
    },
    {
        "word": "入学",
        "reading": "にゅうがく (nyuugaku)",
        "meaning": "enrolling in school",
        "breakdown": """\
            入 = にゅう (enter)
            学 = がく (study)"""
    },
    {
        "word": "休学",
        "reading": "きゅうがく (kyuugaku)",
        "meaning": "leave of absence",
        "breakdown": """\
            休 = きゅう (rest)
            学 = がく (study)"""
    },
    {
        "word": "学会",
        "reading": "がっかい (gakkai)",
        "meaning": "academic society",
        "breakdown": """\
            学 = がっ (study)
            会 = かい (meet)"""
    },
    {
        "word": "語学",
        "reading": "ごがく (gogaku)",
        "meaning": "language study",
        "breakdown": """\
            語 = ご (language / word)
            学 = がく (study)"""
    },
    {
        "word": "文学",
        "reading": "ぶんがく (bungaku)",
        "meaning": "literature",
        "breakdown": """\
            文 = ぶん (sentence)
            学 = がく (study)"""
    },
    {
        "word": "見学",
        "reading": "けんがく (kengaku)",
        "meaning": "field trip",
        "breakdown": """\
            見 = けん (see)
            学 = がく (study)"""
    },
    {
        "word": "中学校",
        "reading": "ちゅうがっこう (chuugakkou)",
        "meaning": "junior high school",
        "breakdown": """\
            中 = ちゅう (inside / middle)
            学 = がっ (study)
            校 = こう (school)"""
    },
    {
        "word": "校",
        "reading": "こう (kou)",
        "meaning": "school",
        "breakdown": """\
            校 = こう (school)"""
    },
    {
        "word": "校長",
        "reading": "こうちょう (kouchou)",
        "meaning": "principal",
        "breakdown": """\
            校 = こう (school)
            長 = ちょう (long)"""
    },
    {
        "word": "高校",
        "reading": "こうこう (koukou)",
        "meaning": "high school",
        "breakdown": """\
            高 = こう (tall / expensive)
            校 = こう (school)"""
    },
    {
        "word": "休校",
        "reading": "きゅうこう (kyuukou)",
        "meaning": "school closure",
        "breakdown": """\
            休 = きゅう (rest)
            校 = こう (school)"""
    },
    {
        "word": "帰校",
        "reading": "きこう (kikou)",
        "meaning": "return to school",
        "breakdown": """\
            帰 = き (return)
            校 = こう (school)"""
    },
    {
        "word": "本",
        "reading": "ほん (hon)",
        "meaning": "book",
        "breakdown": """\
            本 = ほん (book / origin)"""
    },
    {
        "word": "本",
        "reading": "もと (moto)",
        "meaning": "origin",
        "breakdown": """\
            本 = もと (book / origin)"""
    },
    {
        "word": "山本",
        "reading": "やまもと (yamamoto)",
        "meaning": "Yamamoto",
        "breakdown": """\
            山 = やま (mountain)
            本 = もと (book / origin)"""
    },
    {
        "word": "日本語",
        "reading": "にほんご (nihongo)",
        "meaning": "Japanese language",
        "breakdown": """\
            日 = に (day / sun)
            本 = ほん (book / origin)
            語 = ご (language / word)"""
    },
    {
        "word": "古本",
        "reading": "ふるほん (furuhon)",
        "meaning": "used book",
        "breakdown": """\
            古 = ふる (old)
            本 = ほん (book / origin)"""
    },
    {
        "word": "見本",
        "reading": "みほん (mihon)",
        "meaning": "sample",
        "breakdown": """\
            見 = み (see)
            本 = ほん (book / origin)"""
    },
    {
        "word": "読本",
        "reading": "どくほん (dokuhon)",
        "meaning": "reader",
        "breakdown": """\
            読 = どく (read)
            本 = ほん (book / origin)"""
    },
    {
        "word": "語",
        "reading": "ご (go)",
        "meaning": "language",
        "breakdown": """\
            語 = ご (language / word)"""
    },
    {
        "word": "語る",
        "reading": "かたる (kataru)",
        "meaning": "to tell",
        "breakdown": """\
            語 = かた (language / word)
            る = okurigana"""
    },
    {
        "word": "中国語",
        "reading": "ちゅうごくご (chuugokugo)",
        "meaning": "Chinese language",
        "breakdown": """\
            中 = ちゅう (inside / middle)
            国 = ごく (country)
            語 = ご (language / word)"""
    },
    {
        "word": "言語",
        "reading": "げんご (gengo)",
        "meaning": "language",
        "breakdown": """\
            言 = げん (say)
            語 = ご (language / word)"""
    },
    {
        "word": "口語",
        "reading": "こうご (kougo)",
        "meaning": "colloquial language",
        "breakdown": """\
            口 = こう (mouth)
            語 = ご (language / word)"""
    },
    {
        "word": "文語",
        "reading": "ぶんご (bungo)",
        "meaning": "literary language",
        "breakdown": """\
            文 = ぶん (sentence)
            語 = ご (language / word)"""
    },
    {
        "word": "文",
        "reading": "ぶん (bun)",
        "meaning": "sentence",
        "breakdown": """\
            文 = ぶん (sentence)"""
    },
    {
        "word": "文字",
        "reading": "もんじ (monji)",
        "meaning": "letter / character",
        "breakdown": """\
            文 = もん (sentence)
            字 = じ (character)"""
    },
    {
        "word": "文書",
        "reading": "ぶんしょ (bunsho)",
        "meaning": "document",
        "breakdown": """\
            文 = ぶん (sentence)
            書 = しょ (write)"""
    },
    {
        "word": "字",
        "reading": "じ (ji)",
        "meaning": "character",
        "breakdown": """\
            字 = じ (character)"""
    },
    {
        "word": "文字",
        "reading": "もじ (moji)",
        "meaning": "character",
        "breakdown": """\
            文 = も (sentence)
            字 = じ (character)"""
    },
    {
        "word": "赤字",
        "reading": "あかじ (akaji)",
        "meaning": "deficit",
        "breakdown": """\
            赤 = あか (red)
            字 = じ (character)"""
    },
    {
        "word": "黒字",
        "reading": "くろじ (kuroji)",
        "meaning": "surplus",
        "breakdown": """\
            黒 = くろ (black)
            字 = じ (character)"""
    },
    {
        "word": "大字",
        "reading": "おおあざ (ooaza)",
        "meaning": "large district",
        "breakdown": """\
            大 = おお (big)
            字 = あざ (character)"""
    },
    {
        "word": "小字",
        "reading": "こあざ (koaza)",
        "meaning": "small district",
        "breakdown": """\
            小 = こ (small)
            字 = あざ (character)"""
    },
    {
        "word": "書く",
        "reading": "かく (kaku)",
        "meaning": "to write",
        "breakdown": """\
            書 = か (write)
            く = okurigana"""
    },
    {
        "word": "書き方",
        "reading": "かきかた (kakikata)",
        "meaning": "how to write",
        "breakdown": """\
            書 = か (write)
            き = okurigana
            方 = かた (direction / way)"""
    },
    {
        "word": "手書き",
        "reading": "てがき (tegaki)",
        "meaning": "handwritten",
        "breakdown": """\
            手 = て (hand)
            書 = が (write)
            き = okurigana"""
    },
    {
        "word": "書",
        "reading": "しょ (sho)",
        "meaning": "writing",
        "breakdown": """\
            書 = しょ (write)"""
    },
    {
        "word": "読書",
        "reading": "どくしょ (dokusho)",
        "meaning": "reading",
        "breakdown": """\
            読 = どく (read)
            書 = しょ (write)"""
    },
    {
        "word": "読み書き",
        "reading": "よみかき (yomikaki)",
        "meaning": "reading and writing",
        "breakdown": """\
            読 = よ (read)
            み = okurigana
            書 = か (write)
            き = okurigana"""
    },
    {
        "word": "読む",
        "reading": "よむ (yomu)",
        "meaning": "to read",
        "breakdown": """\
            読 = よ (read)
            む = okurigana"""
    },
    {
        "word": "読み方",
        "reading": "よみかた (yomikata)",
        "meaning": "how to read",
        "breakdown": """\
            読 = よ (read)
            み = okurigana
            方 = かた (direction / way)"""
    },
    {
        "word": "聞く",
        "reading": "きく (kiku)",
        "meaning": "to listen",
        "breakdown": """\
            聞 = き (listen / hear)
            く = okurigana"""
    },
    {
        "word": "聞こえる",
        "reading": "きこえる (kikoeru)",
        "meaning": "to be audible",
        "breakdown": """\
            聞 = き (listen / hear)
            こえる = okurigana"""
    },
    {
        "word": "新聞",
        "reading": "しんぶん (shinbun)",
        "meaning": "newspaper",
        "breakdown": """\
            新 = しん (new)
            聞 = ぶん (listen / hear)"""
    },
    {
        "word": "見聞",
        "reading": "けんぶん (kenbun)",
        "meaning": "experience",
        "breakdown": """\
            見 = けん (see)
            聞 = ぶん (listen / hear)"""
    },
    {
        "word": "聞き手",
        "reading": "ききて (kikite)",
        "meaning": "listener",
        "breakdown": """\
            聞 = き (listen / hear)
            き = okurigana
            手 = て (hand)"""
    },
    {
        "word": "話す",
        "reading": "はなす (hanasu)",
        "meaning": "to speak",
        "breakdown": """\
            話 = はな (speak / story)
            す = okurigana"""
    },
    {
        "word": "話",
        "reading": "はなし (hanashi)",
        "meaning": "story",
        "breakdown": """\
            話 = はなし (speak / story)"""
    },
    {
        "word": "話し手",
        "reading": "はなして (hanashite)",
        "meaning": "speaker",
        "breakdown": """\
            話 = はな (speak / story)
            し = okurigana
            手 = て (hand)"""
    },
    {
        "word": "会話",
        "reading": "かいわ (kaiwa)",
        "meaning": "conversation",
        "breakdown": """\
            会 = かい (meet)
            話 = わ (speak / story)"""
    },
    {
        "word": "手話",
        "reading": "しゅわ (shuwa)",
        "meaning": "sign language",
        "breakdown": """\
            手 = しゅ (hand)
            話 = わ (speak / story)"""
    },
    {
        "word": "行く",
        "reading": "いく (iku)",
        "meaning": "to go",
        "breakdown": """\
            行 = い (go)
            く = okurigana"""
    },
    {
        "word": "行う",
        "reading": "おこなう (okonau)",
        "meaning": "to carry out",
        "breakdown": """\
            行 = おこな (go)
            う = okurigana"""
    },
    {
        "word": "行き来",
        "reading": "ゆきき (yukiki)",
        "meaning": "coming and going",
        "breakdown": """\
            行 = ゆ (go)
            き = okurigana
            来 = き (come)"""
    },
    {
        "word": "先行",
        "reading": "せんこう (senkou)",
        "meaning": "preceding",
        "breakdown": """\
            先 = せん (previous / ahead)
            行 = こう (go)"""
    },
    {
        "word": "三行",
        "reading": "さんぎょう (sangyou)",
        "meaning": "three lines",
        "breakdown": """\
            三 = さん (three)
            行 = ぎょう (go)"""
    },
    {
        "word": "来る",
        "reading": "くる (kuru)",
        "meaning": "to come",
        "breakdown": """\
            来 = く (come)
            る = okurigana"""
    },
    {
        "word": "来た",
        "reading": "きた (kita)",
        "meaning": "came",
        "breakdown": """\
            来 = き (come)
            た = okurigana"""
    },
    {
        "word": "来ない",
        "reading": "こない (konai)",
        "meaning": "doesn't come",
        "breakdown": """\
            来 = こ (come)
            ない = okurigana"""
    },
    {
        "word": "本来",
        "reading": "ほんらい (honrai)",
        "meaning": "originally",
        "breakdown": """\
            本 = ほん (book / origin)
            来 = らい (come)"""
    },
    {
        "word": "出来る",
        "reading": "できる (dekiru)",
        "meaning": "to be able to",
        "breakdown": """\
            出 = で (exit / take out)
            来 = き (come)
            る = okurigana"""
    },
    {
        "word": "帰る",
        "reading": "かえる (kaeru)",
        "meaning": "to return",
        "breakdown": """\
            帰 = かえ (return)
            る = okurigana"""
    },
    {
        "word": "帰り",
        "reading": "かえり (kaeri)",
        "meaning": "return",
        "breakdown": """\
            帰 = かえ (return)
            り = okurigana"""
    },
    {
        "word": "帰す",
        "reading": "かえす (kaesu)",
        "meaning": "to send back",
        "breakdown": """\
            帰 = かえ (return)
            す = okurigana"""
    },
    {
        "word": "帰り道",
        "reading": "かえりみち (kaerimichi)",
        "meaning": "way home",
        "breakdown": """\
            帰 = かえ (return)
            り = okurigana
            道 = みち (road / way)"""
    },
    {
        "word": "入る",
        "reading": "はいる (hairu)",
        "meaning": "to enter",
        "breakdown": """\
            入 = はい (enter)
            る = okurigana"""
    },
    {
        "word": "入れる",
        "reading": "いれる (ireru)",
        "meaning": "to put in",
        "breakdown": """\
            入 = い (enter)
            れる = okurigana"""
    },
    {
        "word": "入口",
        "reading": "いりぐち (iriguchi)",
        "meaning": "entrance",
        "breakdown": """\
            入 = いり (enter)
            口 = ぐち (mouth)"""
    },
    {
        "word": "入手",
        "reading": "にゅうしゅ (nyuushu)",
        "meaning": "obtaining",
        "breakdown": """\
            入 = にゅう (enter)
            手 = しゅ (hand)"""
    },
    {
        "word": "出入り",
        "reading": "でいり (deiri)",
        "meaning": "coming and going",
        "breakdown": """\
            出 = で (exit / take out)
            入 = い (enter)
            り = okurigana"""
    },
    {
        "word": "新入",
        "reading": "しんにゅう (shinnyuu)",
        "meaning": "new entrant",
        "breakdown": """\
            新 = しん (new)
            入 = にゅう (enter)"""
    },
    {
        "word": "買い入れ",
        "reading": "かいいれ (kaiire)",
        "meaning": "purchase",
        "breakdown": """\
            買 = か (buy)
            い = okurigana
            入 = い (enter)
            れ = okurigana"""
    },
    {
        "word": "出る",
        "reading": "でる (deru)",
        "meaning": "to go out",
        "breakdown": """\
            出 = で (exit / take out)
            る = okurigana"""
    },
    {
        "word": "出す",
        "reading": "だす (dasu)",
        "meaning": "to take out",
        "breakdown": """\
            出 = だ (exit / take out)
            す = okurigana"""
    },
    {
        "word": "出口",
        "reading": "でぐち (deguchi)",
        "meaning": "exit",
        "breakdown": """\
            出 = で (exit / take out)
            口 = ぐち (mouth)"""
    },
    {
        "word": "出会う",
        "reading": "であう (deau)",
        "meaning": "to meet by chance",
        "breakdown": """\
            出 = で (exit / take out)
            会 = あ (meet)
            う = okurigana"""
    },
    {
        "word": "見る",
        "reading": "みる (miru)",
        "meaning": "to see",
        "breakdown": """\
            見 = み (see)
            る = okurigana"""
    },
    {
        "word": "見える",
        "reading": "みえる (mieru)",
        "meaning": "to be visible",
        "breakdown": """\
            見 = み (see)
            える = okurigana"""
    },
    {
        "word": "見方",
        "reading": "みかた (mikata)",
        "meaning": "viewpoint",
        "breakdown": """\
            見 = み (see)
            方 = かた (direction / way)"""
    },
    {
        "word": "食べる",
        "reading": "たべる (taberu)",
        "meaning": "to eat",
        "breakdown": """\
            食 = た (eat)
            べる = okurigana"""
    },
    {
        "word": "食う",
        "reading": "くう (kuu)",
        "meaning": "to eat (rough)",
        "breakdown": """\
            食 = く (eat)
            う = okurigana"""
    },
    {
        "word": "飲む",
        "reading": "のむ (nomu)",
        "meaning": "to drink",
        "breakdown": """\
            飲 = の (drink)
            む = okurigana"""
    },
    {
        "word": "飲食",
        "reading": "いんしょく (inshoku)",
        "meaning": "food and drink",
        "breakdown": """\
            飲 = いん (drink)
            食 = しょく (eat)"""
    },
    {
        "word": "飲み方",
        "reading": "のみかた (nomikata)",
        "meaning": "how to drink",
        "breakdown": """\
            飲 = の (drink)
            み = okurigana
            方 = かた (direction / way)"""
    },
    {
        "word": "飲み口",
        "reading": "のみくち (nomikuchi)",
        "meaning": "drinking rim",
        "breakdown": """\
            飲 = の (drink)
            み = okurigana
            口 = くち (mouth)"""
    },
    {
        "word": "休む",
        "reading": "やすむ (yasumu)",
        "meaning": "to rest",
        "breakdown": """\
            休 = やす (rest)
            む = okurigana"""
    },
    {
        "word": "休み",
        "reading": "やすみ (yasumi)",
        "meaning": "rest / holiday",
        "breakdown": """\
            休 = やす (rest)
            み = okurigana"""
    },
    {
        "word": "休み時間",
        "reading": "やすみじかん (yasumijikan)",
        "meaning": "break time",
        "breakdown": """\
            休 = やす (rest)
            み = okurigana
            時 = じ (time / hour)
            間 = かん (between / interval)"""
    },
    {
        "word": "休み中",
        "reading": "やすみちゅう (yasumichuu)",
        "meaning": "during the break",
        "breakdown": """\
            休 = やす (rest)
            み = okurigana
            中 = ちゅう (inside / middle)"""
    },
    {
        "word": "買う",
        "reading": "かう (kau)",
        "meaning": "to buy",
        "breakdown": """\
            買 = か (buy)
            う = okurigana"""
    },
    {
        "word": "買い手",
        "reading": "かいて (kaite)",
        "meaning": "buyer",
        "breakdown": """\
            買 = か (buy)
            い = okurigana
            手 = て (hand)"""
    },
    {
        "word": "買い方",
        "reading": "かいかた (kaikata)",
        "meaning": "how to buy",
        "breakdown": """\
            買 = か (buy)
            い = okurigana
            方 = かた (direction / way)"""
    },
    {
        "word": "売買",
        "reading": "ばいばい (baibai)",
        "meaning": "buying and selling",
        "breakdown": """\
            売 = ばい (sell)
            買 = ばい (buy)"""
    },
    {
        "word": "会う",
        "reading": "あう (au)",
        "meaning": "to meet",
        "breakdown": """\
            会 = あ (meet)
            う = okurigana"""
    },
    {
        "word": "会長",
        "reading": "かいちょう (kaichou)",
        "meaning": "chairman",
        "breakdown": """\
            会 = かい (meet)
            長 = ちょう (long)"""
    },
    {
        "word": "立つ",
        "reading": "たつ (tatsu)",
        "meaning": "to stand",
        "breakdown": """\
            立 = た (stand)
            つ = okurigana"""
    },
    {
        "word": "立てる",
        "reading": "たてる (tateru)",
        "meaning": "to set up",
        "breakdown": """\
            立 = た (stand)
            てる = okurigana"""
    },
    {
        "word": "言う",
        "reading": "いう (iu)",
        "meaning": "to say",
        "breakdown": """\
            言 = い (say)
            う = okurigana"""
    },
    {
        "word": "言い方",
        "reading": "いいかた (iikata)",
        "meaning": "way of saying",
        "breakdown": """\
            言 = い (say)
            い = okurigana
            方 = かた (direction / way)"""
    },
    {
        "word": "前言",
        "reading": "ぜんげん (zengen)",
        "meaning": "previous remark",
        "breakdown": """\
            前 = ぜん (before / front)
            言 = げん (say)"""
    },
    {
        "word": "待つ",
        "reading": "まつ (matsu)",
        "meaning": "to wait",
        "breakdown": """\
            待 = ま (wait)
            つ = okurigana"""
    },
    {
        "word": "待ち時間",
        "reading": "まちじかん (machijikan)",
        "meaning": "waiting time",
        "breakdown": """\
            待 = ま (wait)
            ち = okurigana
            時 = じ (time / hour)
            間 = かん (between / interval)"""
    },
    {
        "word": "招待",
        "reading": "しょうたい (shoutai)",
        "meaning": "invitation",
        "breakdown": """\
            招 = しょう (invite)
            待 = たい (wait)"""
    },
    {
        "word": "大",
        "reading": "だい (dai)",
        "meaning": "big",
        "breakdown": """\
            大 = だい (big)"""
    },
    {
        "word": "大きい",
        "reading": "おおきい (ookii)",
        "meaning": "big",
        "breakdown": """\
            大 = おお (big)
            きい = okurigana"""
    },
    {
        "word": "大会",
        "reading": "たいかい (taikai)",
        "meaning": "tournament",
        "breakdown": """\
            大 = たい (big)
            会 = かい (meet)"""
    },
    {
        "word": "大小",
        "reading": "だいしょう (daishou)",
        "meaning": "large and small",
        "breakdown": """\
            大 = だい (big)
            小 = しょう (small)"""
    },
    {
        "word": "小",
        "reading": "しょう (shou)",
        "meaning": "small",
        "breakdown": """\
            小 = しょう (small)"""
    },
    {
        "word": "小さい",
        "reading": "ちいさい (chiisai)",
        "meaning": "small",
        "breakdown": """\
            小 = ちい (small)
            さい = okurigana"""
    },
    {
        "word": "高い",
        "reading": "たかい (takai)",
        "meaning": "tall / expensive",
        "breakdown": """\
            高 = たか (tall / expensive)
            い = okurigana"""
    },
    {
        "word": "高",
        "reading": "こう (kou)",
        "meaning": "high",
        "breakdown": """\
            高 = こう (tall / expensive)"""
    },
    {
        "word": "安い",
        "reading": "やすい (yasui)",
        "meaning": "cheap",
        "breakdown": """\
            安 = やす (cheap / safe)
            い = okurigana"""
    },
    {
        "word": "安心",
        "reading": "あんしん (anshin)",
        "meaning": "peace of mind",
        "breakdown": """\
            安 = あん (cheap / safe)
            心 = しん (heart)"""
    },
    {
        "word": "安全",
        "reading": "あんぜん (anzen)",
        "meaning": "safety",
        "breakdown": """\
            安 = あん (cheap / safe)
            全 = ぜん (whole / all)"""
    },
    {
        "word": "新しい",
        "reading": "あたらしい (atarashii)",
        "meaning": "new",
        "breakdown": """\
            新 = あたら (new)
            しい = okurigana"""
    },
    {
        "word": "新手",
        "reading": "あらて (arate)",
        "meaning": "new type",
        "breakdown": """\
            新 = あら (new)
            手 = て (hand)"""
    },
    {
        "word": "新道",
        "reading": "しんどう (shindou)",
        "meaning": "new road",
        "breakdown": """\
            新 = しん (new)
            道 = どう (road / way)"""
    },
    {
        "word": "新車",
        "reading": "しんしゃ (shinsha)",
        "meaning": "new car",
        "breakdown": """\
            新 = しん (new)
            車 = しゃ (car)"""
    },
    {
        "word": "古い",
        "reading": "ふるい (furui)",
        "meaning": "old",
        "breakdown": """\
            古 = ふる (old)
            い = okurigana"""
    },
    {
        "word": "古車",
        "reading": "こしゃ (kosha)",
        "meaning": "used car",
        "breakdown": """\
            古 = こ (old)
            車 = しゃ (car)"""
    },
    {
        "word": "古道",
        "reading": "こどう (kodou)",
        "meaning": "old road",
        "breakdown": """\
            古 = こ (old)
            道 = どう (road / way)"""
    },
    {
        "word": "長い",
        "reading": "ながい (nagai)",
        "meaning": "long",
        "breakdown": """\
            長 = なが (long)
            い = okurigana"""
    },
    {
        "word": "長",
        "reading": "ちょう (chou)",
        "meaning": "chief / long",
        "breakdown": """\
            長 = ちょう (long)"""
    },
    {
        "word": "多い",
        "reading": "おおい (ooi)",
        "meaning": "many",
        "breakdown": """\
            多 = おお (many)
            い = okurigana"""
    },
    {
        "word": "多",
        "reading": "た (ta)",
        "meaning": "many",
        "breakdown": """\
            多 = た (many)"""
    },
    {
        "word": "多少",
        "reading": "たしょう (tashou)",
        "meaning": "more or less",
        "breakdown": """\
            多 = た (many)
            少 = しょう (few)"""
    },
    {
        "word": "少ない",
        "reading": "すくない (sukunai)",
        "meaning": "few",
        "breakdown": """\
            少 = すく (few)
            ない = okurigana"""
    },
    {
        "word": "少し",
        "reading": "すこし (sukoshi)",
        "meaning": "a little",
        "breakdown": """\
            少 = すこ (few)
            し = okurigana"""
    },
    {
        "word": "少",
        "reading": "しょう (shou)",
        "meaning": "few",
        "breakdown": """\
            少 = しょう (few)"""
    },
    {
        "word": "白",
        "reading": "しろ (shiro)",
        "meaning": "white",
        "breakdown": """\
            白 = しろ (white)"""
    },
    {
        "word": "白い",
        "reading": "しろい (shiroi)",
        "meaning": "white",
        "breakdown": """\
            白 = しろ (white)
            い = okurigana"""
    },
    {
        "word": "白黒",
        "reading": "しろくろ (shirokuro)",
        "meaning": "black and white",
        "breakdown": """\
            白 = しろ (white)
            黒 = くろ (black)"""
    },
    {
        "word": "赤白",
        "reading": "あかしろ (akashiro)",
        "meaning": "red and white",
        "breakdown": """\
            赤 = あか (red)
            白 = しろ (white)"""
    },
    {
        "word": "青白い",
        "reading": "あおじろい (aojiroi)",
        "meaning": "pale",
        "breakdown": """\
            青 = あお (blue)
            白 = じろ (white)
            い = okurigana"""
    },
    {
        "word": "赤",
        "reading": "あか (aka)",
        "meaning": "red",
        "breakdown": """\
            赤 = あか (red)"""
    },
    {
        "word": "赤い",
        "reading": "あかい (akai)",
        "meaning": "red",
        "breakdown": """\
            赤 = あか (red)
            い = okurigana"""
    },
    {
        "word": "赤道",
        "reading": "せきどう (sekidou)",
        "meaning": "equator",
        "breakdown": """\
            赤 = せき (red)
            道 = どう (road / way)"""
    },
    {
        "word": "青",
        "reading": "あお (ao)",
        "meaning": "blue",
        "breakdown": """\
            青 = あお (blue)"""
    },
    {
        "word": "青い",
        "reading": "あおい (aoi)",
        "meaning": "blue",
        "breakdown": """\
            青 = あお (blue)
            い = okurigana"""
    },
    {
        "word": "黒",
        "reading": "くろ (kuro)",
        "meaning": "black",
        "breakdown": """\
            黒 = くろ (black)"""
    },
    {
        "word": "黒い",
        "reading": "くろい (kuroi)",
        "meaning": "black",
        "breakdown": """\
            黒 = くろ (black)
            い = okurigana"""
    },
    {
        "word": "黒目",
        "reading": "くろめ (kurome)",
        "meaning": "pupil of the eye",
        "breakdown": """\
            黒 = くろ (black)
            目 = め (eye)"""
    },
    {
        "word": "明るい",
        "reading": "あかるい (akarui)",
        "meaning": "bright",
        "breakdown": """\
            明 = あか (bright)
            るい = okurigana"""
    },
    {
        "word": "明ける",
        "reading": "あける (akeru)",
        "meaning": "to dawn",
        "breakdown": """\
            明 = あ (bright)
            ける = okurigana"""
    },
    {
        "word": "明",
        "reading": "めい (mei)",
        "meaning": "bright",
        "breakdown": """\
            明 = めい (bright)"""
    },
    {
        "word": "車",
        "reading": "くるま (kuruma)",
        "meaning": "car",
        "breakdown": """\
            車 = くるま (car)"""
    },
    {
        "word": "何",
        "reading": "なに (nani)",
        "meaning": "what",
        "breakdown": """\
            何 = なに (what)"""
    },
    {
        "word": "何",
        "reading": "なん (nan)",
        "meaning": "what",
        "breakdown": """\
            何 = なん (what)"""
    },
    {
        "word": "何人",
        "reading": "なんにん (nannin)",
        "meaning": "how many people",
        "breakdown": """\
            何 = なん (what)
            人 = にん (person)"""
    },
    {
        "word": "何日",
        "reading": "なんにち (nannichi)",
        "meaning": "what day",
        "breakdown": """\
            何 = なん (what)
            日 = にち (day / sun)"""
    },
    {
        "word": "何年",
        "reading": "なんねん (nannen)",
        "meaning": "how many years",
        "breakdown": """\
            何 = なん (what)
            年 = ねん (year)"""
    },
    {
        "word": "何月",
        "reading": "なんがつ (nangatsu)",
        "meaning": "what month",
        "breakdown": """\
            何 = なん (what)
            月 = がつ (month / moon)"""
    },
    {
        "word": "何本",
        "reading": "なんぼん (nanbon)",
        "meaning": "how many (long objects)",
        "breakdown": """\
            何 = なん (what)
            本 = ぼん (book / origin)"""
    },
    {
        "word": "何円",
        "reading": "なんえん (nan'en)",
        "meaning": "how many yen",
        "breakdown": """\
            何 = なん (what)
            円 = えん (yen / circle)"""
    },
    {
        "word": "何曜日",
        "reading": "なんようび (nan'youbi)",
        "meaning": "what day of the week",
        "breakdown": """\
            何 = なん (what)
            曜 = よう (weekday)
            日 = び (day / sun)"""
    },
    {
        "word": "何語",
        "reading": "なにご (nanigo)",
        "meaning": "what language",
        "breakdown": """\
            何 = なに (what)
            語 = ご (language / word)"""
    },
    {
        "word": "何百",
        "reading": "なんびゃく (nanbyaku)",
        "meaning": "how many hundreds",
        "breakdown": """\
            何 = なん (what)
            百 = びゃく (hundred)"""
    },
    {
        "word": "何千",
        "reading": "なんぜん (nanzen)",
        "meaning": "how many thousands",
        "breakdown": """\
            何 = なん (what)
            千 = ぜん (thousand)"""
    },
    {
        "word": "何万",
        "reading": "なんまん (nanman)",
        "meaning": "how many ten-thousands",
        "breakdown": """\
            何 = なん (what)
            万 = まん (ten thousand)"""
    },
    {
        "word": "何人",
        "reading": "なにじん (nanijin)",
        "meaning": "what nationality",
        "breakdown": """\
            何 = なに (what)
            人 = じん (person)"""
    },
    {
        "word": "間",
        "reading": "あいだ (aida)",
        "meaning": "between",
        "breakdown": """\
            間 = あいだ (between / interval)"""
    },
    {
        "word": "手間",
        "reading": "てま (tema)",
        "meaning": "time and effort",
        "breakdown": """\
            手 = て (hand)
            間 = ま (between / interval)"""
    },
    {
        "word": "間",
        "reading": "ま (ma)",
        "meaning": "space / interval",
        "breakdown": """\
            間 = ま (between / interval)"""
    },
    {
        "word": "口",
        "reading": "くち (kuchi)",
        "meaning": "mouth",
        "breakdown": """\
            口 = くち (mouth)"""
    },
    {
        "word": "口",
        "reading": "こう (kou)",
        "meaning": "mouth",
        "breakdown": """\
            口 = こう (mouth)"""
    },
    {
        "word": "出入口",
        "reading": "でいぐち (deiguchi)",
        "meaning": "doorway",
        "breakdown": """\
            出 = で (exit / take out)
            入 = い (enter)
            口 = ぐち (mouth)"""
    },
    {
        "word": "目",
        "reading": "め (me)",
        "meaning": "eye",
        "breakdown": """\
            目 = め (eye)"""
    },
    {
        "word": "手",
        "reading": "て (te)",
        "meaning": "hand",
        "breakdown": """\
            手 = て (hand)"""
    },
    {
        "word": "手",
        "reading": "しゅ (shu)",
        "meaning": "hand",
        "breakdown": """\
            手 = しゅ (hand)"""
    },
    {
        "word": "手足",
        "reading": "てあし (teashi)",
        "meaning": "hands and feet",
        "breakdown": """\
            手 = て (hand)
            足 = あし (foot / leg)"""
    },
    {
        "word": "手口",
        "reading": "てぐち (teguchi)",
        "meaning": "modus operandi",
        "breakdown": """\
            手 = て (hand)
            口 = ぐち (mouth)"""
    },
    {
        "word": "足",
        "reading": "あし (ashi)",
        "meaning": "foot",
        "breakdown": """\
            足 = あし (foot / leg)"""
    },
    {
        "word": "足りる",
        "reading": "たりる (tariru)",
        "meaning": "to be enough",
        "breakdown": """\
            足 = た (foot / leg)
            りる = okurigana"""
    },
    {
        "word": "足す",
        "reading": "たす (tasu)",
        "meaning": "to add",
        "breakdown": """\
            足 = た (foot / leg)
            す = okurigana"""
    },
    {
        "word": "足",
        "reading": "そく (soku)",
        "meaning": "foot",
        "breakdown": """\
            足 = そく (foot / leg)"""
    },
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

def create_anki_cards():
    print(f"Checking/Creating deck: '{DECK_NAME}'...")
    invoke("createDeck", deck=DECK_NAME)

    for item in word_list:
        # Remove leading indentation and turn newlines into HTML breaks
        raw_breakdown = textwrap.dedent(item.get("breakdown", ""))
        formatted_breakdown = raw_breakdown.replace("\n", "<br>")

        # Assemble data values
        item_data = item.copy()
        item_data["formatted_breakdown"] = formatted_breakdown

        # Map everything to your real Anki fields
        anki_fields = {}
        for anki_field, source_key in FIELD_MAPPING.items():
            anki_fields[anki_field] = item_data.get(source_key, "")

        note = {
            "deckName": DECK_NAME,
            "modelName": NOTE_TYPE_NAME,
            "fields": anki_fields,
            "tags": ["vocab_automation"]
        }

        result = invoke("addNote", note=note)
        if result:
            print(f"Successfully added card: {item['word']} ({item['reading']})")
        else:
            print(f"Failed to add card: {item['word']}.")

if __name__ == "__main__":
    create_anki_cards()
