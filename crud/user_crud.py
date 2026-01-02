from models.user import User, Profile

def create_user(db, data):
    user = User(name=data.name)
    profile = Profile(bio=data.bio)
    user.profile = profile
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db):
    return db.query(User).all()

def get_user(db, user_id):
    return db.query(User).filter(User.id == user_id).first()

def delete_user(db, user_id):
    user = get_user(db, user_id)
    if not user:
        return None
    db.delete(user)
    db.commit()
    return True

def update_user(db, user_id, data):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    user.name = data.name
    user.profile.bio = data.bio

    db.commit()
    db.refresh(user)
    return user