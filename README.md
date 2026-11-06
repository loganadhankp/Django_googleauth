# Django Project with Google (Gmail) OAuth2 Login

A complete, production-ready Django project implementing Google / Gmail OAuth 2.0 authentication using `django-allauth`.

---

## 🚀 Features

- **Google OAuth 2.0 Login / Signup** using `django-allauth`
- **Zero manual database config option**: Configure credentials via `.env` or via Django Admin
- **Modern UI** with clean responsive layout and Google Sign-in button
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

### 3. Add Google OAuth Credentials
You can provide credentials in **either of two ways**:

#### Method A: Via `.env` (Recommended - Fastest)
Edit `google_auth/.env` and enter your Google OAuth credentials:
```env
SECRET_KEY=django-insecure-change-this-to-a-random-secret-key
DEBUG=True
GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

#### Method B: Via Django Admin
1. Create a superuser:
   ```powershell
   python google_auth/manage.py createsuperuser
   ```
2. Start server and go to `http://127.0.0.1:8000/admin/`
3. Under **Social Accounts** → **Social Applications** → click **Add**
   - **Provider:** `Google`
   - **Name:** `Google`
   - **Client id:** *<Your Google Client ID>*
   - **Secret key:** *<Your Google Client Secret>*
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

## 🔑 Google Cloud Console Setup Instructions

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Navigate to **APIs & Services** → **OAuth consent screen**
   - Choose **External** user type → click **Create**
   - Fill in **App name**, **User support email**, and **Developer contact email**
   - Under **Scopes**, add:
     - `.../auth/userinfo.email`
     - `.../auth/userinfo.profile`
   - Under **Test users**, add your own Gmail address (required while in testing mode)
4. Navigate to **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth client ID**
   - **Application type:** `Web application`
   - **Name:** `Django Local`
   - **Authorized redirect URIs** (add both):
     - `http://127.0.0.1:8000/accounts/google/login/callback/`
     - `http://localhost:8000/accounts/google/login/callback/`
5. Click **Create** and copy your **Client ID** and **Client Secret**.

---

## ⚠️ Common Troubleshooting

- **Error 400: redirect_uri_mismatch**: Ensure the redirect URI in Google Console exactly matches `http://127.0.0.1:8000/accounts/google/login/callback/` including the trailing slash.
- **Access Blocked / App in Testing**: Make sure you added your Gmail address under **Test users** on the OAuth consent screen.
- **SocialApp matching query does not exist**: Ensure either your `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` are defined in `google_auth/.env`, or you created the Social Application entry in Django Admin.
