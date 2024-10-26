# Employee Management System  

This is a simple **Employee Management System** built with **HTML**, **CSS**, **JavaScript**, and **Django**. It allows users to **add, edit, delete, and search employees**. The application also supports running in two modes:  
1. **Normal Mode** (without Docker)  
2. **Docker Compose Mode**

---

## Features  
- **Add/Edit Employees**: Create or update employee details using a modal form.  
- **Delete Employees**: Confirm deletion through a modal before removing records.  
- **Search Employees**: Filter the employee list in real-time based on input.  
- **Django Backend**: Uses Django to handle data and API calls.  
- **PostgreSQL Support**: Database support through Docker.  
- **Docker Support**: Easily containerized setup using Docker Compose.  

---

## Prerequisites  
Make sure the following are installed on your machine:

1. **Python** (version 3.x)  
2. **Django** (if running in normal mode)  
3. **Docker** (if using Docker mode)  
4. **Docker Compose**  

---


## Installation and Usage  

### Option 1: Run Normally (Without Docker)  

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/employee-management.git
   cd employee-management
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/macOS
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations and run the server**:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access the application** at:  
   [http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

### Option 2: Run Using Docker Compose  

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NithinKrishna10/Employee-Management-System.git
   cd employee-management
   ```

2. **Create a `.env` file for PostgreSQL credentials**:
   Create a new `.env` file in the project root with the following content:
   ```env
   POSTGRES_DB=employee_db
   POSTGRES_USER=admin
   POSTGRES_PASSWORD=admin123
   POSTGRES_HOST=db
   POSTGRES_PORT=5432

   DJANGO_SECRET_KEY=your_secret_key_here
   DJANGO_DEBUG=True
   ```

3. **Build and run the Docker containers**:
   ```bash
   docker-compose up --build
   ```

4. **Access the application** at:  
   [http://localhost:8000](http://localhost:8000)  

5. **To stop the containers**, use:
   ```bash
   docker-compose down
   ```

---

## Configuration  

- **Database Settings**:  
  The `docker-compose.yml` file is configured to use **PostgreSQL** as the database. The credentials are loaded from the `.env` file.

- **Docker Setup**:  
  The `Dockerfile` and `docker-compose.yml` run the Django app using **Gunicorn**.

---

## Environment Variables  

Set the following in your `.env` file:

```env
POSTGRES_DB=employee_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
POSTGRES_HOST=db
POSTGRES_PORT=5432

DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=True
```

---

## Useful Commands  

- **Create a superuser** (for Django admin):
  ```bash
  python manage.py createsuperuser
  ```

- **Apply migrations**:
  ```bash
  python manage.py migrate
  ```

- **Collect static files** (for production):
  ```bash
  python manage.py collectstatic
  ```


Enjoy building with the Employee Management System! 🚀
