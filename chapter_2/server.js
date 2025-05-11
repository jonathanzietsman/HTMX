import express from 'express';

const app = express();

// Serve static files (like HTML, CSS, images) from the 'public' directory
app.use(express.static('public'));

// Parse URL-encoded bodies (form data submitted from HTML forms)
app.use(express.urlencoded({extended: true}));

// Parse JSON payloads (for handling JSON data in requests)
app.use(express.json());

// Handle GET request to fetch users 
app.get('/users', async (req, res) => {
    setTimeout(async ()=>{
        const limit = +req.query.limit || 10;
    
        const reponse = await fetch(`https://jsonplaceholder.typicode.com/users?_limit=${limit}`);
        const users = await reponse.json();
    
        res.send(`
            <h2>Users</h2>
            <ul class = "list-group">
                ${users.map((user)=>`<li class="list-group-item">${user.name}</li>`).join('')}
            </ul>
        `)
    },2000)
});

app.post('/calculate', (req, res) => {
    const height = +req.body.height;
    const weight = +req.body.weight;
    const bmi = weight / (height * height);
    res.send(`
        <p>Height of ${height} & Weight of ${weight} gives you BMI of ${bmi.toFixed(2)}</p>
        `);
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
