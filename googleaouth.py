from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'

app = Flask(__name__)
app.secret_key = "supersekrit"
blueprint = make_google_blueprint(
    client_id="337665130734-8intpse94j1qtbs2e3192krfvovdqvuf.apps.googleusercontent.com",
    client_secret="Gpmyo5mKS6vsM-K1WHz0evMH",
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/plus/v1/people/me")
    assert resp.ok, resp.text
    return "You are {email} on Google".format(email=resp.json()["emails"][0]["value"])

if __name__ == "__main__":
    app.run()