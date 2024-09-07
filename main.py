from flask import Flask, render_template, request, jsonify
from zodiac import get_western_zodiac_sign, get_indian_zodiac_sign, get_zodiac_info, get_zodiac_symbol, generate_daily_benefit

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_zodiac", methods=["POST"])
def get_zodiac():
    data = request.json
    birth_date = data.get("birthDate")
    zodiac_type = data.get("zodiacType")
    
    if not birth_date or not zodiac_type:
        return jsonify({"error": "Birth date and zodiac type are required"}), 400
    
    if zodiac_type == "western":
        zodiac_sign = get_western_zodiac_sign(birth_date)
    elif zodiac_type == "indian":
        zodiac_sign = get_indian_zodiac_sign(birth_date)
    else:
        return jsonify({"error": "Invalid zodiac type"}), 400
    
    zodiac_info = get_zodiac_info(zodiac_sign, zodiac_type)
    zodiac_symbol = get_zodiac_symbol(zodiac_sign, zodiac_type)
    daily_benefit = generate_daily_benefit(birth_date)
    
    return jsonify({
        "sign": zodiac_sign,
        "info": zodiac_info,
        "type": zodiac_type,
        "symbol": zodiac_symbol,
        "dailyBenefit": daily_benefit
    })

if __name__ == "__main__":
    app.run(debug=True, port=5001)
