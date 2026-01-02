from models.author import Author, Book

def create_author(db, data):
    author = Author(name=data.name)
    author.books = [Book(title=b.title) for b in data.books]
    db.add(author)
    db.commit()
    return author

def get_authors(db):
    return db.query(Author).all()

def get_author(db, author_id):
    return db.query(Author).filter(Author.id == author_id).first()

def delete_author(db, author_id):
    author = get_author(db, author_id)
    if not author:
        return None
    db.delete(author)
    db.commit()
    return True


def update_author(db, author_id, data):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        return None

    author.name = data.name
    author.books.clear()

    for b in data.books:
        author.books.append(Book(title=b.title))

    db.commit()
    db.refresh(author)
    return author