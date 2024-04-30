def create_data(model, db, **kwargs):
    item = model(**kwargs)
    db.session.add(item)
    db.session.commit()
    return item.serialize()