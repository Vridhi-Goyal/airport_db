const express = require('express');
const frouter = express.Router()
const pgp = require('pg-promise')({
    receive(data,result,e){
        console.log(`fetched ${data.length} records`)
    }
});

var db = pgp('postgres://postgres:gautham1234@localhost:5432/airport_db');

frouter.post('/',(req,res)=>{
    db.any("SELECT * FROM FLIGHT",123).then((data)=>{
        res.json(data)
    })
})

frouter.post('/:id',(req,res)=>{
    db.any(`SELECT * FROM FLIGHT WHERE flight_id=${req.params.id}`,123).then((data)=>{
        res.json(data)
    })
})

module.exports = frouter;

