How to generate static blog here
===

### Local

  source venv/bin/activate
  pelican content/
  cd output && python -m SimpleHTTPServer 8080

### Publish

  source venv/bin/activate
  pelican content/ -s publishconf.py -o ../rainy.im/
