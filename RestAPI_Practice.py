from fastapi import FastAPI, HTTPException
from schema import GenreURLChoices, Band 

app = FastAPI()

BANDS = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genre': 'Electronic'},
    {'id': 3, 'name': 'Black Sabbath', 'genre': 'Metal'},
    {'id': 4, 'name': 'Wu-Tang Clan', 'genre': 'Hip-Hop'},
]

@app.get('/bands')
async def bands() -> list[dict]:
    return BANDS

@app.get('/bands/{band_id}', status_code= 200)
async def band(band_id: int) -> dict:
    band = next ((b for b in BANDS if b['id'] == band_id), None)
    if band is None:
        #status code 404
        raise HTTPException(status_code=404, detail='Band not found!')
    return band


@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    print(genre)
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]