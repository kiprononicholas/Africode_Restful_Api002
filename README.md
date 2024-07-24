# Flask RESTful API with SQLAlchemy

This is a simple Flask RESTful API that uses SQLAlchemy to interact with a SQLite database. The API provides endpoints for managing users and their posts.

## Features

- Create, read, update, and delete (CRUD) operations for users and posts.
- Users can have multiple posts.
- Each post has a title, content, creation date, and author.

## Getting Started

To clone and use this application, follow these steps:

1. Install Python 3.x and pip.
2. Clone the repository:

```bash
git clone https://github.com/your-username/flask-restful-api-with-sqlalchemy.git
cd flask-restful-api-with-sqlalchemy
```

3. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Install the required dependencies:

```bash
pip install flask flask-sqlalchemy flask-restful
```

5. Run the application:

```bash
python app.py
```

The application will start running on `http://127.0.0.1:5000/`. You can access the API endpoints using a web browser or tools like curl or Postman.

## API Endpoints

### Users

- `GET /users/`: Get a list of all users.
- `POST /users/`: Create a new user.
- `GET /users/<id>`: Get a user by ID.
- `PATCH /users/<id>`: Update a user by ID.
- `DELETE /users/<id>`: Delete a user by ID.

### Posts

- `GET /posts/`: Get a list of all posts.
- `POST /posts/`: Create a new post.
- `GET /posts/<id>`: Get a post by ID.
- `PATCH /posts/<id>`: Update a post by ID.

## Contributing

To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your changes:

```bash
git checkout -b your-feature-branch
```

3. Make your changes and commit them:

```bash
git add .
git commit -m "Add your feature"
```

4. Push your changes to your fork:

```bash
git push origin your-feature-branch
```

5. Create a pull request on the original repository.

