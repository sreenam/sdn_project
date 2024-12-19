# Use an official Python image
FROM python:3.9-slim

# Install dependencies for Mininet and OpenFlow
RUN apt-get update && apt-get install -y \
    mininet \
    openvswitch-switch \
    net-tools \
    python3 \
    python3-pip \
    && apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy your Python scripts into the container
COPY simple_sdn_controller.py simple_network.py /app/

# Install required libraries (update this based on your needs)
RUN pip install --no-cache-dir ryu eventlet==0.30.2

# Expose OpenFlow default port (if needed)
EXPOSE 6633

# Default command to run the SDN controller
CMD ["python", "simple_sdn_controller.py"]

# Keep the container running
CMD ["tail", "-f", "/dev/null"]


