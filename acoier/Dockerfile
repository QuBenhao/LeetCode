# 使用Ubuntu LTS版本
FROM ubuntu:22.04

# 避免apt-get交互式提示
ENV DEBIAN_FRONTEND=noninteractive

# 更新并安装基础工具
RUN apt-get update && apt-get install -y \
    # 基础工具
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
    # SSH服务器
    openssh-server \
    # C++开发工具链
    build-essential \
    gcc \
    g++ \
    gdb \
    clang \
    clangd \
    clang-format \
    clang-tidy \
    # 构建工具
    cmake \
    ninja-build \
    make \
    # Python3（用于某些算法题）
    python3 \
    python3-pip \
    # 其他有用的工具
    valgrind \
    cppcheck \
    bear \
    # 文件传输
    rsync \
    && rm -rf /var/lib/apt/lists/*

# 配置SSH
RUN mkdir /var/run/sshd && \
    echo 'root:root' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# 创建一个非root用户（可选，但推荐）
RUN useradd -m -s /bin/bash benhao && \
    echo 'benhao:benhao' | chpasswd && \
    usermod -aG sudo benhao

# 设置工作目录
WORKDIR /workspace

# 安装常用Python包用于算法训练
RUN pip3 install --no-cache-dir \
    numpy \
    matplotlib \
    pandas \
    scipy \
    ipython

# 为CLion配置环境变量
ENV CC=/usr/bin/gcc
ENV CXX=/usr/bin/g++
ENV PATH="/usr/local/bin:${PATH}"

# 创建项目目录
RUN mkdir -p /workspace/.config && \
    chmod -R 777 /workspace

# 暴露SSH端口
EXPOSE 22

# 启动SSH服务
CMD ["/usr/sbin/sshd", "-D"]