import express from 'express';

const app = express();

// Set static folder
app.use(express.static('public'));

// Parse URL-encoded bodies (as sent by HTML forms)
app.use(express.urlencoded({extended: true}));

// Parse JSON bodies (as sent by API clients)
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

// Handle GET request for profile edit
app.get('/user/:id/edit', (req, res) => {
    
    // send an HTML form for editing
    res.send(`
        <form hx-put="/user/1" hx-target="this" hx-swap="outerHTML">
            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" name="name" value="Greg Lim">
            </div> 
            <div class="mb-3">
                <label for="bio" class="form-label">Bio</label>
                <textarea type="text" 
                    class="form-control" 
                    id="bio" 
                    name="bio">

                    Follower of Christ |Author of Best-selling Amazon Tech Books and Creator of Coding Courses
                </textarea>
            </div>
            <button type="submit" class="btn btn-primary">Save Changes</button>
            <button type="submit" 
                hx-get="/index.html"
                class="btn btn-secondary">
                    Cancel
            </button>
        </form>
    `);
});

// Handle PUT request for editing
app.put('/user/:id', (req, res) => {
    const name = req.body.name;
    const bio = req.body.bio;

    // Send the updated profile back
    res.send(`
        <div class="card" 
            style="width: 18rem;"
            hx-target="this"
            hx-swap="outerHTML">
            
            <div class="card-body">
                <h5 class="card-title">${name}</h5>
                <p class="card-text">${bio}</p>
                <button href="#" 
                    class="btn btn-primary"
                    hx-get="/user/1/edit">
                        Click To Edit
                </button>
            </div>
        </div>
    `);
});

// Start server
app.listen(3000, () => {
    console.log('Server running on port 3000');
});