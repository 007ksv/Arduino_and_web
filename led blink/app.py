from flask import Flask, render_template ,request
import serial

ar=serial.Serial('/dev/ttyACMO',9600)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'keshavsain'

@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method=='POST':
                result = request.form.get('state')
                if result == 'on':
                        print(result)
                        ar.write('1')
                        return render_template('index.html', msg=result)
                elif result == 'off':
                        print(result)
                        ar.write('0')
                        return render_template('index.html', msg=result)
        return render_template('index.html')
        

if __name__ =='__main__':
        app.run('0.0.0.0', debug=True)
