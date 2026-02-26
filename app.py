from flask import Flask, render_template, request

app = Flask(__name__, template_folder='./')  # Task 5 feature branch demo

# Conversion functions
def kg_to_grams(kg):
    # INTENTIONAL BUG FOR TASK 5
    return kg * 1000

def grams_to_kg(grams):
    return grams * 0.001

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds * 0.453592

def grams_to_pounds(grams):
    kg = grams_to_kg(grams)
    return kg_to_pounds(kg)

def pounds_to_grams(pounds):
    kg = pounds_to_kg(pounds)
    return kg_to_grams(kg)


def main_conversion_function(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == 'kg' and to_unit == 'grams':
        return kg_to_grams(value)
    elif from_unit == 'grams' and to_unit == 'kg':
        return grams_to_kg(value)
    elif from_unit == 'kg' and to_unit == 'pounds':
        return kg_to_pounds(value)
    elif from_unit == 'pounds' and to_unit == 'kg':
        return pounds_to_kg(value)
    elif from_unit == 'grams' and to_unit == 'pounds':
        return grams_to_pounds(value)
    elif from_unit == 'pounds' and to_unit == 'grams':
        return pounds_to_grams(value)
    else:
        return "Invalid conversion"


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']

            result = main_conversion_function(value, from_unit, to_unit)

            if result != "Invalid conversion":
                result = f"{value} {from_unit} is equal to {result} {to_unit}"

        except ValueError:
            result = "Invalid input"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)