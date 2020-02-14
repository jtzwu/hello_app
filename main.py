import flask
import google.cloud.datastore
import os

datastore_client = google.cloud.datastore.Client()
app = flask.Flask(__name__)

@app.route('/')
def index():
  return flask.redirect('/')

@app.route('/hello')
def hello():
  return "Hello World!\n"

@app.route('/view')
def view():
  query = datastore_client.query(kind='test-entity')
  names = ('* {name}\n'.format(name=person['Name']) for person in query.fetch())
  return flask.Response(names, mimetype='text/plain')

@app.route('/add/<user>', methods=['PUT'])
def add(user):
  key = datastore_client.key('test-entity')
  person = google.cloud.datastore.Entity(key=key)
  person['Name'] = user
  datastore_client.put(person)

  return "Hello {name}\n".format(name=user)

if __name__ == '__main__':
  app.run('0.0.0.0', port=os.environ['PORT'])
