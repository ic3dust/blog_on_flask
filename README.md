# Hello, to be able to interact with the blog so far, do the following:

> ## I am still learning so I am absolutely insecure about how to correctly setup venv and maintain it in some points, so I decided to make a script, that sets up everything I need: it creates a new venv every time I come to code, loads necessarry libraries and runs the server, after a quick check on everything set up.

### 1. <p style="color:green">Open a terminal inside the folder you unpack this app.</p>

### 2. Execute: <p style="color:green">chmod +x setup.sh</p>

### 3. Execute: <p style="color:green">/.setup.sh</p>

# Database commands:

### 1. flask db init

### 2. flask db migrate -m "migrate message"

### 3. flask dp upgrade (to apply the chabges)

> When working with database servers such as MySQL and PostgreSQL, you have to create the database in the database server before running 'flask dp upgrade'.
