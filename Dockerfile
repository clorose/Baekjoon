FROM python:3.13-alpine

# Install essential packages
RUN apk add --no-cache build-base curl git tzdata nano bash zsh \
  && sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended \
  && git clone https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k \
  && git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions \
  && git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Set working directory and create directories
WORKDIR /app
RUN mkdir -p /app/data /app/src /app/runs

# Set up Python virtual environment in a safe, non-mounted path
RUN python -m venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python dependencies
COPY requirements.txt /app/
RUN $VIRTUAL_ENV/bin/pip install --upgrade pip \
  && $VIRTUAL_ENV/bin/pip install -r /app/requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=/app \
  TZ=Asia/Seoul

# Set timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Set zsh as default shell
SHELL ["/bin/zsh", "-c"]

# Default command
CMD ["zsh"]
