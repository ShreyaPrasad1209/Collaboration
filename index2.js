const path=require('path')
const express = require('express')
const app = express()
const port =process.env.PORT||3000
const publicDirectoryPath=path.join(__dirname,'./public')

app.use(express.static(publicDirectoryPath))



app.get('/', (req, res) => {
	console.log(obj1);
	res.json(obj1);
});

app.listen(5000, () => console.log(`server is running`));