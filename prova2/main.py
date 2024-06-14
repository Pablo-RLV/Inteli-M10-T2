from fastapi import FastAPI, HTTPException

app = FastAPI()

blog_posts = []

class BlogPost:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
    def __str__(self) -> str:
        return f'{self.id} - {self.title} - {self.content}'
    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'content': self.content}

@app.post('/blog')
def create_blog_post(data: dict):
    try:
        blog_posts.append(BlogPost(data['id'], data['title'], data['content']))
        return {'status': 'success'}
    except KeyError:
        raise HTTPException(status_code=400, detail='Invalid request')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/blog')
def get_blog_posts():
    return {'posts': [blog.to_dict() for blog in blog_posts]}

@app.get('/blog/{id}')
def get_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            return {'post': post.__dict__}
    raise HTTPException(status_code=404, detail='Post not found')

@app.delete('/blog/{id}')
def delete_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            return {'status': 'success'}
    raise HTTPException(status_code=404, detail='Post not found')

@app.put('/blog/{id}')
def update_blog_post(id: int, data: dict):
    try:
        for post in blog_posts:
            if post.id == id:
                post.title = data['title']
                post.content = data['content']
                return {'status': 'success'}
        raise HTTPException(status_code=404, detail='Post not found')
    except KeyError:
        raise HTTPException(status_code=400, detail='Invalid request')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)