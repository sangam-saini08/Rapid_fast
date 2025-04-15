# Rapid_fast

🚀 Rapid Fire Microblogging API This is a lightweight and fast REST API built with FastAPI that provides basic features of a microblogging platform, similar to Twitter. Users can sign up, log in, and post short messages ("tweets"). It uses modern Python standards with type hints, Pydantic for data validation, and SQLModel for database interaction.

🔧 Features

✅ User Signup: Register new users with username, email, and password (securely hashed).

✅ User Login: Authenticate using JWT tokens.

✅ Post Message: Authenticated users can post short text-based updates (e.g., 280 characters).

✅ View Posts: Retrieve public posts in a feed-like format.

🔒 Secure Passwords: Passwords are hashed using passlib with bcrypt.

🔐 Token-based Auth: JWT (JSON Web Tokens) used for secure session management.
