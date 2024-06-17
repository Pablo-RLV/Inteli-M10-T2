def update_data(model, db, id, **kwargs):
    item = model.query.get(id)
    for key, value in kwargs.items():
        setattr(item, key, value)
    db.session.commit()
    return item.serialize()