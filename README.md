# 🛡️ Palestra LGPD & Segurança Digital — Riofer Industrial

Aplicação educativa para palestras sobre LGPD, privacidade e segurança digital.

## 📁 Estrutura do Projeto

```
riofer-lgpd/
├── app.py                    # Servidor Flask
├── static/
│   ├── style.css             # Tema visual padronizado Riofer
│   ├── logo.png              # ← COLOQUE O LOGO DA RIOFER AQUI
│   └── favicon.png           # ← COLOQUE O FAVICON AQUI
└── templates/
    ├── index.html             # Hub principal com fingerprint ao vivo
    ├── forca_bruta.html       # Simulador de força bruta (3 níveis)
    ├── alert.html             # Página-isca de phishing (coleta 25+ dados)
    ├── quiz.html              # Quiz interativo (10 perguntas LGPD)
    └── painel.html            # Painel DPO (tempo real no telão)
```

## 🚀 Como Rodar

```bash
pip install flask
python app.py
```

Acesse: `http://localhost:5000`

## 🎯 Roteiro da Palestra

| Ordem | Atividade | URL | Duração |
|-------|-----------|-----|---------|
| 1 | Abrir o Hub e mostrar fingerprint ao vivo | `/` | 5 min |
| 2 | Compartilhar QR Code de `/promocao` | `/promocao` | 5 min |
| 3 | Mostrar o Painel DPO no telão | `/painel` | 5 min |
| 4 | Simulador de Força Bruta | `/forca-bruta` | 10 min |
| 5 | Quiz de Engenharia Social & LGPD | `/quiz` | 10 min |

## 📋 Dados Coletados pela Página-Isca

### Sem permissão (automático):
- Resolução, pixel ratio, profundidade de cor
- Tamanho da tela vs janela
- Orientação da tela
- Núcleos de CPU, RAM estimada
- Max touch points (identifica celular vs desktop)
- Plataforma, idiomas, fuso horário
- Tema escuro, cookies, Do Not Track
- Tipo e velocidade de conexão, RTT
- Nível de bateria e se está carregando
- GPU vendor + renderer (via WebGL)
- Canvas fingerprint hash
- Audio sample rate e canais
- Estimativa de armazenamento
- Quantidade de plugins instalados

### Com permissão (clique no botão):
- Conteúdo da área de transferência (clipboard)
- Geolocalização GPS (latitude/longitude/precisão)
- Permissão de notificação push

## 🎨 Personalização

1. Coloque `logo.png` e `favicon.png` na pasta `/static/`
2. As cores do tema estão em variáveis CSS no `style.css` (prefixo `--rf-`)
