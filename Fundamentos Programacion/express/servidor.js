const express = require('express')
const app = express()
 
app.get('/', Inicio)
app.get('/cursos', Cursos)
 
function Inicio(req, res) {
    res.send('Este es el <strong>home</strong>')
  }

  function Cursos(req, res) {
    res.send('Estos son los <strong>cursos</strong>')

  }

app.listen(8989)