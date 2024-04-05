document.getElementById('postForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    const author = document.getElementById('author').value;

    fetch('http://127.0.0.1:5000/posts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, content, author }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert('Post created successfully!');
        fetchPosts(); // Reload the posts
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

function fetchPosts() {
    fetch('http://127.0.0.1:5000/posts')
        .then(response => response.json())
        .then(data => {
            const postsDiv = document.getElementById('posts');
            postsDiv.innerHTML = ''; 
            data.forEach(post => {
                const postDiv = document.createElement('div');
                postDiv.innerHTML = `<h3>${post.title}</h3><p>${post.content}</p><small>Author: ${post.author}</small>`;
                postsDiv.appendChild(postDiv);
            });
        });
}

document.getElementById('updatePostForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const id = document.getElementById('updateId').value;
    const title = document.getElementById('updateTitle').value;
    const content = document.getElementById('updateContent').value;
    const author = document.getElementById('updateAuthor').value;

    fetch(`http://127.0.0.1:5000/posts/${id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ title, content, author }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Post updated successfully!');
        fetchPosts();
    })
    .catch(error => console.error('Error:', error));
});

// Delete Post
document.getElementById('deletePostForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const id = document.getElementById('deleteId').value;

    fetch(`http://127.0.0.1:5000/posts/${id}`, {
        method: 'DELETE',
    })
    .then(() => {
        alert('Post deleted successfully!');
        fetchPosts();
    })
    .catch(error => console.error('Error:', error));
});

// Add Comment
document.getElementById('commentForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const postId = document.getElementById('commentPostId').value;
    const author = document.getElementById('commentAuthor').value;
    const content = document.getElementById('commentContent').value;

    fetch(`http://127.0.0.1:5000/posts/${postId}/comments`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ content, author }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Comment added successfully!');

    })
    .catch(error => console.error('Error:', error));
});

// Function to load posts on page load remains unchanged
window.onload = function() {
    fetchPosts();
};
