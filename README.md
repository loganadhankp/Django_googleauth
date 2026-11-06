# Django Project with Google & GitHub OAuth2 Login

A complete, production-ready Django project implementing Google and GitHub OAuth 2.0 authentication using `django-allauth`.

---

## 🚀 Features

- **Google & GitHub OAuth 2.0 Login / Signup** using `django-allauth`
- **Zero manual database config option**: Configure credentials via `.env` or via Django Admin
- **Modern UI** with clean responsive layout and branded Google & GitHub Sign-in buttons
- **Automatic User Account Creation** on first login
- **Email as primary identifier** with automatic profile synchronization
- **Unit test coverage** verifying authentication flow and endpoints

---

## 📁 Project Structure

```text
Django_OAuth2 Login/
├── requirements.txt
├── .env.example
├── README.md
├── venv/
└── google_auth/
    ├── manage.py
    ├── db.sqlite3
    ├── .env.example
    ├── .env
    ├── google_auth/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    ├── accounts/
    │   ├── views.py
    │   ├── models.py
    │   ├── tests.py
    │   └── apps.py
    └── templates/
        ├── base.html
        └── home.html
```

---

## 🛠️ Quick Setup & Execution

### 1. Activate Virtual Environment
On Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Run Database Migrations
```powershell
python google_auth/manage.py migrate
```

### 3. Add OAuth Credentials
You can provide credentials in **either of two ways**:

#### Method A: Via `.env` (Recommended - Fastest)
Edit `google_auth/.env` and enter your credentials:
```env
SECRET_KEY=django-insecure-change-this-to-a-random-secret-key
DEBUG=True

# Google OAuth
GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-google-client-secret

# GitHub OAuth
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret
```

#### Method B: Via Django Admin
1. Create a superuser:
   ```powershell
   python google_auth/manage.py createsuperuser
   ```
2. Start server and go to `http://127.0.0.1:8000/admin/`
3. Under **Social Accounts** → **Social Applications** → click **Add**
   - **Provider:** `Google` or `GitHub`
   - **Name:** `Google` or `GitHub`
   - **Client id:** *<Your Client ID>*
   - **Secret key:** *<Your Client Secret>*
   - **Sites:** Select `example.com` (or `localhost`) and move it to **Chosen sites**
4. Click **Save**

### 4. Start the Development Server
```powershell
python google_auth/manage.py runserver
```
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

### 5. Run Unit Tests
```powershell
python google_auth/manage.py test accounts
```

---

## 🔑 Obtaining OAuth Credentials

### 🌐 Google Cloud Console Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Open **APIs & Services** → **OAuth consent screen** (External, add email, scopes: email & profile, add yourself as test user).
3. Open **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth client ID** (Web application).
4. Under **Authorized redirect URIs**, add:
   - `http://127.0.0.1:8000/accounts/google/login/callback/`
   - `http://localhost:8000/accounts/google/login/callback/`
5. Copy **Client ID** and **Client Secret**.

### 🐙 GitHub Developer Setup
1. Go to [GitHub Settings ➔ Developer settings ➔ OAuth Apps](https://github.com/settings/developers)
2. Click **New OAuth App** (or **Register a new application**).
3. Fill in:
   - **Application name:** `Django Local`
   - **Homepage URL:** `http://127.0.0.1:8000/`
   - **Authorization callback URL:**
     ```text
     http://127.0.0.1:8000/accounts/github/login/callback/
     ```
4. Click **Register application**.
5. Copy the **Client ID**, then click **Generate a new client secret** and copy the secret.
6. Paste both into `google_auth/.env`.

---

## ⚠️ Common Troubleshooting

- **redirect_uri_mismatch**: Ensure the redirect URI in Google/GitHub Console exactly matches including the trailing slash `/`.
- **SocialApp matching query does not exist**: Ensure either your credentials are in `.env`, or you added the Social Application in Django Admin.
