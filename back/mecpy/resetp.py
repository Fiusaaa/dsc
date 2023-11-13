from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('reset_password.html')

@app.route('/reset_password', methods=['POST'])
def reset_password():
    # Lógica para enviar e-mail de redefinição de senha
    email = request.form.get('email')
    
    # Aqui você deve implementar a lógica para enviar o e-mail de redefinição de senha
    
    # Após o envio do e-mail, você pode redirecionar o usuário para uma página de confirmação
    return render_template('reset_password_confirmation.html', email=email)

if __name__ == '__main__':
    app.run(debug=True)