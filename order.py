from pyscript import display, document, HTML

# Order form

def ordering_form(e):
    document.getElementById('output').innerHTML = ""

    # Menu details

    food1 = document.getElementById('f1')
    food2 = document.getElementById('f2')
    food3 = document.getElementById('f3')
    food4 = document.getElementById('f4')
    food5 = document.getElementById('f5')

    drink1 = document.getElementById('d1')
    drink2 = document.getElementById('d2')
    drink3 = document.getElementById('d3')
    drink4 = document.getElementById('d4')
    drink5 = document.getElementById('d5')

    tax_rate = 0.06

    total = round(
        (float(food1.value) * food1.checked +
        float(food2.value) * food2.checked +
        float(food3.value) * food3.checked +
        float(food4.value) * food4.checked +
        float(food5.value) * food5.checked +
        float(drink1.value) * drink1.checked +
        float(drink2.value) * drink2.checked +
        float(drink3.value) * drink3.checked +
        float(drink4.value) * drink4.checked +
        float(drink5.value) * drink5.checked) * (1 + tax_rate), 2
    )

    # Customer details

    fname = document.getElementById('fName').value
    add = document.getElementById('address').value
    tel = document.getElementById('number').value

    # Output text

    display(f'Order for: {fname}', target='output')
    display(f'Address: {add}', target='output')
    display(f'Contact Number: {tel}', target='output')
    display(f'Total: ₱{total}', target='output')

    display(HTML("""
    <style>
        #output {
            background-color: #dc3545;
            color: white !important;
            padding: 10px;
            border-radius: 8px;
            font-size: 1.2em;
            margin-top: 5px;
            width: fit-content;
            border-radius: 10px;
            border: 2px solid black;
        }
        #output * {
            color: white !important;
        }
    </style>
    """), target="output", append=True)