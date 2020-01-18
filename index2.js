const path = require('path');
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const csv = require('csvtojson');
const file = "./output.csv"
const publicDirectoryPath = path.join(__dirname, './public');
app.use(express.static(publicDirectoryPath));

app.use('/', (req, res) => {
    res.sendFile(__dirname, '/public/feed.html');
});

app.get('/clicked', (req, res) => {
	csv()
		.fromFile(file)
		.then(data => { 
			res.send(data)
		})
});

app.listen(5000, () => console.log(`server is running`));
