from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sum_result = None #修改变量名更清晰
    error = None #添加错误信息变量

    if request.method == 'POST':
        try:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            sum_result = num1 + num2
        except ValueError:
            error = "Please enter valid numbers." #输入非数字的错误提示
        except KeyError:
            error = "Please fill in both number fields."#处理字段缺失错误

    return render_template('index.html', sum=sum_result, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

    #Come on, you can do it!