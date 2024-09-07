from datetime import datetime
import random

def get_western_zodiac_sign(birth_date):
    date = datetime.strptime(birth_date, "%Y-%m-%d")
    month = date.month
    day = date.day

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

def get_indian_zodiac_sign(birth_date):
    date = datetime.strptime(birth_date, "%Y-%m-%d")
    month = date.month
    day = date.day

    if (month == 3 and day >= 15) or (month == 4 and day <= 13):
        return "Mesha (Aries)"
    elif (month == 4 and day >= 14) or (month == 5 and day <= 14):
        return "Vrishabha (Taurus)"
    elif (month == 5 and day >= 15) or (month == 6 and day <= 14):
        return "Mithuna (Gemini)"
    elif (month == 6 and day >= 15) or (month == 7 and day <= 14):
        return "Karka (Cancer)"
    elif (month == 7 and day >= 15) or (month == 8 and day <= 14):
        return "Simha (Leo)"
    elif (month == 8 and day >= 15) or (month == 9 and day <= 15):
        return "Kanya (Virgo)"
    elif (month == 9 and day >= 16) or (month == 10 and day <= 15):
        return "Tula (Libra)"
    elif (month == 10 and day >= 16) or (month == 11 and day <= 14):
        return "Vrishchika (Scorpio)"
    elif (month == 11 and day >= 15) or (month == 12 and day <= 14):
        return "Dhanu (Sagittarius)"
    elif (month == 12 and day >= 15) or (month == 1 and day <= 13):
        return "Makara (Capricorn)"
    elif (month == 1 and day >= 14) or (month == 2 and day <= 12):
        return "Kumbha (Aquarius)"
    else:
        return "Meena (Pisces)"

def get_zodiac_info(zodiac_sign, zodiac_type):
    western_zodiac_info = {
        "Aries": "Aries is a fire sign known for its boldness and leadership qualities.",
        "Taurus": "Taurus is an earth sign associated with stability and determination.",
        "Gemini": "Gemini is an air sign characterized by adaptability and curiosity.",
        "Cancer": "Cancer is a water sign known for its emotional depth and nurturing nature.",
        "Leo": "Leo is a fire sign associated with confidence and creativity.",
        "Virgo": "Virgo is an earth sign known for its analytical mind and attention to detail.",
        "Libra": "Libra is an air sign associated with balance and harmony.",
        "Scorpio": "Scorpio is a water sign known for its intensity and passion.",
        "Sagittarius": "Sagittarius is a fire sign associated with optimism and adventure.",
        "Capricorn": "Capricorn is an earth sign known for its ambition and discipline.",
        "Aquarius": "Aquarius is an air sign associated with innovation and humanitarianism.",
        "Pisces": "Pisces is a water sign known for its intuition and imagination."
    }

    indian_zodiac_info = {
        "Mesha (Aries)": "Mesha is associated with leadership, courage, and energy.",
        "Vrishabha (Taurus)": "Vrishabha is known for patience, reliability, and determination.",
        "Mithuna (Gemini)": "Mithuna represents communication, adaptability, and intelligence.",
        "Karka (Cancer)": "Karka is associated with emotions, nurturing, and intuition.",
        "Simha (Leo)": "Simha is known for creativity, confidence, and generosity.",
        "Kanya (Virgo)": "Kanya represents analytical skills, practicality, and perfectionism.",
        "Tula (Libra)": "Tula is associated with balance, harmony, and diplomacy.",
        "Vrishchika (Scorpio)": "Vrishchika is known for intensity, passion, and transformation.",
        "Dhanu (Sagittarius)": "Dhanu represents optimism, adventure, and philosophy.",
        "Makara (Capricorn)": "Makara is associated with ambition, discipline, and responsibility.",
        "Kumbha (Aquarius)": "Kumbha is known for innovation, individuality, and humanitarianism.",
        "Meena (Pisces)": "Meena represents intuition, creativity, and spirituality."
    }

    if zodiac_type == "western":
        return western_zodiac_info.get(zodiac_sign, "Information not available.")
    elif zodiac_type == "indian":
        return indian_zodiac_info.get(zodiac_sign, "Information not available.")
    else:
        return "Invalid zodiac type."

def get_zodiac_symbol(zodiac_sign, zodiac_type):
    western_symbols = {
        "Aries": "♈", "Taurus": "♉", "Gemini": "♊", "Cancer": "♋",
        "Leo": "♌", "Virgo": "♍", "Libra": "♎", "Scorpio": "♏",
        "Sagittarius": "♐", "Capricorn": "♑", "Aquarius": "♒", "Pisces": "♓"
    }
    
    indian_symbols = {
        "Mesha (Aries)": "मेष", "Vrishabha (Taurus)": "वृषभ", "Mithuna (Gemini)": "मिथुन",
        "Karka (Cancer)": "कर्क", "Simha (Leo)": "सिंह", "Kanya (Virgo)": "कन्या",
        "Tula (Libra)": "तुला", "Vrishchika (Scorpio)": "वृश्चिक", "Dhanu (Sagittarius)": "धनु",
        "Makara (Capricorn)": "मकर", "Kumbha (Aquarius)": "कुंभ", "Meena (Pisces)": "मीन"
    }
    
    if zodiac_type == "western":
        return western_symbols.get(zodiac_sign, "?")
    elif zodiac_type == "indian":
        return indian_symbols.get(zodiac_sign, "?")
    else:
        return "?"

def generate_daily_benefit(birth_date):
    date = datetime.strptime(birth_date, "%Y-%m-%d")
    seed = date.day + date.month + datetime.now().day + datetime.now().month
    random.seed(seed)
    
    benefits = [
        "Today is a great day for new beginnings.",
        "Focus on self-care and personal growth today.",
        "Your creative energy is high, use it wisely.",
        "A perfect day for strengthening relationships.",
        "Financial opportunities may come your way today.",
        "Trust your intuition in decision-making today.",
        "Your leadership skills will shine bright today.",
        "A day of learning and intellectual growth awaits you.",
        "Today brings harmony in your personal and professional life.",
        "Your determination will help you overcome challenges today."
    ]
    
    return random.choice(benefits)
