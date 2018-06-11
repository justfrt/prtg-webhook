# Build from debian
FROM debian

# Set proxy
ENV http_proxy="http://wsa.network.newyorker.de:3128"
ENV https_proxy="http://wsa.network.newyorker.de:3128"

# Install required packages
RUN apt-get update && apt-get install -y \
    git \
    python-dev \
    build-essential \ 
    curl

# Install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py

# Add workdirektory
RUN mkdir /http_hum
WORKDIR /http_hum

# Download and install the Adafruit DHT library
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT && python setup.py install

# Install the requests library
RUN pip install requests

# Add the sensorreading script and make it executable
ADD ./hum_reading.py /http_hum
RUN chmod +x /http_hum/hum_reading.py

# Run the sensorreading script in the container
CMD ["python", "/http_hum/hum_reading.py"]
