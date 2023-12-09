#modules
from flask import Flask , render_template, abort
#app
app = Flask(__name__)



# project DATA

projects = [
    {
        "name" : "Habit tracking app with Python and MongoDB",
        "thumb" : "img/TrackHabit.png",
        "hero" : "img/habit-tracking-hero.png",
        "categories" : ["Python", "Web"],
        "slug" : "habit-tracking",
        "prod" : "#"
    },
    {
        "name" : "Tkinter APP's & Games",
        "thumb" : "img/tkinter.png",
        "hero" : "img/tkinter.png",
        "categories" : ["Python", "Tkinter", "GUI"],
        "slug" : "tkinter-apps",
        "prod" : "#"
    },
    {
        "name" : "Request, WebScraping and API",
        "thumb" : "img/other_proj.png",
        "hero" : "img/other_proj.png",
        "categories" : ["Python", "Request", "BeautifulSoup4"],
        "slug" : "py-api-scrape",
        "prod" : "#"
    }
]

slug_to_project = {project["slug"]: project for project in projects}


# Route 0 [HOME]
@app.route("/")
def home():
    return render_template("index.html", title = "SaniBoy" , projects = projects)

@app.route("/about")
def about():
    return render_template("about.html", title = "SaniBoy")

@app.route("/contact")
def contact():
    return render_template("contact.html", title = "SaniBoy")



@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html", 
        project=slug_to_project[slug]
        )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

# update folder automaticaly 
if __name__ == "__main__":
    app.run(debug=True)

