# UTTJob - Find Job API

A comprehensive job search API system built with Django REST Framework, providing full-featured functionality for modern recruitment applications.

## 🚀 Key Features

- **Authentication & Authorization**: Login/Registration system with OAuth2 and Social Authentication
- **Job Management**: Post, search, and apply for job opportunities
- **Profile Management**: CV/Resume management for candidates
- **Company Management**: Company information and recruiter profiles
- **Chatbot**: Automated consultation support
- **Notifications**: Firebase push notifications
- **File Upload**: Cloudinary integration for media storage
- **Background Tasks**: Celery with Redis
- **API Documentation**: Swagger/OpenAPI

## 🛠 Tech Stack

- **Backend**: Django 5.1.7, Django REST Framework
- **Database**: PostgreSQL
- **Cache & Message Broker**: Redis
- **Task Queue**: Celery
- **Authentication**: OAuth2, Social Auth (Google, Facebook)
- **File Storage**: Cloudinary
- **Push Notifications**: Firebase
- **API Documentation**: drf-yasg (Swagger)
- **Containerization**: Docker, Docker Compose

## 📋 System Requirements

- Python 3.8+
- Docker & Docker Compose
- PostgreSQL 15
- Redis

## 🚀 Installation & Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd findjob_api
```

### 2. Environment Configuration

Create environment file from template:

```bash
cp .env.example .env
```

Update environment variables in `.env` file:

```env
# Django
DEBUG=True
SECRET_KEY=your-secret-key
APP_ENV=development

# Database
DB_NAME=myjob_db
DB_USER=postgres
DB_PASSWORD=1
DB_HOST=localhost
DB_PORT=5432

# Redis
REDIS_URL=redis://localhost:6379

# Cloudinary
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Firebase
FIREBASE_CREDENTIALS_PATH=firebase_cred.json

# OAuth2
GOOGLE_OAUTH2_KEY=your-google-key
GOOGLE_OAUTH2_SECRET=your-google-secret
FACEBOOK_KEY=your-facebook-key
FACEBOOK_SECRET=your-facebook-secret
```

### 3. Run with Docker (Recommended)

```bash
# Build and run all services
docker-compose up --build

# Run migrations
docker-compose exec backend python manage.py migrate

# Create superuser
docker-compose exec backend python manage.py createsuperuser

# Collect static files
docker-compose exec backend python manage.py collectstatic
```

### 4. Local Development Setup

```bash
# Create virtual environment
python -m venv myvenv
source myvenv/bin/activate  # Linux/Mac
# or
myvenv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run Celery worker (separate terminal)
celery -A findjob_api.celery worker --loglevel=info

# Run Celery beat (separate terminal)
celery -A findjob_api.celery beat --loglevel=info
```

## 📚 API Documentation

After running the server, access:

- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/
- **Django Admin**: http://localhost:8000/admin/

## 🏗 Project Structure

```
findjob_api/
├── authentication/          # User authentication and management
├── job/                    # Job management
├── info/                   # Company information and resumes
├── chatbot/                # Chatbot support
├── common/                 # Shared models and utilities
├── configs/                # System configurations
├── helpers/                # Helper functions
├── middleware/             # Custom middleware
├── findjob_api/           # Django project settings
├── data/                  # Database data
├── media/                 # Uploaded files
├── tests/                 # Test files
├── docker-compose.yml     # Docker configuration
├── Dockerfile            # Docker image
├── requirements.txt      # Python dependencies
└── manage.py            # Django management
```

## 🔧 Useful Commands

```bash
# Run tests
python manage.py test

# Create migrations
python manage.py makemigrations

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell

# Check configuration
python manage.py check
```

## 🐳 Docker Commands

```bash
# Rebuild images
docker-compose build

# Run specific service
docker-compose up backend

# View logs
docker-compose logs -f backend

# Execute into container
docker-compose exec backend bash

# Stop all services
docker-compose down

# Remove volumes
docker-compose down -v
```

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test authentication

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

## 📝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👥 Team

- **Company**: UTTJob
- **Environment**: Development

## 🔗 Useful Links

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Celery Documentation](https://docs.celeryproject.org/)
- [Docker Documentation](https://docs.docker.com/)

## 📞 Support

For support, email support@uttjob.com or create an issue in this repository.

## 🚀 Deployment

### Production Deployment

1. Set `DEBUG=False` in production environment
2. Configure proper database settings
3. Set up SSL certificates
4. Configure static file serving
5. Set up monitoring and logging

### Environment Variables for Production

```env
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://user:password@host:port/dbname
REDIS_URL=redis://redis-host:6379
```

## 🔒 Security

- Always use HTTPS in production
- Keep dependencies updated
- Use strong passwords and API keys
- Regularly backup your database
- Monitor for security vulnerabilities
