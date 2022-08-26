# iSummary

This repository contains source code for my **Hashnode tutorial series** titled "_[Build a Text Summarizer API using Django Rest Framework and spaCy](https://ifenna.hashnode.dev/text-summary-with-drf-and-spacy)_".

iSummary is an Django Rest Framework application for summarizing text. It takes some NLP concepts such as tokenization, frequency distribution and sentence scoring via spaCy. We use a simple heap (`nlargest`) algorithm to summarize texts.

The inspiration behind this project was to build something different. I was tired of DRF beginner tutorials on building todo app, note app or blog.

PS: Delete **db.sqlite3** if you do not want to use the sample database I created.

## Technologies

1. Python
2. Django Rest Framework
3. JSON WebToken
4. OpenAPI (SwaggerAPI)
5. SpaCy

## How to setup locally

1. Create a new virtual environment for this project. *Virtualenv* and *anaconda* are popular choices. ***Please make sure to create a new environment for this project.***
2. Install dependencies:

3. Install dependencies by running the following command in your terminal:

  ```bash
  pip install -r requirements.txt
  ```

4. Setup database migrations:

   ```bash
   python manage.py migrate

  ```

5. To visit the API endpoints in your browser at port <http://localhost:8000>, start iSummary (Python) server:

   ```bash
   python manage.py runserver
   ```

6. OPTIONAL: Create a super admin account

   ```bash
   python manage.py createsuperuser
   ```

   Visit `/admin/` and login with credentials to have access to the admin dashboard.

That's all! For the API Documentation, visit:

- SwaggerAPI: <http://localhost:8000/>
- ReDoc: <http://localhost:8000/redoc/>

### Example account

Username: admin
Password: asdf
