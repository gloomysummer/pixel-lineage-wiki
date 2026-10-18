#!/usr/bin/env python3
import subprocess
import time
import json
import urllib.request
import os

HTML_PATH = os.path.abspath("dist/classes/warrior/index.html")
FILE_URL = f"file://{HTML_PATH}"

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def test_viewport(width, height):
    # Launch chrome with remote debugging
    port = 9223
    cmd = [
        CHROME_BIN,
        "--headless=new",
        f"--remote-debugging-port={port}",
        "--remote-allow-origins=*",
        f"--window-size={width},{height}",
        "--hide-scrollbars",
        "--disable-gpu",
        FILE_URL
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.5)

    try:
        # Get targets
        res = urllib.request.urlopen(f"http://127.0.0.1:{port}/json")
        targets = json.loads(res.read().decode())
        ws_url = targets[0]["webSocketDebuggerUrl"]

        import websocket
        ws = websocket.create_connection(ws_url)

        # Evaluate script
        js_code = """
        (() => {
            const container = document.querySelector('.container-guide');
            const layout = document.querySelector('.article-layout');
            const article = document.querySelector('.article-main');
            const toc = document.querySelector('.sidebar-col-toc');
            const wiki = document.querySelector('.sidebar-col-wiki');
            const mobileToc = document.querySelector('.mobile-toc');

            return {
                viewportWidth: window.innerWidth,
                containerMaxWidth: getComputedStyle(container).maxWidth,
                containerActualWidth: container ? container.getBoundingClientRect().width : null,
                layoutDisplay: getComputedStyle(layout).display,
                layoutGridTemplateColumns: getComputedStyle(layout).gridTemplateColumns,
                articleWidth: article ? article.getBoundingClientRect().width : null,
                tocWidth: toc ? toc.getBoundingClientRect().width : null,
                tocDisplay: toc ? getComputedStyle(toc).display : null,
                wikiWidth: wiki ? wiki.getBoundingClientRect().width : null,
                mobileTocDisplay: mobileToc ? getComputedStyle(mobileToc).display : null
            };
        })()
        """
        eval_req = {
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": js_code,
                "returnByValue": True
            }
        }
        ws.send(json.dumps(eval_req))
        resp = json.loads(ws.recv())
        val = resp.get("result", {}).get("result", {}).get("value", {})
        ws.close()
        return val
    finally:
        proc.terminate()
        proc.wait()

def main():
    print("Testing computed layout across viewports:")
    for w in [1440, 1280, 900]:
        res = test_viewport(w, 900)
        print(f"\n--- Viewport Width: {w}px ---")
        print(json.dumps(res, indent=2))

if __name__ == '__main__':
    main()
