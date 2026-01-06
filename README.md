### Screenshots
<img width="1148" height="488" alt="Django_app" src="https://github.com/user-attachments/assets/e261ff59-ed11-403f-b872-5d226b3b14bc" />
<img width="1768" height="763" alt="streamlit_screenshot" src="https://github.com/user-attachments/assets/fea96835-07e2-427f-8479-162677ac541d" />

## How to run

### Streamlit
```bash
python -m streamlit run streamlit_app/app.py

cd django_app
python manage.py runserver 

Titanic Database (SQLite)
Load dataset into DB
python data_prep/load_titanic_to_db.py

Explore data from DB
python data_prep/explore_titanic.py


(Keep the markdown formatting exactly like that.)

---

## 6) Commit + push to GitHub

```powershell
pip freeze > requirements.txt
git add .
git commit -m "Day 2: Django + Streamlit + Titanic DB load and exploration"
git push
