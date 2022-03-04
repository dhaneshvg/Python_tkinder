from omdbapi.movie_search import GetMovie as g
m=g(api_key='d67ffdb0')

print('----------Movie Details----------')
mv=input('\n Enter the movie name:')

det=m.get_movie(title=mv,plot='full')
print(det)

f=m.get_data('actors','year')
print(f)
