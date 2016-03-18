# Dockerfile for running on Binder Project:
# http://mybinder.org/

# for Matplotlib freetype dependecy
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
 && rm -rf /var/lib/apt/lists/*

# install requirements.txt
RUN pip install -r requirements.txt
