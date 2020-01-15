const express=require('express');
const app=express();
const bodyparser=require('body-parser');

app.get('/',(res,req)=>{
    res.send('Hello World');
} );


const PORT=5000;

app.listen(PORT, ()=>
    console.log(`Server is running on port ${PORT}!`)
)

