from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Define the header gradient colors
header_gradient_colors = "#0A0A0A, #8B008B, #00CED1"

# Dummy data for rooms
rooms = [
    {"id": 1, "name": "Tech Innovations", "description": "Discuss the latest in technology.", "participants": 3, "image": "tech.jpg"},
    {"id": 2, "name": "Creative Corner", "description": "Share and discuss creative projects.", "participants": 5, "image": "creative.jpg"},
    {"id": 3, "name": "Wellness and Mindfulness", "description": "Talk about wellness and healthy living.", "participants": 2, "image": "wellness.jpg"}
]


@app.route('/')
def home():
    return render_template('index.html', rooms=rooms, header_gradient_colors=header_gradient_colors)


@app.route('/room/<int:room_id>')
def room(room_id):
    # Find the room by ID
    room = next((room for room in rooms if room["id"] == room_id), None)
    if room is not None:
        # Render the room.html template passing the room as a variable
        return render_template('room.html', room=room)
    else:
        # If the room doesn't exist, redirect back to the home page
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)