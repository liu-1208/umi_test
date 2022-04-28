
def gen_data(**kwargs):
    return {k: v for k, v in kwargs.items() if v != "--Empty--"}
