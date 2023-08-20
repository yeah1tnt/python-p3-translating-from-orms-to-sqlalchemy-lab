from models import Dog

def create_table(base, engine):
    if not base.metadata.tables:
        base.metadata.create_all(engine)

def save(session, dog):
    if not session.query(Dog).filter_by(name=dog.name).first():
        session.add(dog)
        session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    return session.query(Dog).filter_by(name=dog.name).update({'breed': breed})