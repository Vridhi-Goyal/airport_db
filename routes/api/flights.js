const express = require('express');
const frouter = express.Router()
const pgp = require('pg-promise')({
    receive(data,result,e){
        console.log(`fetched ${data.length} records`)
    }
});

frouter.get('/',(req,res)=>{
    let db = pgp(`postgres://${req.cookies.user}:${req.cookies.password}@localhost:5432/airport_db`);
    db.any("SELECT * FROM FLIGHT",123).then((data)=>{
        res.json(data)
    })
})

frouter.get('/:id',(req,res)=>{
    let db = pgp(`postgres://${req.cookies.user}:${req.cookies.password}@localhost:5432/airport_db`);
    db.any(`SELECT * FROM FLIGHT WHERE flight_id=${req.params.id}`,123).then((data)=>{
        res.json(data)
    })
})

module.exports = frouter;

