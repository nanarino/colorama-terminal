pip wheel --wheel-dir=./dist ./
twine upload dist/*  # username: __token__; password: .pypirc