from webapp import create_app
from webapp.ai import llm_init


app = create_app()


if __name__ == "__main__":
    # llm_init()
    app.run(debug=True, host='0.0.0.0')
