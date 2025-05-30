from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return jsonify({"message": "Welcome to TechSite!"})


@main_bp.route('/')
def home():
    return jsonify({"page": "Home", "message": "LNCT Homepage"})

@main_bp.route('/about')
def about():
    return jsonify({"page": "About LNCT", "content": "LNCT "})

@main_bp.route('/academics')
def academics():
    return jsonify({"page": "Academics", "content": "Information."})

@main_bp.route('/news-events')
def news_events():
    return jsonify({"page": "News & Events", "content": "Upcoming events and news."})

@main_bp.route('/alumni')
def alumni_page():
    return jsonify({"page": "Alumni", "content": "LNCT Alumni Success Stories."})

@main_bp.route('/placement')
def placement():
    return jsonify({"page": "Placement", "content": "Placement stats and company tie-ups."})

@main_bp.route('/colleges')
def colleges():
    return jsonify({"page": "Colleges", "content": "LNCT group colleges list."})

@main_bp.route('/contact')
def contact():
    return jsonify({"page": "Contact", "content": "Get in touch with LNCT."})

# --------------------------------

@main_bp.route('/explore-campus')
def explore_campus():
    return redirect("https://lnct.ac.in/explore-campus")

@main_bp.route('/apply-now')
def apply_now():
    return redirect("https://lnct.ac.in/apply")

# -------------------------?
@main_bp.route('/api/admission')
def admission():
    return jsonify({"title": "Admission", "info": "Admission process and requirements."})

@main_bp.route('/api/courses')
def courses():
    return jsonify({"courses": ["B.Tech", "M.Tech", "MBA", "MCA", "Diploma"]})

@main_bp.route('/api/tour')
def campus_tour():
    return jsonify({"title": "Campus Tour", "video_link": "https://youtube.com/lnct-tour"})

@main_bp.route('/api/facilities')
def facilities():
    return jsonify({"facilities": ["Hostel", "Library", "Labs", "Sports", "Cafeteria"]})