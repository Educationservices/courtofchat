from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def main_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>Discord Court Launcher</title>
      <style>
        body { font-family: sans-serif; margin: 0; padding: 0; }
        #openBtn {
          display: block;
          margin: 100px auto;
          padding: 1em 2em;
          font-size: 1.2em;
          cursor: pointer;
        }
        #fullIframe {
          position: fixed;
          top: 0; left: 0;
          width: 100vw;
          height: 100vh;
          border: none;
          display: none;
          z-index: 9999;
        }
      </style>
    </head>
    <body>
      <button id="openBtn">Click to open Discord Court</button>
      <iframe id="fullIframe" src="/discord-court"></iframe>

      <script>
        const btn = document.getElementById('openBtn');
        const iframe = document.getElementById('fullIframe');

        btn.addEventListener('click', () => {
          iframe.style.display = 'block';
          // Tell the iframe to play audio
          iframe.contentWindow.postMessage('playAudio', '*');
        });

        // Optional: also send playAudio once iframe is loaded
        iframe.addEventListener('load', () => {
          iframe.contentWindow.postMessage('playAudio', '*');
        });
      </script>
    </body>
    </html>
    """

@app.route('/discord-court')
def discord_court():
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
