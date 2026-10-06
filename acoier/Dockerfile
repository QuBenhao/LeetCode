# Use an Ubuntu LTS release
FROM ubuntu:22.04

# Disable interactive apt-get prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update packages and install basic tools
RUN apt-get update && apt-get install -y \
    # Basic tools
    sudo \
    curl \
    wget \
    git \
    vim \
    nano \
    htop \
    procps \
    net-tools \
    iputils-ping \
    # SSH server
    openssh-server \
    # C++ development toolchain
    build-essential \
    gcc \
    g++ \
    gdb \
    clang \
    clangd \
    clang-format \
    clang-tidy \
    # Build tools
    cmake \
    ninja-build \
    make \
    # Python 3 (for some algorithm problems)
    python3 \
    python3-pip \
    # Other useful tools
    valgrind \
    cppcheck \
    bear \
    # File transfer
    rsync \
    && rm -rf /var/lib/apt/lists/*

# Configure SSH
RUN mkdir /var/run/sshd && \
    echo 'root:root' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Create a non-root user (optional but recommended)
RUN useradd -m -s /bin/bash benhao && \
    echo 'benhao:benhao' | chpasswd && \
    usermod -aG sudo benhao

# Set the working directory
WORKDIR /workspace

# Install common Python packages for algorithm practice
RUN pip3 install --no-cache-dir \
    numpy \
    matplotlib \
    pandas \
    scipy \
    ipython

# Configure environment variables for CLion
ENV CC=/usr/bin/gcc
ENV CXX=/usr/bin/g++
ENV PATH="/usr/local/bin:${PATH}"

# Create the project directory
RUN mkdir -p /workspace/.config && \
    chmod -R 777 /workspace

# Expose the SSH port
EXPOSE 22

# Start the SSH service
CMD ["/usr/sbin/sshd", "-D"]
