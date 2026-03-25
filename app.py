from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Lista para armazenar as capturas em memória (será zerada ao reiniciar o servidor)
capturas = []

@app.route('/')
def index():
    # Mantém o seu simulador de força bruta na página inicial
    return render_template('index.html')

@app.route('/promocao')
def phishing_trap():
    # Esta é a URL que você vai mandar para o público (ex: QR Code ou link encurtado)
    return render_template('alert.html')

@app.route('/captura-detalhes', methods=['POST'])
def captura_detalhes():
    dados = request.get_json()
    
    info = {
        "horario": datetime.datetime.now().strftime("%H:%M:%S"),
        "ip": request.remote_addr,
        "dispositivo_raw": request.headers.get('User-Agent', ''),
        "tipo_alerta": dados.get('tipo_alerta', 'Desconhecido'),
        "dados_tecnicos": dados
    }
    
    # Identificação visual do dispositivo
    ua = info['dispositivo_raw'].lower()
    if 'android' in ua: info['icone'] = "📱 Android"
    elif 'iphone' in ua: info['icone'] = "📱 iPhone"
    elif 'windows' in ua: info['icone'] = "💻 Windows"
    elif 'mac' in ua: info['icone'] = "🍏 macOS"
    else: info['icone'] = "🖥️ Outro"

    capturas.insert(0, info) # Adiciona no topo da lista
    return jsonify({"status": "sucesso"})

@app.route('/painel')
def painel_dpo():
    # Esta página é o seu "Centro de Comando" para mostrar no telão
    return render_template('painel.html', capturas=capturas)

if __name__ == '__main__':
    # debug=True ajuda a ver os erros no terminal enquanto você desenvolve
    app.run(host='0.0.0.0', port=5000, debug=True)