import argparse

from src.hamster_app_py import app

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Hamster-App")
    parser.add_argument("--vite-dev", default="", dest="viteport")
    parser.add_argument("--devtool", action=argparse.BooleanOptionalAction, default=False, dest="devtool")

    args = parser.parse_args()
    app.main(None, args.viteport, args.devtool)
