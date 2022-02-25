docker run eurowings-challenge driver local:///opt/app/app.py

#On an average laptop, this took 15 seconds. If you’re going to iterate a lot at this stage
# and want to optimize the speed further; then instead of re-building the image,
# you can simply mount your local files (from your working directory on your laptop)
# to your working directory in the image.
#docker run --mount type=bind,source="$(pwd)",target=/opt/app eurowings-challenge driver local:///opt/app/app.py