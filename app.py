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

@app.route('/add_to_cart_page', methods=['POST'])
def hello():
   p_name = request.form.get('p_name')
   p_quantity = request.form.get('p_quantity')
   total_value = request.form.get('total_value')

   if p_name:
       print('Request for hello page received with name=%s' % p_name)
       return render_template('dd_to_cart_page.html', p_name = p_name, p_quantity=p_quantity,total_value=total_value)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
