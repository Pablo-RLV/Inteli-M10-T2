def update_data(model, db, id, **kwargs):
    data = model.query.get(id)
    if data is None:
        return {"error": "id not found"}
    for key, value in kwargs.items():
        setattr(data, key, value)
    db.session.commit()
    return data.serialize()