# publish on pypi and commit
python3 -m build
python3 -m twine upload dist/*
git add .
git commit -m "$1"
