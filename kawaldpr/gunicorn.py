import multiprocessing

bind = "0.0.0.0:10101"  # Change the port here
workers = 3  # Gunicorn recommend 2n + 1 where n is the number of cores
app_name = "kawaldpr"
