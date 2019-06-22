from timezonefinderL import TimezoneFinder

tf = TimezoneFinder()

longitude, latitude = 13.358, 52.5061
tf.timezone_at(lng=longitude, lat=latitude)  # returns 'Europe/Berlin'
