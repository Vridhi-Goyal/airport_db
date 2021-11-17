const express=require('express');
const bodyParser=require('body-parser');
const frouter=require('./routes/api/flights.js');
const arouter=require('./routes/api/auth.js')
var app=express()
app.use(bodyParser.json())

app.use('/api/flights',frouter)
app.use('/api/auth',arouter);

const port = process.env.PORT || 5000;
app.listen(port, () => console.log(`Server started on port ${port}`));