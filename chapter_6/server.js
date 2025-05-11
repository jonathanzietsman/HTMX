import express from 'express';

const app = express();
const port = 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true })); // Add this line
app.use(express.static('public'));

// Basic route
app.get('/', (req, res) => {
    res.json({ message: 'Welcome to the Express server!' });
});

// Handle GET request for profile edit
app.get('/user/:id/edit', (req, res) => {
    res.send(`
        <div class="card" style="width: 18rem;" hx-target="this" hx-swap="outerHTML">
            <div class="card-body">
                <form hx-put="/user/1" hx-target="closest .card" hx-swap="outerHTML">
                    <div class="mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input type="text" 
                               class="form-control" 
                               id="name" 
                               name="name" 
                               value="Greg Lim">
                    </div>
                    <div class="mb-3">
                        <label for="bio" class="form-label">Bio</label>
                        <textarea class="form-control" 
                                  id="bio" 
                                  name="bio"
                                  rows="3">Follower of Christ | Author of Best-selling Amazon Tech Books and Creator of Coding Courses</textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Save Changes</button>
                    <button type="button" 
                            class="btn btn-secondary" 
                            hx-get="/user/1">Cancel</button>
                </form>
            </div>
        </div>
    `);
});

// Handle GET request for profile view
app.get('/user/:id', (req, res) => {
    res.send(`
        <div class="card" style="width: 18rem;" hx-target="this" hx-swap="outerHTML">
            <div class="card-body">
                <h5 class="card-title">Greg Lim</h5>
                <p class="card-text">
                    Follower of Christ | Author of Best-selling Amazon Tech Books and Creator of Coding Courses
                </p>
                <button href="#" class="btn btn-primary"
                        hx-get="/user/1/edit">
                    Click To Edit
                </button>
            </div>
        </div>
    `);
});

// Handle PUT request for profile update
app.put('/user/:id', (req, res) => {
    // Access form data from request body
    const name = req.body.name || 'Greg Lim';  // Provide default values
    const bio = req.body.bio || 'Follower of Christ | Author of Best-selling Amazon Tech Books and Creator of Coding Courses';
    
    // Send the updated profile back
    res.send(`
        <div class="card" style="width: 18rem;" hx-target="this" hx-swap="outerHTML">
            <div class="card-body">
                <h5 class="card-title">${name}</h5>
                <p class="card-text">${bio}</p>
                <button href="#" class="btn btn-primary"
                        hx-get="/user/1/edit">
                    Click To Edit
                </button>
            </div>
        </div>
    `);
});

// Start server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
