from flask import *
import youtube_downloading as yt_d
import threading
import os
import time

app = Flask(__name__)
app.secret_key = "supposed to be a secret"

def delete_file(file_path):
    time.sleep(10)

    if os.path.exists(file_path):
        try:
            os.rename(file_path, file_path)
            time.sleep(2)
            os.remove(file_path)
        except:
            time.sleep(5)
            delete_file(file_path)


@app.route("/return-file/")
def return_file():

    num_choice = session.get("choice")
    url = session.get("url")

    yt_d.get_media(url, num_choice)

    if num_choice == 1:
        download_name = "youtube_audio.mp3"
        location = "./tmp/audio/audio_1.mp4"

    if num_choice == 2:
        download_name = "youtube_video.mp4"
        location = "./tmp/videos/video_1.mp4"

    t1 = threading.Thread(target=delete_file, args=("./tmp/videos/video_1.mp4",))
    t1.start()

    return send_file(
        location, attachment_filename=download_name, as_attachment=True
    )


@app.route("/", methods=["GET", "POST"])
def home_page():

    if request.method == "GET":

            return render_template("material-life.html")

    elif request.method == "POST":

        attempted_url = request.form["url"]
        attempted_choice = int(request.form["submit"])
        title = [attempted_url, attempted_choice]
        if attempted_url != "":
            if yt_d.verify(attempted_url):

                session["url"] = attempted_url
                session["choice"] = attempted_choice

                return redirect(url_for("return_file"))
            else:
                flash('URL Not From Youtube')
                return render_template( "material-life.html")
        else:
            flash('URL is Empty')
            return render_template("material-life.html")


if __name__ == "__main__":

    app.run(threaded=True, debug=True)
