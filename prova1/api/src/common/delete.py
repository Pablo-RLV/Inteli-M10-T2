def delete_data_by_id(model, db, id):
    data = model.query.get(id)
    if data is None:
        return {"error": "id not found"}
    db.session.delete(data)
    db.session.commit()
    return data.serialize()