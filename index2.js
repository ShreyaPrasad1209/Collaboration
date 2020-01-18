const path = require('path');
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const csv = require('csvtojson');
const file = "./output1.csv"
const publicDirectoryPath = path.join(__dirname, './public');
app.use(express.static(publicDirectoryPath));

app.use('/', (req, res) => {
    res.sendFile(__dirname, '/public/feed.html');
});

app.get('/user1', (req, res) => {
	csv()
		.fromFile(file)
		.then(data => {
			console.log(data[0]) 
			res.send(data[0])
		})
});

app.listen(5000, () => console.log(`server is running`));
