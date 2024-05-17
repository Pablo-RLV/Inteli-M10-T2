def get_all_data(model):
    data = model.query.all()
    return_data = []
    for item in data:
        return_data.append(item.serialize())
    return return_data

def get_data_by_id(model, id):
    data = model.query.get(id)
    if data is None:
        return {"error": "id not found"}
    return data.serialize()