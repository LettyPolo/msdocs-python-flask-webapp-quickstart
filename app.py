import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/dd_to_cart_page', methods=['POST'])
def dd_to_cart_page():
   p_name = request.form.get('p_name')
   p_quantity = request.form.get('p_quantity')
   total_value = request.form.get('total_value')
   
   return render_template('dd_to_cart_page.html', p_name = p_name, p_quantity=p_quantity,total_value=total_value)



@app.route('/confirm', methods=['POST'])
def confirm():
   p_name = request.form.get('p_name')
   p_quantity = request.form.get('p_quantity')
   total_value = request.form.get('total_value')
   
   return render_template('confirm.html', p_name = p_name, p_quantity=p_quantity,total_value=total_value)



if __name__ == '__main__':
   app.run()
