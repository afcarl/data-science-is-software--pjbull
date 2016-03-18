# Dockerfile for running on Binder Project:
# http://mybinder.org/

# for Matplotlib
RUN apt-get update -y libfreetype6-dev

# install requirements.txt
RUN pip install -r requirements.txt
