How to generate static blog here
===

### Local

  source venv/bin/activate
  /*
  pelican content/ -- copying projects
  */
  make html
  cd output && python -m SimpleHTTPServer 8080

### Publish

  source venv/bin/activate
  make pub
  /*
  pelican content/ -s publishconf.py -o ../rainy.im/
  */
