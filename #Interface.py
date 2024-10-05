#Interface 
movie_name_input = widgets.Text(
    value="Toy Story",
    description="Movie Title:",
    disabled=False
)

recommendation_list = widgets.Output()

def on_type(data):
    with recommendation_list:
        recommendation_list.clear_output()
        title = data["new"]
        if len(title) > 5:
            results = search(title)
            movie_id = results.iloc[0]["movieId"]
            display(find_similar_movies(movie_id))

movie_name_input.observe(on_type, names="value")

display(movie_name_input, recommendation_list)