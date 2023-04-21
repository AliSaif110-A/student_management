Get-ChildItem -Path . -Filter *.sqlite3 -Recurse | Remove-Item -Force
Get-ChildItem -Path . -Filter *.pyc -Recurse | Remove-Item -Force
Get-ChildItem -Path . -Filter */migrations/*.py -Recurse | Where-Object { $_.Name -notlike "__init__.py" } | Remove-Item -Force
python manage.py makemigrations
python manage.py migrate
