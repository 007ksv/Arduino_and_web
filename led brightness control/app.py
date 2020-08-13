from flask import Flask, render_template, request
import serial                   #importing python serial module for serial communocation between arduino and python

arduino = serial.Serial('COM1', 9600)


app=Flask(__name__)
app.secret_key = 'keshav'

@app.route('/', methods=['GET','POST'])
def index():
        if request.method=='POST':
                bright = request.form.get('bright')             #fetching the value of brightness using http requests
                arduino.write(str(bright))
                return render_template('index.html', msg=bright)
        return render_template('index.html')

if __name__ == '__main__':
        app.run('0.0.0.0', debug=True)
