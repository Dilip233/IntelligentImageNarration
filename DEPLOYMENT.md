# Production Deployment Guide

This guide provides recommendations for deploying the Intelligent Image Narration System in a production environment.

## Important Security Notes

⚠️ **DO NOT run the Flask development server in production!**

The Flask development server (`app.run(debug=True)`) should only be used for development and testing. For production deployments, use a proper WSGI server.

## Recommended Production Setup

### Option 1: Gunicorn (Recommended for Linux/Unix)

1. **Install Gunicorn:**
   ```bash
   pip install gunicorn
   ```

2. **Run the application:**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 src.app:app
   ```

   Configuration options:
   - `-w 4`: Use 4 worker processes (adjust based on CPU cores)
   - `-b 0.0.0.0:5000`: Bind to all interfaces on port 5000
   - `--timeout 300`: Set timeout for long-running requests (AI processing)

3. **Recommended production command:**
   ```bash
   gunicorn -w 4 -b 127.0.0.1:5000 --timeout 300 --access-logfile - --error-logfile - src.app:app
   ```

### Option 2: uWSGI

1. **Install uWSGI:**
   ```bash
   pip install uwsgi
   ```

2. **Run the application:**
   ```bash
   uwsgi --http :5000 --wsgi-file src/app.py --callable app --processes 4 --threads 2
   ```

### Option 3: Waitress (Cross-platform, including Windows)

1. **Install Waitress:**
   ```bash
   pip install waitress
   ```

2. **Run the application:**
   ```bash
   waitress-serve --host=0.0.0.0 --port=5000 src.app:app
   ```

## Reverse Proxy Setup (Nginx)

For production, it's recommended to use Nginx as a reverse proxy:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # For large file uploads
        client_max_body_size 16M;
        
        # Timeout for AI processing
        proxy_read_timeout 300s;
        proxy_connect_timeout 300s;
    }

    location /static {
        alias /path/to/IntelligentImageNarration/static;
        expires 30d;
    }
}
```

## Environment Configuration

Create a `.env` file for production settings:

```bash
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key-here-change-this
MAX_CONTENT_LENGTH=16777216
```

## Systemd Service (Linux)

Create a systemd service file `/etc/systemd/system/image-narrator.service`:

```ini
[Unit]
Description=Intelligent Image Narration System
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/IntelligentImageNarration
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 --timeout 300 src.app:app

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```bash
sudo systemctl enable image-narrator
sudo systemctl start image-narrator
```

## Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--timeout", "300", "src.app:app"]
```

Build and run:
```bash
docker build -t image-narrator .
docker run -p 5000:5000 image-narrator
```

## Security Checklist

- [ ] Disable Flask debug mode (`FLASK_DEBUG=False`)
- [ ] Use a proper WSGI server (Gunicorn, uWSGI, Waitress)
- [ ] Set up HTTPS with SSL/TLS certificates
- [ ] Use environment variables for sensitive configuration
- [ ] Set up proper file permissions
- [ ] Enable firewall rules
- [ ] Use a reverse proxy (Nginx/Apache)
- [ ] Implement rate limiting
- [ ] Set up monitoring and logging
- [ ] Keep dependencies up to date
- [ ] Restrict file upload types and sizes
- [ ] Validate all user inputs

## Performance Optimization

1. **Model Loading**: The AI model is loaded once and shared across workers (with thread-safe singleton pattern)

2. **Caching**: Consider implementing caching for frequently accessed captions

3. **CDN**: Use a CDN for static files in high-traffic scenarios

4. **Database**: If storing narrations, use a proper database (PostgreSQL, MySQL)

5. **Background Jobs**: For high-load scenarios, consider using Celery for async processing

## Monitoring

Recommended monitoring tools:
- **Application**: Sentry for error tracking
- **Performance**: New Relic or Datadog
- **Logs**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Uptime**: UptimeRobot or Pingdom

## Scaling

For high-traffic scenarios:
- Use multiple worker processes
- Deploy across multiple servers with load balancing
- Consider using Redis for session management
- Implement job queues for image processing (Celery + Redis)

## Backup and Recovery

- Regularly backup uploaded images (if stored)
- Backup configuration files
- Test restore procedures
- Document recovery steps

## Support

For production deployment assistance, please open an issue on GitHub.
