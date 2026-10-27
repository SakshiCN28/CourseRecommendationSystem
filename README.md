# Course Recommendation System

## 1. Introduction

The Course Recommendation System is a web-based application developed using Python and Django. It helps users explore available courses and find courses that match their interests, skill levels, and career goals.

The system provides a simple interface where users can register, log in, search for courses, view course details, and receive personalized course recommendations.

## 2. Objectives

- To help users discover suitable courses.
- To recommend courses based on user interests and career goals.
- To provide information about course levels, duration, skills, and career fields.
- To make course searching easier and more organized.
- To develop a user-friendly web application using Django.

## 3. Features

- User registration and login.
- Home page displaying available courses.
- Course search functionality.
- Course details page.
- Course recommendations based on user preferences.
- Course categories and skill information.
- Django administration panel for managing course data.

## 4. Technologies Used

- **Programming Language:** Python
- **Web Framework:** Django
- **Frontend:** HTML and CSS
- **Database:** SQLite
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

## 5. Project Structure

```text
CourseRecommendationSystem/
├── courserecommendation/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── courses/
│   ├── templates/
│   │   └── courses/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── search.html
│   │       ├── course_detail.html
│   │       └── recommendations.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── .gitignore
└── README.md
```

## 6. Installation and Setup

### Prerequisites

- Python
- Django
- Visual Studio Code

### Steps

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Create and activate a Python virtual environment.
4. Install Django.
5. Apply database migrations.
6. Start the Django development server.

### Example Commands

```bash
python -m venv venv
```

Activate the environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install Django:

```bash
python -m pip install django
```

Apply migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the application in your browser at:

`http://127.0.0.1:8000/`

## 7. How the System Works

1. The user registers or logs in.
2. The user explores the available courses.
3. The user searches for courses or provides preferences.
4. The system uses the available course information and matching logic to generate recommendations.
5. The user views recommended courses and their details.

## 8. Course Information

Each course can include:

- Course name
- Category
- Difficulty level
- Skills covered
- Duration
- Description
- Related career field

## 9. Database

The application uses SQLite as its database through Django's database features and models.

The database stores application data, including course information and user-related records as configured in the project.

## 10. Future Enhancements

- Integrate an external course API.
- Add more courses and categories.
- Improve the recommendation algorithm.
- Add course ratings and reviews.
- Develop a user profile and saved-course feature.
- Improve the interface for mobile devices.

## 11. Conclusion

The Course Recommendation System demonstrates how Python and Django can be used to develop a web application that helps users explore educational opportunities. It combines course information, searching, and recommendation functionality in one application.

The project can be extended with additional courses, improved recommendation methods, and more features to provide a richer learning experience.

## 12. Author

Sakshi CN