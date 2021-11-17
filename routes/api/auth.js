const express = require('express');
const arouter = express.Router()
const pgp = require('pg-promise')({
    receive(data,result,e){
        console.log(`fetched ${data.length} records`)
    }
});

arouter.post('/',(req,res)=>{
    let db = pgp(`postgres://${req.body.user}:${req.body.password}@localhost:5432/airport_db`).connect()
    .then(obj => {
        res.json({
            'logged_in': req.body.user
        })
        obj.done();
    }).catch(e => {
        res.json({
            'error': e.message || e
        })
    });
})

module.exports = arouter;

