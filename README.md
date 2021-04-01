# Sample Django project

## Installation steps

1. Install Python
2. Install libraries
   
   ```bash
   # Linux, macOS, BASH
   python3 -m venv venv
   source ./venv/bin/activate
   pip install -r requirements.txt

   # Windows
   python -m venv venv
   venv\\source\\activate
   pip install -r requirements.txt
   ```

3. Rename *dotenv* to *.env*
4. Migrate the database

   ```bash
   python manage.py migrate
   ```

5. Start the project

   ```bash
   python manage.py runserver
   ```
