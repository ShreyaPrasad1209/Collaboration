const path = require('path');
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const csv = require('csvtojson');
const file = "./output3.csv"
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

const file2 = "./Project1.csv"
app.use('/', (req, res) => {
    res.sendFile(__dirname, '/public/pid1.html');
});

app.get('/user2', (req, res) => {
	csv()
		.fromFile(file2)
		.then(data => {
			console.log(data[0]) 
			res.send(data[0])
		})
});

const file3 = "./output5.csv"
app.use('/', (req, res) => {
    res.sendFile(__dirname, '/public/feed2.html');
});

app.get('/user3', (req, res) => {
	csv()
		.fromFile(file3)
		.then(data => {
			console.log(data[0]) 
			res.send(data[0])
		})
});

const file4 = "./output8.csv"
app.use('/', (req, res) => {
    res.sendFile(__dirname, '/public/feed3.html');
});

app.get('/user4', (req, res) => {
	csv()
		.fromFile(file4)
		.then(data => {
			console.log(data[0]) 
			res.send(data[0])
		})
});

app.listen(5000, () => console.log(`server is running`));
