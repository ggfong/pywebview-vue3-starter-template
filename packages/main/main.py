import os
import webview


def main():
    is_dev = os.getenv('APP_ENV') == 'development'

    if is_dev:
        html_path = "http://localhost:5173"
    else:
        base_path = os.path.abspath(os.path.dirname(__file__))
        html_path = os.path.join(base_path, "renderer_dist", "index.html")

    webview.create_window("Window", html_path, width=1060, height=800)
    webview.start(ssl=True,debug=is_dev)

if __name__ == "__main__":
    main()
