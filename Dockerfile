# Nomad — voice + vision + RAG road-trip companion
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# PyAudio needs the PortAudio headers; build-essential covers any source builds.
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Fail the build early if the package cannot be imported.
RUN python -c "import nomad.config"

# Default entrypoint is the full voice companion (needs a microphone /
# Raspberry Pi camera server at runtime). For the offline single-image
# pipeline instead run:
#   docker run --rm nomad python -m nomad.pipeline data/samples/test1.jpg
CMD ["python", "-m", "nomad.companion"]
