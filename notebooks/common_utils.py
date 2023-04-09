def split_x_and_y(data, label="rating"):
    X_user = data[["user_tags"]]
    X_movie = data[["movie_tags"]]
    y = data[[label]]
    y[label] = y[label].apply(lambda x: x + 1)
    return X_user, X_movie, y
