# ---------- Stage 1: Build ----------
FROM python:3.12-slim AS builder

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.12-slim

WORKDIR /app

# Copy only installed packages from builder stage (not build tools)
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY app/ .

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "app.py"]